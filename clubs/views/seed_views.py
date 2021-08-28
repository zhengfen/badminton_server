from django.http import HttpResponse
from clubs.models import Position

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
    return HttpResponse('Done')