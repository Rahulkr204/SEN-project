from django.conf.urls import include, url, patterns
from rest_framework.urlpatterns import format_suffix_patterns
from logistics_api import views

urlpatterns = patterns('',
		#Following urls give all the tables in the database
		url(r'^api/orderslist/$', views.OrdersList.as_view()),
		url(r'^api/driverlist/$', views.DriverList.as_view()),
		url(r'^api/triplist/$', views.TripList.as_view()),
		url(r'^api/trucklist/$', views.TruckList.as_view()),
		url(r'^api/userlist/$', views.UserList.as_view()),

		#Following urls give a detailed version of the tables in the database
		url(r'^api/userdetail/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
		url(r'^api/ordersdetail/(?P<pk>[0-9]+)$', views.OrdersDetail.as_view()),
		url(r'^api/truckdetail/(?P<pk>[0-9]+)$', views.TruckDetail.as_view()),
		url(r'^api/tripdetail/(?P<pk>[0-9]+)$', views.TripDetail.as_view()),
		url(r'^api/driverdetail/(?P<pk>[0-9]+)$', views.DriverDetail.as_view(),
	)


urlpatterns = format_suffix_patterns(urlpatterns)