# Generated by Django 3.0.2 on 2020-03-10 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200310_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiomedia',
            old_name='file',
            new_name='image',
        ),
    ]