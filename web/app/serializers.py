from rest_framework import serializers

from .models import Category, City, Advert


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    category_names = serializers.SerializerMethodField()

    class Meta:
        model = Advert
        fields = ('id', 'title', 'description', 'city_name', 'category_names', 'views')

    def get_category_names(self, obj):
        return [category.name for category in obj.category.all()]
