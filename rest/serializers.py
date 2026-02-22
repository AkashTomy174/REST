from rest_framework import serializers
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "color_name"]


class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()  

    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        color_data = validated_data.pop("color")


        color = Color.objects.create(**color_data)

        
        person = Person.objects.create(color=color, **validated_data)
        return person

    def update(self, instance, validated_data):
        color_data = validated_data.pop("color", None)


        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

    
        if color_data:
            if instance.color:
                for key, value in color_data.items():
                    setattr(instance.color, key, value)
                instance.color.save()
            else:
                color = Color.objects.create(**color_data)
                instance.color = color
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
            
        