from django.http import HttpResponse
from django.template import loader
from .models import Incident
from .forms import Ajouter_incident, Supprimer_incident
from django.shortcuts import redirect


def index(request):
    template = loader.get_template('index.html')
    if request.method == 'POST' and 'add_message' in request.POST:
        form = Ajouter_incident(request.POST)
        # vérifier si elle est valide
        if form.is_valid():
            title = form.cleaned_data['titre']
            desc = form.cleaned_data['description']
            if Incident.objects.filter(titre=title).count() == 0 :
                Incident.objects.create(titre=title, description=desc)
                return redirect('/')
            else: 
                return HttpResponse("L'incident existe déjà")
        else:
            return HttpResponse("Le formulaire n'est pas valide.")
    elif request.method == 'POST' and 'supprimer' in request.POST:
        form = Supprimer_incident(request.POST)
        if form.is_valid():
            incident = form.cleaned_data['incident_a_supprimer']
            Incident.objects.filter(titre=incident).delete()
            return redirect('/')
    incident = Incident.objects.all()
    context = {'incident':incident}
    return HttpResponse(template.render(context, request))
