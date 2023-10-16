from . import views
from django.urls import path
app_name="todoapp"
urlpatterns=[
    path("",views.task,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id1>/',views.update,name='update'),
    path('cbhome/',views.Tasklistview.as_view(),name="cbhome"),
    path('cbdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbdetail'),
    path('cbupdate/<int:pk>/',views.TaskUpdateView.as_view(),name="cbupdate"),
    path('cbdelete/<int:pk>/',views.TaskDeleteView.as_view(),name="cbdelete")



]