from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    teachers = [
        {"name": "Eriko Sato", "title": "Lektorka języka japońskiego", "bio": "Cześć! Jestem absolwentką ekonomii Uniwersytetu Warszawskiego i filologii orientalnej ze specjalizacją japonistyka Uniwersytetu Jagiellońskiego. Odbyłam roczne stypendium na Uniwersytecie Kobe. Od lat uczę w dowolnej kombinacji języków: japońskiego, angielskiego i polskiego. Lubię aikido i sushi. Mam nadzieję – do zobaczenia!", "image": "img/eriko.jpg"},
        {"name": "Takashi Yamamoto", "title": "Nauczyciel gramatyki", "bio": "Uwielbia tłumaczyć niuanse językowe początkującym.", "image": "img/takashi.jpg"},
        {"name": "Mai Tanaka", "title": "Korepetytorka JLPT", "bio": "Przygotowuje uczniów do egzaminów od N5 do N2.", "image": "img/mai.jpg"},
        {"name": "Kenji Suzuki", "title": "Nauczyciel kultury", "bio": "Łączy naukę języka z tradycją i zwyczajami Japonii.", "image": "img/kenji.jpg"},
        {"name": "Yui Nakamura", "title": "Trener wymowy", "bio": "Skupia się na poprawnym akcentowaniu i intonacji.", "image": "img/yui.jpg"},
    ]
    
    opinions = [
        {"name": "Anna K.", "text": "Bardzo polecam zajęcia! Świetna atmosfera i japoński przestał mnie przerażać.Bardzo polecam zajęcia! Świetna atmosfera i japoński przestał mnie przerażać.Bardzo polecam zajęcia! Świetna atmosfera i japoński przestał mnie przerażać.Bardzo polecam zajęcia! Świetna atmosfera i japoński przestał mnie przerażać.Bardzo polecam zajęcia! Świetna atmosfera i japoński przestał mnie przerażać.", "avatar": "img/eriko.jpg"},
        {"name": "Michał Z.", "text": "Zawsze chciałem nauczyć się japońskiego — w EIPONI to możliwe!", "avatar": "img/eriko.jpg"},
        {"name": "Karolina N.", "text": "Lekcje prowadzone są z pasją. Bardzo wysoki poziom!", "avatar": "img/kenji.jpg"},
        {"name": "Tomek P.", "text": "Wreszcie rozumiem kanji. Polecam każdemu!", "avatar": "img/takashi.jpg"},
        {"name": "Emilia R.", "text": "Zajęcia są różnorodne, ciekawe i bardzo dobrze przygotowane.", "avatar": "img/yui.jpg"},
        {"name": "Julia M.", "text": "Lubię to, że lektorzy są bardzo cierpliwi i pomocni.", "avatar": "img/eriko.jpg"},
        {"name": "Kamil S.", "text": "Uczę się tu od pół roku — progres niesamowity!", "avatar": "img/yui.jpg"},
        {"name": "Natalia W.", "text": "Nie tylko język, ale też kultura. Super podejście!", "avatar": "img/eriko.jpg"},
    ]

    faqs = [
    {"question": "Czy zajęcia są stacjonarne czy online?",
     "answer": "Wszystkie zajęcia w naszej szkole językowej są online. Dzięki temu nie tracisz czasu na dojazdy i możesz uczestniczyć w zajęciach z wygodnego dla Ciebie miejsca."},
    {"question": "Jakiego sprzętu potrzebuję do uczestniczenia w zajęciach online?",
     "answer": "Wystarczy komputer, tablet lub smartfon z dostępem do Internetu oraz słuchawki z mikrofonem."},
    {"question": "Jakiego programu używacie do zajęć?",
     "answer": "Do prowadzenia zajęć używamy platformy Zoom."},
    {"question": "Ile jest osób na zajęciach?",
     "answer": "W grupach uczy się od 4 do maksymalnie 8 osób. Zajęcia indywidualne oraz we dwoje są zgodnie z nazwą."},
    {"question": "Jakich podręczników używacie?",
     "answer": "W zależności od grupy i poziomu używamy serii Genki lub New Approach, a dla zaawansowanych 新完全マスター."},
    {"question": "Kiedy jest początek zajęć?",
     "answer": "Nowe grupy startują regularnie — zwykle co miesiąc. Sprawdź dostępność w zakładce 'Cennik' lub 'Plany'."},
    {"question": "Jak mogę zapłacić za zajęcia?",
     "answer": "Płatności dokonujesz przelewem bankowym po zapisaniu się na zajęcia."}
    ]

    context = {
    "teachers": teachers,
    "opinions": opinions,
    "faqs": faqs
    }

    return render(request, "home.html", context)




