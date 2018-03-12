from django.shortcuts import render
from .models import Cars,Brands

# Create your views here.
def demo_page(request):
    name = 'Test'
    page_name = 'Hello World'

    cars = Cars.get_last_three_and_brands()
    return render(request, 'demoapp/demo.html', {
        'title': name,
        'page_name': page_name,
        'cars': cars,
        # 'cars': cars,
        # 'cars': cars,
        # 'cars_l': cars_l,
    })

def car_details_view(request, id):
    car = Cars.objects.get(id=id)
    return render(request, 'demoapp/demo_details.html', {
        'car': car,
        # 'cars': cars,
        # 'cars': cars,
        # 'cars_l': cars_l,
    })

def demo_page555(request):
    name = 'BBBB'
    page_name = 'khjhjhjkhjkh'

    cars = Cars.get_last_three_and_brands()
    brand = Brands.objects.first()
    cars = brand.get_cars_by_brand_name('7')
    cars_l = brand.count_cars()

    return render(request, 'demoapp/demo.html', {
        'title': name,
        'page_name': page_name,
        'cars': cars,
        'cars': cars,
        'cars_l': cars_l,
    })
def demo_page666(request):
    name = 'Testqqqqq'
    page_name = 'Herld'

    cars = Cars.get_last_three_and_brands()

    return render(request, 'demoapp/demo.html', {
        'title': name,
        'page_name': page_name,
        'cars': cars,
    })

def demo_page777(request):
    name = 'fghfhgfgfh'
    page_name = 'Hellokjhgfhjkrld'

    cars = Cars.get_last_three_and_brands()

    return render(request, 'demoapp/demo.html', {
        'title': name,
        'page_name': page_name,
        'cars': cars,
    })


def second_page(request):
    cars = Cars.get_last_three_and_brands(6)

    return render(request, 'demoapp/page2.html', {
        'cars': cars,
    })


def third_page(request):
    cars = Cars.get_last_three_and_brands(2)
    return render(request, 'demoapp/page3.html', locals())

def form_view(request):
    cars = Cars.objects.all().order_by('brand')
    return render(request, 'demoapp/demo-form.html', locals())
