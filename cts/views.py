from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Clients, Programs, Finances, Psych
from .models import Abusebehav as Abuses
from decimal import Decimal

from collections import namedtuple
from django.core.exceptions import ObjectDoesNotExist


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

@login_required
def test(request):
    form = forms.CourtCaseForm()
    
    context = {}
    if request.method == 'POST':
        form = forms.CourtCaseForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            client = Clients.objects.get(firstname = firstname, lastname = lastname)
            context['client'] = client

            if Abuses.objects.filter(clientid = client.userid).exists():
                abuses = Abuses.objects.filter(clientid = client.userid)
                context['abuses'] = abuses
            
            if Programs.objects.filter(userid = client.userid).exists():
                programs = Programs.objects.filter(userid = client.userid)
                context['programs'] = programs

            if Finances.objects.filter(clientid = client.userid).exists():
                finances = Finances.objects.filter(clientid = client.userid)
                bal = 0.00
                bal = Decimal(bal)
                for finance in finances:
                    if finance.transactiontype == 1 or finance.transactiontype == 3:
                        bal = bal + finance.amount
                    else:
                        bal = bal - finance.amount
                context['bal'] = bal
            context['form'] = forms.CourtCaseForm()
        else:
            context ={
                'form': form
            }
    else:
        context ={
                'form': forms.CourtCaseForm()
            }
    
    return render(request, 'test.html', context)


@login_required
def abuse(request, client_id, program_id):
    context = {}

    client = Clients.objects.get(userid=client_id)
    context['client'] = client

    abuse = Abuses.objects.get(programid = program_id)
    context['abuse'] = abuse
    return render(request, 'abuse.html', context)

@login_required
def psych(request, program_id):
    context = {}
    psych = Psych.objects.get(programid = program_id)
    context['psych'] = psych
    split = psych.con.split(',')
    context['split'] = split
    print(split[22])


    return render(request, 'psych.html', context)