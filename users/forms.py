
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.USER_ROLES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
            # After saving user, update role in profile
            user.userprofile.role = self.cleaned_data['role']
            user.userprofile.save()

        return user
