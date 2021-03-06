# Generated by Django 2.2.3 on 2021-09-19 23:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 9, 19, 23, 12, 46, 811347, tzinfo=utc))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.Category')),
            ],
        ),
    ]
