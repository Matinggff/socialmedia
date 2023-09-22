# Generated by Django 4.1.7 on 2023-06-02 06:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_alter_profile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('3e2407b9-e04d-4350-9e09-b1dba9d64161')),
        ),
    ]
