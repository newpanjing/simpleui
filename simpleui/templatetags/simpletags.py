# -*- coding: utf-8 -*-

import base64
import json
import logging
import os
import platform
import sys
import time
import traceback
from inspect import isfunction

import django
from django.contrib.auth.models import Permission

import simpleui
from django import template
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.urls import is_valid_path, reverse

try:
    from django.utils.encoding import force_text
except:
    from django.utils.encoding import force_str as force_text
from django.utils.functional import Promise
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

PY_VER = sys.version[0]  # 2 or 3
from django.utils.translation import gettext_lazy as _

if PY_VER != '2':
    from importlib import reload
    from urllib.parse import parse_qsl
else:
    from urlparse import parse_qsl

import copy

def unicode_to_str(u, encoding='utf-8'):
    if PY_VER != '2':
        return u
    return u.encode(encoding)


class LazyEncoder(DjangoJSONEncoder):
    """
        解决json __proxy__ 问题
    """

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)


@register.simple_tag(takes_context=True)
def context_test(context):
    print(context)
    pass


# context.get('cl').filter_specs[1].links
@register.simple_tag(takes_context=True)
def load_dates(context):
    data = {}
    cl = context.get('cl')
    if cl.has_filters:
        for spec in cl.filter_specs:
            # 自定义的filter，没有field
            if not hasattr(spec, 'field'):
                continue

            field = spec.field
            field_type = None
            if isinstance(field, models.DateTimeField):
                field_type = 'datetime'
            elif isinstance(field, models.DateField):
                field_type = 'date'
            elif isinstance(field, models.TimeField):
                field_type = 'time'

            if field_type:
                data[spec.field_path] = field_type
    context['date_field'] = data

    return '<script type="text/javascript">var searchDates={}</script>'.format(json.dumps(data, cls=LazyEncoder))


@register.filter
def has_filter(spec):
    return hasattr(spec, 'parameter_name')


@register.filter
def get_date_type(spec):
    field = spec.field
    field_type = ''
    if isinstance(field, models.DateTimeField):
        field_type = 'datetime'
    elif isinstance(field, models.DateField):
        field_type = 'date'
    elif isinstance(field, models.TimeField):
        field_type = 'time'

    return field_type


@register.filter
def test(obj):
    print(obj)
    # pass
    return ''


@register.filter
def to_str(obj):
    return str(obj)


@register.filter
def date_to_json(obj):
    return json.dumps(obj.date_params, cls=LazyEncoder)


@register.simple_tag(takes_context=True)
def home_page(context):
    '''
    处理首页，通过设置判断打开的是默认页还是自定义的页面
    :return:
    '''
    home = __get_config('SIMPLEUI_HOME_PAGE')
    if home:
        context['home'] = home

    title = __get_config('SIMPLEUI_HOME_TITLE')
    if not title:
        title = '首页'

    icon = __get_config('SIMPLEUI_HOME_ICON')
    if not icon:
        icon = 'el-icon-menu'

    context['title'] = title
    context['icon'] = icon

    return ''


def __get_config(name):
    from django.conf import settings
    value = os.environ.get(name, getattr(settings, name, None))
    return value


@register.simple_tag
def get_setting(name):
    """
    获取设置项，默认为None
    自2022.1版本开始增加该方法
    """
    return __get_config(name)


@register.filter
def get_config(key):
    return __get_config(key)


@register.filter
def get_value(value):
    return value


@register.simple_tag
def get_version():
    return simpleui.get_version()


@register.simple_tag
def get_app_info():
    return format_table({"version": simpleui.get_version()})


def format_table(d):
    html = '<table class="simpleui-table"><tbody>'
    for key in d:
        html += '<tr><th>{}</th><td>{}</td></tr>'.format(key, d.get(key))
    html += '</tbody></table>'
    return format_html(html)


def has_permission_in_config(config):
    """
    Recursively check if any menu or sub-menu in the configuration is configured with permissions.
    """
    if 'menus' in config:
        for menu in config['menus']:
            if has_permission_in_config(menu):
                return True
    if 'models' in config:
        for model in config['models']:
            if has_permission_in_config(model):
                return True
    if 'permission' in config:
        return True
    return


def get_filtered_menus(menus, user_permissions):
    def filter_menu(menu, permissions):
        if 'models' in menu:
            menu['models'] = [sub_menu for sub_menu in menu['models'] if 'permission' not in sub_menu or
                              sub_menu['permission'] in permissions]
            for sub_menu in menu['models']:
                filter_menu(sub_menu, permissions)

    menu_configs = [menu for menu in menus if 'permission' not in menu or menu['permission'] in user_permissions]
    for menu in menu_configs:
        filter_menu(menu, user_permissions)
    return menu_configs


