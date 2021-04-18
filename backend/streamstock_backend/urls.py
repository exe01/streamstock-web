"""streamstock_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
from django.urls import include, path
from rest_framework import routers
from streamstock_backend.admin_panel import views as api_views


router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'pipeline_settings', api_views.PipelineSettingsViewSet)
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'compilations', api_views.CompilationViewSet)
router.register(r'compilation_videos', api_views.CompilationVideoViewSet)
router.register(r'sources', api_views.SourceViewSet)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/1.0/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
