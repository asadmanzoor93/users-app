# Generated by Django 2.1.4 on 2019-01-25 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190125_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='update_count',
            new_name='user_number',
        ),
    ]