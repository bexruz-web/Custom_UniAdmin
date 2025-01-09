from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    # FACULTY
    path('faculty/create/', faculty_create, name='faculty_create'),
    path('faculty/<int:pk>/edit/', faculty_edit, name='faculty_edit'),
    path('faculty/<int:pk>/delete/', faculty_delete, name='faculty_delete'),
    path('faculty/list/', faculty_list, name='faculty_list'),
    # KAFEDRA
    path('kafedra/create/', kafedra_create, name='kafedra_create'),
    path('kafedra/<int:pk>/edit', kafedra_edit, name='kafedra_edit'),
    path('kafedra/<int:pk>/delete', kafedra_delete, name='kafedra_delete'),
    path('kafedra/list/', kafedra_list, name='kafedra_list'),
    # SUBJECTS
    path('subject/create/', subject_create, name='subject_create'),
    path('subject/<int:pk>/edit/', subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete', subject_delete, name='subject_delete'),
    path('subjects/list/', subjects_list, name='subjects_list'),

]