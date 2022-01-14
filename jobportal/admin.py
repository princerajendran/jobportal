from django.contrib import admin
from .models import *


admin.site.site_header = 'Job Portal Admin'
admin.site.site_title = 'Job Portal Admin Panel'
admin.site.index_title = 'Welcome To Job Portal Admin Panel'

class JobPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'job_type', 'created_by']
    list_filter = ['job_location', 'category', 'sub_category', 'job_type', 'salary', 'is_published', 'is_closed']
    search_fields = ['job_location', 'category', 'sub_category', 'job_type', 'salary', 'is_published', 'is_closed']

admin.site.register(JobPost, JobPostAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Salary)
admin.site.register(Location)
admin.site.register(JobType)
admin.site.register(JobApply)

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 0


class ProfileAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInline]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorkExperience)
admin.site.register(Education)
