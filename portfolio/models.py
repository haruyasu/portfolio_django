from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=200, null=True)
    thumbnail = models.CharField(max_length=200, null=True)
    image_list = models.CharField(max_length=500, null=True, blank = True)
    video = models.CharField(max_length=200, null=True, blank = True)
    client = models.CharField(max_length=200, null=True)
    date = models.CharField(max_length=200, null=True)
    skills = models.CharField(max_length=200, null=True)
    github = models.CharField(max_length=200, null=True, blank = True)
    demo = models.CharField(max_length=200, null=True)

    def category_upper(self):
        if self.category:
            return self.category.upper()
    
    def get_thumbnail(self):
        if self.thumbnail:
            return "/static/img/" + self.category + "/" + self.thumbnail

    def get_github_url(self):
        if self.github:
            return "https://github.com/haruyasu/" + self.github
        else:
            return

    def images(self):
        if self.image_list:
            image_list = self.image_list.split(",")
            new_image_list = []
            for image in image_list:
                new_image_list.append("/static/img/" + self.category + "/" + image)
            return new_image_list

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def get_previous_by_pk(self):
        queryset = type(self).objects.filter(pk__lt=self.pk).last()
        if queryset:
            return queryset
        else:
            raise self.DoesNotExist("%s matching query does not exist." % self.__class__._meta.object_name)

    def get_next_by_pk(self):
        queryset = type(self).objects.filter(pk__gt=self.pk).first()
        if queryset:
            return queryset
        else:
            raise self.DoesNotExist("%s matching query does not exist." % self.__class__._meta.object_name)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('portfolio.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
    
    def __str__(self):
        return self.text
