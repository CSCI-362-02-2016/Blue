# Amara, universalsubtitles.org
#
# Copyright (C) 2015 Participatory Culture Foundation
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along
# with this program.  If not, see http://www.gnu.org/licenses/agpl-3.0.html.
"""
Teams
-----

Team Resource
*************

Get a list of teams
^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/

    Get a paginated list of all teams

    :>json string name: Name of the team
    :>json slug slug: Machine name for the team slug (used in URLs)
    :>json string description: Team description
    :>json boolean is_visible: Should this team's videos be publicly visible?
    :>json string membership_policy: Team membership policy. One of:

        - ``Open``
        - ``Application``
        - ``Invitation by any team member``
        - ``Invitation by manager``
        - ``Invitation by admin``

    :>json string video_policy: Team video policy.  One of:

        - ``Any team member``
        - ``Managers and admins``
        - ``Admins only``

    :>json uri activity_uri: Team activity resource
    :>json uri members_uri: Team member list resource
    :>json uri safe_members_uri: "Safe" team members list resource
    :>json uri projects_uri: Team projects resource
    :>json uri applications_uri: Team applications resource (or null if the
        membership policy is not by application)
    :>json uri languages_uri: Team preferred/blacklisted languages resource
    :>json uri tasks_uri: Team tasks resource (or null if tasks are not enabled)
    :>json uri resource_uri: Team resource

.. http:get:: /api/teams/(team-slug)/

    Get details on a single team

    The data is the same as the list endpoint

Updating team settings
~~~~~~~~~~~~~~~~~~~~~~

.. http:put:: /api/teams/(team-slug)

    :<json string name: (required) Name of the team
    :<json slug slug: (required) Manchine name for the team (used in URLs)
    :<json string description: Team description
    :<json boolean is_visible: Should this team be publicly visible?
    :<json string membership_policy:  Team membership policy.  One of:

        - ``Open``
        - ``Application``
        - ``Invitation by any team member``
        - ``Invitation by manager``
        - ``Invitation by admin``

    :<json string video_policy:  Team video policy.  One of:

        - ``Any team member``
        - ``Managers and admins``
        - ``Admins only``

Members Resource
****************

API endpoint for team memberships

Listing members of a team
^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/members/

    :>json username username: username
    :>json string role: One of: ``owner``, ``admin``, ``manager``, or
        ``contributor``

Get info on a team member
^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/members/(username)

    The data is in the same format as the listing endpoint.

Adding a member to the team
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:post:: /api/teams/(team-slug)/members/

    :<json username username: username of the user to add
    :<json string role: One of: ``owner``, ``admin``, ``manager``, or
        ``contributor``

Change a team member's role
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:put:: /api/teams/(team-slug)/members/(username)/

    :<json string role: One of: ``owner``, ``admin``, ``manager``, or
        ``contributor``

Removing a user from a team
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:delete:: /api/teams/(team-slug)/members/(username)/

Safe Members Resource
*********************

This resource behaves the same as the normal Team Member resource except
with couple differences for the POST action to add members.

- An invitation is sent to the user to join the team instead of simply
  adding them
- If no user exists with the username, and the email field is included
  in the POST data, we will create a user and send an email to the email
  account.

Projects Resource
*****************

List a team's projects
^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/projects/

    :>json string name: project name
    :>json slug slug: slug for the project
    :>json string description: project description
    :>json string guidelines: Project guidelines for users working on it
    :>json datetime created: datetime when the project was created
    :>json datetime modified: datetime when the project was last changed
    :>json boolean workflow_enabled: Are tasks enabled for this project?
    :>json uri resource_uri: Project details resource

Get details on a project
^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/projects/(project-slug)/

    The data is the same as the listing endpoint

Creating a project
^^^^^^^^^^^^^^^^^^

.. http:post:: /api/teams/(team-slug)/projects/

    :<json string name: project name
    :<json slug slug: slug for the project
    :<json string description: project description **(optional)**
    :<json string guidelines: Project guidelines for users working on it
        **(optional)**

Updating a project
^^^^^^^^^^^^^^^^^^

.. http:put:: /api/teams/(team-slug)/projects/(project-slug)/

    Uses the same data as the POST method

Delete a project
^^^^^^^^^^^^^^^^

.. http:delete:: /api/teams/(team-slug)/projects/(project-slug)/


Tasks Resource
**************

List all tasks for a team
^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/tasks/

    :queryparam username assignee: Show only tasks assigned to a username
    :queryparam integer priority: Show only tasks with a given priority
    :queryparam string type: Show only tasks of a given type
    :queryparam video-id video_id: Show only tasks that pertain to a given video
    :queryparam string order_by: Apply sorting to the task list.  Possible values:

        - ``created``   Creation date
        - ``-created``  Creation date (descending)
        - ``priority``  Priority
        - ``-priority`` Priority (descending)
        - ``type``      Task type (details below)
        - ``-type``     Task type (descending)

    :queryparam boolean completed: Show only complete tasks
    :queryparam integer completed-before: Show only tasks completed before a
        given date (as a unix timestamp)
    :queryparam integer completed-after: Show only tasks completed before a
        given date (as a unix timestamp)
    :queryparam boolean open: Show only incomplete tasks

Get details on a specific task
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/tasks/(task-id)/

    :>json video-id video_id: ID of the video being worked on
    :>json bcp-47 language: Language code being worked on
    :>json integer id: ID for the task
    :>json string type: type of task.  One of ``Subtitle``, ``Translate``,
         ``Review``, or ``Approve``
    :>json username assignee: username of the task assignee (or null)
    :>json integer priority: Priority for the task
    :>json datetime created: Date/time when the task was created
    :>json datetime completed: Date/time when the task was completed (or null)
    :>json string approved: Approval status of the task.  One of
        ``In Progress``, ``Approved``, or ``Rejected``
    :>json resource_uri: Task resource

Create a new task
^^^^^^^^^^^^^^^^^

.. http:post:: /api/teams/(team-slug)/tasks/

    :<json video-id video_id: Video ID
    :<json bcp-47 language: language code
    :<json string type: task type to create.  Must be ``Subtitle`` or
        ``Translate``
    :<json username assignee: Username of the task assignee **(optional)**
    :<json integer priority: Priority for the task **(optional)**

Update an existing task
^^^^^^^^^^^^^^^^^^^^^^^

.. http:put:: /api/teams/(team-slug)/tasks/(task-id)/

    :<json username assignee: Username of the task assignee or null to unassign
    :<json integer priority: priority of the task
    :<json boolean send_back: send a truthy value to send the back back
        **(optional)**
    :<json boolean complete: send a truthy value to complete/approve the task
        **(optional)**
    :<json integer version_number: Specify the version number of the subtitles
        that were created for this task **(optional)**

.. note::
    If both send_back and approved are specified, then send_back will take
    preference.

Delete an existing task
^^^^^^^^^^^^^^^^^^^^^^^

.. http:delete:: /api/teams/(team-slug)/tasks/(task-id)/

Applications Resource
*********************

This endpoint only works for teams with membership by application.

List applications
^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/applications

    :queryparam string status: Include only applications with this status
    :queryparam integer before: Include only applications submitted before
        this time (as a unix timestamp)
    :queryparam integer after: Include only applications submitted after this
        time (as a unix timestamp)
    :queryparam username user: Include only applications from this user

    List results are paginated

Get details on a single application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:get:: /api/teams/(team-slug)/applications/(application-id)/:

    :>json username user: Username of the applicant
    :>json string note: note given by the applicant
    :>json string status: status value.  Possible values are ``Denied``,
        ``Approved``, ``Pending``, ``Member Removed`` and ``Member Left``
    :>json integer id: application ID
    :>json datetime created: creation date/time
    :>json datetime modified: last modified date/time
    :>json uri resource_uri: Application resource

Approve/Deny an application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. http:put:: /api/teams/(team-slug)/applications/(application-id)/

    :<json string status: ``Denied`` to deny the application and ``Approved`` to
        approve it.

Preferred Languages Resource
****************************

Preferred languages will have tasks auto-created for each video.

.. http:put:: /api/teams/(team-slug)/languages/preferred/

    Send a list of language codes as data.

Blacklisted Languages Resource
******************************

Subtitles for blacklisted languages will not be allowed.

.. http:put:: /api/teams/(team-slug)/languages/blacklisted/

    Send a list of language codes as data.
"""

