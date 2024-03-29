from rest_framework import serializers

from files.models import File


class FileSerializer(serializers.ModelSerializer):
    """Сериализатор файла."""

    class Meta:
        model = File
        fields = ('file', 'uploaded_at', 'processed')
        read_only_fields = ('uploaded_at', 'processed')
