# Generated by Django 3.2.6 on 2021-09-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0003_alter_ecomapp11_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecomapp11',
            name='image',
            field=models.ImageField(default='courseapp\\images\\shoe.jpg', upload_to='courseapp\\images'),
        ),
    ]