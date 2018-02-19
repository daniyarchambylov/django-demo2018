from django.shortcuts import render

# Create your views here.
def demo_page(request):
    name = 'Test'
    page_name = 'Hello World'
    items = [
        'Esen',
        'Daniyar',
        'Kairat',
    ]

    return render(request, 'demoapp/demo.html', {
        'title': name,
        'page_name': page_name,
        'students': items,
    })


def second_page(request):
    return render(request, 'demoapp/page2.html', {})


def third_page(request):
    return render(request, 'demoapp/page3.html', {})
