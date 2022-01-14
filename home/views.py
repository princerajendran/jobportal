from django.shortcuts import render
from jobportal.models import JobPost
from django.core.paginator import Paginator, EmptyPage


def index(request, page=1):
    jobs = JobPost.objects.all()
    paginator = Paginator(jobs, 5)
    try:
        jobs = paginator.page(page)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'home/index.html', {'jobs': jobs})