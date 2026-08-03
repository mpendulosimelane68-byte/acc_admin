from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import AuditLog


# ============================================================
# GET CLIENT IP
# ============================================================

def get_client_ip(request):
    if request is None:
        return None

    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")

    if forwarded:
        return forwarded.split(",")[0].strip()

    return request.META.get("REMOTE_ADDR")


# ============================================================
# PASSWORD CHANGE AUDIT
# ============================================================

@receiver(pre_save, sender=User)
def user_password_change(sender, instance, **kwargs):

    if not instance.pk:
        return

    try:
        old_user = User.objects.get(pk=instance.pk)
    except User.DoesNotExist:
        return

    if old_user.password != instance.password:

        AuditLog.objects.create(
            user=instance,
            action="Password Changed",
            description=f"{instance.username} changed their password"
        )


# ============================================================
# DJANGO ADMIN LOGIN AUDIT
# ============================================================

@receiver(user_logged_in)
def admin_login_audit(sender, request, user, **kwargs):

    # Only monitor the actual Django Admin site
    if not request:
        return

    if not request.path.startswith("/admin/"):
        return

    # Only a Django superuser can be considered
    # an Administrator for this audit entry.
    if not user.is_superuser:
        return

    AuditLog.objects.create(
        user=user,
        action="Administrator Login",
        description=(
            f"Administrator '{user.username}' "
            f"logged into the Django Admin site."
        ),
        ip_address=get_client_ip(request),
    )


# ============================================================
# DJANGO ADMIN LOGOUT AUDIT
# ============================================================

@receiver(user_logged_out)
def admin_logout_audit(sender, request, user, **kwargs):

    if not request:
        return

    if not request.path.startswith("/admin/"):
        return

    if user is None:
        return

    if not user.is_superuser:
        return

    AuditLog.objects.create(
        user=user,
        action="Administrator Logout",
        description=(
            f"Administrator '{user.username}' "
            f"logged out of the Django Admin site."
        ),
        ip_address=get_client_ip(request),
    )