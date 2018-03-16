from django import template
from ..models import Abusebehav as Abuses
from ..models import Mastscore as Masts
from ..models import Psych
import re

register = template.Library()

@register.filter(name='programtypes')
def programtype(progid):
    if progid == 1:
        return "Random Alcohol Monitoring"
    if progid == 2:
        return "Continuous Trandermal Alcohol Monitoring"
    if progid == 3:
        return "Home Dentention and Random Alcohol Monitoring"
    if progid == 4:
        return "Home Detention Monitoring"
    if progid == 5:
        return "Home Detention and Secure, Continuous, Remote, Alcohol Monitoring"
    if progid == 6:
        return "Random Alcohol Monitoring ALT"
    if progid == 7:
        return "Sobriter"
    if progid == 8:
        return "Secure, Continuous, Remote, Alcohol Monitoring"
    if progid == 9:
        return "Ignition Interlock"
    if progid == 10:
        return "Alcohol Drug Screening"
    if progid == 11:
        return "Alcohol Drug Education"
    if progid == 12:
        return "Alcohol Drug Treatment"
    if progid == 13:
        return "Alcohol Drug Education UDDP"
    if progid == 14:
        return "Violation Diversion"
    if progid == 15:
        return "Revocation Review Packet"
    if progid == 16:
        return "Alcohol Education Diversion Program"
    if progid == 17:
        return "Domestic Violence"
    if progid == 18:
        return "PEACE (Anger Management)"
    if progid == 19:
        return "Domestic Violence PEACE Screening"


@register.filter(name='provider')
def provider(providerid):
    if providerid == 5:
        return "Scottsdale City Court (SCC)"


@register.filter(name='status')
def status(actualenddate, noncomp):
    if not actualenddate  and  not noncomp:
        return "Active"
    if actualenddate:
        return "Compliant"
    if noncomp:
        return "Non Compliant"

@register.filter(name='programAbuse')
def progamAbuse(program):
    abuses = Abuses.objects.filter(programid=program.programid)
    if abuses:
        return True
    else:
        return False

@register.filter(name='programMast')
def progamMast(program):
    masts = Masts.objects.filter(programid=program.programid)
    if masts:
        return True
    else:
        return False

@register.filter(name='programPsych')
def progamPsych(client):
    masts = Psych.objects.filter(clientid=client.userid)
    if masts:
        return True
    else:
        return False

@register.filter(name='sec2Mins')
def secondsToMinutes(seconds):
    minutes = seconds / 60
    minutes = '%.0f'%(minutes)
    seconds = seconds % 60
    return "{} minutes and {} seconds".format(minutes, seconds)

@register.filter(name='check')
def checked(livList, index):
    if livList[index] == "1":
        return "checked"
    else:
        return "unchecked"

@register.filter(name='sub')
def substance(sub, index):
    split = sub.split(',')
    return split[index]

@register.filter(name='mastResult')
def mastResult(mastScore):
    if mastScore < 3:
        return "Low Risk Abuser"
    if mastScore > 2 and mastScore < 6:
        return "Abuse/early or middle problem drinker"
    if mastScore > 5:
        return "Alcoholic"

@register.filter(name='checkNo')
def checkedNo(livList, index):
    if livList[index] == "0":
        return "checked"
    else:
        return "unchecked"

@register.filter(name='checkYes')
def checkedYes(livList, index):
    if livList[index] == "1":
        return "checked"
    else:
        return "unchecked"