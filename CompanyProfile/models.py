from django.db import models


# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_image = models.ImageField()
    password = models.CharField(max_length=50)
    location_id = models.ForeignKey('job_seeker_profile.Location', on_delete=models.DO_NOTHING)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class CompanyLog(models.Model):
    last_login_date = models.DateTimeField(auto_now_add=True)
    last_job_post = models.DateTimeField(null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    company_name = models.ForeignKey(Company, on_delete=models.DO_NOTHING, related_name='+')
