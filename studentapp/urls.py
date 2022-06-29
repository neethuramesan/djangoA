from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.add_student,name="add_student"),
    path('add_student_details',views.add_student_details,name="add_student_details"),
    path('show_student',views.show_student,name="show_student"),
    path('show_student_details/<int:pk>',views.show_student_details,name="show_student_details"),
    path('edit_page/<int:pk>',views.edit_page,name="edit_page"),
    path('edit_details/<int:pk>',views.edit_details,name="edit_details"),
    path('delete_page/<int:pk>',views.delete_page,name="delete_page"),
    path('addcourse',views.addcourse,name="addcourse")
]