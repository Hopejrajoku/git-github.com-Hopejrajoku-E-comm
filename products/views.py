from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Feedback
from .forms import FeedbackForm

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
    user = "hopejr"
    product_numb = 14
    products = Product.objects.all().order_by('id')[:4]
    return render(request, "products/home.html",{
        "name":user,
        "product_numb": product_numb,
        "products": products,
    })

def signup(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect("signin")

    
    return render(request, "products/signup.html",
                  {"form":form})


def signin(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
    
            messages.info(request, "Username Or password is incorrect.")
    
    
    return render(request, "products/signin.html")



def shop(request):
    return render(request, "products/shop.html")

def profile(request):
    return render(request, "products/profile.html")


def contact(request):
    return render(request, "products/contact.html")


def product_cat(request, product):
    if product =="suits" or product=="shirts" or product=="shoes" or product=="dresses":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("The page you are looking for does not exist.")
    
def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    my_feedback = Feedback.objects.get(product=product, id=1)
    form = FeedbackForm(instance = my_feedback)
    reviews = Feedback.objects.filter(product = product)
    if request.method == "GET":
        
        return render(request, "products/product.html", {
              "product":product,
              "form":form,
              "reviews":reviews,
        })
    
    else:
        form = FeedbackForm(request.POST, instance = my_feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback was submited successfully.")

            
        return render(request, "products/product.html", {
              "product":product,
              "form":form,
              "reviews":reviews,
        })
    

