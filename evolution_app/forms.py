from django import forms
from evolution_app.models import User
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(widget=forms.HiddenInput,
                                 required=False,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Gotcha BOT")
        return botcatcher


class Login(forms.Form):
    name = forms.CharField()
    password = forms.CharField()


class NewUser(forms.Form):
    name = forms.CharField()

    class Meta:
        model = User
        fields = '__all__'
