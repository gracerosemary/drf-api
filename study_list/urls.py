from django.urls import path
from .views import StudyListed, StudyDetail

urlpatterns = [
    path('', StudyListed.as_view(), name='study_list'),
    path('<int:pk>', StudyDetail.as_view(), name='study_detail'),
]