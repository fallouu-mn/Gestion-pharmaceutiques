from django.urls import path
from .views import *
from .views import supprimer
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Acc,name='acc'),
    path('produit/', Affichage.as_view(), name='home'),
    #path('ajout/', ajout_donnees, name='ajout'),
    path('ajout/', AjoutProduits.as_view(), name='ajout'),
    path('test/', test_fn, name='test'),
    #path ('modification/<int:id>/', modifier,name='modifier'),
    path  ('modification/<int:pk>/', update_donnes.as_view(),name='modifier'),
    path('supprimer/<int:id>/', supprimer, name="supprimer"),
    #path('detail/<int:id>/',detail,name='detail'),
    path('detail/<int:pk>/',edit.as_view(),name='detail'),
    path('recherche/', recherche , name='recherche'),
    path('ajoutvente/<int:id>/',VenteProduits, name='ajoutvente'),
    path('enregistrement-recu/<int:id>/',Saverecu, name='saverecu'),
    path('facture/<int:id>/',Facture, name='facture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


  
