import datetime
from django.shortcuts import render, redirect
from todolist.models import BarangToDolist
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers 
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.models import BarangToDolist

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_barang_todolist = BarangToDolist.objects.filter(user=request.user)
    context = {
    'list_todo': data_barang_todolist,
    'nama': request.user.username,
    'last_login': request.COOKIES['last_login'],
}
    return render(request, "todolist.html", context)

def deletee(request, pk):
    item = BarangToDolist.objects.filter(pk=pk)
    item.delete()
    return redirect('todolist:show_todolist')


def add_task(request):
    context = {}
    if request.method == "POST":
        x = BarangToDolist(user=request.user, title=request.POST.get('todo'), description=request.POST.get('description'))
        x.save()
        return redirect('todolist:show_todolist')
    return render(request, "create-task.html",context)    


def checklist(request, pk):

    temp = BarangToDolist.objects.get(id=pk)
    if (temp.is_finished == False):
        temp.is_finished = True
    else :
        temp.is_finished = False
    temp.save()

    return redirect('todolist:show_todolist')
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# AJAX
@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    ajax_todolist = BarangToDolist.objects.filter(user=request.user)
    context = {
    'ajax_todolist' : ajax_todolist,
    'username' :  request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

# AJAX GET
def get_todolist_json(request):
    data_ajax = BarangToDolist.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", data_ajax), content_type="application/json")

# ADD BarangToDolist MODAL
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        BarangToDolist.objects.create(title=title, description=description, date=date, user=user)
         
        return HttpResponse(b"CREATED", status=201)
