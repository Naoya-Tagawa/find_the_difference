# Generated by Django 4.1.7 on 2023-04-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saize', '0002_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.ImageField(upload_to=''),
        ),
    ]
