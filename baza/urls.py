from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('klienci', views.KlienciView.as_view(), name='klienci'),
    path('klienci/dodaj/', views.KlientCreate.as_view(), name='klient_dodaj'),
    path('klienci/<int:pk>/', views.KlientDetail.as_view(), name="klient_szczegoly"),
    path('klienci/<int:pk>/edytuj', views.KlientUpdate.as_view(), name="klient_edytuj"),
    path('klienci/<int:pk>/usun', views.KlientDelete.as_view(), name="klient_usun"),
    path('klienci/<klient>/lokalizacje', views.LokalizacjeView.as_view(), name='lokalizacje'),
    path('klienci/<klient>/dodaj_lokalizacje/', views.LokalizacjaCreate.as_view(), name='lokalizacja_dodaj'),
    path('lokalizacja/<int:pk>/', views.LokalizacjaDetail.as_view(), name='lokalizacja_szczegoly'),
    path('lokalizacja/<int:pk>/edytuj', views.LokalizacjaUpdate.as_view(), name='lokalizacja_edytuj'),
    path('lokalizacja/<int:pk>/usun', views.LokalizacjaDelete.as_view(), name='lokalizacja_usun'),
    path('klienci/<klient>/lokalizacje/<lokalizacja>/generuj_licencje', views.LicencjaCreate.as_view(), name='licencja_generuj'),
    path('licencja/<int:pk>', views.LicencjaDetail.as_view(), name='licencja_szczegoly'),
    ]