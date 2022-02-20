from django.urls import path
from .views import CourseListView, CourseDetailView

app_name = 'courses'

urlpatterns = [
    path('api/courses/', CourseListView.as_view()),
    path('api/courses/<int:pk>/', CourseDetailView.as_view())
]
