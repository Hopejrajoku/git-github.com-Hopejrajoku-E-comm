from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name="home"),
    path('signup', views.signup, name="signup"), #signup page
    path('signin', views.signin, name="signin"), #signin page
    path('shop', views.shop, name="shop"), #shop page
    path('profile', views.profile, name="profile"), #profile page
    path('contact', views.contact, name="contact"), # contact page
    path('products/<product>', views.product_cat, name="productcat"), #Suit product category
    path('products/<product_brand>/<product_slug>', views.product_page, name="product_page")
]
