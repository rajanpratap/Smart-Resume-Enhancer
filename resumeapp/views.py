# resumeapp/views.py
from django.shortcuts import render
from .forms import ResumeJobForm
from .resume_analysis import run_resume_analysis

def home(request):
    result = None
    if request.method == "POST":
        form = ResumeJobForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = form.cleaned_data['resume_file']
            job_url = form.cleaned_data['job_url']
            result = run_resume_analysis(resume_file, job_url)
    else:
        form = ResumeJobForm()
    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'resumeapp/home.html', context)
