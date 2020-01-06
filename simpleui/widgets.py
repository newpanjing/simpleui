# -*- encoding: utf-8 -*-
"""
@File    : widgets.py
@Time    : 2020/1/3 11:22
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :小部件
"""
import typing
import copy
import datetime
import re
import warnings
from collections import defaultdict
from itertools import chain

from django.conf import settings
from django.forms.renderers import get_default_renderer
from django.forms.utils import to_current_timezone
from django.forms.widgets import media_property
from django.templatetags.static import static
from django.utils import datetime_safe, formats
from django.utils.datastructures import OrderedSet
from django.utils.dates import MONTHS
from django.utils.formats import get_format
from django.utils.html import format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.topological_sort import (
    CyclicDependencyError, stable_topological_sort,
)
from django.utils.translation import gettext_lazy as _

__all__ = ('STextInput', 'SPasswordInput',
           'SURLInput', 'SEmailInput', 'SNumberInput',)


class MediaDefiningClass(type):
    """
    元类：媒体定义。
    """

    def __new__(mcs, name, bases, attrs):
        new_class = super(MediaDefiningClass, mcs).__new__(mcs, name, bases, attrs)

        if 'media' not in attrs:
            new_class.media = media_property(new_class)

        return new_class


class CWidget(metaclass=MediaDefiningClass):
    needs_multipart_form = False  # 确定此小部件是否需要多部件表单
    is_localized = False
    is_required = False
    supports_microseconds = True
    bind_attr={}
    def __init__(self, attrs=None):
        self.attrs = {} if attrs is None else attrs.copy()

    def __deepcopy__(self, memo):
        obj = copy.copy(self)
        obj.attrs = self.attrs.copy()
        memo[id(self)] = obj
        return obj

    @property
    def is_hidden(self):
        return self.input_type == 'hidden' if hasattr(self, 'input_type') else False

    def subwidgets(self, name, value, attrs=None):
        context = self.get_context(name, value, attrs)
        yield context['widget']

    def format_value(self, value):
        """
        返回在模板中呈现时应该出现的值。
        """
        if value == '' or value is None:
            return None
        if self.is_localized:
            return formats.localize_input(value)
        return str(value)

    def get_context(self, name, value, attrs):
        context = {}
        context['widget'] = {
            'name': name,
            'is_hidden': self.is_hidden,
            'required': self.is_required,
            'value': self.format_value(value),
            'attrs': self.build_attrs(self.attrs, attrs),
            'template_name': self.template_name,
        }
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """将小部件呈现为HTML字符串。"""
        context = self.get_context(name, value, attrs)
        return self._render(self.template_name, context, renderer)

    def _render(self, template_name, context, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(template_name, context))

    def build_attrs(self, base_attrs, extra_attrs=None):
        """Build an attribute dictionary."""
        return {**base_attrs, **(extra_attrs or {})}

    def value_from_datadict(self, data, files, name):
        """
        Given a dictionary of data and this widget's name, return the value
        of this widget or None if it's not provided.
        """
        return data.get(name)

    def value_omitted_from_data(self, data, files, name):
        return name not in data

    def id_for_label(self, id_):
        """
        给定字段的ID，返回此小部件的HTML ID属性，以供<label>使用。
        如果没有可用的ID，则返回None。
        这个钩子是必需的，因为一些小部件有多个HTML元素，因此有多个id。
        在这种情况下，这个方法应该返回一个ID值，该值对应于小部件标记中的第一个ID。
        """
        return id_

    def use_required_attribute(self, initial):
        return not self.is_hidden

    def get_bind_attr(self, attrs=None):
        """
        获取该控件需要绑定的变量参数
        :return:
        """
        if not attrs:
            self.bind_attr={}
            return
        for key, value in attrs.items():
            if key[0] == ":":
                if isinstance(value, str):
                    self.bind_attr[value] = ''
                elif isinstance(value, dict):
                    for a, b in value.items():
                        self.bind_attr[a] = b
                else:
                    continue

