from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import index
from .import views

urlpatterns = [
    path('', index.as_view(), name='index-home'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards.html'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)