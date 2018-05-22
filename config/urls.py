from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from kanban.board.views import TicketViewSet


router = DefaultRouter()
router.register('tickets', TicketViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
