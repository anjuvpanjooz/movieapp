# Generated by Django 4.2.2 on 2023-06-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(),
        ),
    ]
