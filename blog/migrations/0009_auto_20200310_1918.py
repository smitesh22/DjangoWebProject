# Generated by Django 3.0.2 on 2020-03-10 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200310_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiomedia',
            old_name='image',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='imagemedia',
            old_name='file',
            new_name='image',
        ),
    ]