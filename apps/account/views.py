from django.shortcuts import render, HttpResponse, redirect
from .models import Account_podcategory, Account_category, Account_coming, Account_order, Budget, Color_order
from datetime import date
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
import re
import locale
import random
from . import modules


def login_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/account')
        else:
            messages.info(request, 'Username or Password incorrect')

    return render(request, 'account/login.html')


@login_required(login_url='/account/login')
def index(request):
    categories = Account_category.objects.all()
    budjets = Budget.objects.order_by('category')
    corp_category = Account_category.objects.get(name='Корп расходы')
    kitchen_category = Account_category.objects.get(name='Кухня')
    hoz_category = Account_category.objects.get(name='Хоз товары')
    other_category = Account_category.objects.get(name='Прочие/разовые расходы')
    karantin_category = Account_category.objects.get(name='Карантин')
    if request.method == 'POST':
        month = request.POST['month']
        print(month)
        corp_comings = Account_coming.objects.filter(date__startswith=month).filter(category=corp_category)
        kitchen_comings = Account_coming.objects.filter(date__startswith=month).filter(category=kitchen_category)
        hoz_comings = Account_coming.objects.filter(date__startswith=month).filter(category=hoz_category)
        other_comings = Account_coming.objects.filter(date__startswith=month).filter(category=other_category)
        karantin_comings = Account_coming.objects.filter(date__startswith=month).filter(category=karantin_category)
    else:
        month = date.today().strftime('%Y-%m')
        corp_comings = Account_coming.objects.filter(date__startswith=month).filter(category=corp_category)
        kitchen_comings = Account_coming.objects.filter(date__startswith=month).filter(category=kitchen_category)
        hoz_comings = Account_coming.objects.filter(date__startswith=month).filter(category=hoz_category)
        other_comings = Account_coming.objects.filter(date__startswith=month).filter(category=other_category)
        karantin_comings = Account_coming.objects.filter(date__startswith=month).filter(category=karantin_category)
    # категории

    # приходы корп
    corp_come_summa = []
    for corp_come_sum in corp_comings:
        corp_come_summa.append(corp_come_sum.summa)

    # приходы кухня
    kitchen_come_summa = []
    for kitchen_come_sum in kitchen_comings:
        kitchen_come_summa.append(kitchen_come_sum.summa)


    # приходы хоз товары
    hoz_come_summa = []
    for hoz_come_sum in hoz_comings:
        hoz_come_summa.append(hoz_come_sum.summa)


    # приходы прочие разовые расходы
    other_come_summa = []
    for other_come_sum in other_comings:
        other_come_summa.append(other_come_sum.summa)

    # приходы Карантин
    karantin_come_summa = []
    for karantin_come_sum in karantin_comings:
        karantin_come_summa.append(karantin_come_sum.summa)

    # всего приход

    total_come_summa = sum(corp_come_summa)+sum(kitchen_come_summa)+sum(other_come_summa)+sum(karantin_come_summa)+sum(hoz_come_summa)

    # расходы

    # корп расходы

    corp_order = Account_order.objects.filter(category=corp_category)
    corp_summa_order_total = []

    for corp_order_item in corp_order:
        corp_summa_order_total.append(corp_order_item.summa)

    # кухня расходы

    kitchen_order = Account_order.objects.filter(category=kitchen_category)
    kitchen_summa_order_total = []

    for kitchen_order_item in kitchen_order:
        kitchen_summa_order_total.append(kitchen_order_item.summa)

    # хоз товары расходы
    hoz_order = Account_order.objects.filter(category=hoz_category)
    hoz_summa_order_total = []

    for hoz_order_item in hoz_order:
        hoz_summa_order_total.append(hoz_order_item.summa)

    # прочие расходы
    other_order = Account_order.objects.filter(category=other_category)
    other_summa_order_total = []

    for other_order_item in other_order:
        other_summa_order_total.append(other_order_item.summa)

    # карантин

    karantin_order = Account_order.objects.filter(category=karantin_category)
    karantin_summa_order_total = []

    for karantin_order_item in karantin_order:
        karantin_summa_order_total.append(karantin_order_item.summa)

    # всего расход
    total_order_summa = sum(corp_summa_order_total) + sum(kitchen_summa_order_total) + sum(other_summa_order_total) + sum(karantin_summa_order_total)

    # остатки
    corp_ost = sum(corp_come_summa)-sum(corp_summa_order_total)
    kitchen_ost = sum(kitchen_come_summa)-sum(kitchen_summa_order_total)
    hoz_ost = sum(hoz_come_summa) - sum(hoz_summa_order_total)
    other_ost = sum(other_come_summa) - sum(other_summa_order_total)
    karantin_ost = sum(karantin_come_summa) - sum(karantin_summa_order_total)


    total_ost = corp_ost+kitchen_ost+hoz_ost+other_ost+karantin_ost


    return render(request, 'account/index.html', {'categories':categories, 'corp_come_summa':sum(corp_come_summa),
                                                  'kitchen_come_summa':format(sum(kitchen_come_summa), '10,d'), 'hoz_come_summa':format(sum(hoz_come_summa), '10,d'),
                                                  'other_come_summa':format(sum(other_come_summa), '10,d'), 'karantin_come_summa':format(sum(karantin_come_summa), '10,d'),
                                                  'total_summa':format(total_come_summa, '10,d'), 'corp_summa_order_total':format(sum(corp_summa_order_total), '10,d'),
                                                  'kitchen_summa_order_total':format(sum(kitchen_summa_order_total), '10,d'), 'hoz_summa_order_total':format(sum(hoz_summa_order_total), '10,d'),
                                                  'other_summa_order_total':format(sum(other_summa_order_total), '10,d'), 'karantin_summa_order_total':format(sum(karantin_summa_order_total), '10,d'),
                                                  'total_order_summa':format(total_order_summa, '10,d'), 'corp_ost':format(corp_ost, '10,d'), 'kitchen_ost': format(kitchen_ost, '10,d'),'hoz_ost':format(hoz_ost, '10,d'),
                                                  'other_ost':format(other_ost ,'10,d'), 'karantin_ost': format(karantin_ost, '10,d'), 'total_ost':format(total_ost, '10,d'), 'month':month, 'budjets':budjets})


