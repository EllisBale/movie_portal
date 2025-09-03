from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, label="First Name", required=True)
    last_name = forms.CharField(max_length=50, label="Last Name", required=True)
    email = forms.EmailField(label="Email Address", required=True)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        return user