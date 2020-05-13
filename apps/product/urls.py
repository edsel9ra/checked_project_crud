from django.urls import path, include
from . import views
app_name = 'product'

urlpatterns = [
    # Ingresar o Insertar
    path('', views.product_form, name='produc_insert'),
    path('<int:id>/', views.product_form,
         name='product_update'),  # Modificacion
    path('delete/<int:id>/', views.eliminar_empleado,
         name='eliminar_empleado'),  # Eliminar
    path('list/', views.product_list, name='product_list')  # Listar
]
