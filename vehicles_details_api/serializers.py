from rest_framework import serializers
from main.models.logs import DataLogs


class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataLogs
        fields = "__all__"