class CInput(CWidget):
    """
    Base class for all <input> widgets.
    """
    input_type = None  # Subclasses must define this.
    template_name = 'forms/widgets/input.html'
    flag = False

    def __init__(self, attrs=None):
        if attrs is not None:
            attrs = attrs.copy()
            self.input_type = attrs.pop('type', self.input_type)
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['flag'] = self.flag
        context['widget']['type'] = self.input_type
        return context


class STextInput(CInput):
    input_type = "text"
    template_name = 'forms/widgets/text.html'

    def __init__(self, attrs: typing.Union[typing.Dict[str, str], None] = None):
        self.get_bind_attr(attrs)
        if not  attrs :
            attrs = {}
            attrs['style'] = "width:180px"
        else:
            if not attrs.get('style'):
                attrs['style'] = "width:180px "
        super().__init__(attrs)


class SNumberInput(CInput):
    input_type = 'number'
    template_name = 'forms/widgets/number.html'
    def __init__(self, attrs: typing.Union[typing.Dict[str, str], None] = None):
        self.get_bind_attr(attrs)
        if not attrs:
            attrs = {}
            attrs['style'] = "width:180px"
        else:
            if not attrs.get('style'):
                attrs['style'] = "width:180px "
        super().__init__(attrs)


class SEmailInput(CInput):
    input_type = 'email'
    template_name = 'forms/widgets/email.html'
    def __init__(self, attrs: typing.Union[typing.Dict[str, str], None] = None):
        self.get_bind_attr(attrs)
        if not attrs:
            attrs = {}
            attrs['style'] = "width:180px "
        else:
            if not attrs.get('style'):
                attrs['style'] = "width:180px "
        super().__init__(attrs)

class SURLInput(CInput):
    input_type = 'url'
    template_name = 'forms/widgets/url.html'
    def __init__(self, attrs: typing.Union[typing.Dict[str, str], None] = None):
        self.get_bind_attr(attrs)
        if not attrs:
            attrs = {}
            attrs['style'] = "width:180px"
        else:
            if not attrs.get('style'):
                attrs['style'] = "width:180px "
        super().__init__(attrs)

class SPasswordInput(CInput):
    input_type = 'password'
    template_name = 'forms/widgets/password.html'

    def __init__(self, attrs: typing.Union[typing.Dict[str, str], None] = None,render_value=False):
        self.get_bind_attr(attrs)
        if not attrs:
            attrs = {}
            attrs['style'] = "width:180px"
        else:
            if not attrs.get('style'):
                attrs['style'] = "width:180px "
        super().__init__(attrs)
        self.render_value = render_value
    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)
# Defined at module level so that CheckboxInput is picklable (#17976)
def boolean_check(v):
    return not (v is False or v is None or v == '')

class SCheckboxInput(CInput):
    """
    注意：如果是bool值，会导致渲染之后form表单无法提交该参数，所以要切换到原生的input-checkbox。如果value是有选项的值，再观察
    """
    input_type = 'checkbox'
    template_name = 'forms/widgets/checkbox.html'

    def __init__(self, attrs=None, check_test=None):
        super().__init__(attrs)
        # check_test是一个可调用的函数，它接受一个值，如果复选框被选中，它将返回True。
        self.check_test = boolean_check if check_test is None else check_test

    def format_value(self, value):
        """只有在value不为空时才返回'value'属性。"""
        if value is True or value is False or value is None or value == '':
            return
        return str(value)

    def get_context(self, name, value, attrs):
        if self.check_test(value):
            attrs = {**(attrs or {}), 'checked': True}
        return super().get_context(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        if name not in data:
            # A missing value means False because HTML form submission does not
            # send results for unselected checkboxes.
            return False
        value = data.get(name)
        # Translate true and false strings to boolean values.
        values = {'true': True, 'false': False}
        if isinstance(value, str):
            value = values.get(value.lower(), value)
        return bool(value)

    def value_omitted_from_data(self, data, files, name):
        # 如果没有选中，HTML复选框不会出现在POST数据中，因此永远不知道该值是否实际上被省略了。
        return False