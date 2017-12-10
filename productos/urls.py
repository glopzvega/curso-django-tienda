from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.index, name="index"),	
	# url(r'^nombre/', views.otrometodo, name="otro"),
	url(r'^$', views.listado_cards, name="productos"),
	url(r'^cards/', views.listado_cards, name="cards"),
	url(r'^listado', views.listado, name="listado"),
	url(r'^nuevo/', views.nuevo, name='nuevo'),
	
	url(r'^carrito/', views.ver_carrito, name='carrito'),
	url(r'^(?P<prod_id>[0-9]+)/cantidad/', views.cantidad_carrito, name='cantidad_carrito'),
	url(r'^(?P<prod_id>[0-9]+)/agregar/', views.agregar_carrito, name='agregar_carrito'),
	url(r'^(?P<prod_id>[0-9]+)/quitar/', views.quitar_carrito, name='quitar_carrito'),	

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