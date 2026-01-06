from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Answer
from .serializers import AnswerSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Answer.objects.all()
        question_id = self.request.query_params.get('question')

        if question_id:
            queryset = queryset.filter(question_id=question_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
