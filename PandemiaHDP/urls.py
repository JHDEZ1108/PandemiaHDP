"""
URL configuration for PandemiaHDP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('blog/', views.blog, name='blog'),  # Lista de blogs
    path('blog/hipertension.html/', views.hipertension, name='hipertension'),
    path('blog/colesterol.html/', views.colesterol, name='colesterol'),
    path('blog/artritis.html/', views.artritis, name='artritis'),
    path('blog/renal.html/', views.renal, name='renal'),
    path('blog/cardiaca.html/', views.cardiaca, name='cardiaca'),
    path('blog/alzheimer.html/', views.alzheimer, name='alzheimer'),
    path('blog/cancer.html/', views.cancer, name='cancer'),
    path('blog/asma.html/', views.asma, name='asma'),
    path('blog/diabetes.html/', views.diabetes, name='diabetes'),
    path('blog/vih.html/', views.vih, name='vih'),
    path('blog/EPOC.html/', views.EPOC, name='EPOC'),
    path('blog/epilepsia.html/', views.epilepsia, name='epilepsia'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    # Asegúrate de pasar 'blog_id' como parte de la URL para 'create_comment'
    path('blog/<int:blog_id>/createcomment/', views.create_comment, name='create_comment'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),  # Detalles de un blog específico
    path('blog/create/', views.create_or_update_blog, name='create_blog'),
    path('blog/<int:blog_id>/update/', views.create_or_update_blog, name='update_blog'),

]

