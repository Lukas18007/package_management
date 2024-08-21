from django.urls import path, include
from package.views import UpdatePackageStatusView

urlpatterns = [
    path('api/', include('package.urls')),
]
