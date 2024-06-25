# File to disable signup in allauth

from django.conf import settings

from allauth.account.adapter import DefaultAccountAdapter


# класс для отключения возможности регистрации
class CustomAccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        allow_signups = super(
            CustomAccountAdapter, self).is_open_for_signup(request)
        return getattr(settings, 'ACCOUNT_ALLOW_SIGNUPS', allow_signups)
