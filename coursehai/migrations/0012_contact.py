# Generated by Django 3.2.6 on 2021-09-13 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0011_ecomapp11_extra_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Tel', models.IntegerField()),
                ('Image', models.ImageField(default='courseapp\\images\\shoe.jpg', upload_to='courseapp\\images')),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('Desc', models.CharField(max_length=500)),
            ],
        ),
    ]
