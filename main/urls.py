from django.urls import URLPattern,reverse,path
from . import views
app_name = 'main'
urlpatterns=[
    path("",views.home,name='home'),
    path("add",views.add,name='add'),
    path("search",views.search, name='search'),
]