@login_required(login_url='/account/login')
def create(request):
    if request.method == 'POST':
        # поиск категории
        category_id = request.POST['category']
        summa = request.POST['summa']
        date = request.POST['date']

        category = Account_category.objects.get(pk=category_id)
        # создание прихода

        c = Account_coming.objects.filter(date__startswith='2021-03')

        coming = Account_coming()

        coming.category = category
        coming.date = date
        coming.summa = summa

        try:
            coming.save()
            return redirect('/account')
        except Exception as e:
            return HttpResponse(e)


    categories = Account_category.objects.all()
    return render(request, 'account/create.html', {'categories':categories})


# создание расхода
def create_order(request):
    date = datetime.today().strftime("%Y-%m-%d")
    color_obj = Color_order.objects.filter(date=date)

    if request.method == 'POST':
        category_s = request.POST['category']
        podcategory = request.POST['podcategory']
        if int(podcategory) == 0:
            account_podcategory = None
        if int(podcategory) > 0:
            account_podcategory = Account_podcategory.objects.get(pk=podcategory)
        summa = request.POST['summa']
        description = request.POST['description']
        date = request.POST['date']

    #     creating order
        category = Account_category.objects.get(pk=category_s)
        if color_obj:
            color = color_obj
            account_order = Account_order(category=category, podcategory=account_podcategory, summa=summa,
                                          description=description, date=date, color=color[0])
        else:
            r = modules.random_color()
            color = Color_order.objects.create(color=r, date=date)
            color.save()
            account_order = Account_order(category=category, podcategory=account_podcategory, summa=summa,
                                          description=description, date=date, color=color)

        try:
            account_order.save()
            return redirect('/account')
        except Exception as e:
            return HttpResponse(e)

    account_categories = Account_category.objects.all()
    account_podcategories = Account_podcategory.objects.all()
    return render(request, 'account/create_order.html', {'account_categories':account_categories, 'account_podcategories':account_podcategories, 'date':date})


