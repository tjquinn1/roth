from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import Clients, Programs, Finances, Psych
from .models import Abusebehav as Abuses
from .models import Mastscore as Masts
from decimal import Decimal
import csv
import io
from datetime import datetime

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


    return render(request, 'psych.html', context)

@login_required
def mast(request, program_id, client_id):
    context = {}
    mast = Masts.objects.get(programid = program_id)
    client = Clients.objects.get(userid= client_id)
    context['mast'] = mast
    context['client'] = client


    return render(request, 'mast.html', context)



@login_required
def upload_mast(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST, request.FILES)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    mast = Masts.objects.get(mastid=int(row[0]))
                    if row[6] == '':
                        ans22times=0
                    else:
                        ans22times=int(row[6])
                    if row[5] == '':
                        ans21times=0
                    else:
                        ans21times=int(row[5])
                    if mast:
                        mast.clientid=int(row[1])
                        mast.programid=int(row[2])
                        mast.mastdate=datetime.strptime(row[3],'%Y/%m/%d %H:%M:%S')
                        mast.answers=row[4]
                        mast.ans21times=ans21times
                        mast.ans22times=ans22times
                        mast.mastscore=int(row[7])
                        mast.maststat=int(row[8])
                        mast.totaltime=int(row[9])
                        mast.save()
                        print("Prints")
                except ObjectDoesNotExist:
                    if row[6] == '':
                        ans22times=0
                    else:
                        ans22times=int(row[6])
                    _, created = Masts.objects.update_or_create(
                        mastid=int(row[0]),
                        clientid=int(row[1]),
                        programid=int(row[2]),
                        mastdate=datetime.strptime(row[3],'%Y/%m/%d %H:%M:%S'),
                        answers=row[4],
                        ans21times=int(row[5]),
                        ans22times=ans22times,
                        mastscore=int(row[7]),
                        maststat=int(row[8]),
                        totaltime=int(row[9]),
                        )

        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_mast.html', context)

