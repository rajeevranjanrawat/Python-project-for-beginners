from django.conf.urls import url
from formExample import views

urlpatterns = [

    url(r'^form_example$', views.formExample)
]