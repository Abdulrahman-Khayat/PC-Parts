from django.urls import path

from . import views


urlpatterns = [
    path('', views.product_list_create_view),
    path('<uuid:id>/', views.product_detail_view),
    path('brands/', views.brand_list_create_view),
    path('categories/', views.category_list_create_view)

]