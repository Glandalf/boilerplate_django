# Generated by Django 2.1.1 on 2018-09-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Powkimon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=2)),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=256)),
                ('level', models.IntegerField(verbose_name=2)),
            ],
        ),
    ]