import pytest

from django.core.files.uploadedfile import SimpleUploadedFile

from files.models import File


COUNT_TESTING_OBJECTS = 5


@pytest.fixture
def mock_celery_task_delay(mocker):
    return mocker.patch('api.tasks.file_processing_task.delay')


@pytest.fixture
def files_list():
    for i in range(COUNT_TESTING_OBJECTS):
        File.objects.create(
            file=SimpleUploadedFile('test.txt', b'test file content')
        )
