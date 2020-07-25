#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required
from aplikacja.models import *
from aplikacja.forms import *
from django.template.defaultfilters import date
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def checkWork():
    pass
def calcAvarage():
    suma = 0
    k = Ratings.objects.filter(Is_Deleted = False)
    for f in k:
        suma += f.Rate
    try:
        return round(suma / len(k),2)
    except:
        pass

def index(request):
    dane = Done.objects.all()
    if len(dane) == 0:
        dane = Done()
        dane.save()
    else:
        dane = dane[0]
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    title = "Bramhart.pl - Twoje ogrodzenia "
    return render(request,"index.html", context={"dane":dane,"kontakt":contact,"kategorie":kategorie, "title":title})

def opinions(request):
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    avarage = calcAvarage()
    title = "Bramhart.pl - Opinie"
    comments = Ratings.objects.filter(Is_Deleted = False).order_by("-pub_date")
    return render(request,"opinions.html", context={ "title" :title, "comments":comments , "kontakt":contact, "avarage":avarage,"kategorie":kategorie,} )

def addopinion(request):
    if request.method == "POST":
        form = addCommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = form.save()
            return JsonResponse({"response": model_to_dict(form), "avarage":calcAvarage()}, status = 200)
        else:
            return JsonResponse({"wrong":"true"})

def gallery(request, **kwargs):
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    if "name" in kwargs:
        mainCategory = get_object_or_404(MainCategory,name=kwargs.get("name"))
        categories = Category.objects.filter(category_id = mainCategory.pk)
        breadcrumb = "<a href='http://"+ str(request.META['HTTP_HOST'])+ "/'>START</a> / <a href='http://"+ str(request.META['HTTP_HOST'])+ "/galeria'>GALERIA</a> / "+ str(mainCategory.name.upper())
        bgimage = True
        autoName = True
    else:
        autoName = False
        bgimage = False
        categories = MainCategory.objects.all()
        breadcrumb = "<a href='http://" + str(request.META['HTTP_HOST']) + "/'>START</a> / GALERIA "
        mainCategory = ""
    contact = Contact.objects.all()[0]
    return render(request,"gallery.html",{"categories":categories, "kontakt":contact, "kategoria":mainCategory,"breadcrumb":breadcrumb,"bgimage":bgimage, "autoName":autoName,"kategorie":kategorie,})

def PhotoGallery(request, **kwargs):
    title = "BramHart.pl - galeria"
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    mainCategory =  get_object_or_404(MainCategory,name=kwargs.get("name"))
    parentCategory =  get_object_or_404(Category, pk = kwargs.get("pk"))
    Photos = Object.objects.filter(category_id = kwargs.get("pk"))
    base = "http://" + str(request.META['HTTP_HOST'])
    breadcrumb = "<h5><a href=" + base + "/'>START</a> / <a href="+ base + "/galeria " + ">" + "GALERIA</a> / <a href=" + base + "/galeria/"  + str(mainCategory.name)+ ">" + str(mainCategory.name.upper())+"</a>"+" / "+ parentCategory.name.upper()+"<h5>"
    print(len(breadcrumb))
    return render(request,"photogallery.html", {"kontakt":contact,"breadcrumb":breadcrumb,"parentCategory":parentCategory,"kategorie":kategorie,"items":Photos,"title":title})
def aboutUs(request):
    dane = Done.objects.all()
    if len(dane) == 0:
        dane = Done()
        dane.save()
    else:
        dane = dane[0]
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    return render(request,"aboutus.html",{"dane":dane,"kontakt":contact})
def contact(request):
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email="Email@przykład.pl", telefon="000 000 000",
                          adres="xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    return render(request,"contact.html",{"kontakt":contact})

def sendMessage(request):
    print("Doszło")
    form = addNewMessageForm(data = request.POST)
    if form.is_valid():
        print("sukces")
        form.save()
        return JsonResponse({"state":"success"})
    else:
        print(form.errors)
        return JsonResponse({"state":"failed"})

@staff_member_required
def AdminPanel(requst):
    dane = Done.objects.all()
    if len(dane) == 0:
        dane = Done()
        dane.save()
    else:
        dane = dane[0]
    contact = Contact.objects.all()
    if len(contact) == 0:
        contact = Contact(brandName="Wpisz nazwę firmy", email = "Email@przykład.pl", telefon = "000 000 000", adres = "xx-xxx yyyyyy yyyyyyyyy ul. xxxxx")
        contact.save()
    else:
        contact = contact[0]
    kategorie = MainCategory.objects.all()
    podkategorie = Category.objects.all()
    messagescount = len(Messages.objects.filter(opened = False))
    return  render(requst,"admin-panel.html",{"dane":dane,"kontakt":contact,"kategorie":kategorie,"podkategorie":podkategorie,"messagescount":messagescount})
@staff_member_required
def deleteOpinion(request, pk):
    Ratings.objects.filter(pk=pk).delete()
    return JsonResponse({"id":pk})
@staff_member_required
def messages(request):
    Messagess = Messages.objects.filter(deleted=False).order_by("-pub_date")
    return render(request,"messages.html", {"messages":Messagess})

@staff_member_required
def deletemessage(request,pk):
    Messages.objects.filter(id = pk).delete()
    return JsonResponse({"id":pk},status=200)

@staff_member_required
def openmessage(request,pk):
    Messages.objects.filter(id = pk).update(opened = True)
    return JsonResponse({"id":pk},status=200)

@staff_member_required
def updateBrandData(request):

    form = UpdateBrandDataForm(data = request.POST)
    if form.is_valid():
        Contact.objects.all().delete()
        form.save()
        return JsonResponse({"state": "success"}, status=200)
    else:
        return JsonResponse({"state": "failed"}, status=200)\

@staff_member_required
def addNewMainCategory(request):
    form = addNewMainCategoryForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({"state": "success"}, status=200)
    else:
        return JsonResponse({"state": "failed"}, status=200)


@staff_member_required
def addNewCategory(request):
    form = addNewCategoryForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({"state": "success"}, status=200)
    else:
        return JsonResponse({"state": "failed"}, status=200)

@staff_member_required
def addNewObject(request):
    form = addNewObjectForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({"state": "success"}, status=200)
    else:
        print(form.errors)
        return JsonResponse({"state": "failed"}, status=200)

@staff_member_required
def updateStatistic(request):

    form = UpdateStatisticForm(data = request.POST)
    if form.is_valid():
        Done.objects.all().delete()
        form.save()
        return JsonResponse({"state": "success"}, status=200)
    else:
        return JsonResponse({"state": "failed"}, status=200)



@staff_member_required
def deleteMainCategory(request):
    MainCategory.objects.filter(pk=request.POST.get("category")).delete()
    return JsonResponse({"state": "success"}, status=200)



@staff_member_required
def deleteCategory(request):
    Category.objects.filter(pk=request.POST.get("category")).delete()
    return JsonResponse({"state": "success"}, status=200)


@staff_member_required
def deleteObject(request):
    try:
        Object.objects.filter(pk=request.POST.get("id")).delete()
        return JsonResponse({"state": "success"}, status=200)
    except:
        return JsonResponse({"state": "failed"}, status=200)



