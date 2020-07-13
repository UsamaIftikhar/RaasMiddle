from django.urls import include, path
from django.conf.urls import  url
from rest_framework import routers
from account import views
from account.models import *

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'apps', views.AppsViewSet)
# router.register(r'^verify', views.specsView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('verify/<appid>/<companyid>',views.specsView),
    # url(r'^verify', views.specsView),

    # path(r'^verify/(?P<param1>[\w-]+)/(?P<param2>[\w-]+)/$', views.specsView,name='app_company')
    # path('api-auth/instances/', views.VerifyKeyViewSet.as_view(), name="instances")
]



# urlpatterns=[
#     url(r'companies', views.CompanyViewSet),
#     url(r'apps', views.AppsViewSet),
#     url(r'^verify', views.specsView),
# ]