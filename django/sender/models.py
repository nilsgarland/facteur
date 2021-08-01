from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.models import User

import uuid


class SubmissionForm(models.Model):
    CONTACT_FORM = 'contact'
    LEAD_FORM = 'lead'
    SURVEY_FORM = 'survey'

    FORM_TYPES = (
        CONTACT_FORM,
        LEAD_FORM,
        SURVEY_FORM,
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(_('title'), max_length=40, blank=True)
    type = models.CharField(_('type'), max_length=20, default=CONTACT_FORM)
    recipient = models.EmailField(_('recipient email'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Submission form'
        verbose_name_plural = 'Submission forms'
