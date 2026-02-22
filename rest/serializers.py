from rest_framework import serializers
from .models import Person, Color
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "color_name"]
        model = Color
        fields = ["id", "color_name"]

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer(allow_null=True)

    color = ColorSerializer(allow_null=True)

    class Meta:
        model = Person
        fields = "__all__"

    def update(self, instance, validated_data):
        color_data = validated_data.pop("color", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

    
        if color_data:
            color_serializer = self.fields["color"]

            if instance.color:
                color_serializer.update(instance.color, color_data)
            else:
                new_color = Color.objects.create(**color_data)
                instance.color = new_color
                instance.save()

        return instance
        
    def validate(self, data):
        special_char="!@#$%^&*()?/\|"
        for c in data['name']:
            if c in special_char:
                raise serializers.ValidationError('name shouldnot contain special character ')
                
      
        if data['age']< 18:
            raise serializers.ValidationError('age should be greater than 18 ')
        return data
            
        