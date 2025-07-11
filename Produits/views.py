

import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import ListView, CreateView,UpdateView,DetailView

from .forms import AjoutProduit, AjoutVente
from .models import Produit, Categorie,Vente,Customer,Facture_Client


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def test_fn(request):
    return HttpResponse("Ceci est une page de test.")

@login_required(login_url='login')
def Acc(request):
    return render (request,'acc.html')

class Affichage(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    queryset = Produit.objects.all()



class AjoutProduits(LoginRequiredMixin, CreateView):
    model = Produit
    form_class = AjoutProduit
    template_name = 'ajout-donnes.html'
    success_url = reverse_lazy('home')
# class pour la modification
class update_donnes(LoginRequiredMixin, UpdateView):

    #recuperation du model
    model =Produit
    #specifier le formulaire
    form_class= AjoutProduit
    #precision du template
    template_name='modification.html'
    #redirection
    success_url = reverse_lazy('home')

#fonction pour supprimer
@login_required(login_url='login')
def supprimer(request, id):
    if request.method == "POST":
        produit = get_object_or_404(Produit, id=id)
        produit.delete()
        return JsonResponse({'success': True})
    else:
        print("Méthode utilisée :", request.method)
        return JsonResponse({'success': False, 'message': "Méthode non autorisée"})
    
# fonction de recherche de produit
@login_required(login_url='login')
def recherche (request):
    query = request.GET.get('produit')
    donnees=Produit.objects.filter(name__icontains=query)
    context ={
        'donnees' : donnees
    }
    return render (request, 'resultat_recherche.html', context)
     


# fonction pour voir les details
def detail(request,id):
    n = Produit.objects.get(id=id)
    return render(request,'detail.html' , {'n':n})
# class pour voir les details d'un produit

class edit(LoginRequiredMixin, DetailView):
    model = Produit
    template_name = 'detail.html'
    context_object_name ='n'
# fonction pour la vente
def VenteProduits(request, id):
    produit = get_object_or_404(Produit ,id=id)
    message = None
    
    if request.method =='POST':

        form =AjoutVente(request.POST)

        if form.is_valid():

            quantite = form.cleaned_data['quantite']
            customer = form.cleaned_data['customer']
            
            

            if quantite > produit.quantite:
                message ='La quantite demandée est supérieure à votre stock'

            else:

                customer, _ = Customer.objects.get_or_create(name=customer)

                total_amount = produit.price * quantite 

                sale =Vente(produit =produit, quantite = quantite,total_amount= total_amount , customer=customer)

                sale.save()

                produit.quantite -= quantite
                produit.save()

                return redirect('facture', id = sale.id)
            
    else:
        form =AjoutVente()        

        if produit.quantite <= 5 and not message:
            message ='Attention, le stock est bas !'
        context={
            'produit':produit,
            'form':form,
            'message':message
        }     
        return render (request,'formulaire-vente.html', context )

# fonction pour le recu
def Saverecu(request, id):
    vente = get_object_or_404(Vente, id=id)
    customer = vente.customer  # ← Enlevé la virgule
    quantite = vente.quantite  # ← Enlevé la virgule
    total_amount = vente.total_amount  # ← Enlevé la virgule
    produit = vente.produit  # ← Enlevé la virgule
    
    recu = Facture_Client(
        customer=customer,
        quantite=quantite,
        total_amount=total_amount,
        produit=produit,
    )

    recu.save()
    return redirect('facture', id=id)  # ← Changé 'sale_id' en 'id'



    

#fonction pour la facture
def Facture(request, id):  # ← Changé 'sale_id' en 'id'
    
    sale = get_object_or_404(Vente, id=id)  # ← Changé 'sale_id' en 'id'
    customer = sale.customer
    produit = sale.produit
    quantite = sale.quantite
    sale_date = sale.sale_date
    total_amount = sale.total_amount

    context = {   
        'sale': sale,
        'customer': customer,
        'produit': produit,
        'quantite': quantite,
        'sale_date': sale_date,
        'id': sale.id,
        'prix_unitaire': produit.price,
        'total_amount': total_amount
    }
    return render(request, 'facture-client.html', context)