import json
import logging
import traceback

from django.contrib import admin
from django.contrib.admin import ListFilter
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import path


class AjaxAdmin(admin.ModelAdmin):
    """
    This class is used to add ajax functionality to the admin interface.
    """

    def _get_and_clear_simple_filter(self, request):

        sfs = []
        _filter = {}
        if "_filter" in request.POST:
            _filter = json.loads(request.POST.get("_filter"))
            lls = self.get_list_filter(request)
            if lls:
                for ll in lls:
                    try:
                        name = ll.parameter_name
                        if issubclass(ll, ListFilter):
                            val = _filter[name]

                            def value(*args, **kwargs):
                                return val

                            # 用lambda表达式，重写value 返回val
                            ll.value = value

                            if name in _filter:
                                # 删除
                                del _filter[name]
                            sfs.append(ll)
                    except Exception as e:
                        pass
        return _filter, sfs

    def _get_queryset(self, request):
        post = request.POST
        action = post.get("_action")
        selected = post.get("_selected")
        select_across = post.get("select_across")
        if hasattr(self, action):
            # 过滤simplefilter的key
            _filter, sfs = self._get_and_clear_simple_filter(request)
            # 这里的queryset 会有数据过滤，只包含选中的数据
            queryset = self.get_changelist_instance(request).get_queryset(request)

            # 没有选择全部的时候才过滤数据
            if select_across == "0":
                if selected and selected.split(","):
                    queryset = queryset.filter(pk__in=selected.split(","))
            else:
                # 过滤搜索条件，自simpleui-2022.3.13版本开始，支持搜索条件过滤，simplepro需要3.4.2及以上版本
                # 只有选择全部的时候才过滤数据
                # 字段为_search和_filter 是为了防止命名冲突

                # search
                if "_search" in post:
                    search_fields = self.get_search_fields(request)

                    if search_fields:
                        search_value = post.get("_search")
                        if search_value:
                            q = Q()
                            for s in search_fields:
                                q = q | Q(**{s + "__icontains": search_value})
                            try:
                                queryset = queryset.filter(q)
                            except Exception as e:
                                traceback.print_exc()
                                raise e

                # filter条件过滤
                if "_filter" in post:
                    if _filter:
                        new_filter = self.__clean_filter(_filter)
                        # 过滤simplefilter
                        if sfs:
                            for sf in sfs:
                                queryset = sf.queryset.__call__(sf, request, queryset)
                        queryset = queryset.filter(**new_filter)
            return queryset
        else:
            raise Exception("action not found")

    def __clean_filter(self, _filter):
        new_filter = {}
        for k, v in _filter.items():
            if "__exact" in k and isinstance(v, list):
                new_filter[k.replace('__exact', '__in')] = v[0]
            else:
                new_filter[k] = v

        return new_filter

    def __handler_simple_filter(self, queryset, _filter):
        # 判断_filter里面的字段是否是simplefilter
        # 如果是simplefilter，就调用simplefilter的过滤方法
        # 如果不是simplefilter，就返回原来的queryset

        sf = self.get_list_filter()
        if sf:
            for f in sf:
                if f.__class__.__name__ == "SimpleListFilter":
                    if f.parameter_name in _filter:
                        return f.queryset(request=None, queryset=queryset, value=_filter[f.parameter_name])

        # for k, v in _filter.items():

        return queryset

    def callback(self, request):
        """
        This method is used to handle ajax requests.
        """
        post = request.POST
        action = post.get("_action")

        # call admin
        if hasattr(self, action):
            func, action, description = self.get_action(action)
            qs = self._get_queryset(request)
            r = func(self, request, qs)
            if r is None:
                return JsonResponse(data={
                    "status": "success",
                    "msg": "Success!"
                })
            if isinstance(r, HttpResponseRedirect):
                return JsonResponse(data={
                    "status": "redirect",
                    "url": r.url
                })
            elif isinstance(r, JsonResponse):
                return r
            elif isinstance(r, dict):
                return JsonResponse(data=r)
            else:
                logging.warning(f"action {action} return type is {type(r)}")
                return JsonResponse(data={"status": "error", "msg": r})

    def get_layer(self, request):
        """
        This method is used to get the layer of the admin interface.
        """
        _action = request.POST.get("_action")
        if hasattr(self, _action):
            func, action, description = self.get_action(_action)
            if hasattr(func, "layer"):
                arg_count = func.layer.__code__.co_argcount
                if arg_count == 2:
                    result = func.layer(self, request)
                elif arg_count == 3:
                    # 兼容老版本
                    qs = self._get_queryset(request)
                    result = func.layer(self, request, qs)

                return JsonResponse(data=result, safe=False)
        else:
            raise Exception(f'action "{_action}" not found')

    def get_urls(self):
        """
        This method is used to add ajax functionality to the admin interface.
        """
        info = self.model._meta.app_label, self.model._meta.model_name

        return super().get_urls() + [
            path("ajax", self.callback, name="%s_%s_ajax" % info),
            path("layer", self.get_layer, name="%s_%s_layer" % info)
        ]
