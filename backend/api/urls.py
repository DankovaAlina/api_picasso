from django.urls import path

from api.views import FileViewSet, UploadFilesViewSet

app_name = 'api'

urlpatterns = [
    path('files/', FileViewSet.as_view(), name='files'),
    path('upload/', UploadFilesViewSet.as_view(), name='upload'),
]
