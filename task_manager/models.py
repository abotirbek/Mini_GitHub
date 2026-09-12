from django.db import models
from accounts.models import CustomUser, TimeStampedModel


# Create your models here.
class Project(TimeStampedModel):
    class Visibility(models.TextChoices):
        PRIVATE = 'private', 'Private'
        PUBLIC = 'public', 'Public'

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )
    visibility = models.CharField(
        max_length=7,
        choices=Visibility.choices,
        default=Visibility.PRIVATE
    )
    members = models.ManyToManyField(
        CustomUser,
        through='ProjectMember',
        related_name='projects',
        blank=True, null=True
    )
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name



class ProjectMember(TimeStampedModel):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MEMBER = 'member', 'Member'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_members'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='project_memberships'
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['project', 'user'],
                name = 'unique_project_member',
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.project}"


