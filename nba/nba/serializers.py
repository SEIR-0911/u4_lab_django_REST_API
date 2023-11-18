from rest_framework import serializers
from .models import Team, Player



class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team=serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True,
    )

    team_id=serializers.PrimaryKeyRelatedField(
        queryset = Team.objects.all()
    )

    class Meta:
        model=Player
        fields=('id', 'team', 'position', 'age', 'ir_list', 'team_id')



class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(
        many = True,
        read_only = True,
    )

    team_url=serializers.ModelSerializer.serializer_url_field(
        view_name = 'team_detail'
    )

    class Meta:
        model = Team
        fields=('id', 'name', 'location', 'division', 'wins', 'losses', 'players', 'team_url')

