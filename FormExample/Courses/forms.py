from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from Courses.models import Courses
from Courses.models import INTRO_LENGTH_LIMIT, NAME_LENGTH_LIMIT
from Courses.constants import error_message
from Courses.constants import COURSES_NOT_EXIST, FIELD_FORMAT_ERROR


class BaseForm(forms.Form):

    def error_detail(self):
        error_response = {}

        # only return the first validation error
        validation_error_list = list(self.errors.as_data().values())[0]
        validation_error = validation_error_list[0]

        # if error is not about business logic, show it to the frontend
        # else show it to the user
        if validation_error.code not in error_message.keys():
            error_response['status'] = FIELD_FORMAT_ERROR
            error_response['msg'] = error_message[FIELD_FORMAT_ERROR]
            error_response['data'] = self.errors
        else:
            error_response['status'] = validation_error.code
            error_response['msg'] = error_message[validation_error.code]
            error_response['data'] = {}

        return error_response


class CoursesInfoChangeForm(BaseForm):

    courses_id = forms.IntegerField()
    name = forms.CharField(max_length=NAME_LENGTH_LIMIT, error_messages={'max_length': '名字长度不得超过50字'})
    intro = forms.CharField(max_length=INTRO_LENGTH_LIMIT, error_messages={'max_length': '介绍长度不得超过200字'})

    def clean_courses_id(self):
        # field validation of business logic
        courses_id = self.cleaned_data.get('courses_id')
        try:
            Courses.objects.get(pk=courses_id)
        except Courses.DoesNotExist:
            raise ValidationError(_(error_message[COURSES_NOT_EXIST]), code=COURSES_NOT_EXIST)

        return courses_id

    def clean(self):
        if not self.errors:
            # Do your form validation of business logic
            pass

        return self.cleaned_data
