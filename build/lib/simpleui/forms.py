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


# class CField:
#     widget = TextInput  # 呈现此类字段时使用的默认小部件。
#     hidden_widget = HiddenInput  # 默认小部件使用时，渲染为“隐藏”。
#     default_validators = []  # 默认验证器集
#     # 如果您希望字段验证器不引发特定的字段错误消息，请在default_error_message中添加一个“无效”条目。
#     default_error_messages = {
#         'required': _('This field is required.'),
#     }
#     empty_values = list(validators.EMPTY_VALUES)
#
#     def __init__(self, *, required=True, widget=None, label=None, initial=None,
#                  help_text='', error_messages=None, show_hidden_initial=False,
#                  validators=(), localize=False, disabled=False, label_suffix=None, **kwargs):
#         # required——指定字段是否是必需的布尔值，默认情况下为真。
#         # widget——一个widget类，或者widget类的实例，在显示它时应该用于这个字段。每个字段都有一个默认的小部件，如果您不指定它，它将使用这个小部件。在大多数情况下，默认的小部件是TextInput。
#         # label——此字段的详细名称，用于在表单中显示此字段。默认情况下，Django将使用表单字段名的“漂亮”版本(如果该字段是表单的一部分)。
#         # initial——在该字段的初始显示中使用的值。如果没有提供数据，则*not*将此值用作回退。
#         # help_text——一个可选的字符串，用作这个字段的“帮助文本”。
#         # error_messages——一个可选的字典，用于覆盖字段将引发的默认消息。
#         # show_hidden_initial——布尔值，用于指定是否需要在小部件之后呈现具有初始值的隐藏小部件。
#         # 验证器——要使用的其他验证器的列表
#         # localize——布尔值，指定字段是否应该本地化。
#         # disabled——布尔值，指定字段是否被禁用，也就是说它的小部件显示在表单中，但不可编辑。
#         # label_suffix——添加到标签的后缀。覆盖的label_suffix形式。
#         self.required, self.label, self.initial = required, label, initial
#         self.show_hidden_initial = show_hidden_initial
#         self.help_text = help_text
#         self.disabled = disabled
#         self.label_suffix = label_suffix
#         widget = widget or self.widget
#         if isinstance(widget, type):
#             widget = widget()
#         else:
#             widget = copy.deepcopy(widget)
#
#         # Trigger the localization machinery if needed.
#         self.localize = localize
#         if self.localize:
#             widget.is_localized = True
#
#         # Let the widget know whether it should display as required.
#         widget.is_required = self.required
#
#         # Hook into self.widget_attrs() for any Field-specific HTML attributes.
#         extra_attrs = self.widget_attrs(widget)
#         if extra_attrs:
#             widget.attrs.update(extra_attrs)
#         # simpleui 增加额外属性
#         widget.attrs.update(kwargs)
#
#         self.widget = widget
#
#         messages = {}
#         for c in reversed(self.__class__.__mro__):
#             messages.update(getattr(c, 'default_error_messages', {}))
#         messages.update(error_messages or {})
#         self.error_messages = messages
#
#         self.validators = [*self.default_validators, *validators]
#
#         super().__init__()
#
#     def prepare_value(self, value):
#         return value
#
#     def to_python(self, value):
#         return value
#
#     def validate(self, value):
#         if value in self.empty_values and self.required:
#             raise ValidationError(self.error_messages['required'], code='required')
#
#     def run_validators(self, value):
#         if value in self.empty_values:
#             return
#         errors = []
#         for v in self.validators:
#             try:
#                 v(value)
#             except ValidationError as e:
#                 if hasattr(e, 'code') and e.code in self.error_messages:
#                     e.message = self.error_messages[e.code]
#                 errors.extend(e.error_list)
#         if errors:
#             raise ValidationError(errors)
#
#     def clean(self, value):
#         """
#         Validate the given value and return its "cleaned" value as an
#         appropriate Python object. Raise ValidationError for any errors.
#         """
#         value = self.to_python(value)
#         self.validate(value)
#         self.run_validators(value)
#         return value
#
#     def bound_data(self, data, initial):
#         """
#         Return the value that should be shown for this field on render of a
#         bound form, given the submitted POST data for the field and the initial
#         data, if any.
#
#         For most fields, this will simply be data; FileFields need to handle it
#         a bit differently.
#         """
#         if self.disabled:
#             return initial
#         return data
#
#     def widget_attrs(self, widget):
#         """
#         给定一个小部件实例(*不是*小部件类)，根据这个字段返回应该添加到小部件的任何HTML属性的字典。
#         """
#         return {}
#
#     def has_changed(self, initial, data):
#         """Return True if data differs from initial."""
#         # Always return False if the field is disabled since self.bound_data
#         # always uses the initial value in this case.
#         if self.disabled:
#             return False
#         try:
#             data = self.to_python(data)
#             if hasattr(self, '_coerce'):
#                 return self._coerce(data) != self._coerce(initial)
#         except ValidationError:
#             return True
#         # For purposes of seeing whether something has changed, None is
#         # the same as an empty string, if the data or initial value we get
#         # is None, replace it with ''.
#         initial_value = initial if initial is not None else ''
#         data_value = data if data is not None else ''
#         return initial_value != data_value
#
#     def get_bound_field(self, form, field_name):
#         """
#         Return a BoundField instance that will be used when accessing the form
#         field in a template.
#         """
#         return BoundField(form, self, field_name)
#
#     def __deepcopy__(self, memo):
#         result = copy.copy(self)
#         memo[id(self)] = result
#         result.widget = copy.deepcopy(self.widget, memo)
#         result.error_messages = self.error_messages.copy()
#         result.validators = self.validators[:]
#         return result
#
#
# class CCharField(CField):
#     def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
#         self.max_length = max_length
#         self.min_length = min_length
#         self.strip = strip
#         self.empty_value = empty_value
#         # 增加额外属性，可以通过kwargs传递给field
#         super().__init__(**kwargs)
#         if min_length is not None:
#             self.validators.append(validators.MinLengthValidator(int(min_length)))
#         if max_length is not None:
#             self.validators.append(validators.MaxLengthValidator(int(max_length)))
#         self.validators.append(validators.ProhibitNullCharactersValidator())
#
#     def to_python(self, value):
#         """Return a string."""
#         if value not in self.empty_values:
#             value = str(value)
#             if self.strip:
#                 value = value.strip()
#         if value in self.empty_values:
#             return self.empty_value
#         return value
#
#     def widget_attrs(self, widget):
#         attrs = super().widget_attrs(widget)
#         if self.max_length is not None and not widget.is_hidden:
#             # The HTML attribute is maxlength, not max_length.
#             attrs['maxlength'] = str(self.max_length)
#         if self.min_length is not None and not widget.is_hidden:
#             # The HTML attribute is minlength, not min_length.
#             attrs['minlength'] = str(self.min_length)
#         return attrs


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