# forms.py
from django import forms
from .models import Order
from .models import Contact

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'username','product_name','contact','type_order',
                  'receiver_ville','marque_order', 'size',
                  'quantity','infos']
         # update this with your actual fields

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'message']  # update this with your actual fields