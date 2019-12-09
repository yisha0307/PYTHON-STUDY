from django.shortcuts import render, redirect
from django.http import JsonResponse
from vote.models import Subject, Teacher, User, RegisterForm, LoginForm
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

def register(request):
    # 注册
    # 如果是get，直接去注册的页面，如果以POST方式提交注册表单, 则提交表单
    page, hint = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            page = 'login.html'
            hint = '注册成功，请登录'
        else:
            hint = '请输入有效的注册信息'
    return render(request, page, {'hint': hint})

def login(request):
    hint = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()
            if user:
                return redirect('/')
            else:
                hint = '用户名或者密码错误'
        else:
            hint = '请输入有效的登录信息'
    return render(request, 'login.html', {'hint': hint})