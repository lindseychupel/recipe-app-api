"""
Mapeamento de URLs para o app de receitas.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

# Cria um roteador padrão do Django REST Framework
router = DefaultRouter()

# Registra o ViewSet de receitas no roteador
# Isso cria AUTOMATICAMENTE as URLs:
# GET /recipes/ -> Lista receitas
# POST /recipes/ -> Cria receita
# GET /recipes/1/ -> Detalhe da receita 1
# PUT /recipes/1/ -> Atualiza receita 1
# DELETE /recipes/1/ -> Deleta receita 1
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
# Define o nome do app para usar no reverse()
# Ex: reverse('recipe:recipe-list')
app_name = 'recipe'

# Define a lista de URLs
urlpatterns = [
    # Inclui todas as URLs geradas automaticamente pelo router
    path('', include(router.urls)),
]
