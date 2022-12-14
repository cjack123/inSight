"""inSight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from inSightapi.views import register_user, login_user

from rest_framework import routers
from inSightapi.views import TransactionTypeView
from inSightapi.views import StoreView
from inSightapi.views import CardView
from inSightapi.views import TransactionView
from inSightapi.views import CardHolderView
from inSightapi.views import CategoryView
# routers
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'transactiontypes', TransactionTypeView, 'transactiontype')
router.register(r'stores', StoreView, 'store')
router.register(r'cards', CardView, 'card')
router.register(r'cardholders', CardHolderView, 'cardholder')
router.register(r'transactions', TransactionView, 'transaction')
router.register(r'categories', CategoryView, 'category')


urlpatterns = [
    # Requests to https://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8--/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

