from django.urls import path
from . import views

app_name = 'jobportal'

urlpatterns = [
    path('getSubcategory/', views.get_subcategory),
    path('profile/', views.profile,name="profile" ),
    path('joblist/<int:page>/', views.list_jobs, name='joblist'),
    path('joblist/', views.list_jobs,name="joblist" ),
    path('result/', views.search_result_view, name='search_result'),
    path('jobdetails/<int:pk>/', views.Jobdetails.as_view(), name='jobdetails'),
    path('apply-job/<int:id>/', views.apply_job_view, name='apply-job'),
    path('appliedjoblist/', views.appliedJobList, name='appliedjoblist'),
]