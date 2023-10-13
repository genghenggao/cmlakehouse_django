from django.db import models

# Create your models here.
class MetaData(models.Model):
    _id = models.CharField(primary_key=True, max_length=255)
    filename = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)
    chunkSize = models.IntegerField()
    length = models.FloatField()
    uploadDate = models.DateField()
    contentType = models.CharField(max_length=255)
    metadata = models.CharField(max_length=255)

class ChunkData(models.Model):
    _id = models.CharField(primary_key=True, max_length=255)
    n = models.IntegerField()
    data = models.BinaryField()
    file_id  = models.ForeignKey(MetaData, on_delete=models.CASCADE)
