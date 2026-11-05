# Student Hub

Student Hub is a Django-based student resource portal for notes, projects, lab manuals, internships, placements, video tutorials, tools, and updates. The public student area is open to everyone, while content is managed through the Django admin panel.

## Features

- Public homepage with a futuristic neon design
- Admin-managed content upload for:
  - Banner
  - Notes
  - Lab manuals
  - Question papers
  - Projects
  - Placements
  - Internships
  - Courses
  - Video resources
  - Tools
  - Updates
  - About section
- No student login required
- Image/file upload support
- Secure default Django configuration

## Tech Stack

- Python 3.12+
- Django 5.0
- SQLite (default for local development)

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open:

- Home page: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Admin Usage

Login to the Django admin dashboard and add data for each model section:

- Banner
- Notes
- Lab Manuals
- Question Papers
- Projects
- Placements
- Internships
- Courses
- Video Resources
- Tool Resources
- Update Posts
- About Section

You can upload banners, PDFs, images, and custom links for each resource.

## Production Notes

- Set `DEBUG = False`
- Set a strong `SECRET_KEY`
- Use HTTPS behind a reverse proxy or deployment platform
- Configure static/media serving correctly for production
