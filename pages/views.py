from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ContactUsForm

def home(request):
    return render(request, 'home.html')

def discover_oud(request):
    return render(request, 'discover_oud.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact_us')
    else:
        form = ContactUsForm()

    return render(request, 'contact_us.html', {'form': form})