# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib import auth
from forms import UserLoginForm, UserRegistrationForm, EmailForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from models import Activation
from django.core import signing
from utils import mailing, api
from models import User, Team


# Create your views here.

# Return error for ajax
class _Error(api.Error):
    @staticmethod
    def already_registered(user):
        data = {'user_id': user.id, 'name': user.first_name + u' ' + user.last_name}
        return api.Error(1, u'Already registered as ({}) {}'.format(user.id, data['name']), data=data)

    @staticmethod
    def already_verified(token):
        return api.Error(2, 'Already verified', data={'token': token})

    @staticmethod
    def invalid_email(email):
        return api.Error(3, 'Invalid email', data={'email': email})


# login view
def login(request):
    context = dict()
    context['form'] = UserLoginForm
    shortcut = lambda: render(request, 'login.html', context)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.data['password']
            user = auth.authenticate(username=email, password=password)
            if not user:
                messages.success(request, "Not user!")
                return shortcut()
            else:
                auth.login(request, user)
                return redirect('index')
        else:
            messages.success(request, "Form is not valid!")
            return shortcut()
    return shortcut()


# registration after email verify
def reg(request, token):
    if request.user.is_authenticated():
        return render(request, 'index.html')
    else:
        try:
            activation = Activation.objects.get(token=token)
        except Activation.DoesNotExist:
            raise Exception("Неверный код")
        if activation.status == activation.REGISTERED:
            return render(request, 'login.html')
        elif activation.status == activation.EMAIL_SENT:
            raise Exception("Сначала подтвердите емейл")
        context = dict()
        email = Activation.objects.get(token=token).email
        context['form'] = UserRegistrationForm(initial={'email': email})
        shortcut = lambda: render(request, 'reg.html', context)

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(user.password)
                activation = Activation.objects.get(email=user.email)
                activation.status = activation.REGISTERED
                activation.save()
                user.save()
                return redirect('login')
            else:
                messages.success(request, "Form is not valid!")
                return shortcut()
        return shortcut()


def logout(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    auth.logout(request)
    return redirect(return_path)


# begin registration
@require_POST
@api.handle_error_decor
def add_email_activation(request):
    form = EmailForm(request.POST)
    if not form.is_valid():
        raise _Error.invalid_email(request.POST['email'])
    email = form.cleaned_data['email']
    token = create_token(email)
    mailing.verify_email(email, token)
    return {'email': email}


def create_token(email):
    check_email(email)
    token = signing.dumps({'email': email})
    try:
        activation = Activation.objects.get(pk=email)
    except Activation.DoesNotExist:
        Activation.objects.create(email=email, status=Activation.EMAIL_SENT, token=token)
    else:
        activation.token = token
        activation.save()
    return token


def check_email(email):
    try:
        activation = Activation.objects.get(pk=email)
    except Activation.DoesNotExist:
        return
    if activation.status == Activation.EMAIL_VERIFIED:
        raise _Error.already_verified(activation.token)
    if activation.status == Activation.REGISTERED:
        user = User.objects.get(email=email)
        raise _Error.already_registered(user)


def verify_email(request, token):
    try:
        signing.loads(token)
        activation = Activation.objects.get(token=token)
    except:
        return messages.success(request, u'Неверный код')
        # TODO: page with veriication error render
    if activation.status == Activation.EMAIL_SENT:
        activation.status = Activation.EMAIL_VERIFIED
        activation.save()
    elif activation.status == Activation.REGISTERED:
        return redirect('login', token=token)
    return redirect('reg', token=token)


# customuser views #
def userslist(request):
    context = {'users': User.objects.all()}
    return render(request, 'users.html', context)


def userdetail(request, user_id):
    context = {'user': User.objects.get(id=user_id)}
    return render(request, 'user.html', context)


def teamslist(request):
    context = {'teams': Team.objects.all()}
    return render(request, 'teams.html', context)


def teamdetail(request, team_id):
    context = {'team': Team.objects.get(id=team_id)}
    return render(request, 'team.html', context)