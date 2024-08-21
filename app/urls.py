from django.urls import path
from package.views import UpdatePackageStatusView

urlpatterns = [
    path('package/<int:id>/update-status/', UpdatePackageStatusView.as_view(), name='update-package-status'),
]
