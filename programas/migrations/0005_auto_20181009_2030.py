# Generated by Django 2.0.5 on 2018-10-09 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0004_auto_20181009_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
