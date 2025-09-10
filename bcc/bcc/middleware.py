# inventory/middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


class LoginRequiredMiddleware:
    """
    Require login for all URLs except those explicitly exempted.
    Admin area (/admin/) is only accessible to superusers.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL

        # Exempt URLs from settings
        self.exempt_prefixes = getattr(settings, "LOGIN_EXEMPT_URLS", [])[:]

        # Also exempt static and media URLs
        static_url = getattr(settings, "STATIC_URL", None)
        media_url = getattr(settings, "MEDIA_URL", None)
        if static_url:
            self.exempt_prefixes.append(static_url)
        if media_url:
            self.exempt_prefixes.append(media_url)

    def __call__(self, request):
        path = request.path_info

        # Allow any exempted prefix
        for prefix in self.exempt_prefixes:
            if prefix and path.startswith(prefix):
                return self.get_response(request)

        # Admin area: only superusers allowed
        if path.startswith("/admin/"):
            if request.user.is_authenticated and request.user.is_superuser:
                return self.get_response(request)
            return HttpResponseForbidden("Admin access restricted.")

        # Allow authenticated users
        if request.user.is_authenticated:
            return self.get_response(request)

        # Otherwise redirect to login
        return redirect(f"{self.login_url}?next={request.path}")
