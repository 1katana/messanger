from django import forms

class Authorization(forms.Form):

    username=forms.CharField(max_length=100,label="Имя пользователя", widget=forms.TextInput(attrs={'class':'forms-input'}))

    password=forms.CharField(max_length=100,label="Пароль", widget=forms.PasswordInput(attrs={'class':'forms-input'}))
