from django.conf.urls import url, include
from vahay import views

app_name = 'vahay'

urlpatterns = [
    url(r'^vahay-details/(?P<pk>\d+)/$', views.vahay_details, name='vahay_details'),
    url(r'^vahay-details/(?P<pk>\d+)/edit-vahay/$', views.edit_vahay, name='edit_vahay'),
    url(r'^add-vahay/$', views.add_vahay, name='add_vahay'),
    url(r'^(?P<pk>\d+)/edit-vahay/$', views.edit_vahay, name='edit_vahay'),
	url(r'^delete-vahay/(?P<pk>\d+)/$', views.delete_vahay, name='delete_vahay'),
	
	# url(r'^delete-vahay/(?P<pk>\d+)/$', views.delete_vahay, name='delete_vahay
	url(r'^approve/(?P<pk>\d+)/$', views.approve_reservation, name='approve_reservation'),
	url(r'^deny-reserve/(?P<pk>\d+)/$', views.deny_reservation, name='deny_reservation'),
	url(r'^vahay-list/$', views.get_list_vahay, name='vahay_list'),
	url(r'^vahay-list/(?P<pk>\d+)/$', views.m_get_vahay, name='m_get_vahay'),
	# TO TEST
	url(r'^reserve/$', views.reserve_vahay, name='reserve_vahay'),
	url(r'^cancel-reserve/$', views.cancel_reservation, name='cancel_reservation'),
	url(r'^pay/$', views.pay_rental, name='pay_rental')

]