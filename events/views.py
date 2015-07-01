# coding=utf-8
from django.shortcuts import render, HttpResponse
from models import Event, UserGameAction
from customuser import User
from django.views.decorators.http import require_POST
import json


# Return error for ajax
def error_response(description):
    error = {'error_description': description}
    return HttpResponse(json.dumps({'error': error}), content_type="application/json")


# Create your views here.
def events(request):
    context = {'events': Event.objects.all()}
    try:
        if request.user.is_authenticated():
            user = User.objects.get(email=request.user.email)
            context['current_user'] = user
        else:
            context['current_user'] = None
    except User.DoesNotExist:
        pass
    return render(request, 'events.html', context)


# TODO: error rendering in json format using api._Error
@require_POST
def eventaction(request):
    if request.is_ajax():
        action = request.POST["action"]
        event_id = request.POST["event_id"]
        if request.user.is_authenticated():
            user = User.objects.get(email=request.user.email)
            event = Event.objects.get(id=event_id)
            if event.type == 'game':
                game = event.as_leaf_class()
                if action == 'subscribe':
                    set_action = UserGameAction.SUBSCRIBED
                elif action == 'unsubscribe':
                    set_action = UserGameAction.UNSUBSCRIBED
                elif action == 'reserve':
                    set_action = UserGameAction.RESERVED
                elif action == 'unreserve':
                    set_action = UserGameAction.UNRESERVED
                try:
                    usergameaction = UserGameAction.objects.get(game=game, user=user)
                    current_action = usergameaction.action
                    if current_action == set_action:
                        return error_response('Action already save')
                    else:
                        if set_action == UserGameAction.SUBSCRIBED and not game.has_place:
                            return error_response('There is no place now')
                        elif set_action == UserGameAction.RESERVED and not game.has_reserved_place:
                            return error_response('There is no place now')
                        usergameaction.action = set_action
                        usergameaction.save()
                        return render(request, 'tagtemplates/event.html', {'event': game, 'current_user': user})
                except UserGameAction.DoesNotExist:
                    UserGameAction.objects.create(game=game, user=user, action=set_action)
                    return render(request, 'tagtemplates/event.html', {'event': game, 'current_user': user})
            else:
                return error_response('Unknown type of event')
        else:
            return error_response('Not auth')
    else:
        return error_response('Not AJAX')