# Generated by Django 2.0.5 on 2018-09-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programa',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='programa',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
