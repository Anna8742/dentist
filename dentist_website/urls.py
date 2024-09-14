from django.contrib.auth import views as auth_views

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),  # For login, logout, etc.
]
