# Amara, universalsubtitles.org
#
# Copyright (C) 2014 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see
# http://www.gnu.org/licenses/agpl-3.0.html.

"""
Team Workflows
==============

Team workflows are ways for teams to get their subtitling work done.  Team
workflows compliment the :doc:`subtitle-workflows` and add team-specific
features.

Team workflows are responsible for:
    - Providing a SubtitleWorkflow for team videos
    - Handling the workflow settings page
    - Handling the dashboard page
    - Creating extra tabs or the teams section

..  autoclass:: TeamWorkflow
    :members: type_code, label, dashboard_view, workflow_settings_view,
              setup_team, get_subtitle_workflow, extra_pages,
              extra_settings_pages

.. autoclass:: TeamPage

..  autoclass:: teams.workflows.old.workflow.OldTeamWorkflow
"""

from collections import namedtuple

from django.core.urlresolvers import reverse
from django.shortcuts import render

class TeamWorkflow(object):
    type_code = NotImplemented
    """Team.workflow_type value for this workflow."""
    label = NotImplemented
    """Human-friendly name for this workflow.  This is what appears on the
    team creation form.
    """
    dashboard_view = NotImplemented
    """
    view function for the dashboard page.
    """
    user_dashboard_extra = None
    """
    Team-specific extra data to render in user dashboard page.
    """
    workflow_settings_view = NotImplemented
    """
    view function for the workflow settings page.

    .. note::
      All workflows should allow the user to change membership_policy and
      video_policy in their workflow settings page.
    """

    def __init__(self, team):
        self.team = team

    def setup_team(self):
        """Do any additional setup for newly created teams."""
        pass

    def get_subtitle_workflow(self, team_video):
        """Get the SubtitleWorkflow for a video with this workflow.  """
        raise NotImplementedError()

    def extra_pages(self, user):
        """Get extra team pages to handle this workflow.

        These pages will be listed as tabs in the team section.  Workflows
        will typically use this for things like dashboard pages.

        Args:
            user -- user viewing the page

        Returns:
            list of :class:`TeamPage` objects
        """
        return []

    def extra_settings_pages(self, user):
        """Get extra team settings pages to handle this workflow.

        This works just like extra_pages(), but the pages will show up as
        tabs under the settings section.

        Args:
            user -- user viewing the page

        Returns:
            list of :class:`TeamPage` objects
        """
        return []

    def team_page(self, name, title, view_name):
        """Convenience function to create an TeamPage object

        This method automatically generates the URL from view_name using
        reverse()
        """
        url = reverse(view_name, kwargs={'slug': self.team.slug})
        return TeamPage(name, title,  url)

    # these can be used to customize the content in the project/language
    # manager pages
    def render_project_page(self, request, team, project, page_data):
        page_data['videos'] = (team.videos
                             .filter(teamvideo__project=project)
                             .order_by('-id'))[:5]

        return render(request, 'new-teams/project-page.html', page_data)

    def render_all_languages_page(self, request, team, page_data):
        return render(request, 'new-teams/all-languages-page.html', page_data)

    def render_language_page(self, request, team, language_code, page_data):
        qs = (self.team.videos
              .filter(primary_audio_language_code=language_code)
              .order_by('-id'))
        page_data['videos']= qs[:5]
        return render(request, 'new-teams/language-page.html', page_data)

    _type_code_map = {}

    @classmethod
    def get_workflow(cls, team):
        """Get a TeamWorkflow subclass for a team."""
        klass = cls._type_code_map[team.workflow_type]
        return klass(team)

    @classmethod
    def get_choices(cls):
        choices = [(type_code, cls.label)
                   for (type_code, cls) in cls._type_code_map.items()]
        # sort choices so that:
        #   - unisubs choices are first, then extensions (unisubs choices are
        #     1-char)
        #   - after that it's sorted alphabeticaly by code
        choices.sort(key=lambda (code, _): (len(code), code))
        return choices

    @classmethod
    def register(cls):
        """Register a TeamWorkflow subclass.

        Calling this class method will enable it for teams whose
        workflow_type value is cls.type_code
        """
        TeamWorkflow._type_code_map[cls.type_code] = cls

TeamPage = namedtuple('TeamPage', 'name title url')
"""Represents a page in the team's section

Attributes:
    name: machine-name for this tuple.  This is value to use for current in
        the _teams/tabs.html template
    title: human friendly tab title
    url: URL for the page
"""
