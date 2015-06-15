from django.shortcuts import render, redirect
from django.contrib import auth
from forms import UserLoginForm


# Create your views here.
def login(request):
    args = dict()
    args['form'] = UserLoginForm
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.data['password']
            user = auth.authenticate(username=email, password=password)
            if not user:
                return redirect('index')
            else:
                auth.login(request, user)
                return redirect('index')

    return render(request, 'login.html', args)


def reg(request):
    args = {}
    return render(request, 'index.html', args)


def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)