from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail

from shared import utils

notify = False

class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __unicode__(self):
        return self.title


class BlogComment(models.Model):
    author = models.CharField(max_length=60, blank=True)
    body = models.TextField()
    post = models.ForeignKey(BlogPost, related_name="comments", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s: %s" % (self.post, self.body[:60])

    def save(self, *args, **kwargs):
        """ email when a comment is added. """
        if notify:
            tpl = "Comment was added to '%s' by '%s': \n\n%s"
            message = tpl % (self.post, self.author, self.body)
            from_addr = "no-reply@mydomain.com"
            recipient_list = ["myemail@mydomain.com"]

            send_mail("New comment added", message, from_addr, recipient_list)
        super(BlogComment, self).save(*args, **kwargs)

