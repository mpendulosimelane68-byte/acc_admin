from django.db import models
from django.contrib.auth.models import User
from .encrypted_fields import EncryptedCharField

class Case(models.Model):

    

    STATUS_CHOICES = [
    ("received", "Received"),
    ("investigation", "Under Investigation"),
    ("referral", "Referral"),
    ("closed", "Closed"),
    ("declined", "Declined"),
]


    SECTOR_CHOICES = [
    ("public", "Public Sector"),
    ("private", "Private Sector"),
    ("none", "None"),
]


    PUBLIC_INSTITUTIONS = [
        ("ministry", "Government Ministry"),
        ("department", "Government Department"),
        ("municipality", "Municipality / Town Council"),
        ("parastatal", "Parastatal"),
        ("police", "Police Service"),
        ("public_health", "Public Health Facility"),
        ("public_school", "Public School"),
        ("public_university", "Public University / College"),
        ("procurement", "Procurement Unit"),
        ("revenue", "Revenue Collection Agency"),
        ("other_public", "Other Public Institution"),
    ]


    PRIVATE_INSTITUTIONS = [
        ("insurance", "Insurance Company"),
        ("telecom", "Telecommunications"),
        ("transport", "Transport Company"),
        ("construction", "Construction Company"),
        ("textile", "Textile / Manufacturing"),
        ("retail", "Retail Business"),
        ("mining", "Mining Company"),
        ("agriculture", "Agriculture Business"),
        ("hotel", "Hotel / Tourism"),
        ("private_health", "Private Health Facility"),
        ("private_school", "Private School"),
        ("private_university", "Private University / College"),
        ("security", "Security Company"),
        ("other_private", "Other Private Institution"),
    ]


    REGION_CHOICES = [
        ("hhohho", "Hhohho"),
        ("manzini", "Manzini"),
        ("shiselweni", "Shiselweni"),
        ("lubombo", "Lubombo"),
    ]


    AGE_GROUP_CHOICES = [
        ("under18", "Under 18"),
        ("18_24", "18 - 24"),
        ("25_34", "25 - 34"),
        ("35_44", "35 - 44"),
        ("45_54", "45 - 54"),
        ("55_64", "55 - 54"),
        ("65+", "65+"),

    ]


    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
     
    ]


    case_code = models.CharField(
        max_length=20,
        unique=True
    )


    # Reporter Information

    is_anonymous = models.BooleanField(
        default=True
    )


    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    surname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    contact = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )


    email = models.EmailField(
        blank=True,
        null=True
    )

    id_number = models.CharField(
    max_length=30,
    blank=True,
    null=True
)

    encrypted_id_number = EncryptedCharField(
    blank=True,
    null=True
)
    nationality = models.CharField(
    max_length=100,
    blank=True,
    null=True
)

    # Case Information

    region = models.CharField(
        max_length=20,
        choices=REGION_CHOICES
    )


    location = models.CharField(
        max_length=100
    )


    incident_date = models.DateField()


    incident_time = models.TimeField()


    age_group = models.CharField(
        max_length=20,
        choices=AGE_GROUP_CHOICES
    )


    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )


    sector = models.CharField(
    max_length=20,
    choices=SECTOR_CHOICES,
    default="none",
    blank=True,
    null=True
)


    institution = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )


    description = models.TextField()


    evidence = models.FileField(
        upload_to="evidence/",
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="received"
    )
    decline_reason = models.TextField(
    blank=True,
    null=True
)
    
    referral_notes = models.TextField(
    blank=True,
    null=True
)

    account = models.ForeignKey(
        "AnonymousAccount",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="cases"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


def __str__(self):
        return self.case_code



class AuditLog(models.Model):

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    action = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    ip_address = models.GenericIPAddressField(
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.action
    
class CaseStatusHistory(models.Model):

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )


    old_status = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    new_status = models.CharField(
        max_length=50
    )


    changed_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.case.case_code} - {self.new_status}"
    
class Notification(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    date = models.DateField()

    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class OrganisationSettings(models.Model):

    name = models.CharField(
        max_length=200,
        blank=True
    )


    short_name = models.CharField(
        max_length=50,
        blank=True
    )


    email = models.EmailField(
        blank=True
    )


    phone = models.CharField(
        max_length=50,
        blank=True
    )


    address = models.TextField(
        blank=True
    )


    website = models.URLField(
        blank=True
    )


    logo = models.ImageField(
        upload_to="logos/",
        blank=True,
        null=True
    )


    def __str__(self):
        return self.name

class CaseManagementSettings(models.Model):

    allow_custom_statuses = models.BooleanField(
        default=False
    )

    automatic_case_numbering = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

class AnonymousAccount(models.Model):

    username = models.CharField(
        max_length=50,
        unique=True
    )

    password = models.CharField(
        max_length=128
    )

    first_school = models.CharField(
        max_length=200
    )

    favourite_month = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username

    