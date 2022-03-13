import json

from django.contrib import admin
from django.urls import path


class AjaxAdmin(admin.ModelAdmin):
    """
    This class is used to add ajax functionality to the admin interface.
    """
    def callback(self, request):
        """
        This method is used to handle ajax requests.
        """
        post = request.POST
        action = post.get("_action")
        selected = post.get("_selected")
        select_across = post.get("select_across")

        # call admin
        if hasattr(self, action):
            func, action, description = self.get_action(action)
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
                if hasattr(self, "search_fields") and "_search" in post:
                    search_fields = self.get_search_fields(request)

                    if search_fields:
                        search_value = post.get("_search")
                        if search_value:
                            queryset = queryset.filter(**{
                                "{}__icontains".format(field): search_value
                                for field in search_fields
                            })
                # filter条件过滤
                if "_filter" in post:
                    filter = post.get("_filter")
                    if filter:
                        filter_value = json.loads(filter)
                        queryset = queryset.filter(**filter_value)

            return func(self, request, queryset)

    def get_urls(self):
        """
        This method is used to add ajax functionality to the admin interface.
        """
        info = self.model._meta.app_label, self.model._meta.model_name

        return super().get_urls() + [
            path("ajax", self.callback, name="%s_%s_ajax" % info)
        ]
