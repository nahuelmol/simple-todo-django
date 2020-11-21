from django.contrib import admin
from django.urls import path
from todin.views import seeing_view, adding_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', seeing_view),
    path('addTodo/', adding_data),
]
