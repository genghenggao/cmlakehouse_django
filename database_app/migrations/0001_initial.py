# Generated by Django 4.2.6 on 2023-10-07 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=255)),
                ('md5', models.CharField(max_length=255)),
                ('chunkSize', models.IntegerField()),
                ('length', models.FloatField()),
                ('uploadDate', models.DateField()),
                ('contentType', models.CharField(max_length=255)),
                ('metadata', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChunkData',
            fields=[
                ('_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('n', models.IntegerField()),
                ('data', models.BinaryField()),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database_app.metadata')),
            ],
        ),
    ]
