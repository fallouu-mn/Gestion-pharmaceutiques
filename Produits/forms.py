from django.forms import ModelForm
from .models import Produit, Categorie , Vente,Customer
from django import forms


class AjoutProduit(ModelForm):
    class Meta:
        model = Produit
        fields = [
            'name', 'categorie', 'price', 'quantite', 'description', 'date_expiration', 'image'
        ]
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'placeholder': 'Entrez le nomdu produit',
                    'class':'form-control'
                }
            ),
            'categorie': forms.Select(
                attrs={
                    'class':'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder':'Entrez le prix du produit',
                    'class':'form-control'
                }
            ),
            'quantite': forms.NumberInput(
                attrs={
                    'placeholder':'Entrez la quantite',
                    'class':'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder':'description',
                    'class':'form-control',
                    'rows':4
                }
            ),
            'date_expiration': forms.DateInput(
                attrs={
                    'placeholder':'Date d\'expiration',
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control-file'
                }
            )
        }
        def __init__(self, *args, **kwargs):
            super(AjoutProduit,self).__init__(*args, **kwargs)

            self.fields['name'].error_messages ={
                'required': 'Le nom est obligatoire',
                'invalid': 'Votre message'
            }

            self.fields['categorie'].error_messages ={
                'required':'Le categorie est obligatoire',
                'invalid':'veuillez selectionner une categorie'
            }
            self.fields['price'].error_messages ={
                'required':'Le prix est obligatoire',
                'invalid':'veuillez selectionner le prix'
            }
            self.fields['quantite'].error_messages ={
                'required':'La quantite est obligatoire',
                'invalid':'veuillez entrer la quantite'
            }
            self.fields['description'].error_messages ={
                'required':'Le description est obligatoire',
                'invalid':'veuillez entrer la description'
            }
            self.fields['date_expiration'].error_messages ={
                'required':'Le date est obligatoire',
                'invalid':'veuillez entrer la date'
            }

#formulaire de vente

class AjoutVente(forms.ModelForm)    :

    quantite= forms.IntegerField(
        help_text='Veuillez entrer la quantite du produit',
        required= True,
        
    ) 
    customer= forms.CharField(
        help_text='Veuillez entrer le nom du client',
        required= True,
        max_length=100,
        
    )               

    class Meta:
        model = Vente
        fields = ['quantite','customer']
        

        widgets ={
            'customer':forms.TextInput(
              attrs=  {
                  'placeholder':"Lenom du client",
                  'class':'forms-control'
              }
            ),
            'quantite':forms.TextInput(
              attrs=  {
                  'placeholder':"Le quantite du produit",
                  'class':'forms-control'
              }
            ),

        }
