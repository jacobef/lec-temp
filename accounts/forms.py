from django.contrib.auth.forms import UserCreationForm

from accounts.models import LECUser


class LECUserCreationForm(UserCreationForm):
    class Meta:
        model = LECUser
        fields = ["account_type", "username", "first_name", "last_name", "email", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['account_type'] == LECUser.AccountTypes.ORG_ADMIN:
            self.instance.requesting_org_admin = True
        elif cleaned_data['account_type'] == LECUser.AccountTypes.SITE_ADMIN:
            self.instance.requesting_site_admin = True
        cleaned_data['account_type'] = LECUser.AccountTypes.GUARDIAN
        return cleaned_data