@login_required
def upload_client(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST, request.FILES)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    client = Clients.objects.get(userid=int(row[0]))
                    if row[16] == '':
                        date = '1900-01-01'
                        dob = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        dob=datetime.strptime(row[16],'%Y-%m-%d')
                    if row[20] == '':
                        origin=0
                    else:
                        origin=int(row[20])

                    if row[22] == '':
                        educationyears=0
                    else:
                        educationyears=int(row[22])

                    if row[25] == '':
                        income=0.0
                    else:
                        income=float(row[25])
                    if client:
                        client.firstname=row[1]
                        client.middlename=row[2]
                        client.lastname=row[3]
                        client.suffix=row[4]
                        client.namesoundex=row[5]
                        client.password=row[6]
                        client.emailaddress=row[7]
                        client.address=row[8]
                        client.address2=row[9]
                        client.city=row[10]
                        client.state=row[11]
                        client.zip=row[12]
                        client.homephone=row[13]
                        client.workphone=row[14]
                        client.ssn=row[15]
                        client.dob= dob
                        client.gender=row[17]
                        client.indigent=row[18]
                        client.interpreter=row[19]
                        client.origin=origin
                        client.mstatus=int(row[21])
                        client.educationyears=educationyears
                        client.occupation=row[23]
                        client.empstatus=row[24]
                        client.income=income
                        client.highschoolgrad=row[26]
                        client.collegegrad=row[27]
                        client.familysize=int(row[28])
                        client.dlnumber=row[29]
                        client.dlstate=row[30]
                        client.idnumber=row[31]
                        client.idstate=row[32]
                        client.passport=row[33]
                        client.passportorigin=row[34]
                        client.aclu1=int(row[35])
                        client.aclu2=int(row[36])
                        client.aclu3=int(row[37])
                        client.aclu4=int(row[38])
                        client.aclu5=int(row[39])
                        client.aclu6=int(row[40])
                        client.aclu7=int(row[41])
                        client.aclu8=int(row[42])
                        client.aclu9=int(row[43])
                        client.aclu10=int(row[44])
                        client.aclu11=int(row[45])
                        client.aclu12=int(row[46])
                        client.aclu13=int(row[47])
                        client.aclu14=int(row[48])
                        client.aclu15=int(row[49])
                        client.aclu16=int(row[50])
                        client.aclu17=int(row[51])
                        client.aclu18=int(row[52])
                        client.aclu19=int(row[53])
                        client.aclu20=int(row[54])
                        client.aclu21=int(row[55])
                        client.aclu22=int(row[56])
                        client.aclu23=int(row[57])
                        client.aclu24=int(row[58])
                        client.aclu25=int(row[59])
                        client.aclu26=int(row[60])
                        client.aclu27=int(row[61])
                        client.aclu28=int(row[62])
                        client.aclu29=int(row[63])
                        client.aclu30=int(row[64])
                        client.disabled=int(row[65])
                        client.created=datetime.strptime(row[66],'%Y/%m/%d %H:%M:%S')
                        client.company=int(row[67])
                        client.emercontact=row[68]
                        client.emercontactrel=row[69]
                        client.emercontactphone=row[70]
                        client.emercontactemail=row[71]
                        client.truthfulness=int(row[72])
                        client.truthdate=datetime.strptime(row[73],'%Y/%m/%d %H:%M:%S')
                        client.ipaddress=row[74]
                        client.lastlog=datetime.strptime(row[75],'%Y/%m/%d %H:%M:%S')
                        client.totaltime=int(row[76])
                        client.save()
                except ObjectDoesNotExist:
                    if row[16] == '':
                        date = '1900-01-01'
                        dob = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        dob=datetime.strptime(row[16],'%Y-%m-%d')
                    if row[20] == '':
                        origin=0
                    else:
                        origin=int(row[20])
                    if row[21] == '':
                        mstatus=0
                    else:
                        mstatus=int(row[21])
                    if row[22] == '':
                        educationyears=0
                    else:
                        educationyears=int(row[22])

                    if row[25] == '':
                        income=0.0
                    else:
                        income=float(row[25])

                    if row[75] == '':
                        date = '1900/01/01 12:00:00'
                        lastlogin = datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
                    else:
                        lastlogin=datetime.strptime(row[75],'%Y/%m/%d %H:%M:%S')
                    _, created = Clients.objects.update_or_create(
                        userid=int(row[0]),
                        firstname=row[1],
                        middlename=row[2],
                        lastname=row[3],
                        suffix=row[4],
                        namesoundex=row[5],
                        password=row[6],
                        emailaddress=row[7],
                        address=row[8],
                        address2=row[9],
                        city=row[10],
                        state=row[11],
                        zip=row[12],
                        homephone=row[13],
                        workphone=row[14],
                        ssn=row[15],
                        dob= dob,
                        gender=row[17],
                        indigent=row[18],
                        interpreter=row[19],
                        origin=origin,
                        mstatus=mstatus,
                        educationyears=educationyears,
                        occupation=row[23],
                        empstatus=row[24],
                        income=income,
                        highschoolgrad=row[26],
                        collegegrad=row[27],
                        familysize=int(row[28]),
                        dlnumber=row[29],
                        dlstate=row[30],
                        idnumber=row[31],
                        idstate=row[32],
                        passport=row[33],
                        passportorigin=row[34],
                        aclu1=int(row[35]),
                        aclu2=int(row[36]),
                        aclu3=int(row[37]),
                        aclu4=int(row[38]),
                        aclu5=int(row[39]),
                        aclu6=int(row[40]),
                        aclu7=int(row[41]),
                        aclu8=int(row[42]),
                        aclu9=int(row[43]),
                        aclu10=int(row[44]),
                        aclu11=int(row[45]),
                        aclu12=int(row[46]),
                        aclu13=int(row[47]),
                        aclu14=int(row[48]),
                        aclu15=int(row[49]),
                        aclu16=int(row[50]),
                        aclu17=int(row[51]),
                        aclu18=int(row[52]),
                        aclu19=int(row[53]),
                        aclu20=int(row[54]),
                        aclu21=int(row[55]),
                        aclu22=int(row[56]),
                        aclu23=int(row[57]),
                        aclu24=int(row[58]),
                        aclu25=int(row[59]),
                        aclu26=int(row[60]),
                        aclu27=int(row[61]),
                        aclu28=int(row[62]),
                        aclu29=int(row[63]),
                        aclu30=int(row[64]),
                        disabled=int(row[65]),
                        created=datetime.strptime(row[66],'%Y/%m/%d %H:%M:%S'),
                        company=int(row[67]),
                        emercontact=row[68],
                        emercontactrel=row[69],
                        emercontactphone=row[70],
                        emercontactemail=row[71],
                        truthfulness=int(row[72]),
                        truthdate=datetime.strptime(row[73],'%Y/%m/%d %H:%M:%S'),
                        ipaddress=row[74],
                        lastlog=lastlogin,
                        totaltime=int(row[76])
                        )
        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_client.html', context)


