from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from myapp.models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model=Resume
        fields="__all__"

class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField()
    confirm_password=forms.CharField()
    terms_accepted = forms.BooleanField()

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirm_password
    
    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Use the built-in Django password validators
        try:
            validate_password(password)  # This will apply the validators from AUTH_PASSWORD_VALIDATORS
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return password
