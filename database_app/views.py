from rest_framework import generics
from .models import MetaData, ChunkData
from .serializers import MetaDataSerializer, ChunkDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status

# 上传
class MetaDataViewSet(viewsets.ModelViewSet):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer

class ChunkDataViewSet(viewsets.ModelViewSet):
    queryset = ChunkData.objects.all()
    serializer_class = ChunkDataSerializer


class MetaDataListCreateView(generics.ListCreateAPIView):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer

class ChunkDataListCreateView(generics.ListCreateAPIView):
    queryset = ChunkData.objects.all()
    serializer_class = ChunkDataSerializer

class ChunkDataRetrieveView(generics.RetrieveAPIView):
    queryset = ChunkData.objects.all()
    serializer_class = ChunkDataSerializer
    lookup_field = '_id'
    
class MetaDataRetrieveView(generics.ListAPIView):
    queryset = MetaData.objects.filter(filename='file100.sgy')
    serializer_class = MetaDataSerializer
    
class MetaDataCountView(APIView):
    def get(self, request, format=None):
        data_count = MetaData.objects.count()
        return Response({'data_count': data_count})   

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):
        file_serializer = MetaDataSerializer(data=request.data)

        if file_serializer.is_valid():
            # 保存 meta_data 记录
            file_serializer.save()

            # 获取上传的文件
            uploaded_file = request.data['file']

            # 处理文件分块并保存到 chunk_data 表
            chunk_size = 255 * 1024  # 255 KB
            n = 0
            while True:
                chunk_data = uploaded_file.read(chunk_size)
                if not chunk_data:
                    break

                # 创建一个新的 ChunkData 记录
                chunk_record = ChunkData(file=file_serializer.instance, n=n, data=chunk_data)
                chunk_record.save()
                n += 1

            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    