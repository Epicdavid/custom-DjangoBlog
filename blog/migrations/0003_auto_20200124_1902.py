# Generated by Django 2.2.5 on 2020-01-25 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191209_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='postpic/fog4.jpg', upload_to='postpic/'),
        ),
    ]
