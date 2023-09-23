from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):

    PRIORITY_CHOICES = [
        (4, 'Urgent'),
        (3, 'High'),
        (2, 'Medium'),
        (1, 'Low'),
    ]

    title = models.CharField(_('title'), max_length=100, blank=False)
    description = models.TextField(_('description'), blank=True)
    priority = models.IntegerField(_('priority'), choices=PRIORITY_CHOICES, default=1, blank=True)
    created_date = models.DateTimeField(_('date created'), auto_now_add=True)
    due_date = models.DateTimeField(_('due date'), blank=True, null=True)
    completed = models.BooleanField(_('completed'), default=False, blank=True)
    completed_date = models.DateTimeField(_('completed date'), blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.completed:
            self.completed_date = timezone.now()
        else:
            self.completed_date = None
        super().save(*args, **kwargs)

    def clean(self):
        if self.due_date and self.due_date < timezone.now():
            raise ValidationError("You can't set the due date and time to be in the past")

    class Meta:
        db_table = 'Tasks'
        verbose_name = _('task')
        verbose_name_plural = _('tasks')
        ordering = ['due_date', 'title']
