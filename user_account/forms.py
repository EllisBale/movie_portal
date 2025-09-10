from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=50, label="First Name",
        required=True
    )
    last_name = forms.CharField(
        max_length=50, label="Last Name",
        required=True
    )
    email = forms.EmailField(label="Email Address", required=True)

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50, required=True,
        label='First Name'
        )

    last_name = forms.CharField(
        max_length=50, required=True,
        label="Last Name"
        )
    email = forms.EmailField(required=True, label='Email Address')

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.strip():
            raise forms.ValidationError("First name is required.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.strip():
            raise forms.ValidationError("Last name is required.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if (
            User.objects
            .exclude(pk=self.instance.pk)
            .filter(email=email)
            .exists()
        ):
            raise forms.ValidationError("This email is already in use.")
        return email
