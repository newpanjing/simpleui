# -*- encoding: utf-8 -*-
"""
@File    : forms.py
@Time    : 2020/1/3 11:14
@Author  : chise
@Email   : chise123@live.com
@Software: PyCharm
@info    :simpleui自定义表单
"""
from django import forms
import uuid

from django.core import validators
from django.core.exceptions import ValidationError
# Provide this import for backwards compatibility.
from django.core.validators import EMPTY_VALUES  # NOQA
from django.forms.boundfield import BoundField
from django.forms.forms import DeclarativeFieldsMetaclass, BaseForm
from django.forms.utils import from_current_timezone, to_current_timezone
from django.forms.widgets import (
    FILE_INPUT_CONTRADICTION, CheckboxInput, ClearableFileInput, DateInput,
    DateTimeInput, EmailInput, FileInput, HiddenInput, MultipleHiddenInput,
    NullBooleanSelect, NumberInput, Select, SelectMultiple,
    SplitDateTimeWidget, SplitHiddenDateTimeWidget, TextInput, TimeInput,
    URLInput,
)
from django.utils import formats
from django.utils.dateparse import parse_duration
from django.utils.duration import duration_string
from django.utils.ipv6 import clean_ipv6_address
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _, ngettext_lazy


import copy

from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
# BoundField is imported for backwards compatibility in Django 1.9
from django.forms.boundfield import BoundField  # NOQA
from django.forms.fields import Field, FileField
# pretty_name is imported for backwards compatibility in Django 1.9
from django.forms.utils import ErrorDict, ErrorList, pretty_name  # NOQA
from django.forms.widgets import Media, MediaDefiningClass
from django.utils.functional import cached_property
from django.utils.html import conditional_escape, html_safe
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from widgets import *

class SimpleForm(BaseForm, metaclass=DeclarativeFieldsMetaclass):
    def get_vue_app_js(self,app_id):
        """
        将该方法需要的js渲染进去
        :return:
        """
        base_vue_app="""
<script>
var %(app_name)s = new Vue({
    el: "#%(app_name)s",
    data() {
        return {
            %(data)s
        }
    }
})
</script>
        """
        data={}
        for name, field in self.fields.items():
            data[name] = ''
        data.update(self.data)
        data_s=""
        for key,value in data.items():
            data_s+="%(key)s:'%(value)s'"%{
                'key':key,
                'value':value
            }+','
        return base_vue_app %{"app_name":app_id,"data":data_s}
    def submit_button(self):
        """
        渲染模板增加submit格式
        :return:
        """
        # return '<input type="submit">'


        pass
    def as_element(self):
        "Return this form rendered as HTML <tr>s -- excluding the <table></table>."
        x= self._html_output(
            normal_row='<div %(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True,flag=True
        )
        return x

    def _html_output(self, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row,flag=False):
        "Output HTML. Used by as_table(), as_ul(), as_p()."
        top_errors = self.non_field_errors()  # Errors that should be displayed above all fields.
        output, hidden_fields = [], []

        for name, field in self.fields.items():
            html_class_attr = ''
            bf = self[name]
            if flag:
                bf.field.widget.flag=True
            bf_errors = self.error_class(bf.errors)
            if bf.is_hidden:
                if bf_errors:
                    top_errors.extend(
                        [_('(Hidden field %(name)s) %(error)s') % {'name': name, 'error': str(e)}
                         for e in bf_errors])
                hidden_fields.append(str(bf))
            else:
                # Create a 'class="..."' attribute if the row should have any
                # CSS classes applied.
                css_classes = bf.css_classes()
                if css_classes:
                    html_class_attr = ' class="%s"' % css_classes

                if errors_on_separate_row and bf_errors:
                    output.append(error_row % str(bf_errors))

                if bf.label:
                    label = conditional_escape(bf.label)
                    label = bf.label_tag(label) or ''
                else:
                    label = ''

                if field.help_text:
                    help_text = help_text_html % field.help_text
                else:
                    help_text = ''

                output.append(normal_row % {
                    'errors': bf_errors,
                    'label': label,
                    'field': bf,
                    'help_text': help_text,
                    'html_class_attr': html_class_attr,
                    'css_classes': css_classes,
                    'field_name': bf.html_name,
                })

        if top_errors:
            output.insert(0, error_row % top_errors)
        if hidden_fields:  # Insert any hidden fields in the last row.
            str_hidden = ''.join(hidden_fields)
            if output:
                last_row = output[-1]
                # Chop off the trailing row_ender (e.g. '</td></tr>') and
                # insert the hidden fields.
                if not last_row.endswith(row_ender):
                    # This can happen in the as_p() case (and possibly others
                    # that users write): if there are only top errors, we may
                    # not be able to conscript the last row for our purposes,
                    # so insert a new, empty row.
                    last_row = (normal_row % {
                        'errors': '',
                        'label': '',
                        'field': '',
                        'help_text': '',
                        'html_class_attr': html_class_attr,
                        'css_classes': '',
                        'field_name': '',
                    })
                    output.append(last_row)
                output[-1] = last_row[:-len(row_ender)] + str_hidden + row_ender
            else:
                # If there aren't any rows in the output, just append the
                # hidden fields.
                output.append(str_hidden)
        if flag:
            app_id = "x" + str(uuid.uuid4())[0:5]
            output.insert(0, "<div id='%s'>" %app_id)
            output.append('</div>')
            output.append(self.get_vue_app_js(app_id))
        return mark_safe('\n'.join(output))

class SCharField(forms.CharField):
    widget = STextInput
class SIntegerField(forms.IntegerField):
    def widget_attrs(self, widget):
        """
        解决max和min无法传递到widget的问题
        """
        attrs = super().widget_attrs(widget)
        if isinstance(widget, NumberInput) or isinstance(widget,SNumberInput):
            if self.min_value is not None:
                attrs['min'] = self.min_value
            if self.max_value is not None:
                attrs['max'] = self.max_value
        return attrs
    widget = SNumberInput

class SEmailField(forms.EmailField):
    widget = SEmailInput

class SURLField(forms.URLField):
    widget = SURLInput