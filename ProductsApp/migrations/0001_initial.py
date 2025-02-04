# Generated by Django 5.0.4 on 2024-04-16 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