def plany_grupowe(request):
    
    grupy_grupowe = [
    {"name": "Grupa Nagoja od zera", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 1–3", "level": "poziom A1.1 (N5)", "price": "1 000 zł", "image": "img/miasta/nagoja.jpg"},
    {"name": "Grupa Jokohama", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 4–6", "level": "poziom A1.1 (N5)", "price": "1 000 zł", "image": "img/miasta/yokohama.jpg"},
    {"name": "Grupa Osaka", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 7–9", "level": "poziom A1.2 (N5)", "price": "1 000 zł", "image": "img/miasta/osaka.jpg"},
    {"name": "Grupa Tokio", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 10–12", "level": "poziom A1.2 (N5)", "price": "1 000 zł", "image": "img/miasta/tokio.jpg"},
    {"name": "Grupa Sapporo", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 13–15", "level": "poziom A2.1 (N4)", "price": "1 000 zł", "image": "img/miasta/sapporo.jpg"},
    {"name": "Grupa Fukuoka", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 16–18", "level": "poziom A2.1 (N4)", "price": "1 000 zł", "image": "img/miasta/fukuoka.jpg"},
    {"name": "Grupa Kawasaki", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 19–21", "level": "poziom A2.2 (N4)", "price": "1 000 zł", "image": "img/miasta/kawasaki.jpg"},
    {"name": "Grupa Kobe", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "Genki 22–23", "level": "poziom A2.2 (N4)", "price": "1 000 zł", "image": "img/miasta/kobe.jpg"},
    {"name": "Grupa Kioto", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中級 1–5", "level": "poziom B1.1 (N3)", "price": "1 000 zł", "image": "img/miasta/kioto.jpg"},
    {"name": "Grupa Saitama", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中級 6–10", "level": "poziom B1.1 (N3)", "price": "1 000 zł", "image": "img/miasta/saitama.jpg"},
    {"name": "Grupa Hiroszima", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中級 11–15", "level": "poziom B1.2 (N3)", "price": "1 000 zł", "image": "img/miasta/hiroshima.jpg"},
    {"name": "Grupa Nara", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中級 16–20", "level": "poziom B1.2 (N3)", "price": "1 000 zł", "image": "img/miasta/nara.jpg"},
    {"name": "Grupa Ise", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中上級 1–5", "level": "poziom B2.1 (N2)", "price": "1 000 zł", "image": "img/miasta/ise.jpg"},
    {"name": "Grupa Okinawa", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中上級 6–10", "level": "poziom B2.1 (N2)", "price": "1 000 zł", "image": "img/miasta/okinawa.jpg"},
    {"name": "Grupa Himeji", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中上級 11–15", "level": "poziom B2.2 (N2)", "price": "1 000 zł", "image": "img/miasta/himeji.jpg"},
    {"name": "Grupa Sendai", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "New Approach 中上級 16–20", "level": "poziom B2.2 (N2)", "price": "1 000 zł", "image": "img/miasta/sendai.jpg"},
    {"name": "Grupa Kumamoto", "hours": "30h", "meetings": "20 spotkań po 1,5h", "books": "新完全マスター", "level": "poziom C1.1 (N1)", "price": "600 zł", "image": "img/miasta/kumamoto.jpg"},
]

    return render(request, 'plany_grupowe.html', {'grupy_grupowe': grupy_grupowe})


def plany_dwoje(request):
    grupy_dwoje = [
        {
            "name": "We dwoje – 8 spotkań",
            "details": "8 spotkań po 1 godzinie (cena za 1 osobę)",
            "price": "750 zł",
            "image": "img/dwoje/lekcja_1.jpg"
        },
        {
            "name": "We dwoje – 10 spotkań",
            "details": "10 spotkań po 1 godzinie (cena za 1 osobę)",
            "price": "390 zł",
            "image": "img/dwoje/lekcja_2.jpg"
        }
    ]
    return render(request, "plany_dwoje.html", {"grupy_dwoje": grupy_dwoje})


def plany_indywidualne(request):
    grupy_indywidualne = [
        {
            "name": "Indywidualny na start",
            "details": "3 spotkania po 1 godzinie",
            "price": "650 zł",
            "image": "img/indywidualne/start.jpg"
        },
        {
            "name": "Indywidualny – 5 spotkań",
            "details": "5 spotkań po 1 godzinie",
            "price": "1 300 zł",
            "image": "img/indywidualne/5x.jpg"
        },
        {
            "name": "Indywidualny – 10 spotkań",
            "details": "10 spotkań po 1 godzinie",
            "price": "3 900 zł",
            "image": "img/indywidualne/10x.jpg"
        },
        {
            "name": "Indywidualny – 30 spotkań",
            "details": "30 spotkań po 1 godzinie",
            "price": "1 300 zł",  # ✳️ warto sprawdzić, czy to poprawna cena
            "image": "img/indywidualne/30x.jpg"
        }
    ]
    return render(request, "plany_indywidualne.html", {"grupy_indywidualne": grupy_indywidualne})

def kontakt_view(request):
    success = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Możesz dodać walidację...

        # Wysyłka maila (tylko jeśli masz skonfigurowane SMTP w settings.py)
        send_mail(
            subject=f"Zapytanie od {name}",
            message=f"Od: {name} <{email}>\n\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )
        success = True

    return render(request, "kontakt.html", {"success": success})



