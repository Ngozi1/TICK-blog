# Generated by Django 3.2.15 on 2022-10-08 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile_pics'),
        ),
    ]
