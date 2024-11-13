from rest_framework import serializers

class LibraryStatsSerializer(serializers.Serializer):
    num_books = serializers.IntegerField()
    num_instances = serializers.IntegerField()
    num_instances_available = serializers.IntegerField()
    num_authors = serializers.IntegerField()
    num_visits = serializers.IntegerField()