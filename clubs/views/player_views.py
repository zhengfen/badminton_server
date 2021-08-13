from django.http import HttpResponse
from clubs.models import Club, ClubResponsable, Contact, User
from clubs.serializers import PlayerWithTeamsSerializer
from openpyxl import load_workbook
import os
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

class PlayerViewSet(viewsets.ModelViewSet): 
    serializer_class = PlayerWithTeamsSerializer
    # permission_classes = [IsAdminUser, ]
    def get_queryset(self):
        queryset = User.objects.all()
        filers = ['club']
        for filter in filers: 
            value = self.request.query_params.get(filter)        
            if value is not None:
                queryset = queryset.filter(**{filter: value})
        
        value = self.request.query_params.get('search')
        if value is not None:
            queryset = queryset.filter(name__icontains=value)
        return queryset

def import_responsables(request): 
    filename = os.path.join(settings.BASE_DIR, 'responsables.xlsx')
    wb = load_workbook(filename = filename)
    sh = wb['Responsables des clubs']
    current_club = None
    for i in range(3, 63):
        email = sh['I' + str(i)].value
        if (email==None):
            continue

        # club
        club_name = sh['A' + str(i)].value    
        if (club_name):
            club, created = Club.objects.get_or_create(name=club_name)
            current_club = club

        # user        
        try: 
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            last_name = sh['C' + str(i)].value    
            first_name = sh['D' + str(i)].value 
            if (last_name and first_name):
                username = first_name.lower() + '.' + last_name.lower()
            else:
                username = email
            user = User(last_name=last_name, first_name=first_name, email=email, username=username)
            user.save()

        # contact
        try: 
            contact = Contact.objects.get(user_id=user.id)
        except ObjectDoesNotExist:
            address = sh['E' + str(i)].value
            npa = sh['F' + str(i)].value
            city = sh['G' + str(i)].value
            phone = sh['H' + str(i)].value
            contact = Contact(address=address, npa=npa, city=city, phone=phone, user_id=user.id)
            contact.save()

        # club responsable
        try: 
            club_responsable = ClubResponsable.objects.get(club_id=club.id, user_id=user.id)
        except ObjectDoesNotExist:
            function = sh['B' + str(i)].value
            club_responsable = ClubResponsable(club_id=club.id, user_id=user.id, function=function)
            club_responsable.save()

        return HttpResponse("Done")


def process_users(request): 
    '''
    try to add club_id by analysing club_responsable
    '''
    users = User.objects.filter(club_id__isnull=True)
    for user in users:
        club_responsable = ClubResponsable.objects.filter(user_id = user.id).first()
        if club_responsable: 
            user.club_id = club_responsable.club_id
            user.save()
    return HttpResponse("Done")