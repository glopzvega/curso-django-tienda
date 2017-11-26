from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.index, name="index"),	
	# url(r'^nombre/', views.otrometodo, name="otro"),
	url(r'^$', views.listado, name="listado"),
	url(r'^cards/', views.listado_cards, name="cards"),
	url(r'^nuevo/', views.nuevo, name='nuevo'),
	# url(r'^(?P<prod_id>[0-9]+)/guardar/$', views.guardar, name='guardar'),
	url(r'^(?P<prod_id>[0-9]+)/eliminar/', views.eliminar, name='eliminar'),
	url(r'^(?P<prod_id>[0-9]+)/modificar/', views.modificar, name='modificar'),
	url(r'^(?P<prod_id>[0-9]+)/vender/', views.vender, name='vender'),
	url(r'^(?P<prod_id>[0-9]+)/comprar/', views.comprar, name='comprar'),
	url(r'^(?P<prod_id>[0-9]+)/', views.detail, name='detail'),
]






























# from . import views

# urlpatterns = [
# 	url(r'^$', views.index, name="index"),  
	# url(r'^detail/(?P<prod_id>[0-9]+)/$', views.detail, name='detail'), 
 #    url(r'^(?P<prod_id>[0-9]+)/cantidad/$', views.results, name='cantidad'), 
 #    url(r'^(?P<prod_id>[0-9]+)/vender/$', views.vote, name='vender'),  
# ]