from __future__ import absolute_import
from datetime import datetime

from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from api.fields import TimezoneAwareDateTimeField
from auth.models import CustomUser as User
from teams.models import (Team, TeamMember, Project, Task, TeamVideo,
                          Application, TeamLanguagePreference)
from utils.translation import ALL_LANGUAGE_CODES
import messages.tasks
import subtitles.signals
import teams.permissions as team_permissions
import videos.tasks

def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(int(timestamp))

class MappedChoiceField(serializers.ChoiceField):
    """Choice field that maps internal values to choices."""

    default_error_messages = {
        'unknown-choice': "Unknown choice: {choice}",
    }

    def __init__(self, choices, *args, **kwargs):
        self.map = dict((value, choice) for value, choice in choices)
        self.rmap = dict((choice, value) for value, choice in choices)
        super(MappedChoiceField, self).__init__(self.rmap.keys(), *args,
                                                **kwargs)

    def to_internal_value(self, choice):
        try:
            return self.rmap[choice]
        except KeyError:
            self.fail('unknown-choice', choice=choice)

    def to_representation(self, value):
        return self.map[value]

class TeamSerializer(serializers.ModelSerializer):
    # Handle mapping internal values for membership/video policy to the values
    # we use in the api (currently the english display name)
    MEMBERSHIP_POLICY_CHOICES = (
        (Team.OPEN, u'Open'),
        (Team.APPLICATION, u'Application'),
        (Team.INVITATION_BY_ALL, u'Invitation by any team member'),
        (Team.INVITATION_BY_MANAGER, u'Invitation by manager'),
        (Team.INVITATION_BY_ADMIN, u'Invitation by admin'),
    )
    VIDEO_POLICY_CHOICES = (
        (Team.VP_MEMBER, u'Any team member'),
        (Team.VP_MANAGER, u'Managers and admins'),
        (Team.VP_ADMIN, u'Admins only'),
    )
    membership_policy = MappedChoiceField(
        MEMBERSHIP_POLICY_CHOICES, required=False,
        default=Team._meta.get_field('membership_policy').get_default())
    video_policy = MappedChoiceField(
        VIDEO_POLICY_CHOICES, required=False,
        default=Team._meta.get_field('video_policy').get_default())

    activity_uri = serializers.HyperlinkedIdentityField(
        view_name='api:team-activity',
        lookup_field='slug',
    )
    members_uri = serializers.SerializerMethodField()
    safe_members_uri = serializers.SerializerMethodField()
    projects_uri = serializers.SerializerMethodField()
    applications_uri = serializers.SerializerMethodField()
    tasks_uri = serializers.SerializerMethodField()
    languages_uri = serializers.SerializerMethodField()
    resource_uri = serializers.SerializerMethodField()

    def get_members_uri(self, team):
        return reverse('api:team-members-list', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_safe_members_uri(self, team):
        return reverse('api:safe-team-members-list', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_projects_uri(self, team):
        return reverse('api:projects-list', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_applications_uri(self, team):
        if not team.is_by_application():
            return None
        return reverse('api:team-application-list', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_languages_uri(self, team):
        if not team.is_old_style():
            return None
        return reverse('api:team-languages', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_tasks_uri(self, team):
        if not team.workflow_enabled:
            return None
        return reverse('api:tasks-list', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    def get_resource_uri(self, team):
        return reverse('api:teams-detail', kwargs={
            'team_slug': team.slug,
        }, request=self.context['request'])

    class Meta:
        model = Team
        fields = ('name', 'slug', 'description', 'is_visible',
                  'membership_policy', 'video_policy', 'activity_uri',
                  'members_uri', 'safe_members_uri', 'projects_uri',
                  'applications_uri', 'languages_uri', 'tasks_uri',
                  'resource_uri')

class TeamUpdateSerializer(TeamSerializer):
    name = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

class TeamViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    lookup_field = 'slug'
    lookup_url_kwarg = 'team_slug'
    paginate_by = 20

    def get_queryset(self):
        return Team.objects.for_user(self.request.user)

    def get_serializer_class(self):
        if 'slug' in self.kwargs:
            return TeamUpdateSerializer
        else:
            return TeamSerializer

    def perform_create(self, serializer):
        if not team_permissions.can_create_team(self.request.user):
            raise PermissionDenied()
        team = serializer.save()
        TeamMember.objects.create_first_member(team=team,
                                               user=self.request.user)

    def perform_update(self, serializer):
        if not team_permissions.can_change_team_settings(serializer.instance,
                                                         self.request.user):
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, instance):
        if not team_permissions.can_delete_team(instance, self.request.user):
            raise PermissionDenied()
        instance.delete()

class TeamMemberSerializer(serializers.Serializer):
    default_error_messages = {
        'user-does-not-exist': "User does not exist: {username}",
        'user-already-member': "User is already a team member",
    }

    ROLE_CHOICES = (
         TeamMember.ROLE_OWNER,
         TeamMember.ROLE_ADMIN,
         TeamMember.ROLE_MANAGER,
         TeamMember.ROLE_CONTRIBUTOR,
    )

    username = serializers.CharField(source='user.username')
    role = serializers.ChoiceField(ROLE_CHOICES)

    def validate_username(self, username):
        try:
            self.user = User.objects.get(username=username)
            return username
        except User.DoesNotExist:
            self.fail('user-does-not-exist', username=username)

    def create(self, validated_data):
        try:
            return self.context['team'].members.create(
                user=self.user,
                role=validated_data['role'],
            )
        except IntegrityError:
            self.fail('user-already-member')

class TeamMemberUpdateSerializer(TeamMemberSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    def update(self, instance, validated_data):
        instance.role = validated_data['role']
        instance.save()
        return instance

class TeamSubviewMixin(object):
    def initial(self, request, *args, **kwargs):
        super(TeamSubviewMixin, self).initial(request, *args, **kwargs)
        try:
            self.team = Team.objects.get(slug=kwargs['team_slug'])
        except Team.DoesNotExist:
            self.team = None
            raise Http404

    def get_serializer_context(self):
        return {
            'team': self.team,
            'user': self.request.user,
            'request': self.request,
        }

class TeamSubview(TeamSubviewMixin, viewsets.ModelViewSet):
    pass

class TeamMemberViewSet(TeamSubview):
    lookup_field = 'username'
    paginate_by = 20

    def get_serializer_class(self):
        if 'username' in self.kwargs:
            return TeamMemberUpdateSerializer
        else:
            return TeamMemberSerializer

    def get_queryset(self):
        if not self.team.user_is_member(self.request.user):
            raise PermissionDenied()
        return self.team.members.all().select_related("user")

    def get_object(self):
        if not self.team.user_is_member(self.request.user):
            raise PermissionDenied()
        member = get_object_or_404(self.team.members,
                                   user__username=self.kwargs['username'])
        return member

    def check_join_permissions(self, role):
        if not (role == TeamMember.ROLE_CONTRIBUTOR and
                team_permissions.can_join_team(self.team, self.request.user)):
            raise PermissionDenied()

    def check_add_permissions(self, role):
        if not team_permissions.can_add_member(
                self.team, self.request.user, role):
            raise PermissionDenied()

    def perform_create(self, serializer):
        if serializer.user == self.request.user:
            self.check_join_permissions(serializer.validated_data['role'])
        else:
            self.check_add_permissions(serializer.validated_data['role'])
        serializer.save()

    def perform_update(self, serializer):
        if not team_permissions.can_assign_role(
            self.team, self.request.user, serializer.validated_data['role'],
            serializer.instance.user):
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, member):
        if not team_permissions.can_remove_member(self.team,
                                                  self.request.user):
            raise PermissionDenied()
        if member.role == TeamMember.ROLE_OWNER:
            raise serializers.ValidationError("Can't remove team owner")
        member.delete()

class SafeTeamMemberSerializer(TeamMemberSerializer):
    email = serializers.EmailField(required=False, write_only=True)

    default_error_messages = {
        'email-required': "Email required to create user",
    }

    def validate_username(self, username):
        return username

    def validate(self, attrs):
        try:
            self.user = User.objects.get(username=attrs['user']['username'])
        except User.DoesNotExist:
            if 'email' not in attrs:
                self.fail('email-required')
            self.user = User.objects.create(
                username=attrs['user']['username'],
                email=attrs['email'])
        return attrs

    def create(self, validated_data):
        team = self.context['team']
        if team.members.filter(user=self.user).exists():
            self.fail('user-already-member')
        invite = team.invitations.create(user=self.user,
                                         author=self.context['user'],
                                         role=validated_data['role'])
        messages.tasks.team_invitation_sent.delay(invite.id)
        # return an unsaved TeamMember for serialization purposes
        return TeamMember(user=self.user, team=team,
                          role=validated_data['role'])

class SafeTeamMemberViewSet(TeamMemberViewSet):
    def get_serializer_class(self):
        if 'username' in self.kwargs:
            return TeamMemberUpdateSerializer
        else:
            return SafeTeamMemberSerializer

    def create(self, request, *args, **kwargs):
        response = super(SafeTeamMemberViewSet, self).create(request, *args,
                                                             **kwargs)
        # use 202 status code since we invited the user instead of created a
        # membership
        response.status_code = status.HTTP_202_ACCEPTED
        return response

class ProjectSerializer(serializers.ModelSerializer):
    resource_uri = serializers.SerializerMethodField()
    created = TimezoneAwareDateTimeField(read_only=True)
    modified = TimezoneAwareDateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'slug', 'description', 'guidelines',
                  'modified', 'created', 'workflow_enabled', 'resource_uri')
        # Based on the model code, slug can be blank, but this seems bad to
        # allow for API requests
        read_only_fields = ('modified', 'created')
        extra_kwargs = {
            'slug': { 'required': True },
        }

    def get_resource_uri(self, project):
        return reverse('api:projects-detail', kwargs={
            'team_slug': self.context['team'].slug,
            'slug': project.slug,
        }, request=self.context['request'])

    def create(self, validated_data):
        return Project.objects.create(team=self.context['team'],
                                      **validated_data)

class ProjectUpdateSerializer(ProjectSerializer):
    class Meta(ProjectSerializer.Meta):
        extra_kwargs = {
            'name': { 'required': False },
            'slug': { 'required': False },
        }

class ProjectViewSet(TeamSubview):
    lookup_field = 'slug'
    serializer_class = ProjectSerializer
    update_serializer_class = ProjectUpdateSerializer

    def get_queryset(self):
        if not self.team.user_is_member(self.request.user):
            raise PermissionDenied()
        return Project.objects.for_team(self.team)

    def get_serializer_class(self):
        if 'slug' in self.kwargs:
            return self.update_serializer_class
        else:
            return self.serializer_class

    def get_object(self):
        if not self.team.user_is_member(self.request.user):
            raise PermissionDenied()
        return super(ProjectViewSet, self).get_object()

    def perform_create(self, serializer):
        if not team_permissions.can_create_project(
            self.request.user, self.team):
            raise PermissionDenied()
        serializer.save()

    def perform_update(self, serializer):
        if not team_permissions.can_edit_project(
            self.team, self.request.user, serializer.instance):
            raise PermissionDenied()
        serializer.save()

    def perform_destroy(self, project):
        if not team_permissions.can_delete_project(
            self.request.user, self.team, project):
            raise PermissionDenied()
        project.delete()

class TeamVideoField(serializers.Field):
    default_error_messages = {
        'unknown-video': "Unknown video: {video_id}",
    }

    def to_internal_value(self, video_id):
        team = self.context['team']
        try:
            return team.teamvideo_set.get(video__video_id=video_id)
        except TeamVideo.DoesNotExist:
            self.fail('unknown-video', video_id=video_id)

    def to_representation(self, team_video):
        return team_video.video.video_id

class TeamMemberField(serializers.Field):
    default_error_messages = {
        'unknown-member': "Unknown member: {username}",
    }

    def to_internal_value(self, username):
        team = self.context['team']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.fail('unknown-member', username=username)
        if not team.user_is_member(user):
            self.fail('unknown-member', username=username)
        return user

    def to_representation(self, user):
        return user.username

class TaskSerializer(serializers.ModelSerializer):
    resource_uri = serializers.SerializerMethodField()
    video_id = TeamVideoField(source='team_video')
    assignee = TeamMemberField(required=False)
    type = MappedChoiceField(Task.TYPE_CHOICES)
    created = TimezoneAwareDateTimeField(read_only=True)
    completed = TimezoneAwareDateTimeField(read_only=True)
    approved = MappedChoiceField(
        Task.APPROVED_CHOICES, required=False,
        default=Task._meta.get_field('approved').get_default(),
    )

    class Meta:
        model = Task
        fields = (
            'id', 'video_id', 'language', 'type', 'assignee', 'priority',
            'created', 'completed', 'approved', 'resource_uri',
        )
        read_only_fields = (
            'completed',
        )

    def get_resource_uri(self, task):
        return reverse('api:tasks-detail', kwargs={
            'team_slug': self.context['team'].slug,
            'id': task.id,
        }, request=self.context['request'])

    def create(self, validated_data):
        validated_data['team'] = self.context['team']
        return super(TaskSerializer, self).create(validated_data)

class TaskUpdateSerializer(TaskSerializer):
    video_id = TeamVideoField(source='team_video', required=False,
                              read_only=True)
    type = MappedChoiceField(Task.TYPE_CHOICES, required=False,
                             read_only=True)
    complete = serializers.BooleanField(required=False, write_only=True)
    send_back = serializers.BooleanField(required=False, write_only=True)

    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + (
            'complete', 'send_back',
        )

    def update(self, task, validated_data):
        send_back = validated_data.pop('send_back', False)
        complete = validated_data.pop('complete', False)
        self.check_max_tasks(task, validated_data.get('assignee'))
        task = super(TaskUpdateSerializer, self).update(task, validated_data)
        if send_back:
            task.approved = Task.APPROVED_IDS['Rejected']
            self._complete_task(task)
        elif complete:
            task.approved = Task.APPROVED_IDS['Approved']
            self._complete_task(task)
        return task

    def check_max_tasks(self, task, assignee):
        if not assignee:
            return
        member = self.context['team'].get_member(assignee)
        if member.has_max_tasks() and task.assignee != assignee:
            raise PermissionDenied()

    def _complete_task(self, task):
        if task.assignee is None:
            task.assignee = self.context['user']
        task.complete()
        version = task.get_subtitle_version()
        if version and version.is_public():
            subtitles.signals.subtitles_completed.send(
                version.subtitle_language)
            subtitles.signals.subtitles_published.send(
                version.subtitle_language, version=version)

class TaskViewSet(TeamSubview):
    lookup_field = 'id'
    paginate_by = 20

    def get_queryset(self):
        if not self.team.user_is_member(self.request.user):
            raise PermissionDenied()
        return (self.order_queryset(self.team.task_set.not_deleted())
                .select_related('team_video__video', 'assignee'))

    def order_queryset(self, qs):
        valid_orderings = set(['created', 'priority', 'type'])
        reverse_orderings = set('-' + o for o in valid_orderings)
        order_by = self.request.query_params.get('order_by')
        if order_by in valid_orderings.union(reverse_orderings):
            return qs.order_by(order_by)
        else:
            return qs

    def filter_queryset(self, qs):
        params = self.request.query_params
        if 'assignee' in params:
            qs = qs.filter(assignee__username=params['assignee'])
        if 'priority' in params:
            qs = qs.filter(priority=params['priority'])
        if 'language' in params:
            qs = qs.filter(language=params['language'])
        if 'type' in params:
            try:
                qs = qs.filter(type=Task.TYPE_IDS[params['type']])
            except KeyError:
                qs = qs.none()
        if 'video_id' in params:
            qs = qs.filter(team_video__video__video_id=params['video_id'])
        if 'completed' in params:
            qs = qs.filter(completed__isnull=False)
        if 'completed-after' in params:
            try:
                qs = qs.filter(completed__gte=timestamp_to_datetime(
                    params['completed-after']))
            except (TypeError, ValueError):
                qs = qs.none()
        if 'completed-before' in params:
            try:
                qs = qs.filter(completed__lt=timestamp_to_datetime(
                    params['completed-before']))
            except (TypeError, ValueError):
                qs = qs.none()
        if 'open' in params:
            qs = qs.filter(completed__isnull=True)
        return qs

    def get_serializer_class(self):
        if 'id' not in self.kwargs:
            return TaskSerializer
        else:
            return TaskUpdateSerializer

    def perform_create(self, serializer):
        team_video = serializer.validated_data['team_video']
        if not team_permissions.can_assign_tasks(
            self.team, self.request.user, team_video.project):
            raise PermissionDenied()
        self.task_was_assigned = False
        task = serializer.save()
        self._post_save(task)

    def perform_update(self, serializer):
        team_video = serializer.instance.team_video
        if not team_permissions.can_assign_tasks(
            self.team, self.request.user, team_video.project):
            raise PermissionDenied()
        self.task_was_assigned = serializer.instance.assignee is not None
        task = serializer.save()
        self._post_save(task)

    def perform_destroy(self, instance):
        if not team_permissions.can_delete_tasks(
            self.team, self.request.user, instance.team_video.project,
            instance.language):
            raise PermissionDenied()
        instance.deleted = True
        instance.save()

    def _post_save(self, task):
        if task.assignee and not self.task_was_assigned:
            messages.tasks.team_task_assigned.delay(task.id)
            task.set_expiration()
            task.save()
        videos.tasks.video_changed_tasks.delay(task.team_video.video_id)

class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    status = MappedChoiceField(
        Application.STATUSES,
        default=Application._meta.get_field('status').get_default())
    resource_uri = serializers.SerializerMethodField()
    created = TimezoneAwareDateTimeField(read_only=True)
    modified = TimezoneAwareDateTimeField(read_only=True)

    default_error_messages = {
        'invalid-status-choice': "Unknown status: {status}",
        'not-pending': "Application not pending",
    }

    def get_resource_uri(self, application):
        return reverse('api:team-application-detail', kwargs={
            'team_slug': self.context['team'].slug,
            'id': application.id,
        }, request=self.context['request'])

    class Meta:
        model = Application
        fields = (
            'id', 'status', 'user', 'note', 'created', 'modified',
            'resource_uri',
        )
        read_only_fields = (
            'id', 'note', 'created', 'modified',
        )

    def validate_status(self, status):
        if status not in (Application.STATUS_APPROVED,
                          Application.STATUS_DENIED):
            self.fail('invalid-status-choice', status=status)
        return status

    def update(self, instance, validated_data):
        if instance.status != Application.STATUS_PENDING:
            self.fail('not-pending')
        if validated_data['status'] == Application.STATUS_APPROVED:
            instance.approve(self.context['user'], 'API')
        elif validated_data['status'] == Application.STATUS_DENIED:
            instance.deny(self.context['user'], 'API')
        return instance

class TeamApplicationViewSet(TeamSubviewMixin,
                             mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):
    serializer_class = ApplicationSerializer
    lookup_field = 'id'
    paginate_by = 20

    def get_queryset(self):
        self.check_read_permission()
        if self.team.membership_policy != Team.APPLICATION:
            return self.team.applications.none()
        return self.team.applications.all().select_related('user')

    def get_object(self):
        self.check_read_permission()
        return super(TeamApplicationViewSet, self).get_object()

    def check_read_permission(self):
        if not team_permissions.can_invite(self.team, self.request.user):
            raise PermissionDenied()

    def filter_queryset(self, qs):
        params = self.request.query_params
        if 'user' in params:
            qs = qs.filter(user__username=params['user'])
        if 'status' in params:
            try:
                status_id = Application.STATUSES_IDS[params['status']]
                qs = qs.filter(status=status_id)
            except KeyError:
                qs = qs.none()
        if 'after' in params:
            qs = qs.filter(created__gte=timestamp_to_datetime(params['after']))
        if 'before' in params:
            qs = qs.filter(created__lt=timestamp_to_datetime(params['before']))
        return qs

@api_view(['GET'])
def team_languages(request, team_slug):
    """
    Links to a team's preferred/blacklisted language endpoints.

    These endpoints allows you to control which languages you want worked on in
    a team.  Preferred languages will have tasks auto-created for each video.
    Subtitles for blacklisted languages will not be allowed.
    """

    return Response({
        'preferred': reverse('api:team-languages-preferred', kwargs={
            'team_slug': team_slug,
        }, request=request),
        'blacklisted': reverse('api:team-languages-blacklisted', kwargs={
            'team_slug': team_slug,
        }, request=request),
    })

class TeamLanguageView(TeamSubviewMixin, APIView):
    def queryset(self):
        return (TeamLanguagePreference.objects.for_team(self.team)
                .filter(**self.field_values))

    def get(self, request, *args, **kwargs):
        return Response(sorted(tlp.language_code for tlp in self.queryset()))

    def put(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            raise serializers.ValidationError("Data must be a list")
        for code in request.data:
            if code not in ALL_LANGUAGE_CODES:
                raise serializers.ValidationError(
                    "Invalid language code: {}".format(code))
        with transaction.commit_on_success():
            self.add_languages(request.data)
            self.remove_languages(request.data)
        return Response(sorted(request.data))

    def add_languages(self, language_codes):
        for code in language_codes:
            tlp, created = TeamLanguagePreference.objects.get_or_create(
                team=self.team, language_code=code,
                defaults=self.field_values)
            if not created:
                for name, value in self.field_values.items():
                    setattr(tlp, name, value)
                tlp.save()

    def remove_languages(self, language_codes):
        self.queryset().exclude(language_code__in=language_codes).delete()

class TeamPreferredLanguagesView(TeamLanguageView):
    field_values = {
        'preferred': True,
        'allow_reads': False,
        'allow_writes': False,
    }

class TeamBlacklistedLanguagesView(TeamLanguageView):
    field_values = {
        'preferred': False,
        'allow_reads': False,
        'allow_writes': False,
    }
