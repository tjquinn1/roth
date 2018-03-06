# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Abusebehav(models.Model):
    abuseid = models.AutoField(db_column='ABUSEID', unique=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    lastsave = models.DateTimeField(db_column='LASTSAVE', blank=True, null=True)  # Field name made lowercase.
    abusedate = models.DateTimeField(db_column='ABUSEDATE', blank=True, null=True)  # Field name made lowercase.
    abusesumm = models.TextField(db_column='ABUSESUMM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'abusebehav'


class Adhsscreen(models.Model):
    adhsid = models.AutoField(db_column='ADHSID', unique=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    emailsent = models.IntegerField(db_column='EMAILSENT', blank=True, null=True)  # Field name made lowercase.
    adhsdate = models.DateTimeField(db_column='ADHSDATE', blank=True, null=True)  # Field name made lowercase.
    answers = models.TextField(db_column='ANSWERS', blank=True, null=True)  # Field name made lowercase.
    adhsassign = models.IntegerField(db_column='ADHSASSIGN', blank=True, null=True)  # Field name made lowercase.
    adhsageu21 = models.IntegerField(db_column='ADHSAGEU21', blank=True, null=True)  # Field name made lowercase.
    adhsstat = models.IntegerField(db_column='ADHSSTAT', blank=True, null=True)  # Field name made lowercase.
    adhscounselor = models.IntegerField(db_column='ADHSCOUNSELOR', blank=True, null=True)  # Field name made lowercase.
    adhsbhp = models.IntegerField(db_column='ADHSBHP', blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.
    sumcomments = models.CharField(db_column='SUMCOMMENTS', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    sumreffrom = models.CharField(db_column='SUMREFFROM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sumtarcomp = models.DateField(db_column='SUMTARCOMP', blank=True, null=True)  # Field name made lowercase.
    sumcounselor = models.IntegerField(db_column='SUMCOUNSELOR', blank=True, null=True)  # Field name made lowercase.
    sumbhp = models.IntegerField(db_column='SUMBHP', blank=True, null=True)  # Field name made lowercase.
    sumlocked = models.IntegerField(db_column='SUMLOCKED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adhsscreen'


class Asusscore(models.Model):
    asid = models.AutoField(unique=True)
    clientid = models.IntegerField(blank=True, null=True)
    programid = models.IntegerField(blank=True, null=True)
    asusdate = models.DateTimeField(blank=True, null=True)
    answers = models.CharField(max_length=2000, blank=True, null=True)
    decilesum = models.CharField(max_length=2000, blank=True, null=True)
    asusstat = models.IntegerField(blank=True, null=True)
    asusscore = models.IntegerField(blank=True, null=True)
    asussum = models.CharField(max_length=500, blank=True, null=True)
    totaltime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asusscore'


class Cage(models.Model):
    cageid = models.AutoField(db_column='CAGEID', unique=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    cagedate = models.DateTimeField(db_column='CAGEDATE', blank=True, null=True)  # Field name made lowercase.
    cageq1 = models.CharField(db_column='CAGEQ1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cageq2 = models.CharField(db_column='CAGEQ2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cageq3 = models.CharField(db_column='CAGEQ3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cageq4 = models.CharField(db_column='CAGEQ4', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cage'


class Classattend(models.Model):
    classattendid = models.AutoField(db_column='CLASSATTENDID', primary_key=True)  # Field name made lowercase.
    classnumber = models.IntegerField(db_column='CLASSNUMBER')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID')  # Field name made lowercase.
    attended = models.IntegerField(db_column='ATTENDED')  # Field name made lowercase.
    absent = models.IntegerField(db_column='ABSENT')  # Field name made lowercase.
    lengthattended = models.IntegerField(db_column='LENGTHATTENDED')  # Field name made lowercase.
    lengthcredited = models.IntegerField(db_column='LENGTHCREDITED')  # Field name made lowercase.
    specificclassnumber = models.IntegerField(db_column='SPECIFICCLASSNUMBER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classattend'


class Classenrolled(models.Model):
    classlistid = models.AutoField(db_column='CLASSLISTID', primary_key=True)  # Field name made lowercase.
    classnumber = models.IntegerField(db_column='CLASSNUMBER')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID')  # Field name made lowercase.
    enrolled = models.IntegerField(db_column='ENROLLED')  # Field name made lowercase.
    firstclassdate = models.IntegerField(db_column='FIRSTCLASSDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classenrolled'


class Classes(models.Model):
    classnumber = models.AutoField(db_column='CLASSNUMBER', primary_key=True)  # Field name made lowercase.
    classprogramtype = models.IntegerField(db_column='CLASSPROGRAMTYPE')  # Field name made lowercase.
    classdate = models.DateTimeField(db_column='CLASSDATE', blank=True, null=True)  # Field name made lowercase.
    classdate2 = models.DateTimeField(db_column='CLASSDATE2', blank=True, null=True)  # Field name made lowercase.
    classlength = models.IntegerField(db_column='CLASSLENGTH', blank=True, null=True)  # Field name made lowercase.
    classcredit = models.IntegerField(db_column='CLASSCREDIT', blank=True, null=True)  # Field name made lowercase.
    classmaxstudents = models.IntegerField(db_column='CLASSMAXSTUDENTS', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='CLASSNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    classcounselor = models.IntegerField(db_column='CLASSCOUNSELOR', blank=True, null=True)  # Field name made lowercase.
    classsite = models.IntegerField(db_column='CLASSSITE', blank=True, null=True)  # Field name made lowercase.
    classroom = models.IntegerField(db_column='CLASSROOM', blank=True, null=True)  # Field name made lowercase.
    classgender = models.CharField(db_column='CLASSGENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    classlanguage = models.IntegerField(db_column='CLASSLANGUAGE')  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'


class Clients(models.Model):
    userid = models.AutoField(db_column='USERID', unique=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FIRSTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MIDDLENAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LASTNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='SUFFIX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    namesoundex = models.CharField(db_column='NAMESOUNDEX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EMAILADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HOMEPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    workphone = models.CharField(db_column='WORKPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    indigent = models.CharField(db_column='INDIGENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    interpreter = models.CharField(db_column='INTERPRETER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    origin = models.IntegerField(db_column='ORIGIN', blank=True, null=True)  # Field name made lowercase.
    mstatus = models.IntegerField(db_column='MSTATUS', blank=True, null=True)  # Field name made lowercase.
    educationyears = models.IntegerField(db_column='EDUCATIONYEARS', blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='OCCUPATION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    empstatus = models.CharField(db_column='EMPSTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    income = models.FloatField(db_column='INCOME', blank=True, null=True)  # Field name made lowercase.
    highschoolgrad = models.CharField(db_column='HIGHSCHOOLGRAD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    collegegrad = models.CharField(db_column='COLLEGEGRAD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    familysize = models.IntegerField(db_column='FAMILYSIZE', blank=True, null=True)  # Field name made lowercase.
    dlnumber = models.CharField(db_column='DLNUMBER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dlstate = models.CharField(db_column='DLSTATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    idnumber = models.CharField(db_column='IDNUMBER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idstate = models.CharField(db_column='IDSTATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    passport = models.CharField(db_column='PASSPORT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    passportorigin = models.CharField(db_column='PASSPORTORIGIN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    aclu1 = models.IntegerField(db_column='ACLU1', blank=True, null=True)  # Field name made lowercase.
    aclu2 = models.IntegerField(db_column='ACLU2', blank=True, null=True)  # Field name made lowercase.
    aclu3 = models.IntegerField(db_column='ACLU3', blank=True, null=True)  # Field name made lowercase.
    aclu4 = models.IntegerField(db_column='ACLU4', blank=True, null=True)  # Field name made lowercase.
    aclu5 = models.IntegerField(db_column='ACLU5', blank=True, null=True)  # Field name made lowercase.
    aclu6 = models.IntegerField(db_column='ACLU6', blank=True, null=True)  # Field name made lowercase.
    aclu7 = models.IntegerField(db_column='ACLU7', blank=True, null=True)  # Field name made lowercase.
    aclu8 = models.IntegerField(db_column='ACLU8', blank=True, null=True)  # Field name made lowercase.
    aclu9 = models.IntegerField(db_column='ACLU9', blank=True, null=True)  # Field name made lowercase.
    aclu10 = models.IntegerField(db_column='ACLU10', blank=True, null=True)  # Field name made lowercase.
    aclu11 = models.IntegerField(db_column='ACLU11', blank=True, null=True)  # Field name made lowercase.
    aclu12 = models.IntegerField(db_column='ACLU12', blank=True, null=True)  # Field name made lowercase.
    aclu13 = models.IntegerField(db_column='ACLU13', blank=True, null=True)  # Field name made lowercase.
    aclu14 = models.IntegerField(db_column='ACLU14', blank=True, null=True)  # Field name made lowercase.
    aclu15 = models.IntegerField(db_column='ACLU15', blank=True, null=True)  # Field name made lowercase.
    aclu16 = models.IntegerField(db_column='ACLU16', blank=True, null=True)  # Field name made lowercase.
    aclu17 = models.IntegerField(db_column='ACLU17', blank=True, null=True)  # Field name made lowercase.
    aclu18 = models.IntegerField(db_column='ACLU18', blank=True, null=True)  # Field name made lowercase.
    aclu19 = models.IntegerField(db_column='ACLU19', blank=True, null=True)  # Field name made lowercase.
    aclu20 = models.IntegerField(db_column='ACLU20', blank=True, null=True)  # Field name made lowercase.
    aclu21 = models.IntegerField(db_column='ACLU21', blank=True, null=True)  # Field name made lowercase.
    aclu22 = models.IntegerField(db_column='ACLU22', blank=True, null=True)  # Field name made lowercase.
    aclu23 = models.IntegerField(db_column='ACLU23', blank=True, null=True)  # Field name made lowercase.
    aclu24 = models.IntegerField(db_column='ACLU24', blank=True, null=True)  # Field name made lowercase.
    aclu25 = models.IntegerField(db_column='ACLU25', blank=True, null=True)  # Field name made lowercase.
    aclu26 = models.IntegerField(db_column='ACLU26', blank=True, null=True)  # Field name made lowercase.
    aclu27 = models.IntegerField(db_column='ACLU27', blank=True, null=True)  # Field name made lowercase.
    aclu28 = models.IntegerField(db_column='ACLU28', blank=True, null=True)  # Field name made lowercase.
    aclu29 = models.IntegerField(db_column='ACLU29', blank=True, null=True)  # Field name made lowercase.
    aclu30 = models.IntegerField(db_column='ACLU30', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.
    company = models.IntegerField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase.
    emercontact = models.CharField(db_column='EMERCONTACT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emercontactrel = models.CharField(db_column='EMERCONTACTREL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emercontactphone = models.CharField(db_column='EMERCONTACTPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emercontactemail = models.CharField(db_column='EMERCONTACTEMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    truthfulness = models.IntegerField(db_column='TRUTHFULNESS')  # Field name made lowercase.
    truthdate = models.DateTimeField(db_column='TRUTHDATE', blank=True, null=True)  # Field name made lowercase.
    ipaddress = models.CharField(db_column='IPADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastlog = models.DateTimeField(db_column='LASTLOG', blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'


class Courtreferrals(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    courtid = models.IntegerField(db_column='COURTID')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CREATEDBY')  # Field name made lowercase.
    transferred = models.DateTimeField(db_column='TRANSFERRED', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DATETIME')  # Field name made lowercase.
    defendant = models.TextField(db_column='DEFENDANT')  # Field name made lowercase.
    guardian = models.TextField(db_column='GUARDIAN')  # Field name made lowercase.
    casenum = models.TextField(db_column='CASENUM')  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE')  # Field name made lowercase.
    reorder = models.TextField(db_column='REORDER')  # Field name made lowercase.
    birthdate = models.DateField(db_column='BIRTHDATE')  # Field name made lowercase.
    intake = models.TextField(db_column='INTAKE')  # Field name made lowercase.
    screening = models.TextField(db_column='SCREENING')  # Field name made lowercase.
    level1 = models.TextField(db_column='LEVEL1')  # Field name made lowercase.
    level2 = models.TextField(db_column='LEVEL2')  # Field name made lowercase.
    underage = models.TextField(db_column='UNDERAGE')  # Field name made lowercase.
    interlock = models.TextField(db_column='INTERLOCK')  # Field name made lowercase.
    domesticviolence = models.TextField(db_column='DOMESTICVIOLENCE')  # Field name made lowercase.
    angermanagement = models.TextField(db_column='ANGERMANAGEMENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'courtreferrals'


class Devnames(models.Model):
    devnameid = models.AutoField(db_column='DEVNAMEID', unique=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'devnames'


class Dischargesum(models.Model):
    dischargeid = models.AutoField(db_column='DISCHARGEID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID')  # Field name made lowercase.
    attendchoice = models.IntegerField(db_column='ATTENDCHOICE')  # Field name made lowercase.
    partchoice = models.IntegerField(db_column='PARTCHOICE')  # Field name made lowercase.
    overalscore = models.IntegerField(db_column='OVERALSCORE')  # Field name made lowercase.
    dischagrereason = models.CharField(db_column='DISCHAGREREASON', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    aftercare1 = models.CharField(db_column='AFTERCARE1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aftercare2 = models.CharField(db_column='AFTERCARE2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aftercare3 = models.CharField(db_column='AFTERCARE3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aftercare4 = models.CharField(db_column='AFTERCARE4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    issues = models.CharField(db_column='ISSUES', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    referrals = models.CharField(db_column='REFERRALS', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    clientsigndate = models.CharField(db_column='CLIENTSIGNDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dissumdate = models.CharField(db_column='DISSUMDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    counselor = models.CharField(db_column='COUNSELOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    credentials = models.CharField(db_column='CREDENTIALS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bhpcounselor = models.CharField(db_column='BHPCOUNSELOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bhpcredentials = models.CharField(db_column='BHPCREDENTIALS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    lockitup = models.IntegerField(db_column='LOCKITUP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dischargesum'


class Emdevices(models.Model):
    deviceid = models.AutoField(db_column='DEVICEID', unique=True)  # Field name made lowercase.
    deviceprogramid = models.IntegerField(db_column='DEVICEPROGRAMID', blank=True, null=True)  # Field name made lowercase.
    devicename = models.IntegerField(db_column='DEVICENAME', blank=True, null=True)  # Field name made lowercase.
    deviceserial = models.CharField(db_column='DEVICESERIAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    batteryinstall = models.DateTimeField(db_column='BATTERYINSTALL', blank=True, null=True)  # Field name made lowercase.
    calibration = models.DateTimeField(db_column='CALIBRATION', blank=True, null=True)  # Field name made lowercase.
    calibrationinterval = models.IntegerField(db_column='CALIBRATIONINTERVAL', blank=True, null=True)  # Field name made lowercase.
    company = models.IntegerField(db_column='COMPANY', blank=True, null=True)  # Field name made lowercase.
    location = models.IntegerField(db_column='LOCATION', blank=True, null=True)  # Field name made lowercase.
    ownedrental = models.IntegerField(db_column='OWNEDRENTAL', blank=True, null=True)  # Field name made lowercase.
    package = models.IntegerField(db_column='PACKAGE', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    repair = models.DateTimeField(db_column='REPAIR', blank=True, null=True)  # Field name made lowercase.
    devicenotes = models.TextField(db_column='DEVICENOTES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emdevices'


class Empstatus(models.Model):
    statusid = models.AutoField(db_column='STATUSID', primary_key=True)  # Field name made lowercase.
    empstatus = models.CharField(db_column='EMPSTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empstatus'


class Finances(models.Model):
    financeid = models.AutoField(db_column='FINANCEID', unique=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    posterid = models.IntegerField(db_column='POSTERID', blank=True, null=True)  # Field name made lowercase.
    dateposted = models.DateTimeField(db_column='DATEPOSTED', blank=True, null=True)  # Field name made lowercase.
    transactiondate = models.DateTimeField(db_column='TRANSACTIONDATE', blank=True, null=True)  # Field name made lowercase.
    transactiontype = models.IntegerField(db_column='TRANSACTIONTYPE', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    office = models.IntegerField(db_column='OFFICE')  # Field name made lowercase.
    modifiedid = models.IntegerField(db_column='MODIFIEDID', blank=True, null=True)  # Field name made lowercase.
    modificationdate = models.DateTimeField(db_column='MODIFICATIONDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finances'


class History(models.Model):
    histid = models.AutoField(db_column='HISTID', unique=True)  # Field name made lowercase.
    histdate = models.DateTimeField(db_column='HISTDATE', blank=True, null=True)  # Field name made lowercase.
    histchange = models.TextField(db_column='HISTCHANGE', blank=True, null=True)  # Field name made lowercase.
    histusername = models.CharField(db_column='HISTUSERNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    histemail = models.CharField(db_column='HISTEMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    history = models.TextField(db_column='HISTORY', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'history'


class Hwpackage(models.Model):
    packageid = models.AutoField(db_column='PACKAGEID', unique=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    devicenameid = models.IntegerField(db_column='DEVICENAMEID', blank=True, null=True)  # Field name made lowercase.
    countrequired = models.DateField(db_column='COUNTREQUIRED', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hwpackage'


class It(models.Model):
    itid = models.AutoField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    submitdate = models.DateTimeField(blank=True, null=True)
    resolvedate = models.DateTimeField(blank=True, null=True)
    assigned = models.CharField(max_length=100, blank=True, null=True)
    resolvedby = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    issue = models.TextField(blank=True, null=True)
    resolution = models.TextField(blank=True, null=True)
    issuesex = models.TextField(blank=True, null=True)
    resolutionsex = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'it'


class Itcatown(models.Model):
    itcatid = models.AutoField(unique=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=500, blank=True, null=True)
    disabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itcatown'


class Itstatus(models.Model):
    itstatid = models.AutoField(unique=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    disabled = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itstatus'


class Location(models.Model):
    locationid = models.AutoField(db_column='LOCATIONID', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LOCATIONNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    locationcity = models.CharField(db_column='LOCATIONCITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locationzip = models.CharField(db_column='LOCATIONZIP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationaddress = models.CharField(db_column='LOCATIONADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locationaddress2 = models.CharField(db_column='LOCATIONADDRESS2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locationphone = models.CharField(db_column='LOCATIONPHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationhoursend = models.CharField(db_column='LOCATIONHOURSEND', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationhoursstart = models.CharField(db_column='LOCATIONHOURSSTART', max_length=20, blank=True, null=True)  # Field name made lowercase.
    locationcontactemail = models.CharField(db_column='LOCATIONCONTACTEMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    locationstate = models.CharField(db_column='LOCATIONSTATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    locationtz = models.CharField(db_column='LOCATIONTZ', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'location'


class Mastscore(models.Model):
    mastid = models.AutoField(unique=True)
    clientid = models.IntegerField(blank=True, null=True)
    programid = models.IntegerField(blank=True, null=True)
    mastdate = models.DateTimeField(blank=True, null=True)
    answers = models.CharField(max_length=100, blank=True, null=True)
    ans21times = models.IntegerField(blank=True, null=True)
    ans22times = models.IntegerField(blank=True, null=True)
    mastscore = models.IntegerField(blank=True, null=True)
    maststat = models.IntegerField(blank=True, null=True)
    totaltime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mastscore'


class Mstatus(models.Model):
    statusid = models.AutoField(db_column='STATUSID', primary_key=True)  # Field name made lowercase.
    mstatus = models.CharField(db_column='MSTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mstatus'


class Origin(models.Model):
    originid = models.AutoField(db_column='ORIGINID', primary_key=True)  # Field name made lowercase.
    origin = models.CharField(db_column='ORIGIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'origin'


class Policereports(models.Model):
    prid = models.AutoField(db_column='PRID', unique=True)  # Field name made lowercase.
    pruserid = models.IntegerField(db_column='PRUSERID', blank=True, null=True)  # Field name made lowercase.
    pruploader = models.IntegerField(db_column='PRUPLOADER', blank=True, null=True)  # Field name made lowercase.
    prupdate = models.DateTimeField(db_column='PRUPDATE', blank=True, null=True)  # Field name made lowercase.
    policereport = models.TextField(db_column='POLICEREPORT', blank=True, null=True)  # Field name made lowercase.
    prfile = models.CharField(db_column='PRFILE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prtype = models.CharField(db_column='PRTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prsize = models.CharField(db_column='PRSIZE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'policereports'


class Policy(models.Model):
    policyid = models.AutoField(db_column='POLICYID', primary_key=True)  # Field name made lowercase.
    policyname = models.CharField(db_column='POLICYNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    timeread = models.IntegerField(db_column='TIMEREAD', blank=True, null=True)  # Field name made lowercase.
    datepolicyaccepted = models.DateTimeField(db_column='DATEPOLICYACCEPTED', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'policy'


class Prepostscore(models.Model):
    prepostid = models.AutoField(db_column='PREPOSTID', unique=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    preorpost = models.CharField(db_column='PREORPOST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    compdate = models.DateTimeField(db_column='COMPDATE', blank=True, null=True)  # Field name made lowercase.
    answers = models.CharField(db_column='ANSWERS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prepostscore'


class Programdays(models.Model):
    programid = models.AutoField(db_column='PROGRAMID', unique=True)  # Field name made lowercase.
    daystatus = models.CharField(db_column='DAYSTATUS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    daydate = models.DateField(db_column='DAYDATE', blank=True, null=True)  # Field name made lowercase.
    reported = models.DateField(db_column='REPORTED', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programdays'


class Programfees(models.Model):
    pgmfeeid = models.AutoField(db_column='PGMFEEID', primary_key=True)  # Field name made lowercase.
    programtype = models.IntegerField(db_column='PROGRAMTYPE')  # Field name made lowercase.
    onlinefee = models.DecimalField(db_column='ONLINEFEE', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    onlinehourly = models.IntegerField(db_column='ONLINEHOURLY')  # Field name made lowercase.
    officefee = models.DecimalField(db_column='OFFICEFEE', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    officehourly = models.IntegerField(db_column='OFFICEHOURLY')  # Field name made lowercase.
    oneononefee = models.DecimalField(db_column='ONEONONEFEE', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    oneononehourly = models.IntegerField(db_column='ONEONONEHOURLY')  # Field name made lowercase.
    numberofhours = models.IntegerField(db_column='NUMBEROFHOURS')  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programfees'


class Programs(models.Model):
    programid = models.AutoField(db_column='PROGRAMID', unique=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='USERID', blank=True, null=True)  # Field name made lowercase.
    programtype = models.IntegerField(db_column='PROGRAMTYPE', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='STARTDATE', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='ENDDATE', blank=True, null=True)  # Field name made lowercase.
    actualenddate = models.DateField(db_column='ACTUALENDDATE', blank=True, null=True)  # Field name made lowercase.
    units = models.IntegerField(db_column='UNITS', blank=True, null=True)  # Field name made lowercase.
    unitcount = models.IntegerField(db_column='UNITCOUNT', blank=True, null=True)  # Field name made lowercase.
    provider = models.IntegerField(db_column='PROVIDER', blank=True, null=True)  # Field name made lowercase.
    providername = models.CharField(db_column='PROVIDERNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    treatmentprovider = models.IntegerField(db_column='TREATMENTPROVIDER', blank=True, null=True)  # Field name made lowercase.
    treatmentselected = models.DateTimeField(db_column='TREATMENTSELECTED', blank=True, null=True)  # Field name made lowercase.
    completeby = models.DateField(db_column='COMPLETEBY', blank=True, null=True)  # Field name made lowercase.
    courtappearancedate = models.DateField(db_column='COURTAPPEARANCEDATE', blank=True, null=True)  # Field name made lowercase.
    noncompliance = models.DateField(db_column='NONCOMPLIANCE', blank=True, null=True)  # Field name made lowercase.
    noncompliancereason = models.CharField(db_column='NONCOMPLIANCEREASON', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='CREATED', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    timeofvio = models.CharField(db_column='TIMEOFVIO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dateofvio = models.DateField(db_column='DATEOFVIO', blank=True, null=True)  # Field name made lowercase.
    bac = models.CharField(db_column='BAC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    othercharge = models.CharField(db_column='OTHERCHARGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    charge = models.CharField(db_column='CHARGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    casenumber = models.CharField(db_column='CASENUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    docketnumber = models.CharField(db_column='DOCKETNUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.
    clientdeclinedcourt = models.IntegerField(db_column='CLIENTDECLINEDCOURT', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_column='COMMENTS', blank=True, null=True)  # Field name made lowercase.
    overridehours = models.IntegerField(db_column='OVERRIDEHOURS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'programs'


class Promocodes(models.Model):
    promoid = models.AutoField(db_column='PROMOID', primary_key=True)  # Field name made lowercase.
    promoname = models.CharField(db_column='PROMONAME', max_length=25, blank=True, null=True)  # Field name made lowercase.
    promovalue = models.CharField(db_column='PROMOVALUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    promodesc = models.CharField(db_column='PROMODESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    promostart = models.DateField(db_column='PROMOSTART', blank=True, null=True)  # Field name made lowercase.
    promoend = models.DateField(db_column='PROMOEND', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'promocodes'


class Providers(models.Model):
    providerid = models.AutoField(db_column='PROVIDERID', unique=True)  # Field name made lowercase.
    providername = models.CharField(db_column='PROVIDERNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    providercode = models.CharField(db_column='PROVIDERCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    provideremail = models.CharField(db_column='PROVIDEREMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    providerreporttype = models.IntegerField(db_column='PROVIDERREPORTTYPE', blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=200, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='CONTACT', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'providers'


class Psych(models.Model):
    psychid = models.AutoField(db_column='PSYCHID', primary_key=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    datecompleted = models.DateTimeField(db_column='DATECOMPLETED', blank=True, null=True)  # Field name made lowercase.
    liv = models.CharField(db_column='LIV', max_length=100, blank=True, null=True)  # Field name made lowercase.
    soc = models.CharField(db_column='SOC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp = models.CharField(db_column='EMP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fin = models.CharField(db_column='FIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chi = models.CharField(db_column='CHI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fam = models.CharField(db_column='FAM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    msts = models.CharField(db_column='MSTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    con = models.CharField(db_column='CON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    conother = models.CharField(db_column='CONOTHER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    goa = models.CharField(db_column='GOA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    goaother = models.CharField(db_column='GOAOTHER', max_length=200, blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES', blank=True, null=True)  # Field name made lowercase.
    subused = models.CharField(db_column='SUBUSED', max_length=100, blank=True, null=True)  # Field name made lowercase.
    subalc = models.CharField(db_column='SUBALC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subamp = models.CharField(db_column='SUBAMP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subbar = models.CharField(db_column='SUBBAR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subcaf = models.CharField(db_column='SUBCAF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subcoc = models.CharField(db_column='SUBCOC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subcra = models.CharField(db_column='SUBCRA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subhal = models.CharField(db_column='SUBHAL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subinh = models.CharField(db_column='SUBINH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    submar = models.CharField(db_column='SUBMAR', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subnic = models.CharField(db_column='SUBNIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subpcp = models.CharField(db_column='SUBPCP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subpre = models.CharField(db_column='SUBPRE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    suboth = models.CharField(db_column='SUBOTH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    counselor = models.IntegerField(db_column='COUNSELOR', blank=True, null=True)  # Field name made lowercase.
    bhpcounselor = models.IntegerField(db_column='BHPCOUNSELOR', blank=True, null=True)  # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED', blank=True, null=True)  # Field name made lowercase.
    totaltime = models.IntegerField(db_column='TOTALTIME')  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psych'


class Referralcontact(models.Model):
    referralid = models.AutoField(db_column='REFERRALID', primary_key=True)  # Field name made lowercase.
    referral = models.IntegerField(db_column='REFERRAL', blank=True, null=True)  # Field name made lowercase.
    success = models.IntegerField(db_column='SUCCESS', blank=True, null=True)  # Field name made lowercase.
    contacttype = models.CharField(db_column='CONTACTTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    creator = models.IntegerField(db_column='CREATOR', blank=True, null=True)  # Field name made lowercase.
    contactdate = models.DateTimeField(db_column='CONTACTDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'referralcontact'


class Relofinfo(models.Model):
    relid = models.AutoField(db_column='RELID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    person = models.CharField(db_column='PERSON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    use = models.CharField(db_column='USE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endcondition = models.CharField(db_column='ENDCONDITION', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    datesigned = models.DateField(db_column='DATESIGNED', blank=True, null=True)  # Field name made lowercase.
    daterevoked = models.DateField(db_column='DATEREVOKED', blank=True, null=True)  # Field name made lowercase.
    disable = models.IntegerField(db_column='DISABLE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relofinfo'


class Reminder(models.Model):
    rid = models.AutoField(db_column='RID', unique=True)  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID', blank=True, null=True)  # Field name made lowercase.
    rdate = models.DateTimeField(db_column='RDATE', blank=True, null=True)  # Field name made lowercase.
    rreason = models.CharField(db_column='RREASON', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    rfollowup = models.DateTimeField(db_column='RFOLLOWUP', blank=True, null=True)  # Field name made lowercase.
    rfollowupname = models.IntegerField(db_column='RFOLLOWUPNAME', blank=True, null=True)  # Field name made lowercase.
    rcreation = models.DateTimeField(db_column='RCREATION', blank=True, null=True)  # Field name made lowercase.
    rcreatedby = models.IntegerField(db_column='RCREATEDBY', blank=True, null=True)  # Field name made lowercase.
    rcomplete = models.DateTimeField(db_column='RCOMPLETE', blank=True, null=True)  # Field name made lowercase.
    rcategory = models.CharField(db_column='RCATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rthisuseronly = models.IntegerField(db_column='RTHISUSERONLY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reminder'


class Reporttype(models.Model):
    rtypeid = models.AutoField(db_column='RTYPEID', primary_key=True)  # Field name made lowercase.
    rtype = models.CharField(db_column='RTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reporttype'


class Transactiontypes(models.Model):
    transactid = models.AutoField(db_column='TRANSACTID', unique=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    creditdebit = models.CharField(db_column='CREDITDEBIT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactiontypes'


class Treatmentplan(models.Model):
    treatmentplanid = models.AutoField(db_column='TREATMENTPLANID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    programid = models.IntegerField(db_column='PROGRAMID')  # Field name made lowercase.
    hours = models.CharField(db_column='HOURS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='CLIENTNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    present = models.CharField(db_column='PRESENT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    otherreason = models.CharField(db_column='OTHERREASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    presenting3 = models.CharField(db_column='PRESENTING3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    presenting4 = models.CharField(db_column='PRESENTING4', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goal1 = models.CharField(db_column='GOAL1', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goal2 = models.CharField(db_column='GOAL2', max_length=500, blank=True, null=True)  # Field name made lowercase.
    goal3 = models.CharField(db_column='GOAL3', max_length=500, blank=True, null=True)  # Field name made lowercase.
    m1meth = models.CharField(db_column='M1METH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    m2meth = models.CharField(db_column='M2METH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    m3meth = models.CharField(db_column='M3METH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pgmlevel = models.CharField(db_column='PGMLEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bhpcounselor = models.CharField(db_column='BHPCOUNSELOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    signdate = models.CharField(db_column='SIGNDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    present1 = models.CharField(db_column='PRESENT1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lockitup = models.CharField(db_column='LOCKITUP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    present2 = models.CharField(db_column='PRESENT2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    present3 = models.CharField(db_column='PRESENT3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m1compby = models.CharField(db_column='M1COMPBY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m2compby = models.CharField(db_column='M2COMPBY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m3compby = models.CharField(db_column='M3COMPBY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    m1completed = models.CharField(db_column='M1COMPLETED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    m2completed = models.CharField(db_column='M2COMPLETED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    m3completed = models.CharField(db_column='M3COMPLETED', max_length=20, blank=True, null=True)  # Field name made lowercase.
    counselor = models.CharField(db_column='COUNSELOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tpdate = models.CharField(db_column='TPDATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    credentials = models.CharField(db_column='CREDENTIALS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    bhpcredentials = models.CharField(db_column='BHPCREDENTIALS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treatmentplan'


class Unittype(models.Model):
    unittypeid = models.AutoField(db_column='UNITTYPEID', unique=True)  # Field name made lowercase.
    unitname = models.CharField(db_column='UNITNAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='DISABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unittype'


class Violations(models.Model):
    vioid = models.AutoField(db_column='VIOID', unique=True)  # Field name made lowercase.
    viouserid = models.IntegerField(db_column='VIOUSERID', blank=True, null=True)  # Field name made lowercase.
    vioprogramid = models.IntegerField(db_column='VIOPROGRAMID', blank=True, null=True)  # Field name made lowercase.
    viouploader = models.IntegerField(db_column='VIOUPLOADER', blank=True, null=True)  # Field name made lowercase.
    vioupdate = models.DateTimeField(db_column='VIOUPDATE', blank=True, null=True)  # Field name made lowercase.
    viodate = models.DateTimeField(db_column='VIODATE', blank=True, null=True)  # Field name made lowercase.
    violationreason = models.TextField(db_column='VIOLATIONREASON', blank=True, null=True)  # Field name made lowercase.
    violationreport = models.TextField(db_column='VIOLATIONREPORT', blank=True, null=True)  # Field name made lowercase.
    viofile = models.CharField(db_column='VIOFILE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    viotype = models.CharField(db_column='VIOTYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    viosize = models.CharField(db_column='VIOSIZE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'violations'
