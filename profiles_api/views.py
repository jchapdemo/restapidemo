from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Users HTTP methods as function (get, post, patch, put and delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manuall to URLs'
        ]

        return Response({'message':'hello', 'an_apiview': an_apiview})
