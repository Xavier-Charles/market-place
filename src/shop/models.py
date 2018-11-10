from django.db import models
from django import forms
from django.forms import ModelForm
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length= 100, db_index= True)
    description= models.CharField(blank = True, max_length= 100)
    price= models.DecimalField(max_digits= 10, decimal_places=2)
    image = models.FileField(upload_to='img/items/%Y/%m/%d')
    created = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length= 50)
    email = models.EmailField( max_length=200)
    phone = models.IntegerField()
    available = models.BooleanField(default=True)
    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering= ('-created',)
        index_together= (('id'),)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])

class ProductForm(ModelForm):
    class Meta():
        model = Product
        fields = ['name', 'description', 'price', 'image', 'user_name', 'email', 'phone' ]

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')
        user_name = cleaned_data.get('user_name')
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phonee')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')