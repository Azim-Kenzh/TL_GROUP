from rest_framework import viewsets
from account.serializers import *


class EntityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer


class IndividualViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     children = self.request.query_params.get('children')
    #     parent = self.request.query_params.get('parent')
    #     try:
    #         if children in parent:
    #             queryset = queryset.filter(children)
    #     except:
    #         if parent is None:
    #             return None
    #     return queryset
