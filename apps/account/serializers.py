from rest_framework import serializers
from information.models import Address, Company, Geo
from account.models import User

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name_company', 'catchPhrase', 'bs']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']