from celery import shared_task

from files.models import File


@shared_task
def file_processing_task(file_id):
    """Задача для обработки файла."""
    if not File.objects.filter(id=file_id).exists():
        print(f'Файл с id [{file_id}] не существует.')
    file_instance = File.objects.get(id=file_id)
    file_instance.processed = True
    file_instance.save()