@csrf_protect
def order_views(request, id):
    date = request.POST['date']
    if id == 1:
        account_category = Account_category.objects.get(pk=id)
        # интернет
        internet_podcategories = Account_podcategory.objects.get(name='Интернет')
        internet_orders = Account_order.objects.filter(podcategory=internet_podcategories)
        internet_orders_summa = []
        for internet in internet_orders:
            internet_orders_summa.append(internet.summa)

        # Телефонная связь
        tel_podcategories = Account_podcategory.objects.get(name='Телефонная связь')
        tel_orders = Account_order.objects.filter(podcategory=tel_podcategories)
        tel_orders_summa = []
        for tel in tel_orders:
            tel_orders_summa.append(tel.summa)

        # Поездки на такси/личное авто
        travel_podcategories = Account_podcategory.objects.get(name='Поездки на такси/личное авто')
        travel_orders = Account_order.objects.filter(podcategory=travel_podcategories)
        travel_orders_summa = []
        for travel in travel_orders:
            travel_orders_summa.append(travel.summa)

        # Проездные карточки
        proezd_podcategories = Account_podcategory.objects.get(name='Проездные карточки')
        proezd_orders = Account_order.objects.filter(podcategory=proezd_podcategories)
        proezd_orders_summa = []
        for proezd in proezd_orders:
            proezd_orders_summa.append(proezd.summa)

        # Мобильная связь
        mob_podcategories = Account_podcategory.objects.get(name='Мобильная связь')
        mob_orders = Account_order.objects.filter(podcategory=mob_podcategories)
        mob_orders_summa = []
        for mob in mob_orders:
            mob_orders_summa.append(mob.summa)

        # 	Расход по курьеру/топливо
        cur_podcategories = Account_podcategory.objects.get(name='Расход по курьеру/топливо')
        cur_orders = Account_order.objects.filter(podcategory=cur_podcategories)
        cur_orders_summa = []
        for cur in cur_orders:
            cur_orders_summa.append(cur.summa)

        # 	Печати для клиентов
        pech_podcategories = Account_podcategory.objects.get(name='Печати для клиентов')
        pech_orders = Account_order.objects.filter(podcategory=pech_podcategories)
        pech_orders_summa = []
        for pech in pech_orders:
            pech_orders_summa.append(pech.summa)

        # 	Эцп ключи для клиентов
        ecp_podcategories = Account_podcategory.objects.get(name='Эцп ключи для клиентов')
        ecp_orders = Account_order.objects.filter(podcategory=ecp_podcategories)
        ecp_orders_summa = []
        for ecp in ecp_orders:
            ecp_orders_summa.append(ecp.summa)

        # 		Коммунальные услуги офиса
        com_podcategories = Account_podcategory.objects.get(name='Коммунальные услуги офиса')
        com_orders = Account_order.objects.filter(podcategory=com_podcategories)
        com_orders_summa = []
        for com in com_orders:
            com_orders_summa.append(com.summa)

        # 		Почтовые расходы
        other_podcategories = Account_podcategory.objects.get(name='Почтовые расходы')
        other_orders = Account_order.objects.filter(podcategory=other_podcategories)
        other_orders_summa = []
        for other in other_orders:
            other_orders_summa.append(other.summa)

        # 		Разовые расходы из корп средств
        raz_podcategories = Account_podcategory.objects.get(name='Разовые расходы из корп средств')
        raz_orders = Account_order.objects.filter(podcategory=raz_podcategories)
        raz_orders_summa = []
        for raz in raz_orders:
            raz_orders_summa.append(raz.summa)

        total_corp_order = Account_order.objects.filter(category=account_category)
        total_c = []
        for i in total_corp_order:
            total_c.append(i.summa)

        return render(request, 'account/table_order_corp.html', {'internet_orders_summa':format(sum(internet_orders_summa), '10,d'), 'tel_orders_summa':format(sum(tel_orders_summa), '10,d'),
                                                                 'travel_orders_summa':format(sum(travel_orders_summa), '10,d'), 'proezd_orders_summa':format(sum(proezd_orders_summa), '10,d'),
                                                                 'mob_orders_summa':format(sum(mob_orders_summa), '10,d'), 'cur_orders_summa':format(sum(cur_orders_summa), '10,d'), 'pech_orders_summa':format(sum(pech_orders_summa), '10,d'),
                                                                 'ecp_orders_summa':format(sum(ecp_orders_summa), '10,d'), 'com_orders_summa':format(sum(com_orders_summa), '10,d'),
                                                                 'other_orders_summa':format(sum(other_orders_summa), '10,d'), 'raz_orders_summa':format(sum(raz_orders_summa), '10,d'), 'total_c':format(sum(total_c), '10,d'), 'date':date})
    else:
        account_category = Account_category.objects.get(pk=id)
        account_orders = Account_order.objects.filter(date__startswith=date, category=account_category)
        total_order_summa = []
        for item in account_orders:
            total_order_summa.append(item.summa)
        return render(request, 'account/table_order.html', {'account_orders':account_orders, 'total_order_summa':format(sum(total_order_summa), '10,d')})


def podorder_views(request, id, date):
    podcategory = Account_podcategory.objects.get(pk=id)
    account_orders = Account_order.objects.filter(date__startswith=date, podcategory=podcategory)
    total_order_summa = []
    for item in account_orders:
        total_order_summa.append(item.summa)

    return render(request, 'account/table_podcategory_order.html', {'account_orders':account_orders, 'total_order_summa':format(sum(total_order_summa), '10,d')})


def edit_budget(request, id):
    summa = request.GET['summa']
    budjet = Budget.objects.get(pk=id)
    budjet.summa = int(summa)
    budjet.save()
    return redirect('/account')
