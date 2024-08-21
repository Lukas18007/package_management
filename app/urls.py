from django.urls import path
from package.views import UpdatePackageStatusView

urlpatterns = [
    path('package/<int:id>/authorize/', UpdatePackageStatusView.as_view(), name='update-package-status'),
]
