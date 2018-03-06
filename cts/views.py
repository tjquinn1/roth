from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection

from collections import namedtuple


# from models import Clients
from . import forms

# Create your views here.

@login_required
def court_case(request):
    form = forms.CourtCaseForm()
    
    context = {}
    if request.method == 'POST':
        form = forms.CourtCaseForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            with connection.cursor() as cursor:
                query = """
                SELECT c.firstname, c.middlename, c.lastname, c.dob, p.casenumber, p.docketnumber, p.providername, p.completeby, p.totaltime, p.startdate, p.enddate, p.actualenddate, p.courtappearancedate, p.dateofvio, p.bac, p.charge 
                FROM programs as p
                INNER JOIN clients c ON p.userid = c.userid
                WHERE 
                """
                if firstname:
                    query += 'c.firstname="{}" AND ' .format(firstname)
                if lastname:
                    query += 'c.lastname="{}" '.format(lastname)
                cursor.execute(query)
                Result = namedtuple('Result', [r[0] for r in cursor.description])
                rows = cursor.fetchall()
                context['form'] = forms.CourtCaseForm()
                context['results'] = [Result(*r) for r in rows]
        else:
            context['form'] =  form
    else:
        context['form'] = forms.CourtCaseForm()
    
    return render(request, 'court_case.html', context)
