from django.views.generic import TemplateView

from bundesliga_project.bundesliga_app.common.helpers import get_upcoming_matches, get_all_matches, get_all_teams
from datetime import datetime as dt
from datetime import timedelta

BUNDESLIGA_ONE = "bl1"
BUNDESLIGA_TWO = "bl2"
BUNDESLIGA_THREE = "bl3"
DAYS_AFTER_TODAY = 1


class HomePage(TemplateView):
    template_name = 'bundesliga.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = dt.today() + timedelta(days=DAYS_AFTER_TODAY)

        matches_bl1 = get_upcoming_matches(BUNDESLIGA_ONE, date)
        matches_bl2 = get_upcoming_matches(BUNDESLIGA_TWO, date)
        matches_bl3 = get_upcoming_matches(BUNDESLIGA_THREE, date)
        context['matches_bl1'] = matches_bl1
        context['matches_bl2'] = matches_bl2
        context['matches_bl3'] = matches_bl3
        context['date'] = date
        return context


class AllMatches(TemplateView):
    TEMPLATE_NAME_ALL = "all_matches.html"
    TEMPLATE_NAME_UPCOMING = "upcoming_matches.html"
    TEMPLATE_NAME_PAST = "past_matches.html"
    URL_ALL = 'season-matches'
    URL_UPCOMING = 'upcoming-matches'
    URL_PAST = 'past-matches'

    TEMPLATE_NAME_DICT = {
        URL_ALL: TEMPLATE_NAME_ALL,
        URL_UPCOMING: TEMPLATE_NAME_UPCOMING,
        URL_PAST: TEMPLATE_NAME_PAST,
    }

    def get_template_names(self):
        url = self.request.path.split('/')[1]
        return [self.TEMPLATE_NAME_DICT[url]]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = get_all_matches(kwargs['slug'])
        season_matches = {}
        for match in data:
            if match.matchDateTime.strftime('%Y-%m-%d') not in season_matches.keys():
                season_matches[match.matchDateTime.strftime('%Y-%m-%d')] = []
            season_matches[match.matchDateTime.strftime('%Y-%m-%d')].append(match)

        context['season_matches'] = season_matches

        return context


class AllTeamsView(TemplateView):
    template_name = 'teams_stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = get_all_teams(kwargs['slug'])
        context['teams'] = teams
        searched_item_string = self.request.GET.get('team') or 'Show all'
        context['searched_item_string'] = searched_item_string.lower()

        return context
