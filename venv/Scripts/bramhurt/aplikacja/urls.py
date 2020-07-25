"""bramhurt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from aplikacja import views

app_name = 'app'
urlpatterns = [
    path('',views.index, name="index"),
    path('opinie/',views.opinions, name="opinions"),
    path('opinie/delete/<int:pk>',views.deleteOpinion, name="deleteOpinion"),
    path('dodaj_komentarz/',views.addopinion, name="addopinion"),
    path('galeria/',views.gallery, name="gallery"),
    path('galeria/<slug:name>',views.gallery, name="galleryDet"),
    path('galeria/<slug:name>/<int:pk>',views.PhotoGallery, name="galleryPhoto"),
    path('onas',views.aboutUs, name="AboutUs"),
    path('kontakt',views.contact, name="contact"),
    path('kontakt/sendmessage',views.sendMessage, name="send-message"),
    path('admin-control',views.AdminPanel, name="admin"),
    path('admin-control/messages',views.messages, name="admin-messages"),
    path('admin-control/messages/delete/<int:pk>',views.deletemessage, name="delete-message"),
    path('admin-control/messages/open/<int:pk>',views.openmessage, name="open-message"),
    path('admin-control/updateBrandData',views.updateBrandData, name="update-brand-data"),
    path('admin-control/updateStatistic',views.updateStatistic, name="update-statistic-data"),
    path('admin-control/addNewMainCategory',views.addNewMainCategory, name="add-MainCategory"),
    path('admin-control/addNewCategory',views.addNewCategory, name="add-Category"),
    path('admin-control/addNewObject',views.addNewObject, name="add-Object"),
    path('admin-control/deleteMainCategory',views.deleteMainCategory, name="deleteMainCategory"),
    path('admin-control/deleteCategory',views.deleteCategory, name="deleteCategory"),
    path('admin-control/deleteObject',views.deleteObject, name="deleteObject"),
]
