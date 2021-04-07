from django.shortcuts import render, HttpResponse, redirect
from .models import Task_meet
from django.db.models.functions import Length
from datetime import date
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import httplib2
import urllib
import requests
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
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



@login_required(login_url='/meet/login')
def index(request):
    today = date.today()
    meets_today = Task_meet.objects.filter(date__startswith=today).filter(status=0)
    meets = Task_meet.objects.all().exclude(date__startswith=today)
    meets_last_update = Task_meet.objects.all().order_by('-created_at')[:5] or 'Not found'

    return render(request, 'meet/index.html', {'meets_today':meets_today, 'meets':meets, 'last_meet':meets_last_update,
                                               'today':today})
@login_required(login_url='/meet/login')
def create(request):

    if request.method == 'POST':
        client_name = request.POST['client-name']
        description = request.POST['description']
        datetime = request.POST['date-meet']

        task = Task_meet(user=request.user, client_name=client_name, description=description, date=datetime, status=0)

        try:
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
    meet_id = request.POST['id']
    meet = Task_meet.objects.get(pk=meet_id)
    url = f'https://api.telegram.org/bot{API_TELEGRAM}/sendMessage'
    try:
        meet.delete()
        params = {
            'chat_id': 1376059804,
            'text': f'Клиент {meet.client_name} удален с базы встреч'
        }
        r = requests.get(url=url, params=params)
    except Exception as e:
        return HttpResponse(e)

    return redirect('/meet')


def search(request):
    if request.method == 'POST':
        date = request.POST['date-meet']
        meets = Task_meet.objects.filter(date__startswith=date)
        return render(request, 'meet/search.html', {'meets':meets})


def success_status(request):
    if request.method == 'POST':
        meet_id = request.POST['meet_id']
        meet = Task_meet.objects.get(pk=meet_id)
        meet.status = 1
        try:
            url = 'https://api.telegram.org/bot624760197:AAFUMPSsd3cL59Zvsg00JASKvEuCLUy2yfM/sendMessage'
            params = {
                'chat_id':'1376059804',
                'text':f'Встреча «{meet.client_name}» завершена'
            }

            r = requests.get(url=url, params=params)
            print(r.json())
            meet.save()
            return redirect('/meet')
        except Exception as e:
            HttpResponse(e)


def logout_meet(request):
    logout(request)
    return redirect('/meet/login')