@register.simple_tag(takes_context=True)
def menus(context, _get_config=None):
    data = []

    # return request.user.has_perm("%s.%s" % (opts.app_label, codename))
    if not _get_config:
        _get_config = get_config

    config = _get_config('SIMPLEUI_CONFIG')
    if not config:
        config = {}
    else:
        # config = config.copy()
        config = copy.deepcopy(config)

    # if config.get('dynamic', False) is True:
    #     config = _import_reload(_get_config('DJANGO_SETTINGS_MODULE')).SIMPLEUI_CONFIG

    app_list = context.get('app_list')
    for app in app_list:
        _models = [
            {
                'name': m.get('name'),
                'icon': get_icon(m.get('object_name'), unicode_to_str(m.get('name'))),
                'url': m.get('admin_url'),
                'addUrl': m.get('add_url'),
                'breadcrumbs': [{
                    'name': app.get('name'),
                    'icon': get_icon(app.get('app_label'), app.get('name'))
                }, {
                    'name': m.get('name'),
                    'icon': get_icon(m.get('object_name'), unicode_to_str(m.get('name')))
                }]
            }

            for m in app.get('models')
        ] if app.get('models') else []

        module = {
            'name': app.get('name'),
            'icon': get_icon(app.get('app_label'), app.get('name')),
            'models': _models
        }
        data.append(module)

    if has_permission_in_config(config):
        config["menus"] = get_filtered_menus(config["menus"], context.request.user.get_all_permissions())

    # 如果有menu 就读取，没有就调用系统的
    key = 'system_keep'
    if config and 'menus' in config:
        if config.get(key, None):
            temp = config.get('menus')
            for i in temp:
                # 处理面包屑
                if 'models' in i:
                    for k in i.get('models'):
                        k['breadcrumbs'] = [{
                            'name': i.get('name'),
                            'icon': i.get('icon')
                        }, {
                            'name': k.get('name'),
                            'icon': k.get('icon')
                        }]
                else:
                    i['breadcrumbs'] = [{
                        'name': i.get('name'),
                        'icon': i.get('icon')
                    }]
                data.append(i)
        else:
            data = config.get('menus')

    # 获取侧边栏排序, 如果设置了就按照设置的内容排序, 留空则表示默认排序以及全部显示
    if config.get('menu_display') is not None:
        display_data = list()
        for _app in data:
            if _app['name'] not in config.get('menu_display'):
                continue
            _app['_weight'] = config.get('menu_display').index(_app['name'])
            display_data.append(_app)
        display_data.sort(key=lambda x: x['_weight'])
        data = display_data

    # 给每个菜单增加一个唯一标识，用于tab页判断
    eid = 1000
    handler_eid(data, eid)
    menus_string = json.dumps(data, cls=LazyEncoder)

    # 把data放入session中，其他地方可以调用
    if not isinstance(context, dict) and context.request:
        context.request.session['_menus'] = menus_string

    return '<script type="text/javascript">var menus={}</script>'.format(menus_string)


def handler_eid(data, eid):
    for i in data:
        eid += 1
        i['eid'] = eid
        if 'models' in i:
            eid = handler_eid(i.get('models'), eid)
    return eid


def get_icon(obj, name=None):
    temp = get_config_icon(name)
    if temp != '':
        return temp

    _dict = {
        'auth': 'fas fa-shield-alt',
        'User': 'far fa-user',
        'Group': 'fas fa-users-cog'
    }

    temp = _dict.get(obj)
    if not temp:
        return 'far fa-circle'

    return temp


# 从配置中读取图标
def get_config_icon(name):
    _config_icon = __get_config('SIMPLEUI_ICON')
    if _config_icon is None:
        return ''

    if name in _config_icon:
        return _config_icon.get(name)
    return ''


@register.simple_tag(takes_context=True)
def load_message(context):
    messages = context.get('messages')
    array = [dict(msg=msg.message, tag=msg.tags) for msg in messages] if messages else []

    return '<script id="out_message" type="text/javascript">var messages={}</script>'.format(
        json.dumps(array, cls=LazyEncoder))


@register.simple_tag(takes_context=True)
def context_to_json(context):
    json_str = '{}'

    return mark_safe(json_str)


@register.simple_tag()
def get_language():
    from django.conf import settings
    return settings.LANGUAGE_CODE.lower()


@register.filter
def get_language_code(val):
    from django.conf import settings
    return settings.LANGUAGE_CODE.lower()


def get_analysis_config():
    val = __get_config('SIMPLEUI_ANALYSIS')
    if val:
        return True
    return False


@register.simple_tag(takes_context=True)
def custom_button(context):
    admin = context.get('cl').model_admin
    request = context.request
    data=get_custom_button(request, admin)
    return json.dumps(data, cls=LazyEncoder)

def get_layer_url(admin):
    """
    获取url配置
    """
    try:
        opts = admin.opts
        key = "admin:{}_{}_layer".format(opts.app_label, opts.model_name)
    except Exception:
        # 输出警告
        logging.warning(f"使用异步获取layer配置，需要让Admin继承AjaxAdmin")
        print(f"使用异步获取layer配置，需要让Admin继承AjaxAdmin")
        traceback.print_exc()
    return reverse(key)

