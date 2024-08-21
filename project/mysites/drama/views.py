import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Drama

def crawl_sbs_dramas():
    url = 'https://www.sbs.co.kr/tv/drama?div=tv_total_new&category='
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dramas = soup.select('ul.list_type > li')  
    for drama in dramas:
        title = drama.select_one('strong').get_text(strip=True)
        link = drama.select_one('a')['href']
        thumbnail = drama.select_one('img')['src']
        description = drama.select_one('span.dsc').get_text(strip=True)

        
        if not Drama.objects.filter(title=title).exists():
            Drama.objects.create(title=title, link=link, thumbnail=thumbnail, description=description)

def drama_list(request):
    
    crawl_sbs_dramas()

    dramas = Drama.objects.all()
    return render(request, 'drama/drama_list.html', {'dramas': dramas})