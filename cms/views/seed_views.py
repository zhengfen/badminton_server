from django.http import HttpResponse
from cms.models import Page

def seed_pages(request):
    '''
    seed pages table
    '''
    items = [
        {
            'title':{
                'en':'Home', 
                'fr':'Accueil', 
                'de':'Startseite'
            }
        }, 
        {
            'title':{
                'en':'Commitee', 
                'fr':'Comité', 
                'de':'Komitee'
            }
        }, 
        {
            'title':{
                'en':'Clubs', 
                'fr':'Clubs', 
                'de':'Vereine'
            }
        }, 
        {
            'title':{
                'en':'Interclub', 
                'fr':'Interclub', 
                'de':'Interclub'
            }
        }, 
        {
            'title':{
                'en':'Tournaments', 
                'fr':'Tournois', 
                'de':'Turniere'
            }
        }, 
        {
            'title':{
                'en':'Tournaments', 
                'fr':'Photo gallery', 
                'de':'Photogalerie'
            }
        }, 
        {
            'title':{
                'en':'General assembly', 
                'fr':'Assemblée générale',  
                'de':'Generalversammlung'
            }
        }, 
        {
            'title':{
                'en':'Press', 
                'fr':'Presse',  
                'de':'Presse'
            }
        }, 
        {
            'title':{
                'en':'Contact', 
                'fr':'Contact',  
                'de':'Kontakt'
            }
        }, 
    ]
    for item in items:
        page = Page(title = item['title'])
        page.save()
    return HttpResponse('Done seeding pages')