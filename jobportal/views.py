import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCategory, JobPost, Location
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse, reverse_lazy
from jobportal.permission import user_is_employee
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from jobportal.forms import JobApplyForm
from account.models import User
from jobportal.models import JobApply
from django.contrib import messages


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


def profile(request):
    return render(request, "jobportal/profile.html", {})


def list_jobs(request, page=1):
    jobs = JobPost.objects.all()
    paginator = Paginator(jobs, 5)
    try:
        jobs = paginator.page(page)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    return render(request, 'home/index.html', {'jobs': jobs})


def search_result_view(request):
    job_list = JobPost.objects.order_by('-updated_at')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            job_list = job_list.filter(title__contains=keyword) | job_list.filter(job_description__contains=keyword) |\
                       job_list.filter(category__name__contains=keyword) |job_list.filter(sub_category__name__contains=keyword)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            job_list = job_list.filter(job_location__location__contains=location)

    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home/index.html', {'jobs': page_obj})


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def apply_job_view(request, id):
    form = JobApplyForm(request.POST or None)
    candidate = get_object_or_404(User, id=request.user.id)
    applicant = JobApply.objects.filter(candidate=candidate, job=id)
    if not applicant:
        if request.method == 'POST':

            if form.is_valid():
                instance = form.save(commit=False)
                instance.candidate = candidate
                instance.save()

                messages.success(
                    request, 'You have successfully applied for this job!')
                return redirect(reverse("jobportal:joblist"))

        else:
            return redirect(reverse("jobportal:joblist"))

    else:

        messages.error(request, 'You already applied for the Job!')

        return redirect(reverse("jobportal:joblist"))


class Jobdetails(DetailView):
    model = JobPost
    template_name = "jobportal/jobdetails.html"


@login_required(login_url=reverse_lazy('account:login'))
@user_is_employee
def appliedJobList(request, page=1):
    jobs = JobApply.objects.all()
    paginator = Paginator(jobs, 5)
    try:
        jobs = paginator.page(page)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    return render(request, 'jobportal/appliedjoblist.html', {'jobs': jobs})