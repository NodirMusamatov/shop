# Generated by Django 3.1.3 on 2020-12-13 13:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_testslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testslider',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]