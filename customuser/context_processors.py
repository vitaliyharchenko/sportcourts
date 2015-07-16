from forms import UserLoginForm


def userforms(request):
    return {'loginform': UserLoginForm}