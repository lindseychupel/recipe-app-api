# 1. Comentário de documentação (já está lá)
"""
app URL Configuration
...
"""

# 2. IMPORTS - ISSO É O IMPORTANTE!
from django.contrib import admin
from django.urls import path, include  # ← Nota o 'include'
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# 3. UMA ÚNICA lista urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    path('api/user/', include('user.urls')),
]
