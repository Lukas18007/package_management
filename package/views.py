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
        authorization_status = None

        if status_received == "aprovado":
            package.authorized = True
            package.authorized_at = date.today()
            authorization_status = 'Authorized'

        elif status_received == "aprovado com apontamentos":
            if package.risk == 'B' or package.risk == 'M':
                package.authorized = True
                package.authorized_at = date.today()
                authorization_status = 'Authorized'
            else:
                package.authorized = False
                authorization_status = 'Not authorized'

        elif status_received == "reprovado":
            package.authorized = False
            authorization_status = 'Not authorized'

        package.save()

        return Response({"message": f"Package status updated successfully: {authorization_status}"}, status=status.HTTP_200_OK)
