"""
Views for the recipe APIs
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View para gerenciar APIs de receitas."""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Recupera receitas para o usuário autenticado."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Retorna a classe serializer apropriada para a requisição."""
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer
        
        return self.serializer_class

    def perform_create(self, serializer):
        """Cria uma nova receita atribuindo ao usuário atual."""
        serializer.save(user=self.request.user)
