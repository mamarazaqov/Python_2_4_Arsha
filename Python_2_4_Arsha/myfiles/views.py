from django.db.models import Q
from django.shortcuts import render
from myfiles.models import Portfolio,Team,Murojaat
import datetime
# Create your views here.

def index(request):
    if 'text' in request.POST:
        malumot = request.POST.get('text')
        soz = str(malumot).strip()
        qidirish = Q(nomi__startswith=soz) | Q(comp__name__startswith=soz) | Q(url__startswith=soz)|\
                   Q(date__startswith=soz) | Q(text__startswith=soz) | Q(tur__nomi__startswith=soz)
        port = Portfolio.objects.filter(qidirish)
        return render(request, 'index.html', {'works' : port})
    if 'name' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojaat(ism=name,mail=email,sub=sub,text=msg,date=vaqt).save()
    port = Portfolio.objects.all()
    return render(request,'index.html',{'works': port})

def team(requast):
    port = Team.objects.all()
    return render(requast,'portfolio-details.html',{'worked':port})

def portfolio_detalis(request,id):
    port = Portfolio.objects.get(id=id)
    return render(request,'portfolio-details.html',{'work':port})