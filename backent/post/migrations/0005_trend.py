# Generated by Django 4.2.7 on 2023-12-01 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=255)),
                ('occurences', models.IntegerField()),
            ],
        ),
    ]