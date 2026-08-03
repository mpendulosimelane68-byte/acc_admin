from django.db import models


class Report(models.Model):

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
     
    ]


    AGE_GROUP_CHOICES = [
    ("under_18", "Under 18"),
    ("18_24", "18 - 24"),
    ("25_34", "25 - 34"),
    ("35_44", "35 - 44"),
    ("45_54", "45 - 54"),
    ("55_64", "55 - 64"),
    ("above_65+", "Above 65+"),
]


    REGION_CHOICES = [
        ("hhohho", "Hhohho"),
        ("manzini", "Manzini"),
        ("shiselweni", "Shiselweni"),
        ("lubombo", "Lubombo"),
    ]


    SECTOR_CHOICES = [
        ("public", "Public Institution"),
        ("private", "Private Institution"),
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


    CORRUPTION_TYPE_CHOICES = [
        ("bribery", "Bribery"),
        ("fraud", "Fraud"),
        ("embezzlement", "Misappropriation of Funds"),
        ("conflict_interest", "Conflict of Interest"),
        ("procurement", "Procurement Irregularity"),
        ("abuse_power", "Abuse of Power"),
        ("extortion", "Extortion"),
        ("other", "Other Corruption Issue"),
    ]


    case_code = models.CharField(
        max_length=30,
        unique=True
    )


    anonymous = models.BooleanField(
        default=True
    )


    reporter_name = models.CharField(
        max_length=100,
        blank=True
    )


    reporter_surname = models.CharField(
        max_length=100,
        blank=True
    )


    id_number = models.CharField(
        max_length=20,
        blank=True
    )


    email = models.EmailField(
        blank=True
    )


    contact = models.CharField(
        max_length=20,
        blank=True
    )


    town = models.CharField(
        max_length=100,
        blank=True
    )


    incident_location = models.CharField(
        max_length=255
    )


    incident_date = models.DateField()


    incident_time = models.TimeField()


    nationality = models.CharField(
        max_length=50,
        blank=True
    )


    age_group = models.CharField(
        max_length=20,
        choices=AGE_GROUP_CHOICES
    )


    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )


    region = models.CharField(
        max_length=30,
        choices=REGION_CHOICES
    )


    sector = models.CharField(
        max_length=20,
        choices=SECTOR_CHOICES,
        blank=True
    )


    institution = models.CharField(
        max_length=50,
        blank=True
    )


    corruption_type = models.CharField(
        max_length=50,
        choices=CORRUPTION_TYPE_CHOICES,
        blank=True
    )


    amount_paid = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )


    evidence = models.FileField(
    upload_to='evidence/',
    blank=True,
    null=True
)


    description = models.TextField()


    submitted_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.case_code
class Officer(models.Model):

    officer_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    surname = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.name} {self.surname}"
class Case(models.Model):

    STATUS_CHOICES = [
        ('received', 'Received'),
        ('investigation', 'Under Investigation'),
        ('referral', 'Referral'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(
    max_length=100,
    choices=STATUS_CHOICES,
    default='received'
)

    report = models.OneToOneField(Report, on_delete=models.CASCADE)

    assigned_officer = models.ForeignKey(
        Officer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Received'
    )

    custom_status = models.CharField(max_length=100, blank=True, null=True)

    notes = models.TextField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.report.case_code


class CaseStatusHistory(models.Model):

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=30)

    changed_at = models.DateTimeField(auto_now_add=True)

    changed_by = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.case.report.case_code} - {self.status}"


class AuditLog(models.Model):

    user = models.CharField(max_length=100)

    action = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action