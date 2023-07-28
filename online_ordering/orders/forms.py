# forms.py
from django import forms
from .models import Order
from .models import Contact

#class OrderForm(forms.ModelForm):
  #  class Meta:
  #      model = Order
       # fields = [ 'username','product_name','contact','type_order',
           #       'receiver_ville','marque_order', 'size',
         #         'quantity','infos']
         # update this with your actual fields
CHOICES=(
    ('Normal','Livraison en 24h ou 72h au plus'),
    ('Express','Livraison en moins de 24h (frais supplémentaire à ajouter)')
    )

class OrderForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_order = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    receiver_ville = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    marque_order = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    size = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    infos = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Order
        fields = [ 'username','product_name','contact','type_order',
        'receiver_ville','marque_order', 'size',
        'quantity','infos']

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'message']  # update this with your actual fields