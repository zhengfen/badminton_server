from rest_framework import serializers
from competitions.models import Club, ClubResponsable, Competition, Game, Group, Player, Structure, Team, Type, Contact, User


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'


class ClubListSerializer(serializers.ModelSerializer):
    structures = StructureSerializer(many=True)

    class Meta:
        model = Club
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    players = PlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'club', 'group', 'players']


class ClubShowSerializer(serializers.ModelSerializer):
    teams = TeamSerializer(many=True)

    class Meta:
        model = Club
        fields = ['id', 'name', 'teams']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserContactSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'contact']


class ClubResponsableSerializer(serializers.ModelSerializer):
    user = UserContactSerializer()

    class Meta:
        model = ClubResponsable
        fields = ['user_id', 'function', 'user']
