# Generated by Django 4.2.2 on 2023-07-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]