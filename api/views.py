from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JGdates
from .serializers import JGdatesSerializer
from .parser import GetJGdates

class JGdatesAPIView(APIView):
    def get_object(self, year):
        try:
            return JGdates.objects.get(year=year)
        except JGdates.DoesNotExist:
            data = GetJGdates(year)
            newjgdates = JGdates(year=data[0], date1=data[1], date2=data[2], date3=data[3], date4=data[4])
            newjgdates.save()
            return newjgdates



    def get(self, request, year):
        jgdates = self.get_object(year)
        serializer = JGdatesSerializer(jgdates)
        return Response(serializer.data)

