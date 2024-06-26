from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class Authorization(AuthenticationForm):

    username=forms.CharField(max_length=100,label="Имя пользователя", widget=forms.TextInput(attrs={'class':'forms-input',
                                                                                                    'placeholder':'Имя пользователя'}))

    password=forms.CharField(max_length=100,label="Пароль", widget=forms.PasswordInput(attrs={'class':'forms-input',
                                                                                              'placeholder':'Пароль'}))
    class Meta:
        model=get_user_model()
        field=['username','password']


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label="Имя пользователя",
                               widget=forms.TextInput(attrs={'class': 'forms-input',
                                                             'placeholder': 'Имя пользователя'}))

    password = forms.CharField(max_length=100, label="Пароль", widget=forms.PasswordInput(attrs={'class': 'forms-input',
                                                                                                 'placeholder': 'Пароль'}))

    password2 = forms.CharField(max_length=100, label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'forms-input',
                                                                                                 'placeholder': 'Повтор пароля'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        # labels = {
        #     'email': 'E-mail',
        #     'first_name': "Имя",
        #     'last_name': "Фамилия",
        # }
        widgets={
            'email': forms.TextInput(attrs={'class': 'forms-input',
                                                             'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'class': 'forms-input',
                                                             'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'forms-input',
                                                             'placeholder': 'Фамилия'}),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email


# class FileUploadForm()