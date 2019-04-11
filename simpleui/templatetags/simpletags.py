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
from django.db import models

register = template.Library()


@register.filter
def get_icon(name):
    # 默认为文件图标
    cls = ""

    return format_html('<i class="icon {}"></i>', cls)


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
def date_wrap(spec):
    html = ''

    field = spec.field
    if isinstance(field, models.DateTimeField):
        html = '<el-date-picker v-model="{}" ' \
               '@change="change" ' \
               'type="datetimerange" ' \
               'range-separator="至" ' \
               'start-placeholder="{}开始" ' \
               'end-placeholder="{}结束">' \
               '</el-date-picker>'.format(field.name, spec.title, spec.title)

    elif isinstance(field, models.DateField):
        html = '<el-date-picker v-model="{}" ' \
               '@change="change" ' \
               'type="daterange" ' \
               'range-separator="至" ' \
               'start-placeholder="{}开始" ' \
               'end-placeholder="{}结束">' \
               '</el-date-picker>'.format(field.name, spec.title, spec.title)
    elif isinstance(field, models.TimeField):
        html = '<el-time-picker ' \
               'is-range ' \
               'v-model="{}" ' \
               '@change="change" ' \
               'range-separator="至" ' \
               'start-placeholder="{}时间" ' \
               'end-placeholder="{}时间" ' \
               'placeholder="选择时间范围"> ' \
               '</el-time-picker>'

    return html


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


@register.simple_tag(takes_context=True)
def load_message(context):
    messages = context.get('messages')
    array = []

    for msg in messages:
        array.append({
            'msg': msg.message,
            'tag': msg.tags
        })

    return '<script type="text/javascript"> var messages={}</script>'.format(array)
