from django.contrib import admin
from django.urls import path
from todin.views import seeing_view, adding_data
from timerizer.views import hours_ahead
from to_do.views import main_init

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', seeing_view),
    path('addTodo/', adding_data),
    path('hour/<int:post_id>/', hours_ahead),
    path('init/', main_init),
]
