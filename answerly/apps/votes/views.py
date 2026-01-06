from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import Vote
from apps.questions.models import Question
from apps.answers.models import Answer


class VoteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        vote_value = int(data.get('value'))
        content_type = data.get('content_type')
        object_id = data.get('object_id')

        if content_type == 'question':
            model = Question
        elif content_type == 'answer':
            model = Answer
        else:
            return Response({"error": "Invalid content type"}, status=400)
        
        obj = model.objects.get(id=object_id)


        # self voting not allowed
        if obj.author == user:
            return Response({"error": "You cannot vote on your own content"}, status=400)
        
        content_type_obj = ContentType.objects.get_for_model(model)

        vote, created = Vote.objects.update_or_create(
            user=user,
            content_type=content_type_obj,
            object_id=object_id,
            defaults={'value': vote_value}
        )

        return Response({"message": "Vote recorded"})