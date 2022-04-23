from django.urls import path

from bundesliga_project.bundesliga_app.views import HomePage, AllMatches, AllTeamsView

urlpatterns = (
    path('', HomePage.as_view(), name='home'),
    path('season-matches/<str:slug>/', AllMatches.as_view(), name='season view'),
    path('past-matches/<str:slug>/', AllMatches.as_view(), name='past view'),
    path('upcoming-matches/<str:slug>/', AllMatches.as_view(), name='upcoming view'),
    path('all-teams/<str:slug>/', AllTeamsView.as_view(), name='teams view'),
)
