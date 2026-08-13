from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cases/', views.cases, name='cases'),
    path('analytics/', views.analytics, name='analytics'),
    path('audit/', views.audit_logs, name='audit_logs'),
    path('settings/', views.settings, name='settings'),
    path('cases/<int:id>/', views.case_detail, name='case_detail'),
    path('analytics/regions/', views.regions, name='regions'),
    path(
    "analytics/gender/",
    views.gender_analysis,
    name="gender_analysis"
),
path(
    "analytics/public-institutions/",
    views.public_institutions,
    name="public_institutions"
),
path(
    'analytics/private-institutions/',
    views.private_institutions,
    name='private_institutions'
),
path(
    'analytics/age-groups/',
    views.age_groups,
    name='age_groups'
),
path(
        'analytics/trends/',
        views.trends,
        name='trends'
    ),

path(
    'notifications/add/',
    views.add_notification,
    name='add_notification'
),
path(
        'analytics/overview/',
        views.overview,
        name='overview'
    ),
path(
    "login/",
    views.dashboard_login,
    name="dashboard_login"
),
path(
    "logout/",
    views.dashboard_logout,
    name="dashboard_logout"
),
path(
    "case-management-settings/",
    views.case_management_settings,
    name="case_management_settings"
),

path(
    "cases/export/",
    views.export_cases_excel,
    name="export_cases_excel"
),

path(
    "analytics/export/",
    views.export_overview_excel,
    name="export_overview_excel"
),

path(
    "analytics/regions/export/",
    views.export_region_excel,
    name="export_region_excel"
),

path(
    "analytics/private/export/",
    views.export_private_institutions_excel,
    name="export_private_institutions_excel"
),

path(
    "export-public-institutions/",
    views.export_public_institutions_excel,
     name="export_public_institutions_excel"
),
path(
    "export-gender/",
    views.export_gender_excel,
    name="export_gender_excel"
),
path(
    "export-age-groups/",
    views.export_age_groups_excel,
    name="export_age_groups_excel"
),

path(
    "analytics/reporter-type/",
    views.reporter_type_analysis,
    name="reporter_type_analysis",
),

path(
        "export-reporter-type-excel/",
        views.export_reporter_type_excel,
        name="export_reporter_type_excel"
    ),


path(
    "export-trends/",
    views.export_trends_excel,
    name="export_trends_excel"
),

path(
    "api/reports/",
    views.receive_report,
    name="receive_report"
),

path(
    "api/my-reports/",
    views.get_my_reports,
    name="get_my_reports",
),

path(
    "api/case-status/<str:case_code>/",
    views.get_case_status,
    name="get_case_status"
),

path(
    "api/register/",
    views.register_anonymous_account,
    name="register_anonymous_account",
),

path(
    "api/login/",
    views.login_anonymous_account,
    name="login_anonymous_account",
),

path(
    "api/reset-password/",
    views.reset_anonymous_password,
    name="reset_anonymous_password"
),

path(
    "encrypt-existing-id-numbers/",
    views.encrypt_existing_id_numbers,
    name="encrypt_existing_id_numbers",
),

    path('cases/<int:id>/status/<str:status>/', views.update_case_status, name='update_case_status'),
    path(
    'cases/<int:id>/update/',
    views.update_status,
    name='update_status'
),

]