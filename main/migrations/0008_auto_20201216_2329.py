# Generated by Django 3.1.3 on 2020-12-16 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201216_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size'),
        ),
    ]