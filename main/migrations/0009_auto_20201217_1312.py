# Generated by Django 3.1.3 on 2020-12-17 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201216_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='baker_info',
            field=models.TextField(blank=True),
        ),
    ]