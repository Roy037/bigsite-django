from django.urls import path
from main import views
from . import views

urlpatterns = [
#ex1:path("<int:id>",views.index,name="index"),
path("<str:name>",views.index,name="index"),
path("",views.index,name="home"),


]
