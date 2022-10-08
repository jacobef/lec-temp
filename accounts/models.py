from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class LECUser(AbstractUser):

    class AccountTypes(models.TextChoices):
        PARENT = "parent", "Parent"
        DIRECTOR = "director", "Director"
        SITE_ADMIN = "site_admin", "Site Admin"
    ALL_ACCOUNT_TYPES = [account_type for account_type in AccountTypes]

    account_type = models.CharField(
        max_length=len(max(AccountTypes, key=len)),  # sets it to the maximum length of any value in AccountTypes
        choices=AccountTypes.choices
    )

    class NoSuchAccountType(Exception):
        pass

    def in_database(self):
        return LECUser.objects.filter(pk=self.pk).exists()

    # This entire method is a mess, but I don't know a better way
    def save(self, *args, **kwargs):
        """Saves the user to the database. Adds the user to the group that corresponds to its account_type.
        Removes the user from groups that were added by an older account_type."""

        possible_account_types = self.ALL_ACCOUNT_TYPES

        # 1) Raises an exception if account_type is set to an invalid value.
        #    Doesn't raise an exception if account_type is an empty string, so that Django's createsuperuser command
        #    (which only sets username, password, and email, and leaves every other string attribute as an empty string)
        #    works.
        if self.account_type and (self.account_type not in possible_account_types):
            raise LECUser.NoSuchAccountType(
                f"""self.account_type ("{self.account_type}") is not set to a valid value.
                It should be in LECUser.AccountTypes.Argh, or be an empty string.""")

        # 2) Checks if the user already has an account type.
        #    If it does, sets old_account_type_group (local variable) to the group corresponding to that account type.
        #    If not, sets old_account_type_group to None.
        if self.in_database():
            user_account_types = [account_type for account_type in possible_account_types
                                  if self.groups.filter(name=account_type).exists()]
            if len(user_account_types) == 0:
                old_account_type_group = None
            elif len(user_account_types) == 1:
                old_account_type_group = self.groups.get(name=user_account_types[0])
            else:
                raise LECUser.MultipleObjectsReturned(
                    "User appears to have multiple account types. A user can only have one account type.")
        else:
            old_account_type_group = None

        # 3) Saves the user to the database if they're not already in the database.
        #    This step is necessary because in order to add or remove groups
        #    (which will be done in the following steps), the user needs to be in the database.
        if not self.in_database():
            super().save(*args, **kwargs)

        # 4) Removes the user from their old account type group, if they have one.
        if old_account_type_group is not None:
            self.groups.remove(old_account_type_group)

        # 5) Adds the user to the group corresponding to their new account type
        #    (unless self.account_type is empty; see step 1)
        if self.account_type:
            new_account_type_group = Group.objects.get(name=self.account_type)
            self.groups.add(new_account_type_group)

        # 6) If the user is a site admin, give them access to the Django admin site (which is what is_staff does).
        #    Needs to be here because even though the site admin group will have all permissions,
        #    is_staff doesn't count as a permission (for some reason).
        if self.account_type == self.AccountTypes.SITE_ADMIN:
            self.is_staff = True

        # 7) Finally, saves the user to the database again, in order to save the changes that were made in steps 4-6.
        super().save(*args, **kwargs)
