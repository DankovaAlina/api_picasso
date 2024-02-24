from django.db import models


class File(models.Model):
    """Модель файла."""

    file = models.FileField('Файл', upload_to='files/')
    uploaded_at = models.DateTimeField(
        'Дата и время загрузки',
        auto_now_add=True
    )
    processed = models.BooleanField('Флаг обработки файла', default=False)
