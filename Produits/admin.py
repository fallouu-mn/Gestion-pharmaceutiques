from django.contrib import admin
from .models import Categorie, Produit, Vente, Facture_Client, Customer

admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Vente)
admin.site.register(Facture_Client)
admin.site.register(Customer)
