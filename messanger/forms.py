from django import forms

class Authorization(forms.Form):

    name=forms.CharField(max_length=100)

    def name_toString(self):
        return str(self.name)
    #password=forms.CharField(max_length=100)