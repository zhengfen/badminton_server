from django.http import HttpResponse

from competitions.models import Level 

def seed_levels(request):
    '''
    seed levels table
    '''
    items = [
        {
            'name' : {
                'en': '1st league', 
                'fr': '1e ligue', 
                'de': '1. Liga'
            }
        }, 
        {
            'name' : {
                'en': '2nd league', 
                'fr': '2e ligue', 
                'de': '2. Liga'
            }
        }, 
        {
            'name' : {
                'en': '3rd league', 
                'fr': '3e ligue', 
                'de': '3. Liga'
            }
        }, 
        {
            'name' : {
                'en': '4th league', 
                'fr': '4e ligue', 
                'de': '4. Liga'
            }
        }, 
        {
            'name' : {
                'en': '5th league', 
                'fr': '5e ligue', 
                'de': '5. Liga'
            }
        }, 
        {
            'name' : {
                'en': '6th league', 
                'fr': '6e ligue', 
                'de': '6. Liga'
            }
        }, 
        {
            'name' : {
                'en': 'Junior', 
                'fr': 'Junior', 
                'de': 'Junior'
            }
        }
    ]
    for item in items: 
        level = Level(name = item['name'])
        level.save()
    return HttpResponse("Done")