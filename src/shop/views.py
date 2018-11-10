from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.template.response import TemplateResponse
from .models import Product, ProductForm
from django.template import RequestContext


# Create your views here.

def home(request):
    context = {}
    template= 'home.html'
    return render(request,template,context)

def inventory(request):
    product = Product.objects.order_by('-id')
    context = {'data':product}
    template= 'inventory.html'
    return render(request,template,context)

def sell(request):
    title = ""
    context = {'title': title, 'form':ProductForm}
    template= 'sell.html'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit= True)
            title = "Thanks"
            confirm_message = "Your post was successful"
            context = {'title': title, 'confirm_message': confirm_message}
            return redirect('inventory')
    return render(request,template,context)

