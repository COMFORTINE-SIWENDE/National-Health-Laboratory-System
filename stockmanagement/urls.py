"""
URL configuration for stockmanagement project.

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
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from user import views as user_view
from stock import views
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import include 

urlpatterns = [
    # user urls
    path('login/',user_view.Custom_login, name='login'),
    # path('login/',auth_views.LoginView.as_view(template_name = 'authentication/login.html'), name = 'login'),
    path('sign_up/', user_view.sign_up, name='sign_up'),
    path('logout/',auth_views.LoginView.as_view(template_name = 'authentication/logout.html'), name = 'logout'),
    # stock urls
    # path('login/', views.login, name='login'),
   
    # Admin Routing
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('adm_users/',user_view.users, name='adm_users'),
    path('adm_users/details/<int:pk>/',user_view.staff_detail, name='staff_detail'),
    path('adm_add_items/',views.adm_add_items, name='adm_add_items'),
    path('delete_item/<int:pk>/',views.deleteProduct, name='delete-item'),
    path('update_item/<int:pk>/',views.editProduct,name="edit-item"),
    path('orders/', views.orders, name='orders'),
    path('list_items/', views.list_items, name = 'list_items'),
    path('profile/',user_view.profile, name = 'profile'),
    path('profile/update/',user_view.profile_update, name = 'profile_update'),

    # General Routing
    path('add_items/', views.add_items, name = 'add_items'),
    path('update_items/<str:pk>/',views.update_items, name = 'update_items'),
    path('delete_items/<str:pk>/',views.delete_items, name = 'delete_items'),
    path('stock_detail/<str:pk>/',views.stock_detail, name = 'stock_detail'),
    path('issue_items/<str:pk>/',views.issue_items, name = 'issue_items'),
    path('receive_items/<str:pk>/',views.receive_items, name = 'receive_items'),
    path('reorder_level/<str:pk>/',views.reorder_level, name = 'reorder_level'),
    path('list_history/', views.list_history, name='list_history'),
    
    # manager urls
    path('manager/', views.manager_view, name='manager_view'),
    path('category/<int:category_id>/', views.category_items_view, name='category_items_view'),
    path('update_admin/',views.update, name='update_admin'),
    path('report/',views.report, name='report'),
    # path('selected_items',views.selected_items, name = "selected_items"),
    path('add_items/', views.add_items_view, name='add_items_view'),
    path('download_csv/', views.download_csv, name='download_csv'),
    # admin urls
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # Include URLs from the 'user' app
    path('stock/', include('stock.urls')),  # Include URLs from the 'stock' app
    path('accounts/', include('registration.backends.default.urls')),

        # Root URL redirects to sign_in
    path('', lambda request: redirect('login/', permanent=False)), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
