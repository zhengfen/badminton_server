from django.http import HttpResponse
from clubs.models import Position, Role

def seed_positions(request):
    '''
    seed positions table
    '''
    items = [
        {
            'name':{
                'en':'Captain', 
                'fr':'Capitaine', 
                'de':'Kapitän'
            }
        }, 
        {
            'name':{
                'en':'Extra', 
                'fr':'Extra', 
                'de':'Extra'
            }
        }
    ]
    for item in items:
        position = Position(name=item['name'])
        position.save()
    return HttpResponse('Done seeding positions')

def seed_roles(request): 
    '''
    seed roles table
    '''
    items = [
        {
            'name':{
                'en':'Admin', 
                'fr':'Admin', 
                'de':'Admin'
            }
        }, 
        {
            'name':{
                'en':'Club admin', 
                'fr':'Club admin', 
                'de':'Club admin'
            }
        }
    ]
    for item in items: 
        role = Role(name=item['name'])
        role.save()
    return HttpResponse('Done seeding roles')
