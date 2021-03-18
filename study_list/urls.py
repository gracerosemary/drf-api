from django.urls import path
from .views import StudyListed, StudyDetail

urlpatterns = [
    path('', StudyListed.as_view(), name='study_list'),
    path('<int:pk>/', StudyDetail.as_view(), name='study_detail'),
    path('new/', StudyDetail.as_view(), name='study_create'),
    path('<int:pk>/edit', StudyDetail.as_view(), name='study_update'),
    path('<int:pk>/delete', StudyDetail.as_view(), name='study_delete'),
]