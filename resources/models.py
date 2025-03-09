from django.db import models
from django.contrib.postgres.search import SearchVectorField


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    resource_id = models.AutoField(primary_key=True)

    class ResourceType(models.TextChoices):
        COMMUNITY = "community", "Community"
        CURRICULUM = "curriculum", "Curriculum"
        BOOK = "book", "Book"
        COURSE = "course", "Course"
        HOMESCHOOL_COOP = "homeschool_coop", "Homeschool Co-op"
        ONLINE_COURSE = "online_course", "Online Course"
        FIELD_TRIP = "field_trip", "Field Trip"
        APP = "app", "App"
        WEBSITE = "website", "Website"
        PROGRAM = "program", "Program"
        OTHER = "other", "Other"

    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    tags = models.ManyToManyField(Tag, related_name="resources")
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="resources"
    )
    favorited_count = models.IntegerField(default=0)

    # full text search field
    search_text = SearchVectorField(editable=False)

    resource_type = models.CharField(
        max_length=20,
        choices=ResourceType.choices,
        default=ResourceType.OTHER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
