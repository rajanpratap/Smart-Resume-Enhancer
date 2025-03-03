# resumeapp/forms.py
from django import forms

class ResumeJobForm(forms.Form):
    resume_file = forms.FileField(label="Upload your resume (Word, PPT, or PDF)")
    job_url = forms.URLField(label="Paste the job listing URL")
