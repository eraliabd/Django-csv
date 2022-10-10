from django.db import models


class About(models.Model):
    # me
    image_me = models.ImageField(upload_to='image_me/', blank=True, null=True)
    bg_image = models.ImageField(upload_to='bg_image/', blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)

    # about me
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    csv = models.FileField(upload_to='csv/', blank=True, null=True)

    # contact
    contact_title = models.CharField(max_length=255, blank=True, null=True)
    contact_content = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    # footer
    footer_about = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class RecentWork(models.Model):
    image = models.ImageField(upload_to='portfolio_image/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    link = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    work = models.ForeignKey(RecentWork, on_delete=models.CASCADE, related_name='works')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply_comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    reply_comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name}"
