from django.db import models



class Categorie(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Produit(models.Model):
    name = models.CharField(max_length=100)
    categorie  = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantite = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to='media/')

    class Meta:
        ordering = ['date_ajout']

    def statut_quantite(self):
        if self.quantite == 0:
            return 'red'
        elif self.quantite <= 10:
            return 'orange'
        return 'green'

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveBigIntegerField()
    customer = models.CharField( max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.produit 


class Facture_Client(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantite = models.PositiveBigIntegerField()
    date_achat = models.DateTimeField(auto_now_add=False)
    total_amount = models.ForeignKey(Vente, on_delete= models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Le recu de {self.customer.customer}"
