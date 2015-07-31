# coding=utf-8
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from forms import UserLoginForm, UserRegistrationForm, EmailForm, UpdateForm, ChangePasswordForm
from django.contrib import messages
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from models import Activation
from django.core import signing
from utils import mailing, api, vkontakte
from utils.witgets import JasnyImageModelField
from models import User
import urllib
from django.core.files import File


# Create your views here.

# Return error for ajax
class _Error(api.Error):
    @staticmethod
    def already_registered(user):
        if user:
            # data = {'user_id': user.id, 'name': user}
            return api.Error(1, u'Already registered')
            # return api.Error(1, u'Already registered as ({}) {}'.format(user.id, data['name']), data=data)
        else:
            return api.Error(1, u'Already registered')


    @staticmethod
    def already_verified(token):
        return api.Error(2, 'Already verified', data={'token': token})

    @staticmethod
    def invalid_email(email):
        return api.Error(3, 'Invalid email', data={'email': email})


# login view
def login(request):
    if request.user.is_authenticated():
        return redirect('index')
    context = dict()
    return_path = request.META.get('HTTP_REFERER', '/')
    shortcut = lambda: render(request, 'login.html', context)

    if request.method == 'GET':
        if 'code' in request.GET:
            code = request.GET['code']
            try:
                access_token, user_id = vkontakte.auth_code(code, reverse('login'))
            except vkontakte.AuthError as e:
                messages.warning(request, 'Ошибка авторизации')
                return shortcut()
            try:
                user = User.objects.get(vkuserid=user_id)
                print user
                backend = auth.get_backends()[0]
                user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
                auth.login(request, user)
                print 'success auth'
                try:
                    next = request.GET.__getitem__('next')
                    return redirect(next)
                except KeyError:
                    print return_path.rsplit('/', 1)[1]
                    if return_path.rsplit('/', 1)[1] != 'login':
                        return redirect(return_path)
                    else:
                        return redirect('index')
            except User.DoesNotExist:
                messages.warning(request, 'Такой пользователь не найден')
                return shortcut()


    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email, password = form.cleaned_data['email'], form.data['password']
            user = auth.authenticate(username=email, password=password)
            if not user:
                messages.warning(request, "Пользователь не найден!")
                context['form'] = form
                return shortcut()
            else:
                auth.login(request, user)
                try:
                    next = request.GET.__getitem__('next')
                    return redirect(next)
                except KeyError:
                    if return_path.rsplit('/', 1)[1] != 'login':
                        return redirect(return_path)
                    else:
                        return redirect('index')
        else:
            messages.warning(request, "Введенные данные некорректны!")
            context['form'] = form
            return shortcut()

    context['form'] = UserLoginForm
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
        shortcut = lambda: render(request, 'reg.html', context)

        if 'code' in request.GET:
            code = request.GET['code']
            try:
                access_token, user_id = vkontakte.auth_code(code, request.path)
            except vkontakte.AuthError as e:
                messages.warning(request, 'Ошибка авторизации')
                context['form'] = UserRegistrationForm(request.POST)
                return shortcut()
            if User.objects.filter(vkuserid=user_id).count() == 0 and user_id != 0:
                vkuser = vkontakte.api(access_token, 'users.get', fields=['sex', 'bdate', 'city',
                                                                          'photo_max', 'contacts'])[0]
                vkdata = dict()
                vkdata['vkuserid'] = user_id

                vkdata['first_name'] = vkuser['first_name']
                vkdata['last_name'] = vkuser['last_name']

                if 'mobile_phone' in vkuser:
                    vkdata['phone'] = vkuser['mobile_phone']
                elif 'home_phone' in vkuser:
                    vkdata['phone'] = vkuser['home_phone']
                else:
                    vkdata['phone'] = None

                if vkuser['sex']:
                    if vkuser['sex'] == 2:
                        vkdata['sex'] = 'm'
                    elif vkuser['sex'] == 1:
                        vkdata['sex'] = 'f'
                else:
                    vkdata['sex'] = None

                if 'bdate' in vkuser:
                    if len(vkuser['bdate']) == 10:
                        vkdata['bdate'] = vkuser['bdate']
                    elif vkuser['bdate'] != '':
                        messages.warning(request, 'Неполная дата')
                        vkdata['bdate'] = vkuser['bdate']
                else:
                    vkdata['bdate'] = None

                if 'photo_max' in vkuser:
                    url = vkuser['photo_max']
                    vkdata['avatar'] = url
                    context['avatar_url'] = url

                context['vkdata'] = vkdata
                context['vkuserid'] = user_id

                initial = {'email': email,
                           'sex': vkdata['sex'],
                           'first_name': vkdata['first_name'],
                           'last_name': vkdata['last_name'],
                           'phone': vkdata['phone'],
                           'bdate': vkdata['bdate'],
                           'vkuserid': user_id,
                           'avatar': vkdata['avatar']
                           }

                context['form'] = UserRegistrationForm(initial=initial)
                return shortcut()
            else:
                messages.warning(request, 'Такой пользователь уже зарегестрирован в системе')

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                print form.cleaned_data
                user = form.save(commit=False)
                user.set_password(user.password)
                activation = Activation.objects.get(email=user.email)
                activation.status = activation.REGISTERED
                activation.save()
                user.save()
                newuser = auth.authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                auth.login(request, newuser)
                return redirect('index')
            else:
                context['form'] = form
                messages.success(request, "Form is not valid!")
                return shortcut()
        context['form'] = UserRegistrationForm(initial={'email': email})
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
        user = User.objects.filter(email=email)
        print user
        if user.count() > 0:
            raise _Error.already_registered(user)
        else:
            raise _Error.already_registered(None)


def verify_email(request, token):
    try:
        signing.loads(token)
        activation = Activation.objects.get(token=token)
    except:
        messages.warning(request, u'Неверный код.Возможно, это старое письмо.')
        context = {'form': None}
        return render(request, 'reg.html', context)
    if activation.status == Activation.EMAIL_SENT:
        activation.status = Activation.EMAIL_VERIFIED
        activation.save()
    elif activation.status == Activation.REGISTERED:
        return redirect('login', token=token)
    return redirect('reg', token=token)


# customuser views #
def userslist(request):
    try:
        query = request.GET.__getitem__('q')
        users = User.objects.filter(first_name__icontains=query) | User.objects.filter(last_name__icontains=query)
        context = {'users': users, 'query': query}
    except KeyError:
        context = {'users': User.objects.all()}
    return render(request, 'users.html', context)


def userdetail(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    if request.user.pk == user.pk:
        context['current'] = True
    else:
        pass
    return render(request, 'user.html', context)


# TODO: create my own context processor for forms
# FIXME: update form view
@login_required
def update(request):
    user = User.objects.get(email=request.user.email)
    form = UpdateForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно сохранено!", extra_tags='info')
            return redirect('user_update')
        else:
            messages.warning(request, "Некорректные данные", extra_tags='info')
    return render(request, 'user_update.html', {'form': form, 'passform': ChangePasswordForm})


@login_required
def changepass(request):
    form = ChangePasswordForm(request.POST)
    u = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        if form.is_valid():
            password = form.cleaned_data.get("password")
            u.set_password(password)
            u.save()
            validation = auth.authenticate(username=u.email, password=password)
            auth.login(request, validation)
            messages.success(request, "Пароль изменен", extra_tags='changepass')
        else:
            messages.warning(request, "Введенные пароли некорректны!", extra_tags='changepass')
        return render(request, 'user_update.html', {'form': UpdateForm(instance=u), 'passform': form})
    return redirect('user_update')


@require_GET
def setvkid(request):
    pass