# Generated by Django 3.1.3 on 2020-12-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201216_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_best_seller',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='menu',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]
