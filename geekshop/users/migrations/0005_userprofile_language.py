# Generated by Django 2.2 on 2021-10-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='язык'),
        ),
    ]