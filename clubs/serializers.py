from rest_framework import serializers
from .models import Club, ClubResponsable, Team, TeamPlayer, Contact, User
from competitions.serializers import GroupSerializer, LevelSerializer

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'licence', 'sex', 'birthday', 'club_id']


class TeamPlayerWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta: 
        model = TeamPlayer
        fields = ['id', 'team_id', 'user', 'role']

class TeamPlayerWithTeamSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta: 
        model = TeamPlayer
        fields = ['id', 'team', 'user_id', 'role']

class TeamWithPlayerUserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    level = LevelSerializer()
    team_players = TeamPlayerWithUserSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'club', 'level', 'group', 'team_players']

class PlayerWithTeamsSerializer(serializers.ModelSerializer): 
    teams = TeamPlayerWithTeamSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'licence', 'sex', 'birthday', 'club', 'teams']
class ClubWithTeamsSerializer(serializers.ModelSerializer):
    teams = TeamWithPlayerUserSerializer(many=True)
    class Meta:
        model = Club
        fields = ['id', 'name', 'teams']

class UserWithContactSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'contact']

class ClubResponsableSerializer(serializers.ModelSerializer):
    user = UserWithContactSerializer()
    class Meta:
        model = ClubResponsable
        fields = ['id', 'user_id', 'function', 'user']