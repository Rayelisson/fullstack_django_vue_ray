# Generated by Django 4.2.7 on 2023-11-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='post.postattachment'),
        ),
    ]