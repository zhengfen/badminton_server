from django.http import HttpResponse

from competitions.models import Level, Group

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
    return HttpResponse("Done seeding levels")

def seed_groups(request):
    items = [
        {
            'name' : {
                'en': 'National league A', 
                'fr': 'Ligue nationale A', 
                'de': 'NLA'
            }, 
            'link' : 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/6'
        }, 
        {
            'name' : {
                'en': 'National league B', 
                'fr': 'Ligue nationale B', 
                'de': 'NLB'
            }, 
            'link' : 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/7'
        }, 
        {
            'name' : {
                'en': '1st league gr 101', 
                'fr': '1e ligue gr 101', 
                'de': '1. Liga gruppe 101'
            }, 
            'link' : 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/12'
        }, 
        {
            'name' : {
                'en': '2nd league gr 202', 
                'fr': '2e ligue gr 202', 
                'de': '2. Liga gruppe 202'
            }, 
            'link' : 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/14'
        }, 
        {
            'name' : {
                'en': '3rd league AVCB-31', 
                'fr': '3e ligue AVCB-31', 
                'de': '3. Liga AVCB-31'
            }, 
            'link' : 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/177'
        }, 
        {
            'name' : {
                'en': '4th league AVCB-41', 
                'fr': '4e ligue AVCB-41', 
                'de': '4. Liga AVCB-41'
            }, 
            'link' :'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/215'
        },
        {
            'name' : {
                'en': '4th league AVCB-42', 
                'fr': '4e ligue AVCB-42', 
                'de': '4. Liga AVCB-42'
            }, 
            'link': 'https://www.swiss-badminton.ch/league/05EDB7B3-199D-4C4D-B1C8-85D228FEBA71/draw/216'
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
                'en': '6th league group 1', 
                'fr': '6e ligue groupe 1', 
                'de': '6. Liga gruppe 1'
            }
        },
        {
            'name' : {
                'en': '6th league group 2', 
                'fr': '6e ligue group 2', 
                'de': '6. Liga gruppe 2'
            }
        },        
        {
            'name' : {
                'en': 'Juniors A', 
                'fr': 'Juniors A', 
                'de': 'Juniors A'
            }
        },
        {
            'name' : {
                'en': 'Juniors B', 
                'fr': 'Juniors B', 
                'de': 'Juniors B'
            }
        }
    ]

    for item in items:
        group = Group(name=item['name'])
        if ('link' in item):
            group.link = item['link']
        group.save()

    return HttpResponse("Done seeding groups")