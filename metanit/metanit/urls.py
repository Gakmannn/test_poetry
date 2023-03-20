"""metanit URL Configuration

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
from django.urls import re_path, path, include
from hello import views

product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
]
products_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns = [
    path('', views.index),
    path("postuser/", views.postuser),
    path("data", views.data),
    path("meta", views.meta),
    path("complex", views.complex),
    path("contacts", views.contact),
    path("get", views.get),
    path("set", views.set),
    path("json", views.json),
    path("person", views.person),
    path("notaperson", views.notaperson),
    path("people/<int:id>", views.people),
    path("access/<int:age>", views.access),
    path("products", include(product_patterns)),
    path("products/<int:id>/", include(products_patterns)),
    path("getuser/", views.getUser),
    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),
    # path("user", views.user),
    # path("user/<name>", views.user),
    # path('user/<name>/<int:age>', views.user),
    re_path(r'^about', views.about),
    path("contact/", views.contact),
    path("details/", views.details), 
    path('admin/', admin.site.urls),
    re_path(r"\D+", views.notFound),
]
