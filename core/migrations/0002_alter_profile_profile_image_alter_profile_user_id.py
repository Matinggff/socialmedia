# Generated by Django 4.1.7 on 2023-05-14 11:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='user-image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('d0e3f412-444a-487f-bada-4a167d0556bc')),
        ),
    ]