from django.conf.urls import url
from sites import views


urlpatterns = [

    url(r'^signup$', views.userRegistration, name='signup'),
    url(r'^signin$', views.userLogin, name='signin'),
    url(r'^logout$', views.userLogout, name='logout'),
    url(r'^dashboard$', views.userDashBoard, name='dashboard'),
    url(r'^forgot_password$', views.forgotPassowrd, name='forgot_password'),

    url(r'^static_example$', views.staticExample, name='static_example'),
]
