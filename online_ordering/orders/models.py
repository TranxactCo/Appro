from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    promo_code = models.CharField(max_length=20, null=True, blank=True, default='')
    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
 # New field

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)   
    username = models.CharField(max_length=200, default='')
    contact = models.CharField(max_length=100, default='')
    type_order =models.CharField(max_length=10, default='', choices=[('Normal','Livraison en 24h ou 72h au plus'),('Express','Livraison en moins de 24h (frais supplémentaire à ajouter)')])
    receiver_ville = models.CharField(max_length=100, default='')
    product_name = models.CharField(max_length=200, default='')
    marque_order = models.CharField(max_length=100, default='')
    quantity = models.IntegerField()
    size = models.CharField(max_length=100, default='')
    infos = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,  default='En_attente',choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('terminee', 'Terminée')])
    created_at = models.DateTimeField(auto_now_add=True)# New field

class Contact(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField() # New field