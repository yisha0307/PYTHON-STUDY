from django.shortcuts import render, redirect
from django.http import JsonResponse
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

def praise_or_criticize(request):
    # 好评
    try:
        tno = int(request.GET['tno'])
        teacher = Teacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.good_count += 1
        else:
            teacher.bad_count += 1
        teacher.save()
        data = {'code': 200, 'hint': '操作成功'}
    except (KeyError, ValueError, Teacher.DoesNotExist):
        data = {'code': 404, 'hint': '操作失败'}
    return JsonResponse(data)