from django.urls import path
from . import views


urlpatterns = [
  path('', views.index, name='Index'),
  path('<int:question_id>/', views.detail, name="Detail"),
  path('<int:question_id>/results/', views.result, name="Result"),
    path('<int:question_id>/vote/', views.vote, name="Vote")
]