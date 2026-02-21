from rest_framework import serializers
from .models import Person,Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=['color_name']
        

class PersonSerializer(serializers.ModelSerializer):
    color=ColorSerializer()
    class Meta:
        
        model= Person
        fields='__all__'
        # depth=1
        

        
    def validate(self, data):
        special_char="!@#$%^&*()?/\|"
        for c in data['name']:
            if c in special_char:
                raise serializers.ValidationError('name shouldnot contain special character ')
                
      
        if data['age']< 18:
            raise serializers.ValidationError('age should be greater than 18 ')
        return data
            
        