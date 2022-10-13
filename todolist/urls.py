from django.urls import path
from todolist.views import deletee
from todolist.views import add_task
from todolist.views import register 
from todolist.views import login_user
from todolist.views import logout_user,show_todolist
from todolist.views import checklist, todolist_ajax, get_todolist_json, add


app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='create-task'),
    path('', show_todolist, name='show_todolist'),
    path('deletee/<int:pk>/', deletee, name='deletee'),
    path('checklist/<int:pk>/', checklist, name='checklist'),
    path('json/', todolist_ajax, name='show_json'),
    path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add, name='add'),
]