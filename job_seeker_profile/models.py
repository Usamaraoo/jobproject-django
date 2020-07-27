from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    zip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.city


class EducationDetail(models.Model):
    user_account_id = models.ForeignKey('CV', on_delete=models.CASCADE)
    certificate_degree_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    institute_university_name = models.CharField(max_length=50)
    start_date = models.DateField()
    complete_date = models.DateField(null=True, blank=True)
    percentage = models.IntegerField(null=True, blank=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    location_id = models.ForeignKey('Location', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user_account_id


class CV(models.Model):
    user_account_id = models.ForeignKey('user_management.UserAccount', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    current_salary = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    about = models.CharField(max_length=400, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    reference_name = models.CharField(max_length=20, blank=True, null=True)
    reference_email = models.EmailField(blank=True, null=True)
    reference_phone = models.CharField(max_length=20, blank=True, null=True)
    gender = models.BooleanField()
    mtirial_status = models.BooleanField(default=False)
    location_id = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class PDF(models.Model):
    id = models.AutoField(primary_key=True)
    user_account_id = models.ForeignKey(CV, on_delete=models.DO_NOTHING)
    pdf_cv_file = models.FileField()

    def __str__(self):
        return self.user_account_id


class Reference(models.Model):
    id = models.AutoField(primary_key=True)
    user_account_id = models.ForeignKey(CV, on_delete=models.DO_NOTHING)
    reference_name = models.CharField(max_length=50, blank=False, null=False)
    reference_email = models.EmailField(blank=False, null=False)
    reference_phone = models.CharField(max_length=40, blank=False, null=False)


class ExperienceDetail(models.Model):
    user_account_id = models.ForeignKey(CV, on_delete=models.DO_NOTHING)
    is_current_job = models.BooleanField(null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    job_title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    description = models.TextField(max_length=4000)
    location_id = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user_account_id


class SkillSet(models.Model):
    id = models.AutoField(primary_key=True)
    skill_set_na = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_set_na


class SeekerSkillSet(models.Model):
    skill_set_id = models.ForeignKey(SkillSet, on_delete=models.DO_NOTHING)
    user_account_id = models.ForeignKey(CV, on_delete=models.DO_NOTHING)
    skill_level = models.IntegerField(default=0)

    def __str__(self):
        return self.user_account_id
