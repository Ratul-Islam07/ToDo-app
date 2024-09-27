from django.urls import path
from .views import SignUpView, TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, toggle_task_complete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", TaskList.as_view(), name="tasklist"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="taskdetail"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="taskupdate"),
    path("delete/<int:pk>/", TaskDelete.as_view(), name="taskdelete"),
    path("task_create/", TaskCreate.as_view(), name="taskcreate"),
    path('toggle-task-complete/<int:task_id>/', toggle_task_complete, name='toggle_task_complete'),
]