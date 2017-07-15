from django.conf.urls import url, include
from vahay import views

app_name = 'vahay'

urlpatterns = [
    url(r'^vahay-details/(?P<pk>\d+)/$', views.vahay_details, name='vahay_details'),
    url(r'^add-vahay/$', views.add_vahay, name='add_vahay'),
    url(r'^vahay-list/$', views.get_list_vahay, name='vahay_list'),
    url(r'^vahay-list/(?P<pk>\d+)/$', views.m_vahay_details, name='m_vahay_details'),
]