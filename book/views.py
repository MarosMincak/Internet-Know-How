from django.shortcuts import render
import random


# Create your views here.

def domov(request):
    return render(request, 'book/home.html', context={'text_next': 'Obsah >'})


def obsah(request):
    return render(request, 'book/obsah.html',
                  context={'text_previous': '< Domov',
                           'text_next': '1. Internet - základ novodobého života? >',
                           'title': 'Obsah'})


def one(request):
    return render(request, 'kapitoly/one/one.html', context={
        'text_previous': '< Obsah',
        'text_next': '2. Digitalizácia ľudstva >',
        'title': '1 Internet - základ novodobého ľudstva?'})


def two(request):
    return render(request, 'kapitoly/two/two.html', context={
        'text_previous': '< 1 Internet - základ novodobého ľudstva?',
        'text_next': '2.1 Kybernetická bezpečnosť >',
        'title': '2 Digitalizácia ľudstva'})


def two_one(request):
    return render(request, 'kapitoly/two/two-one.html', context={
        'text_previous': '< 2 Digitalizácia ľudstva',
        'text_next': '2.2 Kybernetické útoky >',
        'title': '2.1 Kybernetická bezpečnosť'})


def two_two(request):
    return render(request, 'kapitoly/two/two-two.html', context={
        'text_previous': '< 2.1 Kybernetická bezpečnosť',
        'text_next': 'Opakovanie 1 >',
        'title': '2.2 Kybernetické útoky'})


def three(request):
    return render(request, 'kapitoly/three/three.html', context={
        'text_previous': '< Opakovanie 1',
        'text_next': '3.1 Bezpečné používanie internetu >',
        'title': '3 Hrozby internetu'})


def three_one(request):
    return render(request, 'kapitoly/three/three-one.html', context={
        'text_previous': '< 3 Hrozby internetu',
        'text_next': '3.1.1 Tvorba hesla >',
        'title': '3.1 Bezpečné používanie internetu'})

