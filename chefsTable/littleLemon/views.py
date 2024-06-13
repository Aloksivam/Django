from django.shortcuts import render
from datetime import datetime
from .models import Menu
from .forms import Demoform
# Create your views here.
from django.http import HttpResponse
# from .models import Menu
def hello(request):
    return HttpResponse("Hello World")
def homepage(request):
    return HttpResponse("Welcome in Homepage")
def displaydate(request):
    return HttpResponse(datetime.today())
def menu(request):
    # menuitem={'name':'Greek Salad','price':23}
    # newmenu={'mains':[
    #     {'name':"falafal",'price':12},
    #     {'name':"jalebi",'price':150},
    #     {'name':"rasmalai",'price':60},
    # ]}
    # # text="""<h1 style="color:#F4CE14;">This is Little Lemon again</h1>"""
    # return render(request,'menu.html',newmenu)
    return render(request,'menu.html')


def about(request):
    return render(request,'about.html')
def home(request):
    return render(request,'index.html')
    # path = request.path
    # scheme=request.scheme
    # method=request.method
    # address=request.META['REMOTE_ADDR']
    # user_agent=request.META['HTTP_USER_AGENT']
    # path_info=request.path_info
    # response = HttpResponse()
    # response.headers['Age']=20
    # msg=f"""
    # <br>Path: {path}
    # <br>scheme: {scheme}
    # <br>method: {method}
    # <br>address: {address}
    # <br>user_agent: {user_agent}
    # <br>path_info: {path_info}    
    # <br>response Header: {response.headers} 

    # """
    # return HttpResponse(msg,content_type='text/html',charset='utf-8')
# def menu_by_id(request,menu_id):
#     menu = Menu.objects.get(pk=menu_id)
#     return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine")
#Path parameter
def pathview(request,name,id=23):
    return HttpResponse(f"Name:{name} userId:{id}")
#QueryParameter
def qryview(request):
    name=request.GET['name']
    id=request.GET['id']
    return HttpResponse(f"Name:{name} user id: {id}")
#Body parameters
def showform(request):
    return render(request,"form.html")
def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse(f"Name:{name} user id: {id}")
def index(request):
    form = Demoform()
    if request.method=='POST':
        form=Demoform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'home.html',{'form':form})

# def about(request):
#     about_content={'about':"Based on chicago, illinois"}
#     return render(request,"about.html",about_content)
def menu_by_id(request):
    newmenu=Menu.objects.all()
    newmenu_dict={'menu':newmenu}
    return render(request,"nmenu.html",newmenu_dict)