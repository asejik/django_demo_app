# Generated by Django 4.0.3 on 2022-04-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
