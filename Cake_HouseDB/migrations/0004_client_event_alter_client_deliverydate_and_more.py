# Generated by Django 4.1.7 on 2023-03-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cake_HouseDB', '0003_rename_gender_client_caketype_remove_client_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='event',
            field=models.CharField(default='Birthday', max_length=50),
        ),
        migrations.AlterField(
            model_name='client',
            name='deliverydate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='orderdate',
            field=models.DateField(),
        ),
    ]