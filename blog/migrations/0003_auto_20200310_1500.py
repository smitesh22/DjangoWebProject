# Generated by Django 3.0.2 on 2020-03-10 09:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_mutlimedia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mutlimedia',
            new_name='Multimedia',
        ),
    ]
