from django.shortcuts import render
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


def home(request):
    banner = Banner.objects.filter(is_active=True).first()
    notes = Note.objects.all().order_by("-created_at")[:10]
    lab_manuals = LabManual.objects.all().order_by("-created_at")[:10]
    question_papers = QuestionPaper.objects.all().order_by("-created_at")[:10]
    projects = Project.objects.all().order_by("-created_at")[:10]
    placements = Placement.objects.all().order_by("-created_at")[:10]
    internships = Internship.objects.all().order_by("-created_at")[:10]
    courses = Course.objects.all().order_by("-created_at")[:10]
    videos = VideoResource.objects.all().order_by("-created_at")[:10]
    tools = ToolResource.objects.all().order_by("-created_at")[:10]
    updates = UpdatePost.objects.all().order_by("-date")[:10]
    about = AboutSection.objects.filter(is_active=True).first()

    context = {
        "banner": banner,
        "notes": notes,
        "lab_manuals": lab_manuals,
        "question_papers": question_papers,
        "projects": projects,
        "placements": placements,
        "internships": internships,
        "courses": courses,
        "videos": videos,
        "tools": tools,
        "updates": updates,
        "about": about,
    }
    return render(request, "portal/home.html", context)
