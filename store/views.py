from this import s
from django.shortcuts import render
from main import models
# Create your views here.

def storehome(request):
    carasoul_obj = models.sotrecarasoul.objects.all()
    laptop_obj = models.laptopinfo.objects.all()
    laptopbrand_obj = models.laptopbrandname.objects.all()
    if request.method == "POST":
        lt = request.POST['filtertext']
        if lt != None:
            laptop_obj = models.laptopinfo.objects.filter(name__icontains = lt)
            for i in laptop_obj:
                laptopbrand_obj = models.laptopbrandname.objects.filter(name__icontains = i.name)
    return render(request, "store/store.html", {'carobj': carasoul_obj, 'lapobj': laptop_obj, 'brand': laptopbrand_obj})

def laptop(request):
    laptop_obj = models.laptopinfo.objects.all()
    laptopbrand_obj = models.laptopbrandname.objects.all()
    if request.method == "POST":
        lt = request.POST['filtertext']
        if lt != None:
            laptop_obj = models.laptopinfo.objects.filter(name__icontains = lt)
            for i in laptop_obj:
                laptopbrand_obj = models.laptopbrandname.objects.filter(name__icontains = i.name)
    return render(request, "store/Laptop.html", {'lapobj': laptop_obj, 'brand': laptopbrand_obj})

def desktop(request):

    return render(request, "store/Desktop.html")

def keyboardandmouse(request):

    return render(request, "store/keyboardandmouse.html")

def other(request):

    return render(request, "store/other.html")

def storeproduct(request, laptopinfo_id):

    laptop_data = models.laptopinfo.objects.get(pk = laptopinfo_id)

    return render(request, "store/storeproductdescription.html", {'lobj': laptop_data})


