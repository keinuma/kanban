from django.contrib.auth import get_user_model
from rest_framework import serializers
import datetime

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

    def validate(self, data):
        start = data['start']
        end = data['end']
        if start and start > end:
            raise serializers.ValidationError('終了日は開始日以降に設定してください')
        return data

    def validate_start(self, value):
        if value and value < datetime.date.today():
            raise serializers.ValidationError('開始日には今日以降を入力してください')
        return value
