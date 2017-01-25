from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class BaseForm(forms.Form):

    def error_detail(self):
        error_response = {}

        error_response['status'] = 2
        error_response['msg'] = 'form validate error'

        error_response['data'] = self.errors

        return error_response


class UserForm(BaseForm):

    name = forms.CharField()
    age = forms.IntegerField()

    def clean(self):
        if not self.errors:
            name = self.cleaned_data.get('name')
            age = self.cleaned_data.get('age')

            if name == 'young' and age > 20:
                raise ValidationError(_("you are too old."), code='old')

        return self.cleaned_data

