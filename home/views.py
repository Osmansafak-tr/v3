from django.shortcuts import render
from django.http import JsonResponse

from .models import Car
import pymongo

# Create your views here.
def homePage(request):
    object_list = Car.objects.all()
    return render(request,'home.html',{'Cars':object_list})

def carDetailView(request,pk):
    cluster = pymongo.MongoClient("<YOUR MONGODB CONNECTİON STRİNG>")
    db = cluster["db_proje"]
    mycol = db["marker"]
    all_records = mycol.find().sort('_id',-1)
    all_records_list = []

    for i in all_records:
        all_records_list+=[i]

    result = str(pk)

    return render(request,'car_detail.html',{'markers':all_records_list,'pk':result})

def ajax_deneme(request):
    cars = Car.objects.filter(user_id = request.user.id)
    context = {'Cars':cars}
    return render(request,'car_api_deneme.html',context)

def testView(request):
    cluster = pymongo.MongoClient("<YOUR MONGODB CONNECTİON STRİNG>")
    db = cluster["db_proje"]
    mycol = db["marker"]
    all_records1 = mycol.find({'Araba':'47'},{'_id': False}).sort('_id',-1).limit(30)
    all_records2 = mycol.find({'Araba':'52'},{'_id': False}).sort('_id',-1).limit(30)
    all_records3 = mycol.find({'Araba':'101'},{'_id': False}).sort('_id',-1).limit(30)
    all_records4 = mycol.find({'Araba':'104'},{'_id': False}).sort('_id',-1).limit(30)
    all_records_list = []

    for i in all_records1:
        all_records_list+=[i]
    for i in all_records2:
        all_records_list+=[i]
    for i in all_records3:
        all_records_list+=[i]
    for i in all_records4:
        all_records_list+=[i]

    return JsonResponse({'markers':all_records_list})

