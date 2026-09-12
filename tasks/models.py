from django.db import models
from accounts.models import TimeStampedModel, CustomUser
from task_manager.models import Project


# Create your models here.
class Task(TimeStampedModel):
    class Status(models.TextChoices):
        TODO = 'todo', 'ToDo'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=11,
        choices=Status.choices,
        default=Status.TODO
    )
    priority = models.CharField(
        max_length=6,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )
    assigned_to = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        blank=True, null=True
    )
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['status', '-created_at']

    def __str__(self):
        return self.title