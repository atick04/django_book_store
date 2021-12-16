# Generated by Django 4.0 on 2021-12-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('image_url', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
