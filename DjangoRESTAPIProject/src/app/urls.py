from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api", views.EmployeeModelViewSet, basename="emp")


urlpatterns = [


    path('', include(router.urls)),

]

