from rest_framework import serializers
from .models import Club, ClubResponsible, Contact, Position, Role, Team, TeamPlayer, User
from competitions.serializers import GroupSerializer, LevelSerializer

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

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

class TeamPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayer
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'licence', 'sex', 'birthday', 'club', 'role']

class PositionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Position
        fields = ['id', 'name']

class ContactWithUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta: 
        model = Contact
        fields = '__all__'

class TeamPlayerWithPlayerSerializer(serializers.ModelSerializer):
    player = UserSerializer()
    class Meta: 
        model = TeamPlayer
        fields = ['id', 'team', 'player', 'position']

class TeamPlayerWithTeamSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    class Meta: 
        model = TeamPlayer
        fields = ['id', 'team', 'player', 'position']

class TeamWithPlayerUserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    level = LevelSerializer()
    team_players = TeamPlayerWithPlayerSerializer(many=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'club', 'level', 'group', 'team_players']

class UserWithTeamsSerializer(serializers.ModelSerializer): 
    teams = TeamPlayerWithTeamSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'licence', 'sex', 'birthday', 'club', 'role', 'is_superuser', 'is_staff', 'teams']
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



class ClubResponsibleSerializer(serializers.ModelSerializer):
    user = UserWithContactSerializer()
    class Meta:
        model = ClubResponsible
        fields = ['id', 'user_id', 'function', 'user']