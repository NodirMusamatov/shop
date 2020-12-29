# Generated by Django 3.1.3 on 2020-12-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201215_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='TestSlider',
        ),
        migrations.AlterField(
            model_name='category',
            name='is_main',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='information',
            name='about_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='baker_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='card_info',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='information',
            name='contact_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='facebook_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='footer_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='instagram_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='order_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='payments_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='shipping',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='time_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='information',
            name='twitter_info',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
