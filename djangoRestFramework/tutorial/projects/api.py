from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    querySet = Project.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class = ProjectSerializer
