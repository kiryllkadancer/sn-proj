from django.db import models


# Create your models here.


class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL = "email_required", "Email required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "publish", "Published"
    COMING_SOON = "soon", "Coming soon"
    DRAFT = "draft", "Draft"


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # image
    access = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )

    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
