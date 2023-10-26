# Далее нам нужна сама форма form, которая будет отображаться в шаблоне для пользователей, отвечать за корректность введенных данных 
# и сохранять результат ввода в базе данных.

from django.forms import ModelForm, CharField, TextInput
from .models import Tag


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']