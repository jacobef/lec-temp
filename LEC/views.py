from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import LECUser


def index(request):
    if request.user.is_authenticated:
        # This assertion is needed for IDEs to recognize that request.user is an LECUser.
        #  It theoretically could be an AnonymousUser if the user is not logged in, but
        #  we just confirmed they're authenticated, so they should always be an LECUser.
        assert isinstance(request.user, LECUser)

        match request.user.account_type:
            case LECUser.AccountTypes.SITE_ADMIN:
                return HttpResponse("site admin app doesn't exist yet")
            case LECUser.AccountTypes.ORG_ADMIN:
                return redirect(reverse("org_admin:home"))
            case LECUser.AccountTypes.GUARDIAN:
                return redirect(reverse("guardian:home"))
            case _:
                # TODO make actual error page, option to report etc
                return HttpResponse("Internal error: Your account type either is not set, or was not set to a valid value.")
    else:
        return redirect(reverse("accounts:login"))

