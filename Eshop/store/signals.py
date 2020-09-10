from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('userer',user)
    request.session['ii'] = user.id
    # request.session['ussser'] = user.id
    print('heelll',request.session['ii'])
