"""Views para a API de usuário."""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings  # ← CORREÇÃO: era 'setting'

# Create your views here.

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

class CreateUserView(generics.CreateAPIView):
    """Cria um novo usuário no sistema."""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Cria um novo token de autenticação para usuário."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES  # ← CORREÇÃO: api_settings
 
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Gerencia o usuário autenticado."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Busca e retorna o usuário autenticado."""
        return self.request.user
