from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)
    age = forms.IntegerField(label="Возраст")
