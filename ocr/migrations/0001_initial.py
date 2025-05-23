# Generated by Django 5.2 on 2025-04-22 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OCR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.JSONField(blank=True, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'OCR',
                'verbose_name_plural': 'OCR',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OCRTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.JSONField(blank=True, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'OCR Test',
                'verbose_name_plural': 'OCR Tests',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OCRTranslate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ocr_translate_tests/')),
                ('target_language', models.CharField(max_length=10)),
                ('original_text', models.TextField(blank=True, null=True)),
                ('detected_language', models.CharField(blank=True, max_length=10, null=True)),
                ('translated_text', models.TextField(blank=True, null=True)),
                ('processing_time', models.FloatField(blank=True, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'OCR Translate Test',
                'verbose_name_plural': 'OCR Translate Tests',
                'ordering': ['-created_at'],
            },
        ),
    ]
