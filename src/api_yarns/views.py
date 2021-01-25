from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api_yarns.models import YarnsModels
from api_yarns.serializers import YarnSerializer
from middlewares.authentications import AuthenticationJWT


class YarnViewSet(viewsets.ModelViewSet):
    queryset = YarnsModels.objects.all()
    serializer_class = YarnSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (AuthenticationJWT,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset()).filter(id=kwargs.get('pk'))
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        data["owner"] = request.user.id
        serializer = self.serializer_class(instance, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['owner'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
