# Generated by Django 3.0.3 on 2020-02-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientdb', '0007_client_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=60),
        ),
    ]