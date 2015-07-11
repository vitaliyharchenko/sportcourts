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


def loggedin_user_context_processor(request):
    context = {'loggedin': request.user.is_authenticated()}
    try:
        if request.user.is_authenticated():
            user = User.objects.get(email=request.user.email)
            context['current_user'] = user
        else:
            context['current_user'] = None
    except User.DoesNotExist:
        pass
    return context