from django import forms
from .models import Mypost


class CreateNewPost(forms.ModelForm):
    text = forms.CharField(max_length=140, help_text='Please type your new post here:', widget=forms.Textarea)

    class Meta:
        model = Mypost
        fields = ('text',)