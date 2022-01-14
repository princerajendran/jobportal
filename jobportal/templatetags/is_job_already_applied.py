from django import template
from jobportal.models import JobApply

register = template.Library()

@register.simple_tag(name='is_job_already_applied')
def is_job_already_applied(job, user):
    applied = JobApply.objects.filter(job=job, candidate=user)
    if applied:
        return True
    else:
        return False
