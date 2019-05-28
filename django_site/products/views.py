from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product

# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     } 
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = RawProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RawProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=53)
    
    if obj != None and obj !='':
        context = {
            'object': obj
        }
    else:
        context = {
            'object': None
        }
    return render(request, "products/product_detail.html", context)