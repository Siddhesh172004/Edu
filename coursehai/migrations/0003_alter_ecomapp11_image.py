# Generated by Django 3.2.6 on 2021-08-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0002_auto_20210830_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecomapp11',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='coursehai\\images'),
        ),
    ]
