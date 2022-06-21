from email import header
from unicodedata import name
from django.shortcuts import redirect, render
from .models import vacany, carasoul, application_form, contactus, sotrecarasoul, laptopinfo, laptopbrandname
# Create your views here.
def home(request):
    obj = vacany.objects.all()
    carasoul_obj = carasoul.objects.all()
    return render(request, "Home.html", {'jobobj': obj, 'carobj': carasoul_obj})

def about(request):

    return render(request, "About.html")

def service(request):

    return render(request, "service.html")

def product(request):

    return render(request, "product.html")

# def store(request):
#     carasoul_obj = sotrecarasoul.objects.all()
#     laptop_obj = laptopinfo.objects.all()
#     laptopbrand_obj = laptopbrandname.objects.all()
#     if request.method == "POST":
#         lt = request.POST['filtertext']
#         if lt != None:
#             laptop_obj = laptopinfo.objects.filter(name__icontains = lt)
#             for i in laptop_obj:
#                 laptopbrand_obj = laptopbrandname.objects.filter(name__icontains = i.name)
#     return render(request, "store.html", {'carobj': carasoul_obj, 'lapobj': laptop_obj, 'brand': laptopbrand_obj})

def career(request):
    obj = vacany.objects.all()
    return render(request, "career.html", {'jobobj': obj})

def contact(request):

    return render(request, "contact.html")

def jobpage(request, job_id):
    job_data = vacany.objects.get(pk = job_id)
    return render(request, "jobpage.html", {'jobobj': job_data})

def jobapp(request):
    if request.method == "POST":
        name = request.POST['fullname']
        phone = request.POST['phonenum']
        email = request.POST['email']
        job_title = request.POST['jobtitle']

        datain = application_form(name = name, phone = phone, email=email, job_title = job_title)
        datain.save()
        return redirect('career')
    return redirect('/')

def contacting(request):
    if request.method == "POST":
        name = request.POST['fullname']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['desc']

        datain = contactus(fullname = name, email=email, subject = subject, message = message)
        datain.save()
        return redirect('contact')
    return redirect('/')
