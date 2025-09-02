from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- Públicas ---
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos, name='servicos'),
    path('contato/', views.contato, name='contato'),
    # --- Autenticação ---
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cliente/trocar-senha/', auth_views.PasswordChangeView.as_view(template_name='core/password_change_form.html', success_url='/cliente/trocar-senha/concluido/'), name='password_change'),
    path('cliente/trocar-senha/concluido/', auth_views.PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'), name='password_change_done'),
    # --- Área do Cliente ---
    path('cliente/', views.area_cliente, name='area_cliente'),
    path('cliente/minha-conta/', views.info_conta, name='info_conta'),
    path('cliente/chamados/', views.lista_chamados, name='lista_chamados'),
    path('cliente/chamados/novo/', views.criar_chamado, name='criar_chamado'),
]