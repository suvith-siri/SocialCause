# Generated by Django 4.0.4 on 2022-05-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_rename_details_datas'),
    ]

    operations = [
        migrations.AddField(
            model_name='datas',
            name='pic',
            field=models.ImageField(default=4, upload_to='pics'),
            preserve_default=False,
        ),
    ]
