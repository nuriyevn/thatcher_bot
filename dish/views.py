from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404, HttpResponseRedirect
from .forms import DishForm
from dish.models import DishType, Dish, Provider

import os
def secure(request):
    return render(request, 'dish/secureinput.html', {})
def sign(request):
    return render(request, 'dish/sign.html', {})

def calculate(request):

    sum = 0
    main_dish_flag = False
    main_dish_price = DishType.objects.filter(name='main_dish')[0].generic_price

    queryDict = request.GET
    myDict = dict(queryDict)

    if 'ids[]' in myDict.keys():
        for key in myDict['ids[]']:

            dish = Dish.objects.filter(pk=key)
            dish_type = str(dish[0].type)
            dish_cost = float(dish[0].cost)
            dish_generic_cost = float(DishType.objects.filter(name=dish_type)[0].generic_price)
            if dish_type == 'main_dish' or  dish_type == 'sauce' or dish_type=='drink' or dish_type=='side_dish':
                print(main_dish_flag)
                main_dish_flag = True
            elif dish_type == 'salad':
                sum += dish_cost
            else:
                sum += dish_generic_cost

    if main_dish_flag:
        sum += main_dish_price

    return HttpResponse(sum)

def zori(request):

    provider = Provider.objects.get(name='zori')
    soup = DishType.objects.filter(name='soup')
    all_soup = Dish.objects.filter(type=soup[0],  provider=provider.id)

    main_dish = DishType.objects.filter(name='main_dish')
    all_mains = Dish.objects.filter(type=main_dish[0],  provider=provider.id)

    side_dish = DishType.objects.filter(name='side_dish')
    all_sides = Dish.objects.filter(type=side_dish[0], provider=provider.id)

    drink = DishType.objects.filter(name='drink')
    all_drinks = Dish.objects.filter(type=drink[0], provider=provider.id)

    salad = DishType.objects.filter(name='salad')
    all_salads = Dish.objects.filter(type=salad[0], provider=provider.id)


    form = DishForm(request.POST or None)
    context = {
        'form': form,
    }

    context = {
    }

    return render(request, "dish/zori.html",  {'provider_name':provider.name,
                                               'all_soup':all_soup,
                                               'all_mains':all_mains,
                                               'all_sides':all_sides,
                                               'all_drinks':all_drinks,
                                               'all_salads':all_salads} ,  context )


def thatcher(request):
    print(os.path.abspath(__file__))
    provider = Provider.objects.get(name='thatcher')

    all_dishes = Dish.objects.all()

    soup = DishType.objects.filter(name='soup')
    all_soup = Dish.objects.filter(type=soup[0], provider=provider.id)

    bruschetta = DishType.objects.filter(name='bruschetta')
    all_bruschettas =  Dish.objects.filter(type=bruschetta[0], provider=provider.id)


    main_dish = DishType.objects.filter(name='main_dish')
    all_mains = Dish.objects.filter(type=main_dish[0], provider=provider.id)

    side_dish = DishType.objects.filter(name='side_dish')
    all_sides = Dish.objects.filter(type=side_dish[0], provider=provider.id)


    sauce = DishType.objects.filter(name='sauce')
    all_sauces = Dish.objects.filter(type=sauce[0], provider=provider.id)

    drink = DishType.objects.filter(name='drink')
    all_drinks = Dish.objects.filter(type=drink[0], provider=provider.id)

    salad = DishType.objects.filter(name='salad')
    all_salads = Dish.objects.filter(type=salad[0], provider=provider.id)

    addon = DishType.objects.filter(name='add_on')
    all_addons= Dish.objects.filter(type=addon[0], provider=provider.id)

    soup_price =  DishType.objects.filter(name='soup')[0].generic_price
    bruschetta_price = DishType.objects.filter(name='bruschetta')[0].generic_price
    main_price = DishType.objects.filter(name='main_dish')[0].generic_price
    addon_price = DishType.objects.filter(name='add_on')[0].generic_price

    form = DishForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'dish/thatcher.html', {
            'provider_name':provider.name,
                                                'all_bruschettas' : all_bruschettas,
                                               'all_soup':all_soup,
                                               'all_mains':all_mains,
                                               'all_sides':all_sides,
                                               'all_sauces': all_sauces,
                                               'all_drinks':all_drinks,
                                               'all_salads':all_salads,
                                               'all_addons':all_addons,
                                               'soup_price':soup_price,
                                               'bruschetta_price':bruschetta_price,
                                               'main_price': main_price,
                                               'addon_price': addon_price} , context)

