from django.contrib.auth.backends import ModelBackend

from models import User


class VkontakteAuthBackend(ModelBackend):
    def authenticate(self, *args, **kwargs):
        vkuserid = kwargs.get('vkuserid', None)
        if vkuserid:
            try:
                return User.objects.get(vkuserid=vkuserid)
            except User.DoesNotExist:
                pass
        return None