from django.contrib import admin
from .models import (
    AboutSection,
    Banner,
    Course,
    Internship,
    LabManual,
    Note,
    Placement,
    Project,
    QuestionPaper,
    ToolResource,
    UpdatePost,
    VideoResource,
)

admin.site.site_header = "Student Hub Admin"
admin.site.site_title = "Student Hub"
admin.site.index_title = "Content Management"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "button_text")
    list_filter = ("is_active",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "category", "created_at")
    list_filter = ("category", "subject")
    search_fields = ("title", "subject", "category")


@admin.register(LabManual)
class LabManualAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "semester", "created_at")
    list_filter = ("subject", "semester")
    search_fields = ("title", "subject")


@admin.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "semester", "exam_type", "created_at")
    list_filter = ("year", "semester", "exam_type")
    search_fields = ("title", "year", "semester")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "category")


@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ("company_name", "title", "created_at")
    search_fields = ("company_name", "title")


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ("title", "company_name", "type", "created_at")
    list_filter = ("type",)
    search_fields = ("title", "company_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "category")


@admin.register(VideoResource)
class VideoResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("title", "category")


@admin.register(ToolResource)
class ToolResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "created_at")
    search_fields = ("title", "icon")


@admin.register(UpdatePost)
class UpdatePostAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "badge")
    list_filter = ("badge", "date")
    search_fields = ("title", "badge")


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "is_active")
    list_filter = ("is_active",)
