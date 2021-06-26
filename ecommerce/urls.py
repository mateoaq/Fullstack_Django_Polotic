"""trabajoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

    path('',views.index, name='index'),
    path('about/',views.about, name='about'),

    path('product/<int:producto_id>/',views.product, name='product'),
    path('product/nuevo_producto/',views.nuevo_producto, name='nuevo_producto'),
    path('product/eliminar_producto/<int:producto_id>/',views.eliminar_producto, name='eliminar_producto'),
    path('product/editar_producto/<int:producto_id>/',views.editar_producto, name='editar_producto'),

    path('search', views.search, name='search'),
    path('search/<int:cat_id>', views.search, name='search'),

    path('login/',LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register',views.register, name='register'),

    path('carrito',views.carrito, name='carrito'),
    path('carrito_add/<int:producto_id>',views.carrito_add, name='carrito_add'),
    path('carrito_del/<int:producto_id>',views.carrito_del, name='carrito_del'),
    path('carrito_decre/<int:producto_id>',views.carrito_decre, name='carrito_decre'),
    path('carrito_clear',views.carrito_clear, name='carrito_clear'),

    path('reset_password/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
]


