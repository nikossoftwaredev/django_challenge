from rest_framework import routers
from .api import LeadViewSet


router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet , 'leads') #registering an end point

urlpatterns = router.urls # gives us the ulrs that were register for this end point