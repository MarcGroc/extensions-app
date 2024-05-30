from django.conf import settings
from django.http import HttpResponse


def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Allow: /",
        f"Host: '{settings.DOMAIN}' ",
        f"Sitemap: https://{settings.DOMAIN}/sitemap.xml",
    ]
    return HttpResponse("\n ".join(lines), content_type="text/plain")
