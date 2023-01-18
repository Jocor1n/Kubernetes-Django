from django import forms

class Ajouter_incident (forms.Form):
    titre = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)

class Supprimer_incident (forms.Form):
    incident_a_supprimer = forms.CharField(max_length=255)