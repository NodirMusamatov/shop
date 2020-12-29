# Generated by Django 3.1.3 on 2020-12-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('photo', models.ImageField(upload_to='upload')),
                ('description', models.TextField()),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
