from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Ticket


User = get_user_model()


class TicketSerializer(serializers.ModelSerializer):
    assignee = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, queryset=User.objects.all(), allow_null=True
    )
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        exclude = ('created', 'modified')

    def get_status_display(self, obj):
        return obj.get_status_display()
