import random
import streamlit as st

# ==============================================================================
# HASŁO ADMINISTRATORA
# ==============================================================================
ADMIN_PASSWORD = "admin123"

# ==============================================================================
# INICJALIZACJA STANUSESSION I MOTYWÓW
# ==============================================================================
if 'theme' not in st.session_state:
    st.session_state.theme = "Ciemny"

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

if 'bazy' not in st.session_state:
    st.session_state.bazy = [
        "BAZA PYTAŃ - CZĘŚĆ 4 (Kwalifikacje, kary, przepisy przejściowe i inne)": [
    {
        "id": 1,
        "pytanie": "Prace geologiczne z zastosowaniem robót geologicznych mogą być wykonane tylko na podstawie:",
        "odpowiedzi": {
            "A": "dokumentacji geologicznej",
            "B": "koncesji",
            "C": "projektu robót geologicznych"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 79 ust.  Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prace geologiczne z zastosowaniem robót geologicznych mogą być wykonywane tylko na podstawie projektu robót geologicznych."
    },
    {
        "id": 2,
        "pytanie": "Wskaż, które z określonych obok warunków powinien spełniać prawidłowo sporządzony projekt robót geologicznych:",
        "odpowiedzi": {
            "A": "określać cel zamierzonych robót oraz sposób jego osiągnięcia",
            "B": "określać rodzaj dokumentacji geologicznej, mającej powstać w wyniku robót geologicznych",
            "C": "harmonogram robót"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 79 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych określa w szczególności: 1) cel zamierzonych robót oraz sposób jego osiągnięcia; 2) rodzaj dokumentacji geologicznej mającej powstać w wyniku robót geologicznych; 3) harmonogram robót geologicznych; 4) przestrzeń, w obrębie której mają być wykonywane roboty geologiczne; 5) przedsięwzięcia konieczne ze względu na ochronę środowiska, w tym wód podziemnych, sposób likwidacji wyrobisk, otworów wiertniczych, rekultywacji gruntów, a także czynności mające na celu zapobieżenie szkodom powstałym wskutek wykonywania zamierzonych robót."
    },
    {
        "id": 3,
        "pytanie": "Wskaż, które z określonych obok warunków powinien spełniać prawidłowo sporządzony projekt robót geologicznych:",
        "odpowiedzi": {
            "A": "określać przestrzeń, w obrębie której mają być wykonywane roboty geologiczne",
            "B": "określać przedsięwzięcia konieczne ze względu na ochronę środowiska, w tym wód podziemnych, sposób likwidacji wyrobisk, otworów wiertniczych, rekultywacji gruntów, a także czynności mające na celu zapobieżenie szkodom powstałym wskutek wykonywania zamierzonych robót",
            "C": "określać spodziewane wyniki wykonanych robót"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 79 ust. 2 pkt 2, 4 i 7 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych określa w szczególności: 1) cel zamierzonych robót oraz sposób jego osiągnięcia; 2) rodzaj dokumentacji geologicznej mającej powstać w wyniku robót geologicznych; 3) harmonogram robót geologicznych; 4) przestrzeń, w obrębie której mają być wykonywane roboty geologiczne; 5) przedsięwzięcia konieczne ze względu na ochronę środowiska, w tym wód podziemnych, sposób likwidacji wyrobisk, otworów wiertniczych, rekultywacji gruntów, a także czynności mające na celu zapobieżenie szkodom powstałym wskutek wykonywania zamierzonych robót."
    },
    {
        "id": 4,
        "pytanie": "Projekt robót geologicznych, których wykonywanie nie wymaga uzyskania koncesji:",
        "odpowiedzi": {
            "A": "zatwierdza w drodze decyzji właściwy organ nadzoru górniczego",
            "B": "zatwierdza w drodze decyzji właściwy organ administracji geologicznej",
            "C": "przyjmuje państwowa służba geologiczna"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 80 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych, których wykonywanie nie wymaga uzyskania koncesji, zatwierdza właściwy organ administracji geologicznej, w drodze decyzji."
    },
    {
        "id": 5,
        "pytanie": "Projekt robót geologicznych zatwierdza się na czas:",
        "odpowiedzi": {
            "A": "nieoznaczony",
            "B": "oznaczony nie dłuższy niż 3 lata",
            "C": "oznaczony nie dłuższy niż 5 lat"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 80 ust. 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych zatwierdza się na czas oznaczony, nie dłuższy niż 5 lat."
    },
    {
        "id": 6,
        "pytanie": "Projekt robót geologicznych przedkłada się do zatwierdzenia w:",
        "odpowiedzi": {
            "A": "2 egzemplarzach",
            "B": "3 egzemplarzach",
            "C": "4 egzemplarzach"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 80 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych przedkłada się organowi administracji geologicznej w 2 egzemplarzach w postaci papierowej lub w postaci elektronicznej."
    },
    {
        "id": 7,
        "pytanie": "Organ administracji geologicznej odmawia zatwierdzenia projektu robót geologicznych, jeżeli:",
        "odpowiedzi": {
            "A": "projektowane roboty geologiczne naruszałyby wymagania ochrony środowiska",
            "B": "projekt robót geologicznych nie odpowiada wymaganiom prawa",
            "C": "organ administracji geologicznej nie odmawia zatwierdzenia projektu robót geologicznych tylko wzywa w drodze decyzji administracyjnej do jego poprawienia"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 80 ust. 7 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organ administracji geologicznej odmawia zatwierdzenia projektu robót geologicznych, jeżeli: 1) projektowane roboty geologiczne naruszałyby wymagania ochrony środowiska; 2) projekt robót geologicznych nie odpowiada wymaganiom prawa."
    },
    {
        "id": 8,
        "pytanie": "Czy we wniosku o zatwierdzenie projektu robót geologicznych zamieszcza się informacje o prawach, jakie przysługują wnioskodawcy do nieruchomości, w granicach której roboty te mają być wykonywane:",
        "odpowiedzi": {
            "A": "jest to kwestia do ustalenia z organem administracji geologicznej",
            "B": "nie ma takiego obowiązku",
            "C": "tak, jest to wymóg prawny"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 80 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "We wniosku o zatwierdzenie projektu robót geologicznych zamieszcza się informacje o prawach, jakie przysługują wnioskodawcy do nieruchomości, w granicach której roboty te mają być wykonywane."
    },
    {
        "id": 9,
        "pytanie": "Ten kto uzyskał koncesję na poszukiwanie lub rozpoznawanie złoża kopaliny albo uzyskał decyzję o zatwierdzeniu projektu robót geologicznych zgłasza zamiar rozpoczęcia robót geologicznych:",
        "odpowiedzi": {
            "A": "właściwemu organowi administracji geologicznej",
            "B": "państwowej służbie geologicznej",
            "C": "wójtowi (burmistrzowi, prezydentowi miasta) a na obszarach morskich Rzeczypospolitej Polskiej - terenowemu organowi administracji morskiej"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 81 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ten, kto uzyskał koncesję na poszukiwanie lub rozpoznawanie złoża kopaliny (...) albo uzyskał decyzję o zatwierdzeniu projektu robót geologicznych, zgłasza na pismie zamiar rozpoczęcia robót geologicznych właściwemu organowi administracji geologicznej, organowi nadzoru górniczego oraz wójtowi (burmistrzowi, prezydentowi miasta)..."
    },
    {
        "id": 10,
        "pytanie": "Ten kto uzyskał koncesję na poszukiwanie lub rozpoznawanie złoża kopaliny albo uzyskał decyzję o zatwierdzeniu projektu robót geologicznych zgłasza zamiar rozpoczęcia robót geologicznych na piśmie, określając m.in.:",
        "odpowiedzi": {
            "A": "imiona i nazwiska osób sprawujących dozór i kierownictwo, a także numery świadectw stwierdzających kwalifikacje do wykonywania tych czynności",
            "B": "zamierzone terminy rozpoczęcia i zakończenia robót geologicznych",
            "C": "kwoty przeznaczone na ewentualne odszkodowania"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 81 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W zgłoszeniu zamierza się w szczególności podać: zamierzone terminy rozpoczęcia i zakończenia robót, imiona i nazwiska osób sprawujących kierownictwo i dozór oraz numery świadectw ich kwalifikacji."
    },
    {
        "id": 11,
        "pytanie": "Ten, kto uzyskał koncesję na poszukiwanie lub rozpoznawanie złoża kopaliny albo uzyskał decyzję o zatwierdzeniu projektu robót geologicznych ma obowiązek:",
        "odpowiedzi": {
            "A": "przekazywania właściwemu organowi administracji geologicznej próbek uzyskanych w wyniku robót geologicznych wraz z wynikami ich badań w przypadku wykonania otworów wiertniczych służących rozpoznaniu budowy głębokiego podłoża",
            "B": "przekazywania właściwemu organowi administracji geologicznej próbek uzyskanych w wyniku robót geologicznych wraz z wynikami ich badań w każdym przypadku dotyczącym wszystkich kopalni",
            "C": "bieżącego dokumentowania przebiegu robót geologicznych oraz ich wyników"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 82 ust. 1 pkt 1 i 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ten, kto uzyskał koncesję (...) albo decyzję o zatwierdzeniu projektu robót geologicznych, jest obowiązany do: 1) bieżącego dokumentowania przebiegu robót geologicznych oraz ich wyników; 2) przekazywania organowi administracji geologicznej próbek uzyskanych w wyniku robót..."
    },
    {
        "id": 12,
        "pytanie": "Jeżeli wymagają tego potrzeby bezpieczeństwa powszechnego, ochrony środowiska lub rozpoznanie budowy geologicznej kraju, w tym racjonalnej gospodarki złożami kopalina, właściwy organ administracji geologicznej może nakazać temu, kto uzyskał koncesję ma poszukiwanie lub rozpoznawanie złoża kopaliny albo decyzję o zatwierdzeniu projektu robót geologicznych, wykonanie, za wynagrodzeniem dodatkowych czynności, w szczególności robót, badań, pomiarów lub pobrania dodatkowych próbek:",
        "odpowiedzi": {
            "A": "w drodze postanowienia",
            "B": "nie ma takiej możliwości",
            "C": "w drodze decyzji"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 83 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Jeżeli wymagają tego potrzeby bezpieczeństwa powszechnego, ochrony środowiska (...), właściwy organ administracji geologicznej może nakazać, w drodze decyzji, wykonanie dodatkowych czynności..."
    },
    {
        "id": 13,
        "pytanie": "Ten, kto uzyskał koncesję na poszukiwanie lub rozpoznawanie złoża kopaliny albo uzyskał decyzję o zatwierdzeniu projektu robót geologicznych ma obowiązek:",
        "odpowiedzi": {
            "A": "bieżącego dokumentowania przebiegu robót geologicznych oraz ich wyników",
            "B": "przekazywania właściwemu organowi administracji geologicznej informacji geologicznych",
            "C": "przekazywania właściwemu organowi administracji geologicznej próbek uzyskanych w wyniku robót geologicznych wraz z wynikami ich badań w przypadku wykonania otworów wiertniczych, służących rozpoznaniu budowy głębokiego podłoża"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 82 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ten, kto uzyskał koncesję (...) jest obowiązany do bieżącego dokumentowania przebiegu robót, przekazywania organowi administracji geologicznej informacji geologicznych oraz próbek uzyskanych w wyniku robót."
    },
    {
        "id": 14,
        "pytanie": "Ten, kto wykonuje roboty geologiczne jest obowiązany do:",
        "odpowiedzi": {
            "A": "zagospodarowania kopaliny wydobytej i stosowania przepisów o opłacie eksploatacyjnej",
            "B": "zagospodarowania kopaliny wydobywającej się samoistnie w czasie ich wykonywania i stosowania przepisów o opłacie eksploatacyjnej",
            "C": "zagospodarowania kopaliny wydobywającej się samoistnie w czasie ich wykonywania bez obowiązku stosowania przepisów o opłacie eksploatacyjnej; nie wymaga zatwierdzenia"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 84 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ten, kto wykonuje roboty geologiczne, jest obowiązany do zagospodarowania kopaliny wydobywającej się samoistnie lub wydobytej w trakcie wykonywania tych robót. Do kopaliny stosuje się odpowiednio przepisy dotyczące opłaty eksploatacyjnej."
    },
    {
        "id": 15,
        "pytanie": "Jeżeli roboty geologiczne obejmują wyłącznie wiercenia w celu wykorzystania ciepła ziemi projekt robót geologicznych:",
        "odpowiedzi": {
            "A": "wymaga zatwierdzenia",
            "B": "wymaga przyjęcia zawiadomieniem",
            "C": "nie wymaga zatwierdzenia"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 85 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych obejmujący wyłącznie wiercenia w celu wykorzystania ciepła ziemi nie wymaga zatwierdzenia."
    },
    {
        "id": 16,
        "pytanie": "Jeżeli roboty geologiczne obejmują wyłącznie wiercenia w celu wykorzystania ciepła ziemi projekt robót geologicznych:",
        "odpowiedzi": {
            "A": "podlega zgłoszeniu marszałkowi województwa",
            "B": "podlega zgłoszeniu staroście",
            "C": "nie podlega zgłoszeniu organom administracji geologicznej"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 85 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Projekt robót geologicznych, o którym mowa w ust. 1, podlega zgłoszeniu staroście."
    },
    {
        "id": 17,
        "pytanie": "Przepisy dotyczące zakładu górniczego i jego ruchu oraz ratownictwa górniczego do robót geologicznych służących poszukiwaniu i rozpoznawaniu złóż kopalin, a także robót geologicznych służących innym celom stosuje się odpowiednio gdy:",
        "odpowiedzi": {
            "A": "roboty są wykonywane na obszarze górniczym utworzonym w celu wykonywania działalności metodą robót podziemnych albo metodą otworów wiertniczych",
            "B": "roboty są wykonywane na głębokości większej niż 100 m",
            "C": "roboty są wykonywane z użyciem środków strzałowych"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 86 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przepisy dotyczące zakładu górniczego i jego ruchu (...) stosuje się odpowiednio do robót geologicznych: 1) wykonywanych na obszarze górniczym... 2) wykonywanych na głębokości większej niż 100 m; 3) wykonywanych z użyciem środków strzałowych."
    },
    {
        "id": 18,
        "pytanie": "W ilu egzemplarzach przekazuje się dokumentację geologiczną złoża kopaliny właściwemu organowi administracji geologicznej:",
        "odpowiedzi": {
            "A": "w dwóch egzemplarzach,",
            "B": "w trzech egzemplarzach,",
            "C": "w czterech egzemplarzach."
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 93 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentację geologiczną przekazuje się właściwemu organowi administracji geologicznej w 2 egzemplarzach w postaci papierowej i w postaci elektronicznej."
    },
    {
        "id": 19,
        "pytanie": "Czy zawsze istnieje obowiązek ustawowy przekazywania dokumentacji geologicznej złoża kopaliny, dokumentacji hydrogeologicznej i geologiczno inżynierskiej właściwemu organowi administracji geologicznej także w postaci dokumentu elektronicznego:",
        "odpowiedzi": {
            "A": "tak, jest to obowiązek ustawowy",
            "B": "nie, nie ma takiego obowiązku",
            "C": "organ może zwrócić się z prośbą o dołączenie dokumentu elektronicznego w określonych przypadkach"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 93 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentację geologiczną przedkłada się właściwemu organowi administracji geologicznej w postaci papierowej i w postaci elektronicznej."
    },
    {
        "id": 20,
        "pytanie": "W jakim terminie od dnia przedłożenia projektu robót geologicznych obejmujących wyłącznie wiercenia w celu wykorzystania ciepła Ziemi staroście może nastąpić rozpoczęcie robót geologicznych, jeżeli starosta w drodze decyzji nie zgłosi do niego sprzeciwu:",
        "odpowiedzi": {
            "A": "2 tygodni",
            "B": "30 dni",
            "C": "2 miesięcy"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 85 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Rozpoczęcie robót geologicznych może nastąpić, jeżeli starosta, w terminie 30 dni od dnia przedłożenia projektu robót geologicznych, nie zgłosi sprzeciwu w drodze decyzji."
    },
    {
        "id": 21,
        "pytanie": "Dokumentację geologiczną w rozumieniu ustawy Prawo geologiczne i górnicze stanowią m.in. następujące rodzaje dokumentacji:",
        "odpowiedzi": {
            "A": "hydrogeologiczna",
            "B": "geologiczna złoża kopaliny",
            "C": "geotechniczna"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 88 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentacją geologiczną są: 1) dokumentacja geologiczna złoża kopaliny; 2) dokumentacja hydrogeologiczna; 3) dokumentacja geologiczno-inżynierska; 4) inna dokumentacja geologiczna."
    },
    {
        "id": 22,
        "pytanie": "Dokumentację geologiczną złoża kopaliny sporządza się w celu:",
        "odpowiedzi": {
            "A": "określenia zasobów przemysłowych",
            "B": "określenia możliwości wydobycia kopaliny ze złoża",
            "C": "określenia zasobów geologicznych"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 89 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentację geologiczną złoża kopaliny sporządza się w celu określenia jego zasobów geologicznych, granic oraz geologicznych warunków występowania i możliwości wydobycia kopaliny ze złoża."
    },
    {
        "id": 23,
        "pytanie": "Jeżeli dokumentacja geologiczna złoża kopaliny stałej ma być podstawą uzyskania koncesji, rozpoznanie złoża następuje w stopniu:",
        "odpowiedzi": {
            "A": "umożliwiającym określenie zasobów geologicznych",
            "B": "umożliwiającym sporządzenie projektu zagospodarowania złoża",
            "C": "umożliwiającym określenie zasobów bilansowych"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 89 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Jeżeli dokumentacja geologiczna złoża kopaliny ma stanowić podstawę udzielenia koncesji na wydobywanie kopaliny, rozpoznanie złoża następuje w stopniu umożliwiającym sporządzenie projektu zagospodarowania złoża."
    },
    {
        "id": 24,
        "pytanie": "W przypadku dokonywania podziału złoża, dla którego jest wykonana dokumentacja geologiczna, należy:",
        "odpowiedzi": {
            "A": "sporządzić nową dokumentację dla części złoża przewidzianej do zagospodarowania; bez konieczności rozliczania zasobów pozostałej części złoża;",
            "B": "sporządzić nową dokumentację dla części złoża przewidzianej do zagospodarowania; dla pozostałej części należy sporządzić rozliczenie zasobów złoża w formie dodatku do dokumentacji geologicznej na koszt Skarbu Państwa;",
            "C": "sporządzić nową dokumentację dla części złoża przewidzianej do zagospodarowania; dla pozostałej części należy sporządzić rozliczenie zasobów złoża w formie dodatku do dokumentacji geologicznej na koszt podmiotu, który sfinansował wykonanie nowej dokumentacji;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 89 ust. 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku dokonywania podziału złoża (...), sporządza się nową dokumentację geologiczną dla części złoża przewidzianej do zagospodarowania. Dla pozostałej części złoża sporządza się rozliczenie jego zasobów w formie dodatku do dokumentacji na koszt podmiotu, który sfinansował nową dokumentację."
    },
    {
        "id": 25,
        "pytanie": "Do sporządzania dokumentacji geologicznej złóż wód leczniczych, wód termalnych i solanek stosuje się wymagania dotyczące:",
        "odpowiedzi": {
            "A": "dokumentacji geologicznej złoża kopaliny",
            "B": "dokumentacji hydrogeologicznej;",
            "C": "dokumentacji geologiczno-inżynierskiej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 89 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do sporządzania dokumentacji geologicznej złóż wód leczniczych, wód termalnych i solanek stosuje się przepisy dotyczące dokumentacji hydrogeologicznej."
    },
    {
        "id": 26,
        "pytanie": "Dokumentacja geologiczna złoża kopaliny określa w szczególności: rodzaj, ilość i jakość kopaliny, w tym przez przedstawienie informacji dotyczących:",
        "odpowiedzi": {
            "A": "kopalin towarzyszących;",
            "B": "współwystępujących użytecznych pierwiastków śladowych",
            "C": "występujących w złożu substancji szkodliwych dla środowiska;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 89 ust. 2 pkt 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentacja geologiczna złoża kopaliny określa rodzaj, ilość i jakość kopaliny (...) w tym kopalin towarzyszących, współwystępujących użytecznych pierwiastków śladowych i substancji szkodliwych dla środowiska."
    },
    {
        "id": 27,
        "pytanie": "Dokumentacja geologiczna złoża kopaliny określa w szczególności:",
        "odpowiedzi": {
            "A": "położenie złoża, jego budowę geologiczną, formę i granice;",
            "B": "elementy środowiska",
            "C": "hydrogeologiczne i inne geologiczno-górnicze warunki występowania złoża, kryteria bilansowości"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 89 ust. 2 pkt 1, 3, 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentacja geologiczna złoża określa położenie złoża, jego budowę geologiczną, formę i granice, jak również geologiczno-górnicze i hydrogeologiczne warunki występowania złoża."
    },
    {
        "id": 28,
        "pytanie": "Dokumentacja geologiczna złoża kopaliny określa w szczególności:",
        "odpowiedzi": {
            "A": "stan zagospodarowania powierzchni w rejonie udokumentowanego złoża;",
            "B": "graniczne wartości parametrów definiujących złoże i jego granice;",
            "C": "kryteria bilansowości"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 89 ust. 2 pkt 2, 5, 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dokumentacja geologiczna złoża kopaliny określa stan zagospodarowania powierzchni w rejonie udokumentowanego złoża oraz graniczne wartości parametrów definiujących złoże i jego granice."
    },
    {
        "id": 29,
        "pytanie": "W przypadku dokonywania podziału złoża, dla którego jest wykonana dokumentacja geologiczna, dla części złoża przewidzianej do zagospodarowania:",
        "odpowiedzi": {
            "A": "tworzy się nową nazwę złoża kopaliny od nazwy najbliższej miejscowości",
            "B": "pozostawia się nazwę złoża kopaliny uzupełnioną kolejną cyfrą arabską;",
            "C": "złoże nazywa się dowolnie"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 2 ust. 2 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "W przypadku dokonywania podziału złoża kopaliny dla wydzielonej części złoża pozostawia się nazwę dotychczasową uzupełnioną o kolejną cyfrę arabską lub literę."
    },
    {
        "id": 30,
        "pytanie": "Załączniki w części tekstowej dokumentacji geologicznej złoża kopaliny dla kopalin objętych własnością górniczą obejmują m.in.:",
        "odpowiedzi": {
            "A": "omówienie wykonanych prac geologicznych i badań specjalistycznych,",
            "B": "kopie dokumentów, których treść ma znaczenie dla opracowanej dokumentacji geologicznej złoża kopaliny, w tym decyzji zatwierdzających dokumentację geologiczną złoża kopaliny i dodatki do dokumentacji, zawiadomień o przyjęciu dokumentacji, koncesji lub decyzji zatwierdzających projekty prac geologicznych lub robót geologicznych;",
            "C": "dowód istnienia prawa do wykorzystania informacji geologicznej, na podstawie której sporządzono dokumentację geologiczną złoża kopaliny;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 4 ust. 2 pkt 4 lit. b, e, f Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Załączniki do części tekstowej dokumentacji geologicznej obejmują kopie decyzji i zawiadomień oraz dowód prawa do wykorzystania informacji geologicznej."
    },
    {
        "id": 31,
        "pytanie": "W dokumentacjach geologicznych złóż kopalin stałych stosuje się następujące kategorie rozpoznania złoża:",
        "odpowiedzi": {
            "A": "D, C2, C1, B, A",
            "B": "E, D, C2, C1, B, A",
            "C": "C2, C1, A+B"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 6 ust. 1 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Zasoby złóż kopalin stałych określa się w kategoriach rozpoznania: A, B, C1, C2, D."
    },
    {
        "id": 32,
        "pytanie": "W dokumentacjach geologicznych złóż węglowodorów i metanu występującego jako kopalina towarzysząca w złożach węgla kamiennego stosuje się następujące kategorie rozpoznania złoża:",
        "odpowiedzi": {
            "A": "D, C2, C1, B, A",
            "B": "C, B, A",
            "C": "D, C, B, A"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 7 ust. 1 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Zasoby złóż węglowodorów oraz metanu jako kopaliny towarzyszącej określa się w kategoriach rozpoznania: A, B, C, D."
    },
    {
        "id": 33,
        "pytanie": "Przy rozpoznaniu złoża kopaliny stałej w kat. D błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "30%",
            "B": "40%",
            "C": "50%"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 4 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii D dopuszczalny błąd oszacowania średnich wartości parametrów złoża i zasobów wynosi do 40%."
    },
    {
        "id": 34,
        "pytanie": "Przy rozpoznaniu złoża kopaliny stałej w kat. C2 błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "30%",
            "B": "40%",
            "C": "50%"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 2 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii C2 dopuszczalny błąd oszacowania średnich wartości parametrów złoża i zasobów wynosi do 30%."
    },
    {
        "id": 35,
        "pytanie": "Przy rozpoznaniu złoża kopaliny stałej w kat. C1 błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "30%",
            "B": "40%",
            "C": "50%"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 3 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii C1 dopuszczalny błąd oszacowania średnich wartości parametrów złoża wynosi do 20-30%."
    },
    {
        "id": 36,
        "pytanie": "Przy rozpoznaniu złoża kopaliny stałej w kat. B błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "20%",
            "B": "30%",
            "C": "40%"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 4 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii B błąd oszacowania nie może przekraczać 20%."
    },
    {
        "id": 37,
        "pytanie": "Przy rozpoznaniu złoża kopaliny stałej w kat. A błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "20%",
            "B": "30%",
            "C": "10%"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 5 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii A błąd oszacowania nie może przekraczać 10%."
    },
    {
        "id": 38,
        "pytanie": "Przy rozpoznaniu złoża węglowodorów i metanu występującego jako kopalina towarzysząca w złożach węgla kamiennego w kat. C błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "50%",
            "B": "30%",
            "C": "40%"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 7 ust. 2 pkt 1 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii C złóż węglowodorów błąd oszacowania parametrów nie przekracza 50%."
    },
    {
        "id": 39,
        "pytanie": "Przy rozpoznaniu złoża węglowodorów i metanu występującego jako kopalina towarzysząca w złożach węgla kamiennego w kat. B błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "50%",
            "B": "35%",
            "C": "40%"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 7 ust. 2 pkt 2 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii B błąd oszacowania nie może przekraczać 35%."
    },
    {
        "id": 40,
        "pytanie": "Przy rozpoznaniu złoża węglowodorów i metanu występującego jako kopalina towarzysząca w złożach węgla kamiennego w kat. A błąd oszacowania średnich wartości parametrów złoża i zasobów nie może przekraczać:",
        "odpowiedzi": {
            "A": "20%",
            "B": "30%",
            "C": "40%"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 7 ust. 2 pkt 3 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dla kategorii A błąd oszacowania nie może przekraczać 20%."
    },
    {
        "id": 41,
        "pytanie": "W jakiej co najmniej kategorii należy rozpoznać złoże kopaliny stałej aby rozpoznanie było wystarczające do opracowania projektu zagospodarowania złoża:",
        "odpowiedzi": {
            "A": "D",
            "B": "C1",
            "C": "C2"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 6 ust. 2 pkt 3 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Podstawę do sporządzenia projektu zagospodarowania złoża stanowi rozpoznanie złoża w kategorii co najmniej C1."
    },
    {
        "id": 42,
        "pytanie": "Załączniki w części tekstowej dokumentacji geologicznej złoża kopaliny dla kopalin objętych własnością górniczą obejmują m.in.:",
        "odpowiedzi": {
            "A": "wyniki badań specjalistycznych, w przypadku badań geofizycznych w formie informatycznych nośników danych...",
            "B": "dowód istnienia prawa do wykorzystania informacji geologicznej...",
            "C": "przedstawienie wykonanych badań statystycznych lub geostatycznych i ich wyników"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 4 ust. 2 pkt 4 Rozporządzenia Ministra Środowiska w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "W części tekstowej dokumentacji załącza się dowód prawa do informacji geologicznej oraz wyniki badań specjalistycznych i geofizycznych na nośnikach danych."
    },
    {
        "id": 43,
        "pytanie": "W dokumentacji geologicznej złoża kopaliny granice geologiczne złoża kopaliny wyznacza się przez stosowanie:",
        "odpowiedzi": {
            "A": "granicznych wartości parametrów definiujących złoże;",
            "B": "kryteriów bilansowości",
            "C": "parametrów ekonomicznych"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 5 ust. 4 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Granice złoża wyznacza się przy zastosowaniu granicznych wartości parametrów definiujących złoże."
    },
    {
        "id": 44,
        "pytanie": "W dodatku do dokumentacji geologicznej eksploatowanego złoża kopaliny stałej, poza wynikami prac geologicznych wykonanych w celu udokumentowania złoża, uwzględnia się dane zawarte w:",
        "odpowiedzi": {
            "A": "dokumentacji mierniczo - geologicznej zakładu górniczego;",
            "B": "wyniki bieżącego opróbowania złoża kopaliny;",
            "C": "wyniki badań specjalistycznych, w tym zwłaszcza hydrogeologicznych, geologiczno-inżynierskich, gazowych, geotermicznych oraz pozostałe informacje niezbędne do planowania wykorzystania terenu po zakończeniu działalności górniczej i jego rekultywacji;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 8 ust. 1 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dodatek do dokumentacji geologicznej uwzględnia dane z dokumentacji mierniczo-geologicznej, wyników bieżącego opróbowania oraz badań specjalistycznych niezbędnych do rekultywacji."
    },
    {
        "id": 45,
        "pytanie": "Dokumentacja geologiczna złóż kopalin, dla których organem koncesyjnym jest starosta składa się m.in. z:",
        "odpowiedzi": {
            "A": "części tekstowej",
            "B": "części graficznej,",
            "C": "zestawienia współrzędnych płaskich prostokątnych w państwowym systemie odniesień przestrzennych: a)punktów załamania granic obszaru dokumentowanego, b)wykonanych otworów wiertniczych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 9 ust. 1, 2, 4 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Dokumentacja geologiczna złoża składa się z części tekstowej, graficznej oraz zestawienia współrzędnych punktów załamania granic i otworów wiertniczych."
    },
    {
        "id": 46,
        "pytanie": "Część graficzną dokumentacji geologicznej złoża kopaliny objętej własnością górniczą stanowią mapy i przekroje geologiczne:",
        "odpowiedzi": {
            "A": "mapa lokalizacji złoża kopaliny sporządzona na mapie topograficznej w zależności od wielkości złoża w skali od 1:10 000 do 1:50 000;",
            "B": "mapa sytuacyjno-wysokościowa pozyskana z państwowego zasobu geodezyjnego i kartograficznego w skali umożliwiającej szczegółowe przedstawienie dokumentowanego obszaru...;",
            "C": "mapa geologiczno-gospodarcza lub mapa geośrodowiskowa rejonu występowaia złoża kopaliny..."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 4 ust. 1 i 2 Rozporządzenia MŚ w sprawie dokumentacji geologicznej złoża kopaliny",
        "tresc_artykulu": "Część graficzną stanowi mapa sytuacyjno-wysokościowa sporządzona w skali umożliwiającej odwzorowanie budowy złoża."
    },
    {
        "id": 47,
        "pytanie": "Operat ewidencyjny zawiera:",
        "odpowiedzi": {
            "A": "część tekstową,",
            "B": "część tabelaryczną,",
            "C": "część graficzną."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 2 ust. 1 pkt 1, 2, 3 Rozporządzenia MŚ z dnia 15 listopada 2011 r. w sprawie operatu ewidencyjnego",
        "tresc_artykulu": "Operat ewidencyjny składa się z części tekstowej, części tabelarycznej oraz części graficznej."
    },
    {
        "id": 48,
        "pytanie": "Operat ewidencyjny zawiera:",
        "odpowiedzi": {
            "A": "część tekstową, w tym uzasadnienie powstałych zmian w zasobach złoża,",
            "B": "kopię mapy obliczenia zasobów złoża kopaliny,",
            "C": "zestawienie przyrostów i ubytków zasobów"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 2 ust. 1, 2, 3 Rozporządzenia MŚ w sprawie operatu ewidencyjnego",
        "tresc_artykulu": "Operat ewidencyjny zawiera uzasadnienie zmian zasobów, kopię mapy obliczenia zasobów oraz zestawienie przyrostów i ubytków zasobów."
    },
    {
        "id": 49,
        "pytanie": "Operat ewidencyjny zawiera:",
        "odpowiedzi": {
            "A": "zestawienie zasobów przemysłowych i nieprzemysłowych,",
            "B": "zestawienie zasobów bilansowych i pozabilansowych",
            "C": "zestawienie zasobów operatywnych."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 2 ust. 1 p. 2a Rozporządzenia MŚ w sprawie operatu ewidencyjnego",
        "tresc_artykulu": "W części tabelarycznej operatu ujmuje się zestawienie zasobów bilansowych i pozabilansowych złoża."
    },
    {
        "id": 50,
        "pytanie": "Operat ewidencyjny zawiera:",
        "odpowiedzi": {
            "A": "tabele obliczenia zasobów złoża kopaliny oraz zmian w tych zasobach,",
            "B": "kopię mapy sytuacyjno-wysokościowej,",
            "C": "zestawienie przyrostów i ubytków zasobów"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 2 ust. 1 p. 2b, Art. 2 ust. 1 p. 2c Rozporządzenia MŚ w sprawie operatu ewidencyjnego",
        "tresc_artykulu": "Operat zawiera tabele obliczeń zasobów i zmian w zasobach oraz zestawienie przyrostów i ubytków."
    },
    {
        "id": 51,
        "pytanie": "W projekcie zagospodarowania złoża należy określić:",
        "odpowiedzi": {
            "A": "zasoby przemysłowe będące częścią zasobów bilansowych złoża;",
            "B": "zasoby nieprzemysłowe będące częścią zasobów bilansowych złoża zaliczoną do zasobów niezaliczoną do zasobów przemysłowych w obszarze przewidzianym do zagospodarowania...",
            "C": "straty w zasobach przemysłowych i nieprzemysłowych, będące ich częścią przewidzianą do pozostawienia w złożu..."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 1 ust. 2 pkt 1, 2, 3 Rozporządzenia MŚ z dnia 24 kwietnia 2012 r. w sprawie PZZ",
        "tresc_artykulu": "W projekcie zagospodarowania złoża określa się zasoby przemysłowe, nieprzemysłowe oraz straty w tych zasobach."
    },
    {
        "id": 52,
        "pytanie": "W projekcie zagospodarowania złoża należy określić:",
        "odpowiedzi": {
            "A": "zasoby przemysłowe będące częścią zasobów bilansowych złoża;",
            "B": "zasoby nieprzemysłowe będące częścią zasobów bilansowych złoża zaliczoną do zasobów niezaliczoną do zasobów przemysłowych w obszarze przewidzianym do zagospodarowania...",
            "C": "zasoby operatywne dla złóż kopalin stałych."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 1 ust. 2 pkt 1, 2, 4 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "PZZ określa zasoby przemysłowe, nieprzemysłowe oraz zasoby operatywne dla złóż kopalin stałych."
    },
    {
        "id": 53,
        "pytanie": "Część opisowa projektu zagospodarowania złoża powinna zawierać:",
        "odpowiedzi": {
            "A": "charakterystykę warunków ekonomicznych prowadzenia eksploatacji i wykorzystania złoża,",
            "B": "przedstawienie zagrożeń mogących wpłynąć na bezpieczeństwo eksploatacji i ochronę zasobów oraz sposób przeciwdziałania tym zagrożeniom,",
            "C": "stan prawny nieruchomości gruntowej, w granicach której ma być wykonywana działalność;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 2 ust. 2 pkt 3, 5 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Część opisowa PZZ zawiera charakterystykę warunków ekonomicznych oraz zagrożeń dla bezpieczeństwa ruchu i ochrony zasobów."
    },
    {
        "id": 54,
        "pytanie": "W projekcie zagospodarowania złoża należy określić:",
        "odpowiedzi": {
            "A": "zasoby przemysłowe będące częścią zasobów bilansowych złoża;",
            "B": "zasoby operatywne dla złóż kopalin stałych,",
            "C": "straty w zasobach przemysłowych i nieprzemysłowych."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 1 ust. 2 pkt 1, 3, 4 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Projekt zagospodarowania złoża zawiera podział na zasoby przemysłowe, operatywne oraz wyliczenie strat."
    },
    {
        "id": 55,
        "pytanie": "Część opisowa projektu zagospodarowania złoża powinna zawierać:",
        "odpowiedzi": {
            "A": "określenie granic projektowanego obszaru i terenu górniczego,",
            "B": "przedstawienie przewidywanej wielkości wydobycia,",
            "C": "stan prawny nieruchomości gruntowej w granicach której ma być wykonywana działalność."
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 2 ust. 2 pkt 6 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Część opisowa określa granice obszaru i terenu górniczego oraz przewidywaną wielkość wydobycia."
    },
    {
        "id": 56,
        "pytanie": "Część opisowa projektu zagospodarowania złoża powinna zawierać:",
        "odpowiedzi": {
            "A": "określenie granic projektowanego obszaru i terenu górniczego,",
            "B": "uzasadnienie granic zamierzonej eksploatacji,",
            "C": "projektowane granice filarów ochronnych wraz z określeniem warunków ich ewentualnej eksploatacji."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 2 ust. 2 pkt 2, 3 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "W części opisowej PZZ wskazuje się granice terenu górniczego, filary ochronne oraz uzasadnienie granic eksploatacji."
    },
    {
        "id": 57,
        "pytanie": "Część opisowa projektu zagospodarowania złoża powinna zawierać:",
        "odpowiedzi": {
            "A": "przedstawienie przewidywanej wielkości wydobycia,",
            "B": "kryteria klasyfikacji zasobów do przemysłowych lub nieprzemysłowych,",
            "C": "szczegółowe zasady, sposób i zakres ochrony zasobów nieprzemysłowych."
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 2 ust. 2 pkt 6, 8, 11 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Część opisowa zawiera informacje o wielkości wydobycia, kryteria klasyfikacji zasobów oraz zasady ochrony zasobów nieprzemysłowych."
    },
    {
        "id": 58,
        "pytanie": "Część graficzna projektu zagospodarowania złoża, stosownie do zamierzonego sposobu eksploatacji i rodzaju kopaliny powinna zawierać:",
        "odpowiedzi": {
            "A": "mapę sytuacyjno - wysokościową sporządzoną w skali umożliwiającej szczegółowe przedstawienie obszaru przewidzianego do zagospodarowania,",
            "B": "mapę sytuacyjno - wysokościową powierzchni z oznaczeniem przewidywanych zmian powstałych na skutek eksploatacji,",
            "C": "mapy rozmieszczenia zasobów zakwalifikowanych do przemysłowych, nieprzemysłowych oraz strat z wiązanych z wcześniejszą eksploatacją;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 2 ust. 3 pkt 1, 2, 3 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Część graficzna PZZ obejmuje mapy sytuacyjno-wysokościowe z uwzględnieniem granic zagospodarowania, osiadania i rozmieszczenia zasobów."
    },
    {
        "id": 59,
        "pytanie": "Część graficzna projektu zagospodarowania złoża stosownie do zamierzonego sposobu eksploatacji i rodzaju kopaliny powinna zawierać:",
        "odpowiedzi": {
            "A": "mapę sytuacyjno – wysokościową sporządzoną w skali umożliwiającej szczegółowe przedstawienie obszaru przewidzianego do zagospodarowania,",
            "B": "kopię decyzji o środowiskowych uwarunkowaniach,",
            "C": "przekroje geologiczno – górnicze;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 2 ust. 3 pkt 1, 4 Rozporządzenia MŚ w sprawie PZZ",
        "tresc_artykulu": "Część graficzna PZZ składa się z właściwych map sytuacyjno-wysokościowych oraz przekrojów geologiczno-górniczych."
    },
    {
        "id": 60,
        "pytanie": "Do części tekstowej dokumentacji sporządzanej przypadku wykonywania prac geologicznych niekończących się udokumentowaniem zasobów złoża kopaliny dołącza się:",
        "odpowiedzi": {
            "A": "Kopię decyzji zatwierdzającej projekt robót geologicznych lub kopie decyzji o udzieleniu koncesji;",
            "B": "Wyniki badań w formie zbioru danych na informatycznych nośnikach danych;",
            "C": "Rozliczenie finansowe między inwestorem a wykonawcą prac geologicznych;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 4 ust. 3 Rozporządzenia MŚ w sprawie innej dokumentacji geologicznej",
        "tresc_artykulu": "Do dokumentacji prac niekończących się dokumentacją zasobową dołącza się kopię decyzji zatwierdzającej PRG/koncesję oraz wyniki badań na nośnikach elektronicznych."
    },
    {
        "id": 61,
        "pytanie": "Do części tekstowej dokumentacji sporządzanej przypadku wykonywania otworu wiertniczego w celu rozpoznania budowy głębokiego podłoża dołącza się:",
        "odpowiedzi": {
            "A": "Kopię decyzji zatwierdzającej projekt robót geologicznych;",
            "B": "Wyniki badań w formie zbioru danych na informatycznych nośnikach danych;",
            "C": "Tabelaryczne zestawienie wypadków i awarii, jakie miały miejsce podczas wiercenia otworu;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 5 ust. 3, 4 Rozporządzenia MŚ w sprawie innej dokumentacji geologicznej",
        "tresc_artykulu": "W dokumentacji otworu wiertniczego rozpoznania głębokiego podłoża zamieszcza się kopię decyzji zatwierdzającej PRG oraz cyfrowe wyniki badań."
    },
    {
        "id": 62,
        "pytanie": "Część tekstowa dokumentacji sporządzanej w przypadku wykonywania prac geologicznych w celu wykorzystania ciepła Ziemi obejmuje m.in.:",
        "odpowiedzi": {
            "A": "Opis profilu geologicznego wraz z charakterystyką przewiercanych warstw wodonośnych i temperatury na dnie otworu wiertniczego;",
            "B": "Charakterystyki rozwiązań technicznych, w tym określenia ilości, głębokości i średnicy otworów wiertniczych;",
            "C": "Obliczonej mocy instalacji wyrażonej w A/m²"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 5 ust. 1 pkt 1, 2 Rozporządzenia MŚ w sprawie innej dokumentacji geologicznej",
        "tresc_artykulu": "Część tekstowa dokumentacji ciepła ziemi zawiera profil geologiczny, dane o hydrogeologii oraz opis parametrów technicznych otworów."
    },
    {
        "id": 63,
        "pytanie": "Część tekstowa dokumentacji sporządzanej w przypadku likwidacji otworu wiertniczego obejmuje m.in.:",
        "odpowiedzi": {
            "A": "Określenie przyczyn likwidacji otworu wiertniczego;",
            "B": "Określenie daty rozpoczęcia i zakończenia prac likwidacyjnych;",
            "C": "Fotografie terenu sprzed rozpoczęcia likwidacji otworu;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 7 ust. 1 pkt 1, 4 Rozporządzenia MŚ w sprawie innej dokumentacji geologicznej",
        "tresc_artykulu": "Dokumentacja likwidacji otworu wiertniczego podaje przyczyny likwidacji oraz faktyczny czas trwania prac."
    },
    {
        "id": 64,
        "pytanie": "Wskaż komu przekazuje się mapę obszaru górniczego wraz z adnotacją o wpisie tego obszaru do rejestru:",
        "odpowiedzi": {
            "A": "przedsiębiorcy, właściwemu miejscowo organowi koncesyjnemu, organowi nadzoru górniczego oraz wójtowi (burmistrzowi, prezydentowi miasta);",
            "B": "Prezesowi Wyższego Urzędu Górniczego, wojewodzie, staroście;",
            "C": "Ministrowi Gospodarki, Ministrowi właściwemu do spraw gospodarki morskiej (...) oraz Narodowemu Funduszowi Ochrony Środowiska i Gospodarki Wodnej..."
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 167 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Mapę obszaru górniczego z adnotacją o wpisie przekazuje się przedsiębiorcy, organowi koncesyjnemu, organowi nadzoru górniczego oraz wójtowi (burmistrzowi, prezydentowi)."
    },
    {
        "id": 65,
        "pytanie": "W jakim terminie prowadzący rejestr obszarów górniczych przekazuje przedsiębiorcy mapę obszaru górniczego wraz z adnotacją o wpisie tego obszaru do rejestru:",
        "odpowiedzi": {
            "A": "14 dni od otrzymania od organu koncesyjnego;",
            "B": "60 dni od uprawomocnienia się decyzji koncesyjnej;",
            "C": "1 miesiąca od zatwierdzenia dokumentacji geologicznej złoża kopaliny;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 167 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prowadzący rejestr przekazuje mapę z adnotacją w terminie 14 dni od dnia otrzymania zawiadomienia od organu koncesyjnego."
    },
    {
        "id": 66,
        "pytanie": "Projekt robót geologicznych składa się z:",
        "odpowiedzi": {
            "A": "Jednej części – opisowej;",
            "B": "Dwóch części: opisowej i graficznej;",
            "C": "Trzech części: opisowej, graficznej oraz wykazu osób, które będą prowadziły prace geologiczne;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 1 ust. 1 Rozporządzenia MŚ z dnia 20 grudnia 2011 r. w sprawie PRG",
        "tresc_artykulu": "Projekt robót geologicznych składa się z części opisowej oraz części graficznej."
    },
    {
        "id": 67,
        "pytanie": "Prawidłowo sporządzony projekt robót geologicznych powinien być podpisany:",
        "odpowiedzi": {
            "A": "Przez przedsiębiorcę, zgodnie z zasadami reprezentacji w KRS;",
            "B": "Przez osobę posiadającą stwierdzone odpowiednie kwalifikacje do wykonywania, dozorowania i kierowania pracami geologicznymi;",
            "C": "Przez osobę świadczącą usługi transgraniczne w zakresie projektowania prac geologicznych;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 86 Ustawy Prawo geologiczne i górnicze (oraz Rozporządzenie PRG)",
        "tresc_artykulu": "Projekt robót geologicznych podpisuje osoba posiadająca stwierdzone odpowiednie kwalifikacje geologiczne."
    },
    {
        "id": 68,
        "pytanie": "Kiedy projekt prac geologicznych powinien zawierać opis przedsięwzięć technicznych, technologicznych i organizacyjnych, mających na celu zapewnienie bezpieczeństwa powszechnego?",
        "odpowiedzi": {
            "A": "Wówczas, gdy projektowane są roboty geologiczne, do których nie stosuje się przepisów w sprawie planu ruchu zakładu górniczego;",
            "B": "Nigdy;",
            "C": "Zawsze;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 79 ust. 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opis przedsięwzięć zapewniających bezpieczeństwo powszechne zamieszcza się, gdy do robót geologicznych nie stosuje się przepisów o ruchu zakładu górniczego."
    },
    {
        "id": 69,
        "pytanie": "W przypadku, gdy projekt robót geologicznych wymaga prowadzenia prac w etapach, wówczas w projekcie:",
        "odpowiedzi": {
            "A": "Szczegółowo określa się rodzaje, zakres i harmonogram robót geologicznych oraz ich lokalizację dla wszystkich etapów prac;",
            "B": "Szczegółowo określa się rodzaje, zakres i harmonogram robót geologicznych oraz ich lokalizację dla etapu pierwszego oraz wstępnie dla kolejnych etapów;",
            "C": "Stopień szczegółowości opisu poszczególnych etapów zależy wyłącznie od koncepcji osoby sporządzającej projekt;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 3 ust. 4 Rozporządzenia MŚ w sprawie PRG",
        "tresc_artykulu": "W przypadku etapowania prac w projekcie określa się szczegółowo dane dla pierwszego etapu, a dla kolejnych - dane wstępne."
    },
    {
        "id": 70,
        "pytanie": "Część tekstowa projektu robót geologicznych powinna zawierać:",
        "odpowiedzi": {
            "A": "Omówienie wyników przeprowadzonych wcześniej robót geologicznych i badań geofizycznych;",
            "B": "Charakterystykę i uzasadnienie zakresu oraz metod zamierzonych badań geofizycznych i geochemicznych oraz ich lokalizacji;",
            "C": "Mapę geologiczno – inżynierską w skali, co najmniej 1:100 000;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 1 ust. 2 pkt 2, 4 Rozporządzenia MŚ w sprawie PRG",
        "tresc_artykulu": "Tekst projektu zawiera omówienie dotychczasowych prac oraz charakterystykę i uzasadnienie zamierzonych metod badań."
    },
    {
        "id": 71,
        "pytanie": "Co powinien zawierać projekt robót geologicznych sporządzony po drugim z planowanych etapów prowadzenia prac geologicznych?",
        "odpowiedzi": {
            "A": "Wyłącznie rodzaje, zakres i harmonogram robót geologicznych oraz ich lokalizację dla następnego etapu prac;",
            "B": "Podsumowanie wyników robót geologicznych uzyskanych w poprzednim etapie;",
            "C": "Szczegółowe określenie rodzaju, zakresu i harmonogramu robót geologicznych, które mają być prowadzone w kolejnym etapie;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 3 ust. 3 Rozporządzenia MŚ w sprawie PRG",
        "tresc_artykulu": "Projekt robót dla kolejnego etapu zawiera podsumowanie wyników z etapów poprzednich oraz szczegółowy zakres prac dla etapu nowego."
    },
    {
        "id": 72,
        "pytanie": "Część tekstowa projektu robót geologicznych zawiera:",
        "odpowiedzi": {
            "A": "Informację dotyczące lokalizacji zamierzonych robót geologicznych, w tym lokalizacji w ramach trójstopniowego podziału terytorialnego państwa;",
            "B": "Graniczne wartości parametrów definiujących złoże i jego granice;",
            "C": "Opis i uzasadnienie liczby, lokalizacji i rodzaju projektowanych wyrobisk;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 1 ust. 2 pkt 1, 4 Rozporządzenia MŚ w sprawie PRG",
        "tresc_artykulu": "Część tekstowa PRG wskazuje lokalizację administracyjną zamierzonych prac oraz uzasadnienie liczby i typu projektowanych wyrobisk."
    }
]

#Restar aplikacji mobilnych 
if 'wybrana_baza' not in st.session_state:
    st.session_state.wybrana_baza = None
if 'aktywny_tryb' not in st.session_state:
    st.session_state.aktywny_tryb = None
if 'pytania_sesji' not in st.session_state:
    st.session_state.pytania_sesji = []
if 'indeks' not in st.session_state:
    st.session_state.indeks = 0
if 'sprawdzono_odpowiedz' not in st.session_state:
    st.session_state.sprawdzono_odpowiedz = False
if 'odpowiedzi_egzamin' not in st.session_state:
    st.session_state.odpowiedzi_egzamin = {}

# Konfiguracja układu strony
st.set_page_config(
    page_title="Aplikacja Testowa - Prawo Geologiczne i Górnicze",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stylizacja CSS (sidebar, formularze, równe kafelki i poprawiony żółty kolor)
if st.session_state.theme == "Jasny":
    st.markdown("""
    <style>
        .stApp { background-color: #f8f9fa; color: #212529; }
        
        section[data-testid="stSidebar"] { background-color: #f1f3f5 !important; }
        section[data-testid="stSidebar"] * { color: #212529 !important; }

        input, textarea, select, div[role="combobox"], div[data-baseweb="select"] {
            background-color: #ffffff !important;
            color: #212529 !important;
            border: 1px solid #ced4da !important;
        }
        div[data-baseweb="select"] * {
            background-color: #ffffff !important;
            color: #212529 !important;
        }
        
        .stButton>button, .stFormSubmitButton>button {
            background-color: #e9ecef !important;
            color: #212529 !important;
            border: 1px solid #ced4da !important;
            width: 100% !important;
        }
        .stButton>button:hover, .stFormSubmitButton>button:hover {
            background-color: #dee2e6 !important;
            border-color: #adb5bd !important;
        }

        label, .stRadio p, .stCheckbox p, p { color: #212529 !important; }

        .main-header { font-size: 22px; font-weight: bold; color: #0d6efd; border-bottom: 2px solid #dee2e6; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ced4da; margin-bottom: 15px; color: #212529; }
        .legal-box { background-color: #e7f1ff; padding: 15px; border-radius: 6px; border: 1px solid #b6d4fe; margin-top: 15px; margin-bottom: 15px; color: #084298; }

        /* Równe kafelki na stronie głównej - jasny motyw */
        .card-blue, .card-yellow, .card-green, .card-red {
            padding: 20px;
            border-radius: 8px;
            height: 220px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            margin-bottom: 20px;
            box-sizing: border-box;
        }
        .card-blue { background-color: #cfe2ff; color: #084298; border: 1px solid #b6d4fe; }
        .card-yellow { background-color: #ffe5d0; color: #7c2d12; border: 1px solid #ffbb99; }
        .card-green { background-color: #d1e7dd; color: #0f5132; border: 1px solid #badbcc; }
        .card-red { background-color: #f8d7da; color: #842029; border: 1px solid #f5c2c7; }
    </style>
    """, unsafe_allow_html=True)
elif st.session_state.theme in ["Cciemny", "Ciemny"]:
    st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        
        section[data-testid="stSidebar"] { background-color: #161b22 !important; }
        section[data-testid="stSidebar"] * { color: #ffffff !important; }

        input, textarea, select, div[role="combobox"], div[data-baseweb="select"] {
            background-color: #21262d !important;
            color: #ffffff !important;
            border: 1px solid #30363d !important;
        }
        div[data-baseweb="select"] * {
            background-color: #21262d !important;
            color: #ffffff !important;
        }

        .stButton>button, .stFormSubmitButton>button {
            width: 100% !important;
        }

        label, .stRadio p, .stCheckbox p, p { color: #ffffff !important; }

        .main-header { font-size: 22px; font-weight: bold; color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #161b22; padding: 15px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; color: #ffffff; }
        .legal-box { background-color: #0d1117; padding: 15px; border-radius: 6px; border: 1px solid #238636; margin-top: 15px; margin-bottom: 15px; color: #e6edf3; }

        /* Równe kafelki na stronie głównej - ciemny motyw */
        .card-blue, .card-yellow, .card-green, .card-red {
            padding: 20px;
            border-radius: 8px;
            height: 220px;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            margin-bottom: 20px;
            box-sizing: border-box;
        }
        .card-blue { background-color: #1f364d; color: #58a6ff; border: 1px solid #30363d; }
        .card-yellow { background-color: #452800; color: #ffbc54; border: 1px solid #633800; }
        .card-green { background-color: #1b3a2b; color: #3fb950; border: 1px solid #238636; }
        .card-red { background-color: #421e22; color: #f85149; border: 1px solid #da3633; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        @media (prefers-color-scheme: dark) {
            .stApp { background-color: #0e1117; color: #ffffff; }
            section[data-testid="stSidebar"] { background-color: #161b22 !important; }
            section[data-testid="stSidebar"] * { color: #ffffff !important; }
            input, textarea, select, div[role="combobox"], div[data-baseweb="select"] { background-color: #21262d !important; color: #ffffff !important; border: 1px solid #30363d !important; }
            div[data-baseweb="select"] * { background-color: #21262d !important; color: #ffffff !important; }
            .stButton>button, .stFormSubmitButton>button { width: 100% !important; }
            label, .stRadio p, .stCheckbox p, p { color: #ffffff !important; }
            .main-header { font-size: 22px; font-weight: bold; color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 5px; margin-bottom: 15px; }
            .question-box { background-color: #161b22; padding: 15px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; color: #ffffff; }
            .legal-box { background-color: #0d1117; padding: 15px; border-radius: 6px; border: 1px solid #238636; margin-top: 15px; margin-bottom: 15px; color: #e6edf3; }
            .card-blue { background-color: #1f364d; color: #58a6ff; border: 1px solid #30363d; }
            .card-yellow { background-color: #452800; color: #ffbc54; border: 1px solid #633800; }
            .card-green { background-color: #1b3a2b; color: #3fb950; border: 1px solid #238636; }
            .card-red { background-color: #421e22; color: #f85149; border: 1px solid #da3633; }
            .card-blue, .card-yellow, .card-green, .card-red { padding: 20px; border-radius: 8px; height: 220px; display: flex; flex-direction: column; justify-content: flex-start; margin-bottom: 20px; box-sizing: border-box; }
        }
        @media (prefers-color-scheme: light) {
            .stApp { background-color: #f8f9fa; color: #212529; }
            section[data-testid="stSidebar"] { background-color: #f1f3f5 !important; }
            section[data-testid="stSidebar"] * { color: #212529 !important; }
            input, textarea, select, div[role="combobox"], div[data-baseweb="select"] { background-color: #ffffff !important; color: #212529 !important; border: 1px solid #ced4da !important; }
            div[data-baseweb="select"] * { background-color: #ffffff !important; color: #212529 !important; }
            .stButton>button, .stFormSubmitButton>button { background-color: #e9ecef !important; color: #212529 !important; border: 1px solid #ced4da !important; width: 100% !important; }
            label, .stRadio p, .stCheckbox p, p { color: #212529 !important; }
            .main-header { font-size: 22px; font-weight: bold; color: #0d6efd; border-bottom: 2px solid #dee2e6; padding-bottom: 5px; margin-bottom: 15px; }
            .question-box { background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ced4da; margin-bottom: 15px; color: #212529; }
            .legal-box { background-color: #e7f1ff; padding: 15px; border-radius: 6px; border: 1px solid #b6d4fe; margin-top: 15px; margin-bottom: 15px; color: #084298; }
            .card-blue { background-color: #cfe2ff; color: #084298; border: 1px solid #b6d4fe; }
            .card-yellow { background-color: #ffe5d0; color: #7c2d12; border: 1px solid #ffbb99; }
            .card-green { background-color: #d1e7dd; color: #0f5132; border: 1px solid #badbcc; }
            .card-red { background-color: #f8d7da; color: #842029; border: 1px solid #f5c2c7; }
            .card-blue, .card-yellow, .card-green, .card-red { padding: 20px; border-radius: 8px; height: 220px; display: flex; flex-direction: column; justify-content: flex-start; margin-bottom: 20px; box-sizing: border-box; }
        }
    </style>
    """, unsafe_allow_html=True)

# Pomocnicze funkcje nawigacyjne
def start_sesji(tryb):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.odpowiedzi_egzamin = {}
    pula = list(st.session_state.bazy[st.session_state.wybrana_baza])
    if "Losow" in tryb or "Egzamin" in tryb:
        random.shuffle(pula)
    st.session_state.pytania_sesji = pula

def powrot_do_wyboru():
    st.session_state.wybrana_baza = None
    st.session_state.aktywny_tryb = None
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False

# ==============================================================================
# MENU GŁÓWNE W PASKU BOCZNYM
# ==============================================================================
st.sidebar.title("📌 Menu Główne")
menu_glowne = st.sidebar.radio(
    "Przejdź do:",
    [
        "🏠 Strona Główna", 
        "🎮 Testy i Nauka", 
        "➕ Dodaj Pytanie", 
        "🔍 Przegląd Bazy", 
        "🔑 Panel Administratora",
        "⚙️ Ustawienia / Motyw"
    ]
)

# ==============================================================================
# WIDOK: STRONA GŁÓWNA
# ==============================================================================
if menu_glowne == "🏠 Strona Główna":
    st.markdown("<div class='main-header'>Witaj w Aplikacji Testowej</div>", unsafe_allow_html=True)
    st.write("Wybierz odpowiednią sekcję z paska bocznego po lewej stronie, aby rozpocząć pracę z aplikacją.")
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card-blue">
            <h4 style="margin-top:0;">🎮 Rozwiązywanie Testów</h4>
            <p style="margin:0;">Wybierz część bazy, ustal tryb nauki lub spróbuj sił w symulacji egzaminu.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-green">
            <h4 style="margin-top:0;">🔍 Baza Pytań</h4>
            <p style="margin:0;">Przeglądaj pytania razem z przypisanymi podstawami prawnymi oraz tekstami artykułów.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-yellow">
            <h4 style="margin-top:0;">➕ Dodawanie Pytań</h4>
            <p style="margin:0;">Rozszerzaj bazę testową o własne pytania i odpowiedzi.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-red">
            <h4 style="margin-top:0;">🔑 Tryb Administratora</h4>
            <p style="margin:0;">Pozwala edytować oraz usuwać dowolne pytania w bazie po podaniu hasła.</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# WIDOK: TESTY I NAUKA
# ==============================================================================
elif menu_glowne == "🎮 Testy i Nauka":
    if st.session_state.wybrana_baza is None:
        st.markdown("<div class='main-header'>Wybierz część bazy pytań</div>", unsafe_allow_html=True)
        for nazwa_bazy in st.session_state.bazy.keys():
            if st.button(f"📁 {nazwa_bazy}", use_container_width=True):
                st.session_state.wybrana_baza = nazwa_bazy
                st.rerun()

    elif st.session_state.aktywny_tryb is None:
        baza_pytania = st.session_state.bazy[st.session_state.wybrana_baza]
        st.markdown(f"**Wybrana baza:** {st.session_state.wybrana_baza}")
        st.markdown(f"**Wybrana baza liczy: {len(baza_pytania)} pytań**")
        st.write("")

        if st.button("Tryb Nauki (Kolejno + Podpowiedzi)", use_container_width=True):
            start_sesji("Tryb Nauki (Kolejno + Podpowiedzi)")
            st.rerun()

        if st.button("Tryb Nauki (Losowa kolejność + Podpowiedzi)", use_container_width=True):
            start_sesji("Tryb Nauki (Losowa kolejność + Podpowiedzi)")
            st.rerun()

        if st.button("Tryb Egzaminu (Losowo, Wynik na końcu)", use_container_width=True):
            start_sesji("Tryb Egzaminu (Losowo, Wynik na końcu)")
            st.rerun()

        st.write("")
        if st.button("← Powrót do wyboru części", use_container_width=True):
            powrot_do_wyboru()
            st.rerun()

    else:
        st.markdown(f"<div class='main-header'>{st.session_state.aktywny_tryb} - {st.session_state.wybrana_baza}</div>", unsafe_allow_html=True)
        lista = st.session_state.pytania_sesji
        idx = st.session_state.indeks

        if st.button("← Zmień tryb / powrót"):
            st.session_state.aktywny_tryb = None
            st.rerun()

        st.markdown("---")

        if idx < len(lista):
            p = lista[idx]
            st.markdown(f"**Pytanie {idx + 1} z {len(lista)}** (ID: {p['id']})")
            st.markdown(f"<div class='question-box'><h3>{p['pytanie']}</h3></div>", unsafe_allow_html=True)

            if "Nauki" in st.session_state.aktywny_tryb:
                with st.form(key=f"form_nauka_{idx}"):
                    wybrane = []
                    for k, v in p["odpowiedzi"].items():
                        if st.checkbox(f"**{k}**: {v}", key=f"cb_nauka_{idx}_{k}"):
                            wybrane.append(k)
                    
                    sprawdz = st.form_submit_button("Sprawdź odpowiedź")

                if sprawdz:
                    st.session_state.sprawdzono_odpowiedz = True

                if st.session_state.sprawdzono_odpowiedz:
                    poprawne = set(p["poprawne"])
                    zaznaczone = set(wybrane)
                    
                    if zaznaczone == poprawne:
                        st.success("✅ Poprawna odpowiedź!")
                    else:
                        st.error(f"❌ Błąd! Poprawne odpowiedzi to: {', '.join(p['poprawne'])}")

                    podstawa = p.get("podstawa_prawna", "Brak zdefiniowanej podstawy prawnej")
                    artykul = p.get("tresc_artykulu", "Brak opisu treści artykułu")
                    
                    st.markdown(f"""
                    <div class='legal-box'>
                        <strong>📜 Podstawa prawna:</strong> {podstawa}<br><br>
                        <strong>📖 Treść artykułu:</strong><br>
                        <em>{artykul}</em>
                    </div>
                    """, unsafe_allow_html=True)

            else:
                poprzednie_wybory = st.session_state.odpowiedzi_egzamin.get(idx, [])
                wybrane = []
                for k, v in p["odpowiedzi"].items():
                    zaznaczone = k in poprzednie_wybory
                    if st.checkbox(f"**{k}**: {v}", value=zaznaczone, key=f"cb_egz_{idx}_{k}"):
                        wybrane.append(k)
                
                st.session_state.odpowiedzi_egzamin[idx] = wybrane

            col_p, col_n = st.columns([1, 1])
            with col_p:
                if st.button("⬅️ Poprzednie") and idx > 0:
                    st.session_state.indeks -= 1
                    st.session_state.sprawdzono_odpowiedz = False
                    st.rerun()
            with col_n:
                if idx < len(lista) - 1:
                    if st.button("Następne ➡️"):
                        st.session_state.indeks += 1
                        st.session_state.sprawdzono_odpowiedz = False
                        st.rerun()
                else:
                    if st.button("🏁 Zakończ Test"):
                        st.session_state.indeks += 1
                        st.rerun()

        else:
            st.balloons()
            st.success("🎉 Zakończyłeś test!")
            
            if "Egzamin" in st.session_state.aktywny_tryb:
                punkty = 0
                for i, q in enumerate(lista):
                    user_ans = set(st.session_state.odpowiedzi_egzamin.get(i, []))
                    correct_ans = set(q["poprawne"])
                    if user_ans == correct_ans:
                        punkty += 1

                st.markdown(f"### Twój Wynik Egzaminu: **{punkty} / {len(lista)}** ({(punkty/len(lista)*100):.1f}%)")

            if st.button("🔄 Rozpocznij ponownie"):
                start_sesji(st.session_state.aktywny_tryb)
                st.rerun()

# ==============================================================================
# WIDOK: DODAJ PYTANIE
# ==============================================================================
elif menu_glowne == "➕ Dodaj Pytanie":
    st.markdown("<div class='main-header'>Dodaj nowe pytanie do bazy</div>", unsafe_allow_html=True)
    baza_docelowa = st.selectbox("Wybierz bazę:", list(st.session_state.bazy.keys()))

    with st.form("form_dodaj"):
        tresc = st.text_area("Treść pytania:")
        ans_a = st.text_input("Odpowiedź A:")
        ans_b = st.text_input("Odpowiedź B:")
        ans_c = st.text_input("Odpowiedź C:")
        
        pop_a = st.checkbox("A jest poprawne")
        pop_b = st.checkbox("B jest poprawne")
        pop_c = st.checkbox("C jest poprawne")
        
        podstawa = st.text_input("Podstawa prawna (opcjonalnie):")
        artykul = st.text_area("Treść artykułu (opcjonalnie):")
        
        if st.form_submit_button("Zapisz pytanie"):
            poprawne_list = []
            if pop_a: poprawne_list.append("A")
            if pop_b: poprawne_list.append("B")
            if pop_c: poprawne_list.append("C")

            if tresc and ans_a and ans_b and ans_c and poprawne_list:
                nowe_id = max([p["id"] for p in st.session_state.bazy[baza_docelowa]], default=0) + 1
                nowe_pytanie = {
                    "id": nowe_id,
                    "pytanie": tresc,
                    "odpowiedzi": {"A": ans_a, "B": ans_b, "C": ans_c},
                    "poprawne": poprawne_list,
                }
                if podstawa: nowe_pytanie["podstawa_prawna"] = podstawa
                if artykul: nowe_pytanie["tresc_artykulu"] = artykul

                st.session_state.bazy[baza_docelowa].append(nowe_pytanie)
                st.success(f"Dodano pytanie o ID {nowe_id}!")
            else:
                st.error("Uzupełnij pola i wybierz co najmniej jedną poprawną odpowiedź!")

# ==============================================================================
# WIDOK: PRZEGLĄD BAZY
# ==============================================================================
elif menu_glowne == "🔍 Przegląd Bazy":
    st.markdown("<div class='main-header'>Przegląd Bazy Pytań</div>", unsafe_allow_html=True)
    wybrana = st.selectbox("Wybierz część:", list(st.session_state.bazy.keys()))
    
    for item in st.session_state.bazy[wybrana]:
        with st.expander(f"ID {item['id']}: {item['pytanie'][:80]}..."):
            st.write(f"**Pytanie:** {item['pytanie']}")
            for k, v in item["odpowiedzi"].items():
                is_correct = "✅" if k in item["poprawne"] else "❌"
                st.write(f"{is_correct} **{k}**: {v}")
            if "podstawa_prawna" in item:
                st.caption(f"Podstawa: {item['podstawa_prawna']}")
            if "tresc_artykulu" in item:
                st.info(f"Artykuł: {item['tresc_artykulu']}")

# ==============================================================================
# WIDOK: PANEL ADMINISTRATORA
# ==============================================================================
elif menu_glowne == "🔑 Panel Administratora":
    st.markdown("<div class='main-header'>🔑 Panel Administratora</div>", unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        with st.form("admin_login_form"):
            pass_input = st.text_input("Podaj hasło administratora:", type="password")
            btn_login = st.form_submit_button("Zaloguj się")
            if btn_login:
                if pass_input == ADMIN_PASSWORD:
                    st.session_state.admin_logged_in = True
                    st.success("Pomyślnie zalogowano do Panelu Administratora!")
                    st.rerun()
                else:
                    st.error("Niepoprawne hasło!")
    else:
        if st.button("🔒 Wyloguj z Panelu Admina"):
            st.session_state.admin_logged_in = False
            st.rerun()

        st.markdown("---")
        st.subheader("Edycja oraz zarządzanie pytaniami w bazie")

        wybrana_baza_admin = st.selectbox("Wybierz część bazy do edycji:", list(st.session_state.bazy.keys()), key="admin_baza_select")
        lista_pytan = st.session_state.bazy[wybrana_baza_admin]

        if not lista_pytan:
            st.warning("Wybrana baza nie posiada żadnych pytań.")
        else:
            opcje_pytan = [f"ID {p['id']}: {p['pytanie'][:60]}..." for p in lista_pytan]
            wybrane_pytanie_str = st.selectbox("Wybierz pytanie do edycji/usunięcia:", opcje_pytan)
            
            pytanie_idx = opcje_pytan.index(wybrane_pytanie_str)
            p = lista_pytan[pytanie_idx]

            col_del, col_edit = st.columns([1, 4])
            
            with col_del:
                st.write("**Usuwanie**")
                if st.button("🗑️ Usuń pytanie", type="primary"):
                    st.session_state.bazy[wybrana_baza_admin].pop(pytanie_idx)
                    st.success("Pytanie zostało pomyślnie usunięte z bazy!")
                    st.rerun()

            st.markdown("---")
            st.write("### Formularz edycji pytania")

            with st.form(key=f"edit_form_{p['id']}"):
                nowa_tresc = st.text_area("Treść pytania:", value=p["pytanie"])
                
                ans_a = st.text_input("Odpowiedź A:", value=p["odpowiedzi"].get("A", ""))
                ans_b = st.text_input("Odpowiedź B:", value=p["odpowiedzi"].get("B", ""))
                ans_c = st.text_input("Odpowiedź C:", value=p["odpowiedzi"].get("C", ""))

                pop_a = st.checkbox("Odpowiedź A jest poprawne", value=("A" in p["poprawne"]))
                pop_b = st.checkbox("Odpowiedź B jest poprawne", value=("B" in p["poprawne"]))
                pop_c = st.checkbox("Odpowiedź C jest poprawne", value=("C" in p["poprawne"]))

                podstawa = st.text_input("Podstawa prawna:", value=p.get("podstawa_prawna", ""))
                artykul = st.text_area("Treść artykułu:", value=p.get("tresc_artykulu", ""))

                if st.form_submit_button("💾 Zapisz zmiany w pytaniu"):
                    nowe_poprawne = []
                    if pop_a: nowe_poprawne.append("A")
                    if pop_b: nowe_poprawne.append("B")
                    if pop_c: nowe_poprawne.append("C")

                    if nowa_tresc and ans_a and ans_b and ans_c and nowe_poprawne:
                        p["pytanie"] = nowa_tresc
                        p["odpowiedzi"] = {"A": ans_a, "B": ans_b, "C": ans_c}
                        p["poprawne"] = nowe_poprawne
                        p["podstawa_prawna"] = podstawa
                        p["tresc_artykulu"] = artykul

                        st.success("Zmiany zostały pomyślnie zapisane!")
                        st.rerun()
                    else:
                        st.error("Pola pytania/odpowiedzi nie mogą być puste, oraz co najmniej jedna odpowiedź musi być zaznaczona jako poprawna!")

# ==============================================================================
# WIDOK: USTAWIENIA I ZMIANA MOTYWU
# ==============================================================================
elif menu_glowne == "⚙️ Ustawienia / Motyw":
    st.markdown("<div class='main-header'>Ustawienia i Personalizacja</div>", unsafe_allow_html=True)
    
    st.subheader("🎨 Wybór motywu wizualnego")
    nowy_motyw = st.radio(
        "Wybierz preferowany motyw:",
        ["Ciemny", "Jasny", "Zgodny z ustawieniami systemowymi"],
        index=["Ciemny", "Jasny", "Zgodny z ustawieniami systemowymi"].index(st.session_state.theme)
    )

    if nowy_motyw != st.session_state.theme:
        st.session_state.theme = nowy_motyw
        st.success(f"Zmieniono motyw na: {nowy_motyw}")
        st.rerun()
