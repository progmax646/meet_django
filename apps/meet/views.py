from datetime import date
from datetime import timedelta

import requests
from dateutil.parser import parse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Task_meet, Status

try:
    from local_settings import API_TELEGRAM
except ImportError:
    from prod_settings import API_TELEGRAM


def login_meet(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/meet')
        else:
            messages.info(request, 'Username or Password incorrect')

    return render(request, 'meet/login.html')


def search_notification(request=None):
    status = {
        'status': True,
        'error': str()
    }
    now = timezone.now()
    after_one_hour__now = now + timedelta(hours=1)
    meets = Task_meet.objects.filter(status=Status.DURING) \
        .filter(date__startswith=now.date()) \
        .filter(date__gte=now) \
        .filter(date__lte=after_one_hour__now)
    for meet in meets:
        if meet.notification:
            print(meet)
            # -1001296908744
            # 7339360
            # 272339311
            try:
                url = f'https://api.telegram.org/bot{API_TELEGRAM}/sendMessage'
                params = {
                    'chat_id': '7339360',
                    'text': f'❗️Встреча «{meet.client_name}» запланирована на сегодня в {timezone.localtime(meet.date).strftime("%H:%M")}'
                }
                requests.get(url=url, params=params)
                meet.notification = False
                meet.save()
            except Exception as e:
                status['status'] = False
                status['error'] = e
                break
    return JsonResponse(status)


@login_required(login_url='/meet/login')
def index(request):
    today = date.today()
    meets_today = Task_meet.objects.filter(date__startswith=today).filter(status=0).order_by('date')
    meets = Task_meet.objects.all().exclude(date__startswith=today).order_by('date')
    meets_last_update = Task_meet.objects.all().order_by('-created_at')[:5] or 'Not found'

    return render(request, 'meet/index.html',
                  {'meets_today': meets_today, 'meets': meets, 'last_meet': meets_last_update,
                   'today': today})


@login_required(login_url='/meet/login')
def create(request):
    if request.method == 'POST':
        type = request.POST['type']
        print(type)
        if int(type) == 2:
            date_ot = request.POST['date_ot']
            date_do = request.POST['date_do']
            comment = request.POST['comment']

            task = Task_meet(user=request.user, type=type, date=date_ot, date_do=date_do,
                             description=comment, status=0)
            try:
                print(task)
                task.save()
                return redirect('/meet')
            except Exception as e:
                return HttpResponse(e)
        if int(type) == 1:
            client_name = request.POST['client-name']
            description = request.POST['description']
            datetime2 = parse(request.POST['date-meet'])
            if 'is_private' in request.POST:
                is_private = True
                task = Task_meet(user=request.user, client_name=client_name, description=description, date=datetime2,
                                 status=0, notification=True)

            else:
                is_private = False
                task = Task_meet(user=request.user, client_name=client_name, description=description, date=datetime2,
                                 status=0)

            try:
                print(task.notification)
                task.save()
                return redirect('/meet')
            except Exception as e:
                return HttpResponse(e)

    return render(request, 'meet/create.html')


@csrf_exempt
def edit(request):
    if request.method == 'POST':
        meet_id = request.POST['id']
        date = request.POST['date']
        url = f'https://api.telegram.org/bot{API_TELEGRAM}/sendMessage'
        meet = Task_meet.objects.get(pk=meet_id)
        meet.date = date
        meet.status = 0
        meet.save()
        params = {
            'chat_id': 1376059804,
            'text': f'Дата клиента {meet.client_name} на встречу изменена на {meet.date}'
        }

        r = requests.get(url=url, params=params)

        return redirect('/meet')


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        meet_id = request.POST['id']
        meet = Task_meet.objects.get(pk=meet_id)
        url = f'https://api.telegram.org/bot{API_TELEGRAM}/sendMessage'
        try:
            meet.status = 2
            meet.save()
            params = {
                'chat_id': 1376059804,
                'text': f'Клиент {meet.client_name} удален с базы встреч'
            }
            r = requests.get(url=url, params=params)
        except Exception as e:
            return HttpResponse(e)
    else:
        meet_id = request.GET['id']
        meet = Task_meet.objects.get(pk=meet_id)
        meet.status = 2
        meet.save()

    return redirect('/meet')


def search(request):
    if request.method == 'POST':
        date = request.POST['date-meet']
        meets = Task_meet.objects.filter(date__startswith=date)
        return render(request, 'meet/search.html', {'meets': meets})


@csrf_exempt
def success_status(request):
    if request.method == 'POST':
        meet_id = request.POST['meet_id']
        meet = Task_meet.objects.get(pk=meet_id)
        meet.status = 1
        try:
            url = 'https://api.telegram.org/bot624760197:AAFUMPSsd3cL59Zvsg00JASKvEuCLUy2yfM/sendMessage'
            params = {
                'chat_id': '1376059804',
                'text': f'Встреча «{meet.client_name}» завершена'
            }

            r = requests.get(url=url, params=params)
            print(r.json())
            meet.save()
            return redirect('/meet')
        except Exception as e:
            HttpResponse(e)
    else:
        meet_id = request.GET['meet_id']
        meet = Task_meet.objects.get(pk=meet_id)
        meet.status = 1
        meet.save()
        return redirect('/meet')


def logout_meet(request):
    logout(request)
    return redirect('/meet/login')


# функция для редактирования бронирования


def get_reserve_page(request, id):
    meet = Task_meet.objects.get(pk=id)
    return render(request, 'meet/edit.html', {'meet': meet})


def edit_reserve(request):
    if request.method == 'POST':
        meet_id = request.POST['meet_id']
        date_ot = request.POST['date_ot']
        date_do = request.POST['date_do']

        meet = Task_meet.objects.get(pk=meet_id)
        meet.date = date_ot
        meet.date_do = date_do
        meet.save()
        return redirect('/meet')

# функция проверки встреч
