# polling_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import CurrentUserView, RegisterView

urlpatterns = [
    # 1) Admin
    path('admin/', admin.site.urls),

    # 2) Who-ami endpoint
    path('api/users/me/', CurrentUserView.as_view(), name='current_user'),

    # 3) Register endpoint
    path('api/users/register/', RegisterView.as_view(), name='register'),

    # 4) Polls API
    path('api/polls/', include('polls.urls')),

    # 5) JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 6) qui ripristiniamo il client “statico”
    #path('client/', include('client.urls')),
    # Tutte le altre richieste servono client/index.html
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
]
