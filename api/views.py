from classes.models import Classroom
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from .serializers import (
    ClassroomListSerializer,
    ClassroomDetailSerializer,
    ClassroomCreateUpdateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    permission_classes = [AllowAny,]
    search_fields = ['name', 'description',]



class ClassroomDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Classroom_id'
    permission_classes = [AllowAny,]


class ClassroomCreateView(CreateAPIView):
    serializer_class = ClassroomCreateUpdateSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ClassroomUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Classroom_id'
    permission_classes = [IsAuthenticated,]


class ClassroomDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'Classroom_id'
    permission_classes = [IsAuthenticated,IsAdminUser]
