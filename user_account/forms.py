from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model

User = get_user_model()

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


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email