from rest_framework import pagination
from rest_framework.response import Response


class CountPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'total_count': self.page.paginator.count,
            'results': data
        })