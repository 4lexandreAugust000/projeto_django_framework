"""MusicOni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from musica import views

# inseri as urls, 'index', 'adicionar novo registro', 'editar', 'atualizar', 'deletar', 'exportar' e 'login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('export_excel', views.export_excel),
    path('login/',views.login),
    path('home/',views.home),
]


