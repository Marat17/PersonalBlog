from django import forms
from .models import Mypost
from django.utils.translation import ugettext_lazy as _


class CreateNewPost(forms.ModelForm):
    header = forms.CharField(max_length=15, help_text=_('Title:'))
    text = forms.CharField(max_length=140, help_text=_('Please type your new post here:'), widget=forms.Textarea)

    class Meta:
        model = Mypost
        fields = ('header','text', )