from django import forms
from django.forms import SelectDateWidget

from evolution_app.models import Cliente
from django.core import validators


class FormName(forms.ModelForm):
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


TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


class NewUser(forms.ModelForm):
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    data_nascimento = forms.DateField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())

    # A custom empty label with tuple
    field1 = forms.DateField(
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
    )

    class Meta:
        model = Cliente
        fields = '__all__'
