# Generated by Django 3.1.2 on 2023-11-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talleres',
            name='imagen',
            field=models.ImageField(default='default_image.jpg', upload_to='talleres_images/'),
        ),
    ]
