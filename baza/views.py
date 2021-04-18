from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Count
from .models import Klient, Lokalizacja, Licencja
from .forms import KlientForm, LokalizacjaForm, LicencjaForm


def index(request):
    return render(request, 'baza/index.html')


class KlientCreate(generic.CreateView):
    template_name = 'baza/klient_dodaj.html'
    form_class = KlientForm

    def form_valid(self, form):
        return super().form_valid(form)


class KlientDetail(generic.DetailView):
    model = Klient
    template_name = 'baza/klient_szczegoly.html'
    context_object_name = 'klient'


class KlientUpdate(generic.UpdateView):
    model = Klient
    template_name = "baza/klient_edytuj.html"
    context_object_name = 'klient'
    fields = ['prefixnip', 'nip','nazwa','pelna_nazwa','ulica','miejscowosc','kod_pocztowy','telfon', 'email']

    def form_valid(self, form):
        return super().form_valid(form)


class KlientDelete(generic.DeleteView):
    model = Klient
    template_name = "baza/klient_usun.html"
    success_url = reverse_lazy('klienci')


class KlienciView(generic.ListView):
    template_name = 'baza/klienci.html'
    context_object_name = 'klienci'
    paginate_by = 4

    def get_queryset(self):
        """Zwróć wszystkich klientów"""
        return Klient.objects.annotate(num_lok=Count('lokalizacja')).order_by('id')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(f"Lokalizacje: {Klient.objects.annotate(num_lok=Count('lokalizacja'))}")
    #     context['lok'] = Klient.objects.annotate(num_lok=Count('lokalizacja'))
    #     return context




class LokalizacjaCreate(generic.CreateView):
    template_name = 'baza/lokalizacja_dodaj.html'
    form_class = LokalizacjaForm

    def form_valid(self, form):
        form.instance.klient = get_object_or_404(Klient,
                                                 id=self.kwargs['klient'])
        return super().form_valid(form)


class LokalizacjaDetail(generic.DetailView):
    model = Lokalizacja
    template_name = 'baza/lokalizacja_szczegoly.html'
    context_object_name = 'lokalizacja'
    queryset = Lokalizacja.objects.all()


class LokalizacjaUpdate(generic.UpdateView):
    model = Lokalizacja
    template_name = 'baza/lokalizacja_edytuj.html'
    fields = fields = ['nazwa','ulica','miejscowosc','kod_pocztowy','telfon', 'email','extra_info']

class LokalizacjaDelete(generic.DeleteView):
    model = Lokalizacja
    template_name = "baza/lokalizacja_usun.html"

    def get_success_url(self):
        return reverse('lokalizacje', kwargs={'klient': self.object.klient.id})


class LokalizacjeView(generic.ListView):
    template_name = 'baza/lokalizacje_dla_klienta.html'
    context_object_name = 'lokalizacje'

    def get_queryset(self):
        self.klient = get_object_or_404(Klient, id=self.kwargs['klient'])
        return Lokalizacja.objects.filter(klient=self.klient)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.licencja = Licencja.objects.filter(lokalizacja = self.lokalizacja)
        # context['licencja'] = self.licencja
        context['klient'] = self.klient
        return context

class LicencjaCreate(generic.CreateView):
    template_name = 'baza/licencja_generuj.html'
    form_class = LicencjaForm
    success_url = reverse_lazy('klienci')

    def form_valid(self, form):
        form.instance.lokalizacja = get_object_or_404(Lokalizacja,
                                                 id=self.kwargs['lokalizacja'])

        return super().form_valid(form)



class LicencjaDetail(generic.DetailView):
    model = Licencja
    template_name = 'baza/licencja_szczegoly.html'
    context_object_name = 'licencja'



