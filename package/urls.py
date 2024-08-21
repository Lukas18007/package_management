from django.urls import path
from . import views

urlpatterns = [
    path('package/authorize/<int:id>/', views.UpdatePackageStatusView.as_view(), name='update-package-status'),
]
