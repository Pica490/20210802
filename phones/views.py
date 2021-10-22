from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    value = request.GET.get('sort', None)
    if value == 'name':
        phones = phones.order_by('name')
    elif value == 'min_price':
        phones = phones.order_by('price')
    elif value == 'max_price':
        phones = phones.order_by('-price')
    context = {"phones": phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.all()
    for phone in phones:
        if phone.slug == slug:
            c_phone = phone
    context = {'phone':c_phone}
    return render(request, template, context)


