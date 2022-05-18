# Generated by Django 3.2.11 on 2022-03-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0002_bottom_pictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=200)),
                ('b', models.TextField()),
                ('c', models.ImageField(upload_to='folder')),
            ],
        ),
        migrations.DeleteModel(
            name='bottom_pictures',
        ),
    ]