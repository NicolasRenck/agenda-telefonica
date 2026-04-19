from django.urls import path
from .views import ListaContatos, AdicionarContato, EditarContato, DeletarContato
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Rota para a lista (Página Inicial do seu App)
    path('', ListaContatos.as_view(), name='agenda'),
    
    # Rota para adicionar novo item
    path('adicionar/', AdicionarContato.as_view(), name='add_contato'),
    
    # Rota para editar (precisa do ID do item, que o Django chama de 'pk')
    path('editar/<int:pk>/', EditarContato.as_view(), name='editar_contato'),
    
    # Rota para deletar
    path('deletar/<int:pk>/', DeletarContato.as_view(), name='deletar_contato'),
]

