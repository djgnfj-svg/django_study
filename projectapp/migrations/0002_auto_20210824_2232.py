# Generated by Django 3.2.5 on 2021-08-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='created_ay',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]