def three_one_one(request):
    thepassword = ''
    length = int(request.GET.get('length', 10))
    characters = list('abcdefghijklmnoprstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPRSTUVWXYZ'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('+`@#$~^&*{}°^¨;–><'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'kapitoly/three/three-one-one.html', context={
        'text_previous': '< 3.1 Bezpečné používanie internetu',
        'text_next': '3.1.2 Ukladanie hesla >',
        'title': '3.1.1 Tvorba hesla',
        'password': thepassword})

def three_one_two(request):
    return render(request, 'kapitoly/three/three-one-two.html', context={
        'text_previous': '< 3.1.1 Tvorba hesla',
        'text_next': '3.1.3 Verejné siete (WIFI) >',
        'title': '3.1.2 Ukladanie hesla'})


def three_one_three(request):
    return render(request, 'kapitoly/three/three-one-three.html', context={
        'text_previous': '< 3.1.2 Ukladanie hesla',
        'text_next': '3.2 Sociálne siete >',
        'title': '3.1.3 Verejné siete (WIFI)'})


def three_two(request):
    return render(request, 'kapitoly/three/three-two.html', context={
        'text_previous': '< 3.1.3 Verejné siete (WIFI)',
        'text_next': '3.2.1 Pár základných tipov k bezpečnému používaniu sociálnych sietí >',
        'title': '3.2 Sociálne siete'})


def three_two_one(request):
    return render(request, 'kapitoly/three/three-two-one.html', context={
        'text_previous': '< 3.2 Sociálne siete',
        'text_next': '3.3 Počítačové vírusy a spam >',
        'title': '3.2.1 Pár základných tipov k bezpečnému používaniu sociálnych sietí'})


def three_three(request):
    return render(request, 'kapitoly/three/three-three.html', context={
        'text_previous': '< 3.2.1 Pár základných tipov k bezpečnému používaniu sociálnych sietí',
        'text_next': '3.3.1 Najbežnejšie typy počítačových vírusov >',
        'title': '3.3 Počítačové vírusy a spam'})


def three_three_one(request):
    return render(request, 'kapitoly/three/thre-thre-one.html', context={
        'text_previous': '< 3.3 Počítačové vírusy a spam',
        'text_next': '3.3.2 Mylné predstavy o počítačových vírusoch >',
        'title': '3.3.1 Najbežnejšie typy počítačových vírusov'})


def three_three_two(request):
    return render(request, 'kapitoly/three/thre-thre-two.html', context={
        'text_previous': '< 3.3.1 Najbežnejšie typy počítačových vírusov',
        'text_next': '3.3.3 Ako (ne)dostať počítačový vírus >',
        'title': '3.3.2 Mylné predstavy o počítačových vírusoch'})


def three_three_three(request):
    return render(request, 'kapitoly/three/tre-tre-tre.html', context={
        'text_previous': '< 3.3.2 Mylné predstavy o počítačových vírusoch',
        'text_next': '3.3.4 Ako identifikovať a zneškodniť počítačový vírus >',
        'title': '3.3.3 Ako (ne)dostať počítačový vírus'})


def three_three_four(request):
    return render(request, 'kapitoly/three/tre-tre-four.html', context={
        'text_previous': '< 3.3.3 Ako (ne)dostať počítačový vírus',
        'text_next': '3.4 Spam >',
        'title': '3.3.4 Ako identifikovať a zneškodniť počítačový vírus'})


def three_four(request):
    return render(request, 'kapitoly/three/three-four.html', context={
        'text_previous': '< 3.3.4 Ako identifikovať a zneškodniť počítačový vírus',
        'text_next': '3.4.1 Phishing >',
        'title': '3.4 Spam'})


def three_four_one(request):
    return render(request, 'kapitoly/three/three-four-one.html', context={
        'text_previous': '< 3.4 Spam',
        'text_next': '3.4.2 Ako sa brániť proti Spamu a Phishingu >',
        'title': '3.4.1 Phishing'})


def three_four_two(request):
    return render(request, 'kapitoly/three/three-four-two.html', context={
        'text_previous': '< 3.4.1 Phishing',
        'text_next': '3.4.3 Sociálne inžinierstvo >',
        'title': '3.4.2 Ako sa brániť proti Spamu a Phishingu'})


def three_four_three(request):
    return render(request, 'kapitoly/three/thre-four-thre.html', context={
        'text_previous': '< 3.4.2 Ako sa brániť proti Spamu a Phishingu',
        'text_next': 'Opakovanie 2 >',
        'title': '3.4.3 Sociálne inžinierstvo'})


def four(request):
    return render(request, 'kapitoly/four/four.html', context={
        'text_previous': '< Opakovanie 2',
        'text_next': '4.1 Kyberšikana >',
        'title': '4 Netiketa'})


def four_one(request):
    return render(request, 'kapitoly/four/four-one.html', context={
        'text_previous': '< 4 Netiketa',
        'text_next': '4.1.1 Ako sa kyberšikane vyvarovať a brániť >',
        'title': '4.1 Kyberšikana'})


def four_one_one(request):
    return render(request, 'kapitoly/four/four-one-one.html', context={
        'text_previous': '< 4.1 Kyberšikana',
        'text_next': 'Opakovanie 3 >',
        'title': '4.1.1 Ako sa kyberšikane vyvarovať a brániť'})


def five(request):
    return render(request, 'kapitoly/five/five.html', context={
        'text_previous': '< Opakovanie 3',
        'text_next': 'Zoznam použitých zdrojov >',
        'title': '5. Dvojjazyčný výkladový slovník použitých pojmov'})


def zoznam_pouzitych_zdrojov(request):
    return render(request, 'book/zoz-pouz-zdroj.html', context={
        'text_previous': '< 5. Dvojjazyčný výkladový slovník použitých pojmov',
        'title': 'Zoznam použitých zdrojov'})

def test1(request):
    return render(request, 'testy/test1-kap-2.html', context={
        'text_previous': '< 2.2 Kybernetické útoky',
        'text_next': '3. Hrozby internetu >',
        'title': 'Opakovanie 1'})

def test2(request):
    return render(request, 'testy/test2-kap-3.html', context={
        'text_previous': '< 3.4.3 Sociálne inžinierstvo',
        'text_next': '4 Netiketa >',
        'title': 'Opakovanie 2'})

def test3(request):
    return render(request, 'testy/test3-kap-4.html', context={
        'text_previous': '< 4.1.1 Ako sa kyberšikane vyvarovať a brániť',
        'text_next': '5. Dvojjazyčný výkladový slovník použitých pojmov >',
        'title': 'Opakovanie 3'})