from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('storehome', views.storehome, name="storehome"),
    path('laptop', views.laptop, name="laptop"),
    path('desktop', views.desktop, name="desktop"),
    path('keyboardandmouse', views.keyboardandmouse, name="keyboardandmouse"),
    path('other', views.other, name="other"),
    path('storeproduct/<int:laptopinfo_id>', views.storeproduct, name = "storeproduct"),
]