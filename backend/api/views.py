from rest_framework import generics, status
from rest_framework.response import Response

from api.serializers import FileSerializer
from api.tasks import file_processing_task
from files.models import File


class UploadFilesViewSet(generics.CreateAPIView):
    """Вью загрузки файлов."""

    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        file_processing_task.delay(instance.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileViewSet(generics.ListAPIView):
    """Вью получение списка файлов."""

    serializer_class = FileSerializer
    queryset = File.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
