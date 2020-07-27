from django.db import models


# Create your models here.
class JobPost(models.Model):
    id = models.AutoField(primary_key=True)
    # posted_by_id = models.ForeignKey('CompanyProfile.Company',on_delete=models.DO_NOTHING,related_name='+')
    job_type_id = models.ForeignKey('JobType',on_delete=models.DO_NOTHING ,related_name='+')
    created_date = models.DateTimeField(auto_now_add=True)
    job_description = models.CharField(max_length=500)
    is_active = models.BooleanField()
    location_id = models.ForeignKey('job_seeker_profile.Location', on_delete=models.DO_NOTHING)
    company_id = models.ForeignKey('CompanyProfile.Company', on_delete=models.DO_NOTHING , default=1)
    company_name = models.ForeignKey('CompanyProfile.Company', related_name='+',on_delete=models.DO_NOTHING, default='google')
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title

class JobPostActivity(models.Model):
    user_account_id = models.ForeignKey('job_seeker_profile.CV', on_delete=models.DO_NOTHING)
    job_post_id = models.ForeignKey(JobPost, on_delete=models.DO_NOTHING)
    apply_date = models.DateTimeField(auto_now_add=True)


class JobType(models.Model):
    id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=30)


class JobPostSkillSet(models.Model):
    skill_set_id = models.ForeignKey('job_seeker_profile.SkillSet',on_delete=models.DO_NOTHING)
    job_post_id = models.ForeignKey(JobPost,on_delete=models.DO_NOTHING)
    skill_level = models.IntegerField(default=0)

