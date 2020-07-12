from rest_framework import serializers

from account.models import *

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = (
            'company_id',
            'email',
            'password',
                )
class AppsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APP
        fields = (
            'app_id',
            'appname',
            'webaddress',
            'company_id',
                )
