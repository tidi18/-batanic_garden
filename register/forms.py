from django import forms
from captcha.fields import CaptchaField
from .models import Visitor


class RegisterForm(forms.ModelForm):
    time = forms.Select(attrs={'class': 'form-control'})
    name = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = Visitor
        fields = ['time', 'name', 'last_name', 'captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['time'].widget.attrs['placeholder'] = ''
            self.fields['name'].widget.attrs['placeholder'] = 'Ваше имя'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Ваша фамилия'
            self.fields['captcha'].widget.attrs.update({"placeholder": 'Напишите текст с картинки'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class TokenCheckForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    token = forms.CharField(label='Токен', max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        fields = ['name', 'last_name', 'token']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['name'].widget.attrs['placeholder'] = 'Ваше имя'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Ваша фамилия'
            self.fields['token'].widget.attrs['placeholder'] = 'Введите ваш токен'
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})
