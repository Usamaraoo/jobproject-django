# Generated by Django 3.0.7 on 2020-07-27 18:50

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('email_notifi_active', models.BooleanField(blank=True)),
                ('user_image', models.ImageField(blank=True, default='images/defaultuserimage.jpg', upload_to='')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login_date', models.DateTimeField(blank=True, null=True)),
                ('last_jobapply_date', models.DateTimeField(blank=True, null=True)),
                ('user_account_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_management.UserAccount')),
            ],
        ),
    ]
