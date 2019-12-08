from django.shortcuts import render, redirect
from vote.models import Subject, Teacher
# Create your views here.
def show_subjects(request):
    # 查看所有学科
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})

def show_teachers(request):
    # 查看指定学科的老师
    try:
        sno = int(request.GET['sno'])
        subject = Subject.objects.get(no=sno)
        # xxx_set 反查
        teachers = subject.teacher_set.all()
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except (KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')