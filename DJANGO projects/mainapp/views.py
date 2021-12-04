from django.http import HttpResponse
from django.shortcuts import render


def home (request):
   products = ['Apples', 'Cherries', 'Banana', 'Pears', 'Watermelon']
   context = {
      "products": products
   }
   return render(request, "home.html", context)