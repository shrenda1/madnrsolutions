from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('product', views.product, name="product"),
    #path('store', views.store, name="store"),
    path('career', views.career, name="career"),
    path('contact', views.contact, name="contact"),
    path('jobpage/<int:job_id>', views.jobpage, name="jobpage"),
    path('jobapplication', views.jobapp, name="jobapplication"),
    path('contactingus', views.contacting, name="contactingus"),
    
]