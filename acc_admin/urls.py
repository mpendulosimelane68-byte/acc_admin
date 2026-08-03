from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from dashboard.views import ACCPasswordResetConfirmView
from dashboard.views import ACCPasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('dashboard.urls')),

    path('cases/', include('cases.urls')),


    # Password reset URLs
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset"
    ),

    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),

   path(
    "password-reset-confirm/<uidb64>/<token>/",
    ACCPasswordResetConfirmView.as_view(),
    name="password_reset_confirm"
),


path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html"
    ),
    name="password_reset"
),

path(
    "password-reset/done/",
    auth_views.PasswordResetDoneView.as_view(),
    name="password_reset_done"
),

path(
    "password-reset-confirm/<uidb64>/<token>/",
    auth_views.PasswordResetConfirmView.as_view(),
    name="password_reset_confirm"
),

path(
    "password-reset/",
    auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        email_template_name="registration/password_reset_email.txt",
        subject_template_name="registration/password_reset_subject.txt",
    ),
    name="password_reset"
),

]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)