from django.urls import path

from . import views

app_name = "freq"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # This pattern leads to the default view/template
    path("<int:pk>/", views.StationView.as_view(), name="frequency"), # This pattern will show the details of
    path("<int:pk>/delete/", views.StationDelete.as_view(), name="delete"),
 

    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]