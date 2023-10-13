from django.urls import path
from . import views

urlpatterns = [
    path('metadata/', views.MetaDataListCreateView.as_view(), name='metadata-list-create'),
    path('chunkdata/', views.ChunkDataListCreateView.as_view(), name='chunkdata-list-create'),
    path('chunkdata/<str:_id>/', views.ChunkDataRetrieveView.as_view(), name='chunkdata-retrieve'),
    path('metadata/filename/file100.sgy/', views.MetaDataRetrieveView.as_view(), name='metadata-retrieve'),
    path('metadata/count/', views.MetaDataCountView.as_view(), name='metadata-count'),
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),  # 新的文件上传视图
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),  # 新的文件上传视图
]
