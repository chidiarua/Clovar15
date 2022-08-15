from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"


class SelectTemplateView(TemplateView):
    template_name = "select_template.html"


class BloggerUsersView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard_users.html"


class ComingSoonView(LoginRequiredMixin, TemplateView):
    template_name = 'coming_soon.html'


def error_404(request, exception):
    return render(request, "404.html")


# def error_500(request):
# return render(request, "404.html")
