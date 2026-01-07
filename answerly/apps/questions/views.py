from rest_framework.viewsets import ModelViewSet
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.common.permissions import IsAuthorOrReadOnly

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = Question.objects.all()
        
        tag = self.request.query_params.get('tag')
        if tag:
            queryset = queryset.filter(tags__name=tag.lower())

        return queryset