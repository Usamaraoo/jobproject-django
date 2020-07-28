# Generated by Django 3.0.7 on 2020-07-28 07:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('job_seeker_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(max_length=500)),
                ('phone_number', models.CharField(max_length=20)),
                ('company_image', models.ImageField(upload_to='')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='job_seeker_profile.Location')),
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
            name='CompanyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login_date', models.DateTimeField(auto_now_add=True)),
                ('last_job_post', models.DateTimeField(blank=True, null=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CompanyProfile.Company')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='CompanyProfile.Company')),
            ],
        ),
    ]