def get_custom_button(request, admin):
    data = {}
    actions = admin.get_actions(request)
    # if hasattr(admin, 'actions'):
    # actions = admin.actions
    # 输出自定义按钮的属性

    app_label = admin.opts.app_label
    if actions:
        id = 0
        for name in actions:
            values = {}
            fun = actions.get(name)[0]
            for key, v in fun.__dict__.items():
                if key != '__len__' and key != '__wrapped__':
                    if key == 'layer' and isfunction(v):
                        # 直接返回url到前台
                        values['layer'] = {
                            'is_fun': True,
                            'url': get_layer_url(admin)
                        }
                    else:
                        values[key] = v
            values['eid'] = id
            id += 1
            if name == 'export_admin_action':
                values['label'] = '选中导出'
                values['isExport'] = True
                values['icon'] = 'el-icon-finished'
                formats = []
                for i in enumerate(admin.get_export_formats()):
                    formats.append({
                        'value': i[0],
                        'label': i[1]().get_title()
                    })

                values['formats'] = formats
            else:
                values['label'] = actions.get(name)[2]

            # 判断权限，如果数据库中有才进行判断
            # ContentType.objects.first()
            # 不是超级用户才开始判断
            if not request.user.is_superuser:
                exists = Permission.objects.filter(codename=name, content_type__app_label=app_label,
                                                   content_type__model=admin.opts.model_name).exists()
                if exists:
                    if request.user.has_perm('{}.{}'.format(app_label, name)):
                        data[name] = values
                else:
                    data[name] = values
            else:
                data[name] = values
    if 'delete_selected' in data:
        del data['delete_selected']
    return data

from django.db.models.fields.related import ForeignKey


def get_model_fields(model, base=None):
    field_list = []
    fields = model._meta.fields
    for f in fields:
        label = f.name
        if hasattr(f, 'verbose_name'):
            label = getattr(f, 'verbose_name')

        if isinstance(label, Promise):
            label = str(label)

        if base:
            field_list.append(('{}__{}'.format(base, f.name), label))
        else:
            field_list.append((f.name, label))

    return field_list


@register.simple_tag(takes_context=True)
def search_placeholder(context):
    cl = context.get('cl')

    # 取消递归，只获取2级
    fields = get_model_fields(cl.model)

    for f in cl.model._meta.fields:
        if isinstance(f, ForeignKey):
            fields.extend(get_model_fields(f.related_model, f.name))

    verboses = []

    for s in cl.search_fields:
        for f in fields:
            if f[0] == s:
                verboses.append(f[1])
                break

    return ",".join(verboses)


def _import_reload(_modules):
    _obj = __import__(_modules, fromlist=_modules.split('.'))
    reload(_obj)
    return _obj


@register.simple_tag
def get_tz_suffix():
    # 判断settings.py中的TZ是否为false
    tz = __get_config('USE_TZ')
    # 必须明确指定为True的时候，才返回+8 的后缀
    if tz:
        return '+08:00'
    return ''


@register.simple_tag
def simple_version():
    return simpleui.get_version()


@register.simple_tag(takes_context=True)
def get_model_url(context):
    # reverse()
    opts = context.get("opts")
    request = context.get("request")

    key = "{}:{}_{}_changelist".format(
        get_current_app(request), opts.app_label, opts.model_name
    )
    url = reverse(key)
    preserved_filters = dict(parse_qsl(context.get("preserved_filters")))
    if "_changelist_filters" in preserved_filters:
        preserved_filters = preserved_filters["_changelist_filters"]
        url = add_preserved_filters({"preserved_filters": preserved_filters, "opts": opts}, url)
    return url


def get_current_app(request):
    app = None
    if hasattr(request, 'current_app'):
        app = getattr(request, 'current_app')
    elif hasattr(request, 'model_admin'):
        model_admin = getattr(request, 'model_admin')
        if hasattr(model_admin, 'opts'):
            opts = getattr(model_admin, 'opts')
            app = opts.app_config.name
    return app


@register.simple_tag(takes_context=True)
def get_model_ajax_url(context):
    opts = context.get("opts")
    key = "admin:{}_{}_ajax".format(opts.app_label, opts.model_name)
    try:
        return reverse(key)
    except:
        pass


@register.simple_tag
def has_enable_admindoc():
    from django.conf import settings
    apps = settings.INSTALLED_APPS
    return 'django.contrib.admindocs' in apps


@register.simple_tag(takes_context=True)
def has_admindoc_page(context):
    if hasattr(context, 'template_name'):
        return context.template_name.find('admin_doc') == 0
    return False


@register.simple_tag
def get_boolean_choices():
    return (
        ('True', _('Yes')),
        ('False', _('No'))
    )


@register.simple_tag(takes_context=True)
def get_previous_url(context):
    referer = context.request.META.get("HTTP_REFERER")
    if not referer or context.request.META.get("PATH_INFO") in referer:
        # return to model list
        return get_model_url(context)
    return context.request.META.get("HTTP_REFERER")


@register.simple_tag(takes_context=True)
def get_verbose_name_plural(context):
    return context['cl'].model._meta.verbose_name_plural


@register.simple_tag
def django_version_is_gte_32x():
    arrays = django.get_version().split(".")
    version = []
    for s in arrays:
        version.append(int(s))
    return tuple(version) >= (3, 2)