@login_required
def upload_fin(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    fin = Finances.objects.get(financeid=int(row[0]))
                    if fin:
                        fin.clientid=int(row[1])
                        fin.programid=int(row[2])
                        fin.posterid=int(row[3])
                        fin.dateposted=datetime.strptime(row[4],'%Y/%m/%d %H:%M:%S')
                        fin.transactiondate=datetime.strptime(row[5],'%Y/%m/%d %H:%M:%S')
                        fin.transactiontype=int(row[6])
                        fin.description=row[7]
                        fin.amount=Decimal(row[8])
                        fin.office=int(row[9])
                        fin.modifiedid=int(row[10])
                        fin.modificationdate=datetime.strptime(row[11],'%Y/%m/%d %H:%M:%S')
                        fin.save()
                except ObjectDoesNotExist:
                    _, created = Finances.objects.update_or_create(
                            financeid=int(row[0]),
                            clientid=int(row[1]),
                            programid=int(row[2]),
                            posterid=int(row[3]),
                            dateposted=datetime.strptime(row[4],'%Y/%m/%d %H:%M:%S'),
                            transactiondate=datetime.strptime(row[5],'%Y/%m/%d %H:%M:%S'),
                            transactiontype=int(row[6]),
                            description=row[7],
                            amount=Decimal(row[8]),
                            office=int(row[9]),
                            modifiedid=int(row[10]),
                            modificationdate=datetime.strptime(row[11],'%Y/%m/%d %H:%M:%S'),
                        )
        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_fin.html', context)


@login_required
def upload_psych(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    if row[32] == '':
                        locked = 99
                    else:
                        locked=int(row[32])
                    if row[31] == '':
                        bhpcounselor = 99
                    else:
                        bhpcounselor=int(row[31])
                    if row[30] == '':
                        counselor = 99
                    else:
                        counselor=int(row[30])
                    if row[3] == '':
                        date = '1900-01-01 12:00:00'
                        datecompleted = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        datecompleted=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')
                    pysch = Psych.objects.get(psychid=int(row[0]))
                    if psych:
                        pysch.programid=int(row[1])
                        pysch.clientid=int(row[2])
                        pysch.datecompleted=datecompleted
                        pysch.liv=row[4]
                        pysch.soc=row[5]
                        pysch.emp=row[6]
                        pysch.fin=row[7]
                        pysch.chi=row[8]
                        pysch.fam=row[9]
                        pysch.msts=row[10]
                        pysch.con=row[11]
                        psych.conother=row[12]
                        psych.goa=row[13]
                        psych.goaother=row[14]
                        psych.notes=row[15]
                        psych.subused=row[16]
                        psych.subalc=row[17]
                        psych.subamp=row[18]
                        psych.subbar=row[19]
                        psych.subcaf=row[20]
                        psych.subcoc=row[21]
                        psych.subcra=row[22]
                        psych.subhal=row[23]
                        psych.subinh=row[24]
                        psych.submar=row[25]
                        psych.subnic=row[26]
                        psych.subpcp=row[27]
                        psych.subpre=row[28]
                        psych.suboth=row[29]
                        psych.counselor=counselor
                        psych.bhpcounselor=bhpcounselor
                        psych.locked=locked
                        psych.totaltime=int(row[33])
                        psych.disabled=int(row[34])
                        pysch.save()
                except ObjectDoesNotExist:
                    if row[32] == '':
                        locked = 99
                    else:
                        locked=int(row[32])
                    if row[31] == '':
                        bhpcounselor = 99
                    else:
                        bhpcounselor=int(row[31])
                    if row[30] == '':
                        counselor = 99
                    else:
                        counselor=int(row[30])
                    if row[3] == '':
                        date = '1900-01-01 12:00:00'
                        datecompleted = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        datecompleted=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')
                    _, created = Psych.objects.update_or_create(
                            psychid=int(row[0]),
                            programid=int(row[1]),
                            clientid=int(row[2]),
                            datecompleted=datecompleted,
                            liv=row[4],
                            soc=row[5],
                            emp=row[6],
                            fin=row[7],
                            chi=row[8],
                            fam=row[9],
                            msts=row[10],
                            con=row[11],
                            conother=row[12],
                            goa=row[13],
                            goaother=row[14],
                            notes=row[15],
                            subused=row[16],
                            subalc=row[17],
                            subamp=row[18],
                            subbar=row[19],
                            subcaf=row[20],
                            subcoc=row[21],
                            subcra=row[22],
                            subhal=row[23],
                            subinh=row[24],
                            submar=row[25],
                            subnic=row[26],
                            subpcp=row[27],
                            subpre=row[28],
                            suboth=row[29],
                            counselor=counselor,
                            bhpcounselor=bhpcounselor,
                            locked=locked,
                            totaltime=int(row[33]),
                            disabled=int(row[34]),
                        )
        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_psych.html', context)


@login_required
def upload_abuse(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    if row[3] == '':
                        date = '1900-01-01 12:00:00'
                        lastsave = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        lastsave=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')

                    if row[4] == '':
                        date = '1900-01-01 12:00:00'
                        abusedate = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        abusedate =datetime.strptime(row[4],'%Y-%m-%d %H:%M:%S')
                    abuse = Abuses.objects.get(abuseid=int(row[0]))
                    if abuse:
                        abuse.clientid=int(row[1])
                        abuse.programid=int(row[2])
                        abuse.lastsave=lastsave
                        abuse.abusedate=abusedate
                        abuse.abusesumm=row[5]
                        abuse.save()
                except ObjectDoesNotExist:
                        if row[3] == '':
                            date = '1900-01-01 12:00:00'
                            lastsave = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                        else:
                            lastsave=datetime.strptime(row[3],'%Y-%m-%d %H:%M:%S')

                        if row[4] == '':
                            date = '1900-01-01 12:00:00'
                            abusedate = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                        else:
                            abusedate =datetime.strptime(row[4],'%Y-%m-%d %H:%M:%S')
                        _, created = Abuses.objects.update_or_create(
                                abuseid=int(row[0]),
                                clientid=int(row[1]),
                                programid=int(row[2]),
                                lastsave=lastsave,
                                abusedate=abusedate,
                                abusesumm=row[5]
                            )
        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_abuse.html', context)



@login_required
def upload_program(request):
    context = {}
    pathForm = forms.PathForm()
    
    context = {}
    if request.method == 'POST':
        pathForm = forms.PathForm(request.POST, request.FILES)
        if pathForm.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            for row in csv.reader(io_string, delimiter=',', quotechar='"'):
                try:
                    if row[4] == '':
                        date = '1900-01-01'
                        enddate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        enddate=datetime.strptime(row[4],'%Y-%m-%d')

                    if row[5] == '':
                        date = '1900-01-01'
                        actualenddate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        actualenddate =datetime.strptime(row[5],'%Y-%m-%d')
                    
                    if row[6] == '':
                        units = 0
                    else:
                        units =int(row[6])
                    
                    if row[8] == '':
                        provider = 0
                    else:
                        provider =int(row[8])

                    if row[10] == '':
                        treatmentprovider = 0
                    else:
                        treatmentprovider=int(row[10])

                    if row[11] == '':
                        date = '1900-01-01 12:00:00'
                        treatmentselected = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        treatmentselected =datetime.strptime(row[11],'%Y-%m-%d %H:%M:%S')
                    
                    if row[12] == '' or row[12] == '0000-00-00':
                        date = '1900-01-01'
                        completeby = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        completeby =datetime.strptime(row[12],'%Y-%m-%d')

                    if row[13] == '' or row[13] == '0000-00-00':
                        date = '1900-01-01'
                        courtappearancedate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        courtappearancedate =datetime.strptime(row[13],'%Y-%m-%d')

                    if row[14] == '':
                        date = '1900-01-01'
                        noncompliance = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        noncompliance =datetime.strptime(row[14],'%Y-%m-%d')

                    if row[19] == '':
                        date = '1900-01-01'
                        dateofvio = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        dateofvio =datetime.strptime(row[19],'%Y-%m-%d')
                    try:
                        if row[25] == '':
                            totaltime = 0
                        else:
                            totaltime=int(row[25])
                    except ValueError:
                        totaltime = 0

                    if row[28] == '':
                        overridehours = 0
                    else:
                        overridehours=int(row[28])

                    try:
                        client = Clients.objects.get(userid=int(row[1]))
                    except ObjectDoesNotExist:
                        client = Clients.objects.get(userid=772)


                    program = Programs.objects.get(programid=int(row[0]))
                    if program:
                        program.userid=client
                        program.programtype=int(row[2])
                        program.startdate=datetime.strptime(row[3],'%Y-%m-%d')
                        program.enddate=enddate
                        program.actualenddate=actualenddate
                        program.units=units
                        program.unitcount=int(row[7])
                        program.provider=provider
                        program.providername=row[9]
                        program.treatmentprovider=treatmentprovider
                        program.treatmentselected=treatmentselected
                        program.completeby=completeby
                        program.courtappearancedate=courtappearancedate
                        program.noncompliance=noncompliance
                        program.noncompliancereason=row[15]
                        program.created=datetime.strptime(row[16],'%Y-%m-%d %H:%M:%S')
                        program.disabled=int(row[17])
                        program.timeofvio=row[18]
                        program.dateofvio=dateofvio
                        program.bac=row[20]
                        program.othercharge=row[21]
                        program.charge=row[22]
                        program.casenumber=row[23]
                        program.docketnumber=row[24]
                        program.totaltime=totaltime
                        program.clientdeclinedcourt=int(row[26])
                        program.comments=row[27]
                        program.overridehours=overridehours
                        program.save()

                except ObjectDoesNotExist:
                    if row[4] == '':
                        date = '1900-01-01'
                        enddate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        enddate=datetime.strptime(row[4],'%Y-%m-%d')

                    if row[5] == '':
                        date = '1900-01-01'
                        actualenddate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        actualenddate =datetime.strptime(row[5],'%Y-%m-%d')
                    
                    if row[6] == '':
                        units = 0
                    else:
                        units =int(row[6])
                    
                    if row[8] == '':
                        provider = 0
                    else:
                        provider =int(row[8])

                    if row[10] == '':
                        treatmentprovider = 0
                    else:
                        treatmentprovider=int(row[10])

                    if row[11] == '':
                        date = '1900-01-01 12:00:00'
                        treatmentselected = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
                    else:
                        treatmentselected =datetime.strptime(row[11],'%Y-%m-%d %H:%M:%S')

                    if row[12] == '' or row[12] == '0000-00-00':
                        date = '1900-01-01'
                        completeby = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        completeby =datetime.strptime(row[12],'%Y-%m-%d')

                    if row[13] == '' or row[13] == '0000-00-00':
                        date = '1900-01-01'
                        courtappearancedate = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        courtappearancedate =datetime.strptime(row[13],'%Y-%m-%d')

                    if row[14] == '':
                        date = '1900-01-01'
                        noncompliance = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        noncompliance =datetime.strptime(row[14],'%Y-%m-%d')

                    if row[19] == '':
                        date = '1900-01-01'
                        dateofvio = datetime.strptime(date,'%Y-%m-%d')
                    else:
                        dateofvio =datetime.strptime(row[19],'%Y-%m-%d')
                    
                    try:
                        if row[25] == '':
                            totaltime = 0
                        else:
                            totaltime=int(row[25])
                    except ValueError:
                        totaltime = 0

                    if row[28] == '':
                        overridehours = 0
                    else:
                        overridehours=int(row[28])
                    try:
                        client = Clients.objects.get(userid=int(row[1]))
                    except ObjectDoesNotExist:
                        client = Clients.objects.get(userid=772)
                    _, created = Programs.objects.update_or_create(
                            programid=int(row[0]),
                            userid=client,
                            programtype=int(row[2]),
                            startdate=datetime.strptime(row[3],'%Y-%m-%d'),
                            enddate=enddate,
                            actualenddate=actualenddate,
                            units=units,
                            unitcount=int(row[7]),
                            provider=provider,
                            providername=row[9],
                            treatmentprovider=treatmentprovider,
                            treatmentselected=treatmentselected,
                            completeby=completeby,
                            courtappearancedate=courtappearancedate,
                            noncompliance=noncompliance,
                            noncompliancereason=row[15],
                            created=datetime.strptime(row[16],'%Y-%m-%d %H:%M:%S'),
                            disabled=int(row[17]),
                            timeofvio=row[18],
                            dateofvio=dateofvio,
                            bac=row[20],
                            othercharge=row[21],
                            charge=row[22],
                            casenumber=row[23],
                            docketnumber=row[24],
                            totaltime=totaltime,
                            clientdeclinedcourt=int(row[26]),
                            comments=row[27],
                            overridehours=overridehours
                                )
        else:
            context ={
                'form': pathForm
            }
    else:
        context ={
                'form': forms.PathForm()
            }

    return render(request, 'upload_program.html', context)