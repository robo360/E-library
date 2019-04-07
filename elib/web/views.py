from django.shortcuts import render
from django.http import HttpResponse
import os 
import csv
from web.models import File
# Create your views here.
cwd=os.getcwd
def index(request):
    subdirs=os.listdir(cwd)
    return render(request, 'html/index.html', {"subdirs":subdirs})
    
def content(request,dir):
    raise NotImplementedError

def update(request):
    populate_db()
    all_objects=File.objects.all().values()
    return HttpResponse(all_objects)


def search(request,q):
    q=request.Get.get('q')
    files=File.objects.Filter(Description_contains=q,keywords_contains=q,location_contains=q)
    return HttpResponse(files)

def populate_db():
    #helps populate the db when give a base directory
    with open('web/content_table.csv', 'r') as csvfile:
        freader = csv.reader(csvfile)
        File.objects.all().delete()
        for row in freader:
            if row[0]=="description":
                pass
            else:
                filesave=File(Description=row[0], keywords=row[1], location=row[2])
                filesave.save()


    