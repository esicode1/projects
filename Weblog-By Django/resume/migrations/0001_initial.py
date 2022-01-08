# Generated by Django 4.0 on 2021-12-27 22:22

from django.db import migrations, models
import django.db.models.deletion
import resume.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='images/user_avatar/', validators=[resume.models.validate_jpg_png_file])),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
