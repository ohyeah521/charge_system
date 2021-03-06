# Generated by Django 2.1 on 2018-08-23 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updatetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='buy',
            name='total',
            field=models.FloatField(max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='money',
            field=models.FloatField(max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
