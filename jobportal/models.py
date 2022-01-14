# import uuid
from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

class JobType(models.Model):
    jobtype = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.jobtype

    class Meta:
        verbose_name = 'JobType'
        verbose_name_plural = 'JobTypes'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategorys'

class Salary(models.Model):
    salary = models.CharField(max_length=30, default='10000 - 50000')

    def __str__(self):
        return self.salary

    class Meta:
        verbose_name = 'Salary'
        verbose_name_plural = 'Salaries'

class Location(models.Model):
    location = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

class JobPost(models.Model):
    # jobpost_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=True, default='')
    job_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='produits', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory,related_name='produits', on_delete=models.CASCADE)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    job_description = RichTextField()
    skills_required = TaggableManager()
    company = models.CharField(max_length=50, default='')
    website = models.URLField()
    industry = models.CharField(max_length=50)
    company_description = RichTextField(blank=True, null=True)
    recruiter_name = models.CharField(max_length=50, default='')
    recruiter_email = models.EmailField(max_length=200, default='')
    logo = models.ImageField(upload_to='company_logos/', blank=True)
    vacancy = models.IntegerField()
    experience = models.IntegerField()
    benefits = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Job Post'
        verbose_name_plural = 'Job Posts'


class JobApply(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True)
    is_hired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.candidate.email

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Job Apply'
        verbose_name_plural = 'Job Applies'


class Profile(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    about = RichTextField()
    image = models.ImageField(upload_to='profile/', blank=True)
    job_title = models.CharField(max_length=50, default='')
    skills = TaggableManager()
    years_experience = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    website = models.URLField(max_length=50, default='')
    highest_education = models.CharField(max_length=100, default='')
    linkedin = models.URLField()
    github = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    certificate = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.candidate.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=200, default='')
    company = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    work_from = models.DateField()
    work_to = models.DateField()
    description = RichTextField()
    currently_working_here = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.profile.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200, default='')
    field_of_study = models.CharField(max_length=200, default='')
    school = models.CharField(max_length=200, default='')
    year_from = models.DateField()
    year_to = models.DateField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.profile.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'