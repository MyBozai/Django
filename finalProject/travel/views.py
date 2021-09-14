from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import User,Search,PlaceAddress
from django.contrib import messages
# Create your views here.
def showPage(request):
    username = request.COOKIES.get('username')
    if not username:
         return render(request,'firstpage.html')
    else:
        return render(request,'index.html')


def index(request):
    username = request.COOKIES.get('username')
    if request.method == 'POST':
        place = request.POST.get('place')
        Search.objects.all().delete()
        user = Search.objects.create(place=place)
        user.save()
        place_list = PlaceAddress.objects.all()
        for i in place_list:
            if i.address == place:
                context={
                    'username':username,
                    'xxx':i.address,
                    'infom':i.infom
                }
                return render(request,'search.html',context=context)
            else:
                messages.error(request, '地址不存在,请重新输入查询!')
    return render(request,'index.html',{'username':username})



def showAbout(request):
    username = request.COOKIES.get('username')
    return render(request,'about.html',{'username':username})


def showInfo(request):
    username = request.COOKIES.get('username')
    return render(request,'informations.html',{'username':username})


def showSce(request):
    username = request.COOKIES.get('username')
    return render(request,'scenery.html',{'username':username})


def showTicket(request):
    username = request.COOKIES.get('username')
    return render(request,'ticket.html',{'username':username})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user_list = User.objects.filter(username=username)
        if user_list :
            messages.error(request,'用户已存在，请重新登录！')
        else:
            user = User.objects.create(username=username, password=password, email=email)
            user.save()
            return render(request,'success.html',{'operation':username})
    return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ret = User.objects.filter(username = username,password = password)
        if ret:
            response = render(request,"After Login.html", {'operation': username})
            response.set_cookie('username',username,60)
            return response
        else:
            messages.error(request,'账号或者密码错误，请重新登录!')
    return render(request,'login.html')



def search(request):
    username = request.COOKIES.get('username')
    return render(request, 'search.html', {'username': username})