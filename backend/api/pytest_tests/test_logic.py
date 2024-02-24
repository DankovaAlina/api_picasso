import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status

from api.serializers import FileSerializer
from conftest import COUNT_TESTING_OBJECTS
from files.models import File


pytest_plugins = ["docker_compose"]


@pytest.mark.django_db
def test_upload_files_view(client, mock_celery_task_delay):
    """"Проверяет загрузку файлов."""
    data = {
        'file': SimpleUploadedFile('test.png', b'test file content')
    }
    url = reverse('api:upload')
    response = client.post(url, data)
    mock_celery_task_delay.assert_called_once_with(1)
    assert response.status_code == status.HTTP_201_CREATED
    last_record = File.objects.last()
    serializer = FileSerializer(instance=last_record)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_files_list(client, files_list):
    """Проверяет получение списка файлов."""
    url = reverse('api:files')
    response = client.get(url)
    assert len(response.data) == COUNT_TESTING_OBJECTS
