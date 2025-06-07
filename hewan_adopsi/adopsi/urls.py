from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('daftar-hewan/', views.daftar_hewan, name='daftar_hewan'), 
    path('login/', views.login_page, name='login_page'), 
    path('user-login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('hewan/<int:pk>/', views.detail_hewan, name='detail_hewan'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('admin-dashboard/tambah/', views.tambah_hewan, name='tambah_hewan'),
    path('admin-dashboard/edit/<int:pk>/', views.edit_hewan, name='edit_hewan'),
    path('admin-dashboard/hapus/<int:pk>/', views.hapus_hewan, name='hapus_hewan'),
    path('admin-dashboard/pengajuan/<int:pk>/ubah-status/', views.ubah_status_pengajuan, name='ubah_status_pengajuan'),
]