# Generated by Django 4.1.4 on 2023-08-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siteadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=80)),
                ('password', models.CharField(default='password', max_length=40)),
            ],
            options={
                'db_table': 'siteadmin',
            },
        ),
    ]