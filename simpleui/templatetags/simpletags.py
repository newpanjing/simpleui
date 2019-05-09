# -*- coding: utf-8 -*-

import django
from django import template
from django.utils.html import format_html
from django.conf import settings
from django.utils.safestring import mark_safe

from django.templatetags import static

import os
import json

import platform
import socket

import simpleui

import base64
import time

from django.db import models

register = template.Library()


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
            field = spec.field
            field_type = None
            if isinstance(field, models.DateTimeField):
                field_type = 'datetime'
            elif isinstance(field, models.DateField):
                field_type = 'date'
            elif isinstance(field, models.TimeField):
                field_type = 'time'

            if field_type:
                data[field.name] = field_type
    context['date_field'] = data

    return '<script type="text/javascript">var searchDates={}</script>'.format(json.dumps(data))


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
    return json.dumps(obj.date_params)


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
    value = os.environ.get(name, getattr(settings, name, None))
    return value


@register.filter
def get_config(key):
    return __get_config(key)


@register.simple_tag
def get_app_info():
    dict = {
        'version': simpleui.get_version()
    }

    return format_table(dict)


def format_table(dict):
    html = '<table class="simpleui-table"><tbody>'
    for key in dict:
        html += '<tr><th>{}</th><td>{}</td></tr>'.format(key, dict.get(key))
    html += '</tbody></table>'
    return format_html(html)


@register.simple_tag(takes_context=True)
def menus(context):
    data = []

    # return request.user.has_perm("%s.%s" % (opts.app_label, codename))

    config = get_config('SIMPLEUI_CONFIG')

    app_list = context.get('app_list')
    for app in app_list:
        models = []
        if app.get('models'):
            for m in app.get('models'):
                models.append({
                    'name': str(m.get('name')),
                    'icon': get_icon(m.get('object_name'), str(m.get('name'))),
                    'url': m.get('admin_url'),
                    'addUrl': m.get('add_url'),
                    'breadcrumbs': [str(app.get('name')), str(m.get('name'))]
                })

        module = {
            'name': str(app.get('name')),
            'icon': get_icon(app.get('app_label'), str(app.get('name'))),
            'models': models
        }
        data.append(module)

    # 如果有menu 就读取，没有就调用系统的
    if config and 'menus' in config:
        if 'system_keep' in config:
            temp = config.get('menus')
            for i in temp:
                data.append(i)
        else:
            data = config.get('menus')

    return '<script type="text/javascript">var menus={}</script>'.format(json.dumps(data))


def get_icon(obj, name):
    temp = get_config_icon(name)
    if temp != '':
        return temp

    dict = {
        'auth': 'fas fa-shield-alt',
        'User': 'far fa-user',
        'Group': 'fas fa-users-cog'

    }
    temp = dict.get(obj)
    if not temp:
        _default = __get_config('SIMPLEUI_DEFAULT_ICON')
        if _default is None or _default:
            return 'far fa-file'
        else:
            return ''
    return temp


# 从配置中读取图标
def get_config_icon(name):
    _config_icon = __get_config('SIMPLEUI_ICON')
    if _config_icon is None:
        return ''

    if name in _config_icon:
        return _config_icon.get(name)
    else:
        return ''


@register.simple_tag(takes_context=True)
def load_message(context):
    messages = context.get('messages')
    array = []
    if messages:
        for msg in messages:
            array.append({
                'msg': msg.message,
                'tag': msg.tags
            })

    return '<script type="text/javascript"> var messages={}</script>'.format(array)


@register.simple_tag(takes_context=True)
def context_to_json(context):
    json_str = '{}'

    return mark_safe(json_str)


@register.simple_tag()
def get_language():
    return django.utils.translation.get_language()


@register.filter
def get_language_code(val):
    return django.utils.translation.get_language()


def get_analysis_config():
    val = __get_config('SIMPLEUI_ANALYSIS')
    if not val and val == False:
        return False
    return True


@register.simple_tag(takes_context=True)
def load_analysis(context):
    try:
        if get_analysis_config() == False:
            return ''

        # 理论上值一天只上报一次
        key = 'simpleui_' + time.strftime('%Y%m%d', time.localtime())

        if key in context.request.session:
            return ''

        b64 = ""
        j = {
            "n": platform.node(),
            "o": platform.platform(),
            "p": platform.python_version(),
            "d": django.get_version(),
            "s": simpleui.get_version(),
        }
        if 'theme_name' in context.request.COOKIES:
            j['t'] = context.request.COOKIES['theme_name']
        else:
            j['t'] = 'Default'

        b64 = base64.b64encode(str(j).encode('utf-8'))

        url = '//simpleui.88cto.com/analysis'
        b64 = b64.decode('utf-8')
        html = '<script async type="text/javascript" src="{}/{}"></script>'.format(url, b64);
        context.request.session[key] = True

        return mark_safe(html)
    except:
        return ''
