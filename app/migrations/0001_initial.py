# Generated by Django 2.1 on 2018-08-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=256)),
                ('version', models.CharField(max_length=256)),
                ('downloadurl', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechatid', models.CharField(max_length=256)),
                ('number', models.IntegerField()),
                ('total', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('cost', models.IntegerField()),
                ('record', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wechatid', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=256)),
                ('money', models.CharField(max_length=256)),
                ('time', models.DateTimeField()),
                ('record', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=256)),
                ('appid', models.CharField(max_length=256)),
                ('usekey', models.CharField(max_length=256)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('password_md5', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=256)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
    ]
