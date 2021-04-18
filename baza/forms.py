from django import forms
from .models import Klient, Lokalizacja, Moduly, Licencja


class KlientForm(forms.ModelForm):
    class Meta:
        model = Klient
        fields = [
            'prefixnip',
            'nip',
            'nazwa',
            'pelna_nazwa',
            'ulica',
            'miejscowosc',
            'kod_pocztowy',
            'telfon',
            'email'
        ]

class LokalizacjaForm(forms.ModelForm):
    class Meta:
        model = Lokalizacja
        fields = [
            'nazwa',
            'ulica',
            'miejscowosc',
            'kod_pocztowy',
            'telfon',
            'email',
            'extra_info',
        ]

class LicencjaForm(forms.ModelForm):

    modul = forms.ModelMultipleChoiceField(queryset=Moduly.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Licencja
        fields = ['nazwa',
                  'wersja_programu',
                  'modul',
                  ]

