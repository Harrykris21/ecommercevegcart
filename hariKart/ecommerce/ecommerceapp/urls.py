
from django.urls import path,include
from ecommerceapp import views

app_name = 'ecommerceapp' 

urlpatterns = [
    path('',views.index,name='index'),
    path('category/',views.category_list_view,name='category_list'),
    path('product/',views.product_list_view,name='product_list'),
    path('category/<cid>/',views.category_product_list_view,name='category_product_list'),
    path('vendor-list/',views.vendor_list_view,name='vendor_list'), 
    path('vendor-detail/<vid>',views.vendor_detail_view,name='vendor_detail'), 
    path('product-detail/<pid>',views.product_detail_view,name='product_detail'), 

    #Add Revies
    path('ajax/add_review/<str:pid>/', views.ajax_add_review, name='ajax_add_review'),

    #Search
    path('search/', views.search_view, name='search'),




    
]
