# Generated by Django 3.0.7 on 2020-07-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2),
        ),
    ]
