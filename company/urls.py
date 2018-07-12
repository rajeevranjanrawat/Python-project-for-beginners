from django.conf.urls import url
from company import views
from testApp import views as testview

urlpatterns = [

    url(r'^hello_company$', views.hellocompany, name='hello_company'),
    url(r'^hello_company2$', testview.helloDjango, name='hello_company2')
]