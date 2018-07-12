from django.conf.urls import url
from crud import views
from crud import views


urlpatterns = [

    url(r'^create_view', views.CreateView.as_view(), name="create_view"),
    url(r'^create$', views.create, name='create'),
    url(r'^index$', views.index, name='index'),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='update'),
    url(r'^view/(?P<id>[0-9]+)$', views.view, name='view'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete'),


    url(r'^edu_create$', views.create2, name='edu_create'),
    url(r'^edu_index$', views.index2, name='edu_index'),



]