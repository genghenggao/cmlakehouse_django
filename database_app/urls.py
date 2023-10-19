from django.urls import path
from . import views

urlpatterns = [
    path('metadata/', views.MetaDataListCreateView.as_view(), name='metadata-list-create'),
    path('chunkdata/', views.ChunkDataListCreateView.as_view(), name='chunkdata-list-create'),
    path('metadata/filename/file100.sgy/', views.MetaDataRetrieveView.as_view(), name='metadata-retrieve'),
    path('metadata/count/', views.MetaDataCountView.as_view(), name='metadata-count'),
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),  # 新的文件上传视图
    path('chunkdata1/', views.DataListView.as_view(),name='chunk-data-detail1'),
    path('chunkdata/<str:file_id>/', views.ChunkDataList.as_view(), name='chunkdata-list'),
]
