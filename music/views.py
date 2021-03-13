from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CurrentSong
from .serializers import PlaylistSerializer


class MusicViewSet(APIView):
    def get(self, request):
        return Response({"ms": "hello"})

class PlaylistView(APIView):
    def get(self, request):
        queryset = CurrentSong.objects.all()
        serializer = PlaylistSerializer(queryset, many=True)
        return Response(serializer.data)

        # permission_classes = [permissions.IsAuthenticated]

