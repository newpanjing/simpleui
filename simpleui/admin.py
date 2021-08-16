from django.contrib import admin
from django.urls import path


class AjaxAdmin(admin.ModelAdmin):
    def callback(self, request):
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

            return func(self, request, queryset)

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name

        return super().get_urls() + [
            path("ajax", self.callback, name="%s_%s_ajax" % info)
        ]
