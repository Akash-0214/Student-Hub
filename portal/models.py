from django.db import models


class BaseContent(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=200, default="Student Hub")
    subtitle = models.CharField(max_length=200, default="All You Need as a Student, in One Place")
    description = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default="Explore")
    button_link = models.CharField(max_length=255, default="#")
    image = models.ImageField(upload_to="banners/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Note(BaseContent):
    file = models.FileField(upload_to="notes/", blank=True, null=True)
    category = models.CharField(max_length=100, default="General")
    subject = models.CharField(max_length=100, blank=True)


class LabManual(BaseContent):
    file = models.FileField(upload_to="lab-manuals/", blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True)
    semester = models.CharField(max_length=50, blank=True)


class QuestionPaper(BaseContent):
    file = models.FileField(upload_to="question-papers/", blank=True, null=True)
    year = models.CharField(max_length=20, blank=True)
    semester = models.CharField(max_length=50, blank=True)
    exam_type = models.CharField(max_length=50, default="End Sem")


class Project(BaseContent):
    category = models.CharField(max_length=100, default="Tech")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    source_link = models.URLField(blank=True, null=True)


class Placement(BaseContent):
    company_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="placements/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Internship(BaseContent):
    company_name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, default="Remote")
    link = models.URLField(blank=True, null=True)


class Course(BaseContent):
    category = models.CharField(max_length=100, default="Development")
    image = models.ImageField(upload_to="courses/", blank=True, null=True)
    link = models.URLField(blank=True, null=True)


class VideoResource(BaseContent):
    thumbnail = models.ImageField(upload_to="videos/", blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, default="Programming")


class ToolResource(BaseContent):
    icon = models.CharField(max_length=80, default="⚙️")
    link = models.URLField(blank=True, null=True)


class UpdatePost(BaseContent):
    date = models.DateField()
    badge = models.CharField(max_length=50, default="News")


class AboutSection(models.Model):
    heading = models.CharField(max_length=200, default="About Us")
    content = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading
