# Generated by Django 4.1.5 on 2023-02-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompanyParser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='curent_value',
            field=models.CharField(blank=True, max_length=220),
        ),
    ]