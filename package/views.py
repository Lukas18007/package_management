from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from .models import Package

class UpdatePackageStatusView(APIView):
    def patch(self, request, id):
        try:
            package = Package.objects.get(pk=id)
        except Package.DoesNotExist:
            return Response({"error": "Package not found."}, status=status.HTTP_404_NOT_FOUND)

        status_received = request.data.get("status")

        if status_received == "aprovado":
            package.authorized = True
            package.authorized_at = date.today()

        elif status_received == "aprovado com apontamentos":
            if package.risk == 'B' or package.risk == 'M':
                package.authorized = True
                package.authorized_at = date.today()
            else:
                package.authorized = False

        elif status_received == "reprovado":
            package.authorized = False

        package.save()

        return Response({"message": "Package status updated successfully."}, status=status.HTTP_200_OK)

