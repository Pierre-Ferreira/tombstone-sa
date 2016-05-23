from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# from . import views
from .views import feedback_form_page

urlpatterns = [
    url(r'^$', feedback_form_page),

    # url(r'^$', "feedback.views.feedback_form_page"),
    # url(r'^create/$', "feedback.views.feedback_create"),
    # url(r'^read/$', "feedback.views.feedback_read"),
    # url(r'^update/$', "feedback.views.feedback_update"),
    # url(r'^delete/$', "feedback.views.feedback_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
