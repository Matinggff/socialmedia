# Generated by Django 4.1.7 on 2023-06-11 12:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_like_alter_profile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('8916fa82-e861-41ee-929b-68a4948838d6')),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=90)),
                ('user', models.CharField(max_length=90)),
                ('comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.post')),
            ],
        ),
    ]
