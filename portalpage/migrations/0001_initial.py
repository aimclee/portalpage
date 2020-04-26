# Generated by Django 3.0.5 on 2020-04-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accessTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('price', models.CharField(max_length=200)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='mainBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='rollingBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='subBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]
