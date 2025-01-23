from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from . import services


def login_required_decorator(func):
    return login_required(func, login_url='login_page')


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'login.html')


@login_required_decorator
def home_page(requset):
    faculties = services.get_data_from_table("adminapp_faculty")
    kafedras = services.get_data_from_table("adminapp_kafedra")
    subjects = services.get_data_from_table("adminapp_subjects")
    teachers = services.get_data_from_table("adminapp_teachers")
    groups = services.get_data_from_table("adminapp_groups")
    students = services.get_data_from_table("adminapp_students")
    ctx = {
        'counts': {
            'faculties': len(faculties),
            'kafedras': len(kafedras),
            'subjects': len(subjects),
            'teachers': len(teachers),
            'groups': len(groups),
            'students': len(students),
        }
    }
    return render(requset, 'index.html', ctx)

# FACULTY
@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions

        faculty_count = request.session.get('faculty_count', 0)
        faculty_count += 1
        request.session['faculty_count'] = faculty_count

        return redirect('faculty_list')
    ctx = {
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('faculty_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    name = model.name
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Faculty: {name}"]
    request.session['actions'] = actions

    return redirect('faculty_list')


@login_required_decorator
def faculty_list(request):
    faculties = services.get_data_from_table("adminapp_faculty")
    print(faculties)
    ctx = {
        'faculties': faculties
    }
    return render(request, 'faculty/list.html', ctx)


# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions

        kafedra_count = request.session.get('kafedra_count', 0)
        kafedra_count += 1
        request.session['kafedra_count'] = kafedra_count

        return redirect('kafedra_list')
    ctx = {
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('kafedra_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'kafedra/form.html', ctx)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    name = model.name
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Kafedra: {name}"]
    request.session['actions'] = actions

    return redirect('kafedra_list')


@login_required_decorator
def kafedra_list(request):
    kafedras = services.get_kafedra_with_faculty()
    ctx = {
        'kafedras': kafedras
    }
    return render(request, 'kafedra/list.html', ctx)


# SUBJECTS
@login_required_decorator
def subject_create(request):
    model = Subjects()
    form = SubjectsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Subject: {request.POST.get('name')}"]
        request.session['actions'] = actions

        subject_count = request.session.get('subject_count', 0)
        subject_count +=1
        request.session['subject_count'] = subject_count

        return redirect('subjects_list')
    ctx = {
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subjects.objects.get(pk=pk)
    form = SubjectsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Subject: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('subjects_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subjects.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Subject: {request.POST.get('name')}"]
    request.session['actions'] = actions

    return redirect('subjects_list')


@login_required_decorator
def subjects_list(request):
    subjects = services.get_data_from_table("adminapp_subjects")
    ctx = {
        'subjects': subjects
    }
    return render(request, 'subject/list.html', ctx)


# TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teachers()
    form = TeachersForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Teacher: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
        request.session['actions'] = actions

        teacher_count = request.session.get('teacher_count', 0)
        teacher_count += 1
        request.session['teacher_count'] = teacher_count

        return redirect('teachers_list')

    ctx = {
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teachers.objects.get(pk=pk)
    form = TeachersForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Teacher: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
        request.session['actions'] = actions

        return redirect('teachers_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teachers.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Teacher: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
    request.session['actions'] = actions

    return redirect('teachers_list')


@login_required_decorator
def teachers_list(request):
    teachers = services.get_teachers_with_details()
    ctx = {
        'teachers': teachers
    }
    return render(request, 'teacher/list.html', ctx)


# GROUPS
@login_required_decorator
def group_create(request):
    model = Groups()
    form = GroupsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Group: {request.POST.get('name')}"]
        request.session['actions'] = actions

        group_count = request.session.get('group_count', 0)
        group_count +=1
        request.session['group_count'] = group_count

        return redirect('groups_list')
    ctx = {
        'form': form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Groups.objects.get(pk=pk)
    form = GroupsForm(request.POST, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Group: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('groups_list')
    ctx = {
        'model': model,
        'form':form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Groups.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Group: {request.POST.get('name')}"]
    request.session['actions'] = actions

    return redirect('groups_list')


@login_required_decorator
def groups_list(request):
    groups = services.get_groups_with_details()
    ctx = {
        'groups': groups
    }
    return render(request, 'group/list.html', ctx)


# STUDENTS
@login_required_decorator
def student_create(request):
    model = Students()
    form = StudentsForm(request.POST, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created Student: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
        request.session['actions'] = actions

        student_count = request.session.get('student_count', 0)
        student_count += 1
        request.session['student_count'] = student_count

        return redirect('students_list')
    else:
        print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Students.objects.get(pk=pk)
    form = StudentsForm(request.POST, request.FILES, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited Student: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
        request.session['actions'] = actions

        return redirect('students_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Students.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted Student: {request.POST.get('first_name')} {request.POST.get('last_name')}"]
    request.session['actions'] = actions

    return redirect('students_list')


@login_required_decorator
def student_list(request):
    students = services.get_students_with_groups()
    ctx = {
        "students": students
    }
    return render(request, 'student/list.html', ctx)


@login_required_decorator
def profile(request):
    return render(request, 'profile.html')


