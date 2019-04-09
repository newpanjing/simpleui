# -*- coding: utf-8 -*-

import django
from django import template
from django.utils.html import format_html
from django.conf import settings
import os
import json

import platform
import socket

import simpleui

register = template.Library()


@register.filter
def get_icon(name):
    # 默认为文件图标
    cls = "layui-icon-file"

    return format_html('<i class="layui-icon {}"></i>', cls)


@register.filter
def test(obj):
    print(obj)
    # pass
    return ''


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
        icon = 'layui-icon-console'

    context['title'] = format_html('<i class="layui-icon {}"></i>{}', icon, title)

    return ''


def __get_config(name):
    value = os.environ.get(name, getattr(settings, name, None))
    return value


@register.simple_tag
def get_server_info():
    dict = {
        '网络名': platform.node(),
        'IP': socket.gethostbyname(socket.gethostname()),
        '操作系统': platform.platform(),
        '处理器核心': os.cpu_count()
    }

    return format_table(dict)


@register.simple_tag
def get_app_info():
    dict = {
        'Python': platform.python_version(),
        'Django': django.get_version(),
        'Simpleui': simpleui.get_version()
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
    data.append({
        'name': '首页',
        'active': True,
        'icon': 'fas fa-home'
    })
    app_list = context.get('app_list')
    for app in app_list:
        models = []
        if app.get('models'):
            for m in app.get('models'):
                models.append({
                    'name': str(m.get('name')),
                    'icon': get_icon(m.get('object_name')),
                    'url': m.get('admin_url'),
                    'addUrl': m.get('add_url'),
                    'breadcrumbs': [str(app.get('name')), str(m.get('name'))]
                })

        module = {
            'name': str(app.get('name')),
            'icon': get_icon(app.get('app_label')),
            'models': models
        }
        data.append(module)

    return '<script type="text/javascript">var menus={}</script>'.format(json.dumps(data))


def get_icon(obj):
    dict = {
        'auth': 'fas fa-shield-alt',
        'User': 'far fa-user',
        'Group': 'fas fa-users-cog'

    }
    temp = dict.get(obj)
    if not temp:
        return 'far fa-file'
    return temp
