from rest_framework.serializers import ModelSerializer

from account.serializers import UserSerializer
from review.serializers import CommentSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['likes'] = instance.likes.all().count()
        repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return repr

    def create(self, validated_data):
        validated_data['customer'] = self.context.get('request').user
        product = super().create(validated_data)
        return product