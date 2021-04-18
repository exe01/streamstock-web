from django.contrib.auth.models import User, Group
from streamstock_backend.admin_panel.models import (
    PipelineSettings,
    Project,
    Compilation,
    CompilationVideo,
    Source,
)
from streamstock_backend.admin_panel.serializers import (
    UserSerializer,
    GroupSerializer,
    PipelineSettingsSerializer,
    ProjectSerializer,
    CompilationSerializer,
    CompilationVideoSerializer,
    SourceSerializer,
)
from rest_framework import viewsets
import datetime
from django.utils import timezone
import django_filters


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PipelineSettingsViewSet(viewsets.ModelViewSet):
    queryset = PipelineSettings.objects.all()
    serializer_class = PipelineSettingsSerializer
    filterset_fields = '__all__'


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = '__all__'


class CompilationViewSet(viewsets.ModelViewSet):
    queryset = Compilation.objects.all()
    serializer_class = CompilationSerializer
    filterset_fields = '__all__'


class CompilationVideoViewSet(viewsets.ModelViewSet):
    queryset = CompilationVideo.objects.all()
    serializer_class = CompilationVideoSerializer
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = self.queryset
        if 'is_ready' in self.request.query_params:
            published__lt = datetime.datetime.now(tz=timezone.utc)
            published__lt -= datetime.timedelta(hours=1)
            queryset = queryset.filter(published__lt=published__lt, status='AC')

        return queryset


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    filterset_fields = '__all__'
