from django.shortcuts import render
from . forms import ProductForm
from .models import Product
# Create your views here.


def index(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    category = request.POST.get('category')
    image = request.FILES.get('image')
    amounts = request.POST.get('amounts')
    
    v_data = Product(name=name, price=price, category=category, image=image, amounts=amounts)
    if request.method == "POST":
        if Product.objects.filter(name=name):
            print("Error")
        else:
            v_data.save()
    else:
        print("Error")
    return render(request, 'index.html',{'prduct':ProductForm})


def products(request):
    search = request.GET.get('search')
    if Product.objects.filter(name = search):
        product = Product.objects.filter(name = search)
    else:
        product = Product.objects.all()

    x = {
        'products':product,
        'search':search
    }
    return render(request, 'products.html',x)
