# Generated by Django 3.2.6 on 2021-09-13 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coursehai', '0016_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('isSameBillingAddress', models.BooleanField(default=False)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.IntegerField()),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
