# Generated by Django 3.1.3 on 2020-11-29 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker', models.CharField(max_length=30)),
                ('sentence', models.CharField(max_length=200)),
            ],
        ),
    ]
