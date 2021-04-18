from django.contrib.auth.models import User, Group
from streamstock_backend.admin_panel.models import (
    PipelineSettings,
    Project,
    Compilation,
    CompilationVideo,
    Source
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PipelineSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PipelineSettings
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CompilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compilation
        fields = '__all__'


class CompilationVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompilationVideo
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
