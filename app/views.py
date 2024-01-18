from django.shortcuts import render
from app.models import *
from django.http import HttpResponse 
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.order_by('-topic_name')
    QLWO=Webpage.objects.order_by(Length('name'))
    QLWO=Webpage.objects.order_by(Length('name').desc())
    QLWO=Webpage.objects.exclude(topic_name='Cricket')



    QLWO=Webpage.objects.filter(pk__gt=4)
    QLWO=Webpage.objects.filter(pk__gte=4)
    QLWO=Webpage.objects.filter(pk__lt=5)
    QLWO=Webpage.objects.filter(pk__lte=4)
    QLWO=Webpage.objects.filter(name__startswith='r')
    QLWO=Webpage.objects.filter(name__endswith='t')
    QLWO=Webpage.objects.filter(url__startswith='r')
    QLWO=Webpage.objects.filter(url__endswith='in')
    QLWO=Webpage.objects.filter(name__contains='i')
    QLWO=Webpage.objects.filter(topic_name__in=('Cricket','Kabbadi'))


    QLWO=Webpage.objects.filter(name__regex='\w+t$')
    QLWO=Webpage.objects.filter(topic_name='Cricket',name__endswith='t')
    QLWO=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name__endswith='o'))
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',context=d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)



def insert_topic(request):
    tn=input('Enter Topic Nmae:')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)
    return HttpResponse('Topic is created')


def insert_webpage(request):
    tn=input('Enter topic name')
    n=input('enter the name')
    u=input('Enter url')

    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()

    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',context=d)
    return HttpResponse('Webpage Data Inserted Successfully')


def insert_accesssrecord(request):
    pk=int(input('Enter pk value of webpage'))
    a=input('Enter the author')
    d=input('Enter the date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()

    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',context=d)
    return HttpResponse('Access is Created')




def update_webpage(request):
    QLWO=Webpage.objects.all()
    Webpage.objects.filter(pk=7).update(name='Dhoni')
    Webpage.objects.filter(topic_name='valleyBall').update(name='Gibaaa')
    Webpage.objects.update_or_create(topic_name='Cricket',pk=7,defaults={'name':'MS Dhoni'})
    Webpage.objects.update_or_create(topic_name=7,defaults={'name':'MSD'})[0]
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)


# def update_topic(request):

#     QLTO=Topic.objects.all()
#     Topic.objects.
#     d={'topics':QLTO}
#     return render(request,'display_topic.html',d)

def delete_webpage(request):
    Webpage.objects.filter(topic_name='valleyBall').delete()
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    return render(request,'display_webpage.html',d)
     