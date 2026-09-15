import streamlit as st
import random
import time
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
    st.session_state.bazy = {
        "BAZA PYTAŃ - CZĘŚĆ 1 (Hydrogeologia i geologia inżynierska [...])": [
       { "id": 1,
        "pytanie": "Miejscowy plan zagospodarowania przestrzennego, sporządzany dla terenu górniczego w sytuacji, gdy w wyniku zamierzonej działalności określonej w koncesji przewiduje się istotne skutki dla środowiska powienien zapewniać integrację wszelkich działań podejmowanych w granicach terenu górniczego w celu:",
        "odpowiedzi": {
            "A": "Wykonania działalności określonej w koncesji;",
            "B": "Zapewnienia bezpieczeństwa powszechnego;",
            "C": "Ochrony środowiska, w tym obiektów budowlanych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 104 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Miejscowy plan zagospodarowania przestrzennego dla terenu górniczego sporządza się dla terenu górniczego wyznaczonego koncesją udzieloną na wydobywanie kopalin ze złóż, podziemne bezzbiornikowe magazynowanie substancji albo podziemne składowanie odpadów, jeżeli w wyniku zamierzonej działalności przewiduje się istotne skutki dla środowiska. Plan ten powinien zapewniać integrację wszelkich działań podejmowanych w granicach terenu górniczego w celu ochrony środowiska, w tym obiektów budowlanych."
    },
    ],  
    "BAZA PYTAŃ - CZĘŚĆ 2 (Informacja geologiczna, organy administracji geologicznej, organy nadzoru górniczego, plany ruchu zakładu górniczego)": [
       { "id": 1,
        "pytanie": "Miejscowy plan zagospodarowania przestrzennego, sporządzany dla terenu górniczego w sytuacji, gdy w wyniku zamierzonej działalności określonej w koncesji przewiduje się istotne skutki dla środowiska powienien zapewniać integrację wszelkich działań podejmowanych w granicach terenu górniczego w celu:",
        "odpowiedzi": {
            "A": "Wykonania działalności określonej w koncesji;",
            "B": "Zapewnienia bezpieczeństwa powszechnego;",
            "C": "Ochrony środowiska, w tym obiektów budowlanych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 104 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Miejscowy plan zagospodarowania przestrzennego dla terenu górniczego sporządza się dla terenu górniczego wyznaczonego koncesją udzieloną na wydobywanie kopalin ze złóż, podziemne bezzbiornikowe magazynowanie substancji albo podziemne składowanie odpadów, jeżeli w wyniku zamierzonej działalności przewiduje się istotne skutki dla środowiska. Plan ten powinien zapewniać integrację wszelkich działań podejmowanych w granicach terenu górniczego w celu ochrony środowiska, w tym obiektów budowlanych."
    },
    {
        "id": 2,
        "pytanie": "Miejscowy plan zagospodarowania przestrzennego, sporządzany dla terenu górniczego w sytuacji, gdy w wyniku zamierzonej działalności określonej w koncesji przewiduje się istotne skutki dla środowiska,może określić:",
        "odpowiedzi": {
            "A": "Obiekty, dla których wyznacza się filar ochronny;",
            "B": "Obszary, dla których wyznacza się filar ochronny;",
            "C": "Obszary wyłączone z zabudowy;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 104 ust. 2 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Miejscowy plan zagospodarowania przestrzennego dla terenu górniczego może w szczególności określić obszary, dla których wyznacza się filar ochronny w granicach którego, ze względu na ochronę dóbr chronionych, kopalina nie może być wydobywana albo może być wydobywana tylko w sposób zapewniający ochronę tych dóbr."
    },
    {
        "id": 3,
        "pytanie": "Planu ruchu zakładu górniczego nie sporządza się:",
        "odpowiedzi": {
            "A": "Jeżeli koncesji udzielił starosta;",
            "B": "Jeżeli roboty geologiczne służące poszukiwaniu lub rozpoznawaniu złóż kopalin są wykonywane bez użycia środków strzałowych na głębokości do 100 m poza obszarem górniczym;",
            "C": "Jeżeli roboty geologiczne służące poszukiwaniu lub rozpoznawaniu złóż kopalin są wykonywane bez użycia środków strzałowych na głębokości do 200 m w obszarze górniczym;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 105 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Planu ruchu nie sporządza się, jeżeli koncesji na wydobywanie kopalin udzielił starosta."
    },
    {
        "id": 4,
        "pytanie": "Plan ruchu zakładu górniczego określa m.in. szczegółowe przedsięwzięcia w celu zapewnienia:",
        "odpowiedzi": {
            "A": "Wykonywania działalności objętej koncesją;",
            "B": "Bezpieczeństwa powszechnego;",
            "C": "Bezpieczeństwa pożarowego;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 107 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Plan ruchu zakładu górniczego określa szczegółowe przedsięwzięcia niezbędne w celu zapewnienia bezpieczeństwa powszechnego."
    },
    {
        "id": 5,
        "pytanie": "Plan ruchu zakładu górniczego określa m.in. szczegółowe przedsięwzięcia w celu zapewnienia:",
        "odpowiedzi": {
            "A": "Bezpieczeństwa osób przebywających w zakładzie górniczym, w szczególności dotyczące bezpieczeństwa i higieny pracy;",
            "B": "Racjonalnej gospodarki złożem;",
            "C": "Ochrony elementów środowiska;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 107 ust. 1 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Plan ruchu zakładu górniczego określa szczegółowe przedsięwzięcia niezbędne w celu zapewnienia bezpieczeństwa osób przebywających w zakładzie górniczym, w szczególności dotyczące bezpieczeństwa i higieny pracy."
    },
    {
        "id": 6,
        "pytanie": "Plan ruchu zakładu górniczego określa m.in. szczegółowe przedsięwzięcia w celu zapewnienia:",
        "odpowiedzi": {
            "A": "Ochrony obiektów budowlanych;",
            "B": "Zapobieganie szkodom i ich naprawy;",
            "C": "Wykonywania działalności objętej koncesją;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 107 ust. 1 pkt 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Plan ruchu zakładu górniczego określa szczegółowe przedsięwzięcia niezbędne w celu zapewnienia ochrony obiektów budowlanych."
    },
    {
        "id": 7,
        "pytanie": "Plan ruchu zakładu górniczego sporządza się na okres:",
        "odpowiedzi": {
            "A": "od 2 do 6 lat albo na cały planowany okres",
            "B": "do 8 lat niezależnie od planowanego okresu",
            "C": "na cały planowany okres prowadzenia ruchu niezależnie od"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 108 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Plan ruchu zakładu górniczego sporządza się na okres od 2 do 6 lat albo na cały planowany okres prowadzenia ruchu, jeżeli jest on krótszy."
    },
    {
        "id": 8,
        "pytanie": "Wniosek o zatwierdzenie planu ruchu zakładu górniczego przedkłada się:",
        "odpowiedzi": {
            "A": "Organowi nadzoru górniczego właściwemu dla miejsca wykonywania robót objętych planem",
            "B": "Prezeswoi Wyższego Urzędu Górniczego;",
            "C": "Organowi koncesyjnemu"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 108 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wniosek o zatwierdzenie planu ruchu zakładu górniczego przedkłada się organowi nadzoru górniczego właściwemu dla miejsca wykonywania robót objętych planem, co najmniej na 30 dni przed zamierzonym rozpoczęciem wykonywania robót."
    },
    {
        "id": 9,
        "pytanie": "Przechowywanie lub używanie przez przedsiębiorcę w ruchu zakładu górniczego sprzętu strzałowego wymaga:",
        "odpowiedzi": {
            "A": "Pozwolenia wydanego w drodze decyzji przez organ nadzoru górniczego właściwemu dla miejsca wykonywania robót strzałowych;",
            "B": "Pozwolenia wydanego w drodze decyzji przez Prezesa Wyższego Urzędu Górniczego;",
            "C": "Pozwolenia wydanego w drodze decyzji przez komendanta Policji Państwowej właściwego dla miejsca wykonywania robót strzałowych"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 120 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przechowywanie lub używanie środków strzałowych i sprzętu strzałowego w ruchu zakładu górniczego wymaga pozwolenia wydanego, w drodze decyzji, przez organ nadzoru górniczego właściwy dla miejsca wykonywania robót strzałowych."
    },
    {
        "id": 10,
        "pytanie": "Przedsiębiorca lub podmiot wykonujący w zakresie swojej działalności zawodowej roboty strzałowe powierzone mu w ruchu zakładu górniczego, są zobowiązani:",
        "odpowiedzi": {
            "A": "Przestrzegać wymagań dotyczących bezpiecznego przechowywania środków strzałowych",
            "B": "Zapewnić ewidencjonowanie znajdujących się w zakładzie górniczym tam środków wykorzystywanych",
            "C": "Zapewnić prowadzenie wykazu używanych środków strzałowych i sprzętu strzałowego, określającego warunki ich używania;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 120 ust. 5 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca oraz podmiot wykonujący w zakresie swojej działalności zawodowej roboty powierzone mu w ruchu zakładu górniczego są zobowiązani zapewnić prowadzenie wykazu używanych środków strzałowych i sprzętu strzałowego określającego warunki ich używania."
    },
    {
        "id": 11,
        "pytanie": "Obowiązek posiadania dokumentacji mierniczo-geologicznej nałożony jest na przedsiębiorcę, który uzyskał koncesję na:",
        "odpowiedzi": {
            "A": "podziemne bezzbiornikowe magazynowanie substancji",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych własnością górniczą",
            "C": "Podziemne składowanie odpadów"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 116 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca, który uzyskał koncesję na wydobywanie kopalin ze złóż, podziemne bezzbiornikowe magazynowanie substancji albo podziemne składowanie odpadów, posiada dokumentację mierniczo-geologiczną, mierzy obiekty zakładu górniczego oraz na bieżąco uzupełnia tę dokumentację w trakcie postępu robót górniczych."
    },
    {
        "id": 12,
        "pytanie": "Obowiązek posiadania dokumentacji mierniczo-geologicznej nałożony jest na przedsiębiorcę, który uzyskał koncesję na:",
        "odpowiedzi": {
            "A": "poszukiwanie i rozpoznawanie złóż kopalin",
            "B": "wydobywanie kopalin ze złóż, z wyjątkiem koncesji udzielonej przez starostę;",
            "C": "wydobywanie kopalin ze złóż, niezależnie od organu udzielającego koncesji;"
        },
        "poprawne": ["A","B"],
        "podstawa_prawna": "Art. 116 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca, który uzyskał koncesję na wydobywanie kopalin ze złóż, podziemne bezzbiornikowe magazynowanie substancji albo podziemne składowanie odpadów, posiada dokumentację mierniczo-geologiczną..."
    },
    {
        "id": 13,
        "pytanie": "W skład dokumentacji mierniczo-geologicznej wchodzą:",
        "odpowiedzi": {
            "A": "Dokumenty pomiarowe",
            "B": "Dokumenty obliczeniowe",
            "C": "Dokumenty finansowe"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 116 ust. 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "W skład dokumentacji mierniczo-geologicznej wchodzą dokumenty miernicze i geologiczne, w tym dokumenty pomiarowe, obliczeniowe i kartograficzne, stanowiące jej treść."
    },
    {
        "id": 14,
        "pytanie": "Przy wykonywaniu nadzoru i kontroli upoważnionym pracownikom administracji geologicznej oraz pracownikom organów nadzoru górniczego, w granicach ich właściwości rzeczowej i miejscowej przysługuje, po okazaniu legitymacji służbowej, prawo:",
        "odpowiedzi": {
            "A": "Całodobowego wstępu do miejsc wykonywania robót objętych własnością",
            "B": "Dostępu do niezbędnych informacji;",
            "C": "Żądania udzielenia wyjaśnień w zakresie niezbędnym do sprawowania nadzoru i kontroli;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 156 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przy wykonywaniu nadzoru i kontroli upoważnionym pracownikom organów nadzoru górniczego oraz pracownikom organów administracji geologicznej, w granicach ich właściwości rzeczowej i miejscowej, przysługuje, po okazaniu legitymacji służbowej, prawo całodobowego wstępu, wraz z niezbędnym sprzętem, do miejsc wykonywania prac geologicznych, robót górniczych, zakładów górniczych, a także na tereny i do obiektów, w których wykonywana jest działalność regulowana ustawą."
    },
    {
        "id": 15,
        "pytanie": "Przy wykonywaniu nadzoru i kontroli upoważnionym pracownikom administracji geologicznej oraz pracownikom organów nadzoru górniczego, w granicach ich właściwości rzeczowej i miejscowej przysługuje, po okazaniu legitymacji służbowej, prawo:",
        "odpowiedzi": {
            "A": "Całodobowego wstępu do miejsc wydobywania kopalin;",
            "B": "Całodobowego wstępu do zakładów górniczych;",
            "C": "Żądania okazania dokumentów i udostępnienia niezbędnych danych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 156 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przy wykonywaniu nadzoru i kontroli upoważnionym pracownikom... przysługuje, po okazaniu legitymacji służbowej, prawo całodobowego wstępu... do zakładów górniczych..."
    },
    {
        "id": 16,
        "pytanie": "Organami administracji geologicznej są:",
        "odpowiedzi": {
            "A": "Minister środowiska",
            "B": "Marszałkowie województw",
            "C": "Wójtowie gmin"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 156 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organami administracji geologicznej są: minister właściwy do spraw środowiska, marszałkowie województw, starostowie."
    },
    {
        "id": 17,
        "pytanie": "Organami administracji geologicznej są:",
        "odpowiedzi": {
            "A": "Minister środowiska",
            "B": "Marszałkowie województw",
            "C": "Prezes Wyższego Urzędu Górniczego"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 156 ust. 1 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organami administracji geologicznej są: minister właściwy do spraw środowiska, marszałkowie województw, starostowie."
    },
    {
        "id": 18,
        "pytanie": "Właściwy organ administracji geologicznej może w drodze decyzji wstrzymać działalność określoną ustawą Prawo geologiczne i górnicze, jeżeli jest wykonywana:",
        "odpowiedzi": {
            "A": "Z naruszeniem warunków określonych w koncesji;",
            "B": "Bez zatwierdzonego projektu robót geologicznych",
            "C": "Z naruszeniem warunków zapewniających bezpieczeństwo finansowe przedsiębiorcy."
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 160 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Jeżeli działalność regulowana ustawą jest wykonywana z naruszeniem warunków określonych w projekcie robót geologicznych lub bez zatwierdzonego projektu robót geologicznych, właściwy organ administracji geologicznej wydaje decyzję o wstrzymaniu działalności."
    },
    {
        "id": 19,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Złóż kopalin nieobjętych własnością górniczą, poszukiwanych lub rozpoznawanych na obszarze do 2 ha w celu wydobycia metodą odkrywkową w ilości do 20000 m³ w roku kalendarzowym i bez użycia środków strzałowych;",
            "B": "Złóż kopalin objętych własnością górniczą, poszukiwanych lub rozpoznawanych na obszarze do 2 ha w celu wydobycia metodą podziemną w ilości do 20000 m³ w roku kalendarzowym i bez użycia środków strzałowych;",
            "C": "Złóż kopalin nieobjętych własnością górniczą, poszukiwanych lub rozpoznawanych na obszarze do 3 ha w celu wydobycia metodą odkrywkową w ilości do 30000 m³ w roku kalendarzowym i bez użycia środków strzałowych;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach związanych z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczących złóż kopalin nieobjętych własnością górniczą, poszukiwanych lub rozpoznawanych na obszarze do 2 ha w celu wydobycia metodą odkrywkową w ilości do 20 000 m³ w roku kalendarzowym i bez użycia środków strzałowych."
    },
    {
        "id": 20,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Ujęć wód podziemnych, których przewidywane lub ustalone zasoby nie przekraczają 50 m³/h;",
            "B": "Ujęć wód podziemnych, których przewidywane lub ustalone zasoby nie przekraczają 50 m³/dobę;",
            "C": "Ujęć wód podziemnych, których przewidywane lub ustalone zasoby nie przekraczają 500 m³/h;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach... dotyczących ujęć wód podziemnych, których przewidywane lub ustalone zasoby nie przekraczają 50 m³/h."
    },
    {
        "id": 21,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Odwodnień budowlanych o wydajności nieprzekraczającej 50 m³/h;",
            "B": "Odwodnień budowlanych o wydajności nieprzekraczającej 50 m³/dobę;",
            "C": "Odwodnień budowlanych o wydajności nieprzekraczającej 500 m³/h;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach... dotyczących odwodnień budowlanych, których wydajność nie przekracza 50 m³/h."
    },
    {
        "id": 22,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Badań geologiczno-inżynierskich wykonywanych na potrzeby zagospodarowania przestrzennego gminy oraz warunków posadawiania obiektów budowlanych;",
            "B": "Określania warunków hydrogeologicznych oraz geologiczno – inżynierskich dla potrzeb podziemnego bezzbiornikowego magazynowania substancji;",
            "C": "Określania warunków hydrogeologicznych oraz geologiczno-inżynierskich dla potrzeb podziemnego składowania odpadów."
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach... dotyczących badań geologiczno-inżynierskich wykonywanych na potrzeby zagospodarowania przestrzennego gminy oraz warunków posadawiania obiektów budowlanych."
    },
    {
        "id": 23,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Warunków hydrogeologicznych w związku z zamierzonym wykonywaniem przedsięwzięć mogących negatywnie oddziaływać na wody podziemne, w tym powodować ich zanieczyszczenie, dotyczących przedsięwzięć mogących znacząco oddziaływać na środowisko, dla których obowiązek sporządzenia raportu o oddziaływaniu przedsięwzięcia na środowisko może być wymagany, z wyłączeniem przedsięwzięć mogących negatywnie oddziaływać na wody lecznicze;",
            "B": "wykonywaniem przedsięwzięć mogących negatywnie oddziaływać na wody podziemne, w tym powodować ich zanieczyszczenie, dotyczących przedsięwzięć mogących znacząco oddziaływać na środowisko, dla których obowiązek sporządzenia raportu o oddziaływaniu przedsięwzięcia na środowisko może być wymagany, w tym przedsięwzięć mogących negatywnie oddziaływać na wody lecznicze;",
            "C": "ustanawianiem obszarów ochronnych zbiorników wód podziemnych;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 5 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach... dotyczących warunków hydrogeologicznych w związku z zamierzonym wykonywaniem przedsięwzięć mogących negatywnie oddziaływać na wody podziemne..."
    },
    {
        "id": 24,
        "pytanie": "Do starosty jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Robót geologicznych wykonywanych w celu wykorzystywania ciepła ziemi;",
            "B": "Regionalnych badań hydrogeologicznych;",
            "C": "Regionalnych prac kartografii geologicznej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 161 ust. 2 pkt 6 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta jest organem administracji geologicznej pierwszej instancji w sprawach... dotyczących robót geologicznych wykonywanych w celu wykorzystania ciepła Ziemi."
    },
    {
        "id": 25,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Złóż kopalin objętych własnością górniczą, z wyjątkiem wód objętych własnością górniczą;",
            "B": "Warunków hydrogeologicznych w związku z projektowaniem odwodnień złóż kopalin stałych objętych własnością górniczą;",
            "C": "Obszarów morskich Rzeczypospolitej Polskiej;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej pierwszej instancji w sprawach związanych z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczących złóż kopalin objętych własnością górniczą, z wyjątkiem wód objętych własnością górniczą."
    },
    {
        "id": 26,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Regionalnych badań hydrogeologicznych;",
            "B": "Regionalnych prac kartografii geologicznej;",
            "C": "Regionalnych badań budowy geologicznej kraju;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej... dotyczących regionalnych badań budowy geologicznej kraju."
    },
    {
        "id": 27,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Otworów wiertniczych do rozpoznania budowy głębokiego podłoża;",
            "B": "Obiektów budownictwa wodnego o wysokości piętrzenia przekraczającej 5 m;",
            "C": "Ponadwojewódzkich inwestycji liniowych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej... dotyczących otworów wiertniczych do rozpoznania budowy głębokiego podłoża, niezwiązanego z dokumentowaniem złóż kopalin."
    },
    {
        "id": 28,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Określania warunków hydrogeologicznych w związku z ustanawianiem obszarów ochronnych zbiorników wód podziemnych;",
            "B": "Złóż wód leczniczych;",
            "C": "Określania warunków hydrogeologicznych oraz geologiczno – inżynierskich dla potrzeb podziemnego bezzbiornikowego magazynowania substancji;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 5 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej... dotyczących określania warunków hydrogeologicznych oraz geologiczno-inżynierskich dla potrzeb podziemnego bezzbiornikowego magazynowania substancji albo podziemnego składowania odpadów."
    },
    {
        "id": 29,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Złóż gipsu i anhydrytu;",
            "B": "Złóż wód termalnych;",
            "C": "Złóż darniowych rud żelaza;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej... dotyczących złóż kopalin objętych własnością górniczą."
    },
    {
        "id": 30,
        "pytanie": "Do ministra właściwego do spraw środowiska jako organu administracji geologicznej pierwszej instancji, należą sprawy związane z zatwierdzaniem projektów robót geologicznych oraz dokumentacjami geologicznymi, dotyczące:",
        "odpowiedzi": {
            "A": "Obiektów budownictwa wodnego o wysokości piętrzenia 3 m;",
            "B": "Warunków hydrogeologicznych w związku z projektowaniem odwodnień złóż kopalin objętych prawem własności nieruchomości gruntowej;",
            "C": "Otworów wiertniczych do rozpoznania budowy głębokiego podłoża, niezwiązanego z dokumentowaniem złóż kopalin;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 161 ust. 3 pkt 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska jest organem administracji geologicznej... dotyczących otworów wiertniczych do rozpoznania budowy głębokiego podłoża, niezwiązanego z dokumentowaniem złóż kopalin."
    },
    {
        "id": 31,
        "pytanie": "Organami nadzoru górniczego są:",
        "odpowiedzi": {
            "A": "Minister Środowiska;",
            "B": "Prezes Wyższego Urzędu Górniczego;",
            "C": "Prezesi regionalnych urzędów górniczych;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 163 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organami nadzoru górniczego są: Prezes Wyższego Urzędu Górniczego oraz dyrektorzy okręgowych urzędów górniczych i Dyrektor Specjalistycznego Urzędu Górniczego."
    },
    {
        "id": 32,
        "pytanie": "Organy nadzoru górniczego sprawują nadzór i kontrolę nad ruchem zakładów górniczych, w szczególności w zakresie:",
        "odpowiedzi": {
            "A": "Bezpieczeństwa i Higieny pracy;",
            "B": "Bezpieczeństwa pożarowego",
            "C": "Bezpieczeństwa finansowego przedsiębiorcy górniczego;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 167 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organy nadzoru górniczego sprawują nadzór i kontrolę nad ruchem zakładów górniczych, w szczególności w zakresie bezpieczeństwa i higieny pracy oraz bezpieczeństwa pożarowego."
    },
    {
        "id": 33,
        "pytanie": "Organy nadzoru górniczego sprawują nadzór i kontrolę nad ruchem zakładów górniczych, w szczególności w zakresie:",
        "odpowiedzi": {
            "A": "Ratownictwa górniczego;",
            "B": "Zapobiegania szkodom;",
            "C": "Rekultywacji gruntów po działalności górniczej;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 167 ust. 1 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organy nadzoru górniczego sprawują nadzór i kontrolę nad ruchem zakładów górniczych, w szczególności w zakresie ratownictwa górniczego."
    },
    {
        "id": 34,
        "pytanie": "Nadzór i kontrolę nad wykonywaniem robót geologicznych służących poszukiwaniu i rozpoznawaniu złóż kopalin, wykonywanych z użyciem środków strzałowych sprawuje:",
        "odpowiedzi": {
            "A": "Minister właściwy do spraw wewnętrznych;",
            "B": "Organ nadzoru górniczego;",
            "C": "Wójt gminy lub burmistrz (prezydent) miasta"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 167 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Nadzór i kontrolę nad wykonywaniem prac geologicznych służących poszukiwaniu lub rozpoznawaniu złóż kopalin, wykonywanych z użyciem środków strzałowych, sprawują właściwe organy nadzoru górniczego."
    },
    {
        "id": 35,
        "pytanie": "Prawo do informacji geologicznej uzyskanej od dnia 1 stycznia 2012 r. przysługuje:",
        "odpowiedzi": {
            "A": "wykonawcy prac geologicznych;",
            "B": "podmiotowi, który sfinansował wykonanie prac geologicznych;",
            "C": "Skarbowi Państwa;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 99 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawo do informacji geologicznej przysługuje Skarbowi Państwa."
    },
    {
        "id": 36,
        "pytanie": "Prawo do informacji geologicznej uzyskanej od dnia 1 stycznia 2012 r. przysługuje:",
        "odpowiedzi": {
            "A": "Skarbowi Państwa;",
            "B": "gminie, na terenie której zlokalizowane jest miejsce wykonywania prac",
            "C": "podmiotowi, który opracował dokumentację geologiczną;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 99 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawo do informacji geologicznej przysługuje Skarbowi Państwa."
    },
    {
        "id": 37,
        "pytanie": "Temu, kto ponosząc koszt prac prowadzonych w wyniku decyzji wydanych na podstawie ustawy, uzyskał informację geologiczną, przysługuje:",
        "odpowiedzi": {
            "A": "prawo własności do tej informacji",
            "B": "prawo do nieodpłatnego korzystania z niej.",
            "C": "roszczenie wobec Skarbu Państwa o zwrot poniesionych kosztów."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 99 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podmiotowi, który poniósł koszty prac geologicznych prowadzonych na podstawie decyzji wydanych na podstawie ustawy, przysługuje prawo do korzystania z informacji geologicznej."
    },
    {
        "id": 38,
        "pytanie": "Temu, kto ponosząc koszt prac prowadzonych w wyniku decyzji wydanych na podstawie ustawy, uzyskał informację geologiczną, przysługuje:",
        "odpowiedzi": {
            "A": "prawo do nieodpłatnego korzystania z niej;",
            "B": "wyłączne prawo do korzystania z informacji geologicznej w celu ubiegania się o wykonywanie działalności w zakresie: - wydobywania kopalin ze złóż, - podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne w okresie 5 lat od dnia utraty mocy decyzji, na podstawie której wykonano prace będące źródłem informacji;",
            "C": "prawo sprzedaży uzyskanych informacji;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 99 ust. 2 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podmiotowi, który poniósł koszty... przysługuje wyłączne prawo do korzystania z informacji geologicznej w celu ubiegania się o wykonywanie działalności w zakresie wydobywania kopalin, podziemnego bezzbiornikowego magazynowania substancji albo podziemnego składowania odpadów."
    },
    {
        "id": 39,
        "pytanie": "Temu, kto ponosząc koszt prac prowadzonych w wyniku decyzji wydanych na podstawie ustawy, uzyskał informację geologiczną, przysługuje:",
        "odpowiedzi": {
            "A": "wyłączne prawo do korzystania z informacji geologicznej w celu ubiegania się o wykonywanie działalności w zakresie: wydobywania kopalin ze złóż, podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne w okresie 5 lat od dnia utraty mocy decyzji, na podstawie której wykonano prace będące źródłem informacji",
            "B": "wyłączne prawo do korzystania z informacji geologicznej w celu ubiegania się o wykonywanie działalności w zakresie: wydobywania kopalin ze złóż, podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne w okresie 3 lat od dnia utraty mocy decyzji, na podstawie której wykonano prace będące źródłem informacji;",
            "C": "prawo do nieodpłatnego korzystania z niej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 99 ust. 2 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podmiotowi, który poniósł koszty... przysługuje wyłączne prawo do korzystania z informacji geologicznej w celu ubiegania się o wykonywanie działalności... w okresie 5 lat od dnia utraty mocy decyzji."
    },
    {
        "id": 40,
        "pytanie": "Ten, komu przysługuje wyłączne prawo do korzystania z informacji geologicznej, zachowuje to prawo jeżeli:",
        "odpowiedzi": {
            "A": "przed upływem 5 lat od dnia utraty mocy decyzji, na podstawie której wykonano prace będące źródłem informacji uzyskał decyzję stanowiącą podstawę wykonywania działalności w zakresie: - wydobywania kopalin ze złóż, - podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne,",
            "B": "przed upływem 5 lat od dnia utraty mocy decyzji, na podstawie której wykonano prace będące źródłem informacji uzyskał decyzję stanowiącą podstawę wykonywania działalności w zakresie poszukiwania złóż kopalin",
            "C": "wniesie na rzecz Skarbu Państwa opłatę ryczałtową za korzystanie z informacji geologicznej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 99 ust. 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podmiot, któremu przysługuje wyłączne prawo do korzystania z informacji geologicznej, zachowuje to prawo, jeżeli przed upływem określonego terminu uzyska decyzję stanowiącą podstawę do wykonywania działalności."
    },
    {
        "id": 41,
        "pytanie": "Ten, komu przysługuje wyłączne prawo do korzystania z informacji geologicznej, po uzyskaniu decyzji stanowiącej podstawę wykonywania działalności zakresie: - wydobywania kopalin ze złóż, - podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne, zachowuje wyłączne prawo do korzystania z informacji geologicznej",
        "odpowiedzi": {
            "A": "przez czas określony w takiej decyzji oraz dodatkowo przez 5 lata od dnia utraty jej mocy,",
            "B": "przez czas określony w takiej decyzji oraz dodatkowo przez 2 lata od dnia utraty jej mocy,",
            "C": "wyłącznie przez czas określony w takiej decyzji,"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 99 ust. 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Zachowuje to prawo przez czas określony w tej decyzji oraz dodatkowo przez okres 2 lat od dnia utraty jej mocy."
    },
    {
        "id": 42,
        "pytanie": "Prawem do informacji geologicznej rozporządza:",
        "odpowiedzi": {
            "A": "organ administracji geologicznej;",
            "B": "ten, komu przysługują prawa do korzystania z informacji geologicznej w granicach określonych przepisami ustawy;",
            "C": "Skarb Państwa;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 43,
        "pytanie": "Ten, komu przysługują prawa do korzystania z informacji geologicznej, może:",
        "odpowiedzi": {
            "A": "sprzedać informację geologiczną na rynku wtórnym;",
            "B": "rozporządzać nimi w granicach określonych przepisami ustawy;",
            "C": "zgłaszać do Skarbu Państwa roszczenia o zwrot poniesionych nakładów na pozyskanie informacji geologicznej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 44,
        "pytanie": "Do praw dotyczących rozporządzania informacją geologiczną przez podmioty finansujące prace geologiczne, w zakresie nieuregulowanym prawem geologicznym i górniczym, stosuje się przepisy:",
        "odpowiedzi": {
            "A": "ustawy o dostępie do informacji o środowisku;",
            "B": "ustawy o dostępie do informacji publicznej;",
            "C": "Kodeksu cywilnego;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 100 ust. 3 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do rozporządzania prawem do informacji geologicznej przysługującym Skarbowi Państwa w sprawach nieuregulowanych w ustawie stosuje się przepisy Kodeksu cywilnego."
    },
    {
        "id": 45,
        "pytanie": "Korzystanie z informacji geologicznej, do której prawa przysługują Skarbowi Państwa, jest:",
        "odpowiedzi": {
            "A": "zawsze nieodpłatne;",
            "B": "odpłatne w sytuacji kiedy korzystanie z informacji geologicznej, następuje w celu wykonywania działalności w zakresie: - wydobywania kopalin ze złóż, - podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne; realizowane wyłącznie za wynagrodzeniem;",
            "C": "odpłatne w wyjątkiem kiedy korzystanie z informacji geologicznej, jest związane z badaniem powodującym uszkodzenie, zniszczenie lub zużycie próbki geologicznej;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 100 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Korzystanie z informacji geologicznej, do której prawo przysługuje Skarbowi Państwa, jest nieodpłatne, chyba że ustawa stanowi inaczej."
    },
    {
        "id": 46,
        "pytanie": "Korzystanie z informacji geologicznej, do której prawa przysługują Skarbowi Państwa, jest:",
        "odpowiedzi": {
            "A": "odpłatne w sytuacji kiedy korzystanie z informacji geologicznej związane jest z udostępnieniem danych geologicznych;",
            "B": "podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów;",
            "C": "odpłatne z wyjątkiem sytuacji kiedy korzystanie z informacji geologicznej, następuje w celu wykonywania działalności w zakresie poszukiwania złóż kopalin; w jakim wymagane pozwolenie wodnoprawne;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 100 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Korzystanie z informacji geologicznej, do której prawo przysługuje Skarbowi Państwa, jest nieodpłatne, chyba że ustawa stanowi inaczej."
    },
    {
        "id": 47,
        "pytanie": "Korzystanie z informacji geologicznej, do której prawa przysługują Skarbowi Państwa, następuje w drodze umowy za wynagrodzeniem w celu wykonywania działalności w zakresie:",
        "odpowiedzi": {
            "A": "wydobywania kopalin ze złóż,",
            "B": "związane jest z badaniem powodującym uszkodzenie, zniszczenie lub zużycie próbki geologicznej, bez względu na cel korzystania;",
            "C": "związane jest z udostępnieniem danych geologicznych, bez względu na cel korzystania;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 100 ust. 2 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Rozporządzenie prawem do informacji geologicznej w celu wykonywania działalności w zakresie wydobywania kopalin ze złóż następuje za wynagrodzeniem w drodze umowy."
    },
    {
        "id": 48,
        "pytanie": "Korzystanie z informacji geologicznej, do której prawa przysługują Skarbowi Państwa, następuje w drodze umowy za wynagrodzeniem jeżeli:",
        "odpowiedzi": {
            "A": "związane jest z badaniem powodującym uszkodzenie, zniszczenie lub zużycie próbki geologicznej, bez względu na cel korzystania;",
            "B": "związane jest z udostępnieniem danych geologicznych, bez względu na cel korzystania;",
            "C": "następuje w celu wykonywania działalności w zakresie: - wydobywania kopalin ze złóż, - podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów, - w jakim wymagane jest pozwolenie wodnoprawne;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 100 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Rozporządzenie prawem do informacji geologicznej w celu wykonywania działalności gospodarczej następuje za wynagrodzeniem w drodze umowy."
    },
    {
        "id": 49,
        "pytanie": "Podstawę określenia wynagrodzenia za korzystanie z informacji geologicznej:",
        "odpowiedzi": {
            "A": "opinia organu koncesyjnego;",
            "B": "wycena określająca koszty projektowania, wykonywania i",
            "C": "wycena określająca koszty projektowania, wykonywania i"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wysokość wynagrodzenia ustala się na podstawie wyceny określającej koszty projektowania, wykonywania i dokumentowania prac geologicznych."
    },
    {
        "id": 50,
        "pytanie": "Wycenę określającą koszty projektowania, wykonywania i dokumentowania prac geologicznych",
        "odpowiedzi": {
            "A": "finansuje podmiot ubiegający się o korzystanie z tej informacji",
            "B": "finansuje Skarb Państwa",
            "C": "finansuje NFOŚiGW"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 100 ust. 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wysokość wynagrodzenia ustala się na podstawie wyceny określającej koszty projektowania, wykonywania i dokumentowania prac geologicznych."
    },
    {
        "id": 51,
        "pytanie": "Rozporządzanie informacją geologiczną, do której prawa przysługują Skarbowi Państwa, zawartą w dokumentacji geologicznej:",
        "odpowiedzi": {
            "A": "następuje na czas nieoznaczony",
            "B": "następuje wyłącznie na czas oznaczony",
            "C": "wymaga zgody organu administracji geologicznej"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 52,
        "pytanie": "Rozporządzanie informacją geologiczną, do której prawa przysługują Skarbowi Państwa, zawartą w dokumentacji geologicznej:",
        "odpowiedzi": {
            "A": "realizowane jest wyłącznie przez Ministra Środowiska",
            "B": "następuje wyłącznie na czas oznaczony",
            "C": "następuje wyłącznie nieodpłatnie"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 53,
        "pytanie": "Przed zawarciem umowy o korzystanie z informacji geologicznej za wynagrodzeniem Skarb Państwa:",
        "odpowiedzi": {
            "A": "dokonuje weryfikacji wyceny informacji geologicznej",
            "B": "sporządza kontrwycenę informacji geologicznej",
            "C": "ustala kwotę wynagrodzenia w oparciu o kwoty bazowe określone ustawą"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza... minister właściwy do spraw środowiska."
    },
    {
        "id": 54,
        "pytanie": "Zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności polegającej na wydobywaniu kopalin ze złóż, wykonuje:",
        "odpowiedzi": {
            "A": "starosta powiatowy;",
            "B": "marszałek województwa;",
            "C": "minister właściwy do spraw środowiska;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza minister właściwy do spraw środowiska."
    },
    {
        "id": 55,
        "pytanie": "Zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności polegającej na podziemnym bezzbiornikowym magazynowaniu substancji oraz podziemnym składowania odpadów, geologicznej wykonuje:",
        "odpowiedzi": {
            "A": "starosta powiatowy;",
            "B": "marszałek województwa;",
            "C": "minister właściwy do spraw środowiska;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 56,
        "pytanie": "Zadania Skarbu Państwa dotyczącego:",
        "odpowiedzi": {
            "A": "starosta powiatowy",
            "B": "marszałek województwa",
            "C": "minister właściwy do spraw środowiska"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 57,
        "pytanie": "Zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności w zakresie w jakim wymagane jest pozwolenie wodnoprawne, wykonuje:",
        "odpowiedzi": {
            "A": "starosta powiatowy;",
            "B": "marszałek województwa;",
            "C": "minister właściwy do spraw środowiska;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza... minister właściwy do spraw środowiska."
    },
    {
        "id": 58,
        "pytanie": "Minister właściwy do spraw środowiska wykonuje zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności w zakresie:",
        "odpowiedzi": {
            "A": "wydobywania kopalin ze złóż;",
            "B": "podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów;",
            "C": "w jakim wymagane jest pozwolenie wodno prawne;"
        },
       "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 59,
        "pytanie": "Marszałkiem województwa wykonuje zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności w zakresie:",
        "odpowiedzi": {
            "A": "wydobywania kopalin ze złóż;",
            "B": "podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów;",
            "C": "w jakim wymagane jest pozwolenie wodno prawne;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza minister właściwy do spraw środowiska."
    },
    {
        "id": 60,
        "pytanie": "Starosta powiatowy wykonuje zadania Skarbu Państwa dotyczące rozporządzania prawem do informacji geologicznej, w celu wykonywania działalności w zakresie:",
        "odpowiedzi": {
            "A": "wydobywania kopalin ze złóż;",
            "B": "podziemnego bezzbiornikowego magazynowania substancji oraz podziemnego składowania odpadów;",
            "C": "starosta powiatowy nie wykonuje zadań Skarbu Państwa dotyczącego rozporządzania prawem do informacji geologicznej;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 100 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawem do informacji geologicznej przysługującym Skarbowi Państwa rozporządza, w granicach określonych ustawą, minister właściwy do spraw środowiska."
    },
    {
        "id": 61,
        "pytanie": "Wpływy z tytułu rozporządzania prawem do informacji geologicznej należącej do Skarbowi Państwa stanowią dochód:",
        "odpowiedzi": {
            "A": "w 60% gminy z terenu której pochodzi informacja oraz 40% NFOŚiGW;",
            "B": "budżetu państwa;",
            "C": "państwowej służby geologicznej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 100 ust. 7 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Dochody z tytułu rozporządzania prawem do informacji geologicznej stanowią dochód budżetu państwa."
    },
    {
        "id": 62,
        "pytanie": "Państwowa służba geologiczna:",
        "odpowiedzi": {
            "A": "wykonuje niektóre zadania państwa w zakresie geologii",
            "B": "pełni rolę organu doradczego ministra do spraw środowiska;",
            "C": "jest organem administracji geologicznej;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 162 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Państwowa służba geologiczna wykonuje zadania państwa w zakresie geologii."
    },
    {
        "id": 63,
        "pytanie": "Państwowa służba geologiczna wykonuje m.in. następujące zadania państwa w zakresie geologii:",
        "odpowiedzi": {
            "A": "- prowadzi centralne archiwum geologiczne, - gromadzi, udostępnia, przetwarza i archiwizuje dane geologiczne, - prowadzi bazy danych geologicznych;",
            "B": "rozporządza prawem do informacji geologicznej;",
            "C": "inicjuje, koordynuje i wykonuje zadania zmierzające do rozpoznania budowy geologicznej kraju, w tym prac o podstawowym znaczeniu dla gospodarki narodowej, w szczególności dla odnowienia bazy surowcowej kraju, ustalania zasobów złóż kopalin, a także dla ochrony środowiska;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 162 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Państwowa służba geologiczna wykonuje zadania państwa w zakresie geologii, obejmujące prowadzenie centralnego archiwum geologicznego, gromadzenie, udostępnianie, przetwarzanie i archiwizowanie danych geologicznych oraz prowadzenie baz danych geologicznych."
    },
    {
        "id": 64,
        "pytanie": "Państwowa służba geologiczna wykonuje m.in. następujące zadania państwa w zakresie geologii:",
        "odpowiedzi": {
            "A": "sporządza krajowy bilans zasobów kopalin;",
            "B": "prowadzi rejestr obszarów górniczych;",
            "C": "koordynuje zadania z zakresu ochrony georóżnorodności oraz geologii środowiskowej, sporządza krajowy bilans wód podziemnych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 162 ust. 1 pkt 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do zadań państwowej służby geologicznej należy sporządzanie krajowego bilansu zasobów kopalin."
    },
    {
        "id": 65,
        "pytanie": "Państwowa służba geologiczna wykonuje m.in. następujące zadania państwa w zakresie geologii:",
        "odpowiedzi": {
            "A": "rozporządza prawem do informacji geologicznej;",
            "B": "prowadzi centralne archiwum geologiczne;",
            "C": "Polska Akademia Nauk;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 162 ust. 1 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do zadań państwowej służby geologicznej należy prowadzenie centralnego archiwum geologicznego."
    },
    {
        "id": 66,
        "pytanie": "Państwową służbę geologiczną pełni:",
        "odpowiedzi": {
            "A": "Państwowy Instytut Geologiczny – Państwowy Instytut Badawczy;",
            "B": "Polska Akademia Nauk;",
            "C": "Główny Instytut Górnictwa;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 163 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Państwową służbę geologiczną pełni Państwowy Instytut Geologiczny – Państwowy Instytut Badawczy."
    },
    {
        "id": 67,
        "pytanie": "Organy administracji geologicznej, stosownie do zakresu swojej właściwości, gromadzą informację geologiczną:",
        "odpowiedzi": {
            "A": "pochodzącą z bieżącego dokumentowania przebiegu robót geologicznych i ich wyników;",
            "B": "przekazywaną przez podmioty wykonujące prace geologiczne; przedstawione w formie",
            "C": "przekazywana przez państwową służbę geologiczną;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 98 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Informację geologiczną stanowi treść dokumentów geologicznych oraz dane geologiczne uzyskane w wyniku wykonywania prac geologicznych."
    },
    {
        "id": 68,
        "pytanie": "Organy administracji geologicznej gromadzą informację geologiczną jako:",
        "odpowiedzi": {
            "A": "dokumenty geologiczne;",
            "B": "wartości informacji geologicznej;",
            "C": "zbiory danych geologicznych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 98 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Informację geologiczną gromadzi się w postaci dokumentów geologicznych oraz danych geologicznych."
    },
    {
        "id": 69,
        "pytanie": "Organy administracji geologicznej umożliwiają:",
        "odpowiedzi": {
            "A": "nieodpłatne zapoznanie się ze zgromadzoną informacją geologiczną, bez prawa dokonywania reprodukcji, odpisu, odrysu, wydruku, fotokopii lub kopii w postaci elektronicznej dokumentów i zbiorów danych, a także bez prawa pobierania próbek;",
            "B": "odpłatne zapoznanie się ze zgromadzoną informacją geologiczną, bez prawa dokonywania reprodukcji, odpisu, odrysu, wydruku, fotokopii lub kopii w postaci elektronicznej dokumentów i zbiorów danych, a także bez prawa pobierania próbek;",
            "C": "wykonywanie reprodukcji, odpisu, odrysu, wydruku, fotokopii lub kopii w postaci elektronicznej dokumentów i zbiorów danych oraz pobieranie próbek geologicznych;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 100 ust. 2 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Korzystanie z informacji geologicznej, do której prawo przysługuje Skarbowi Państwa, w celu wglądu i nieodpłatnego zapoznania się ze zgromadzoną dokumentacją jest bezpłatne."
    },
    {
        "id": 70,
        "pytanie": "Szacowania wartości informacji geologicznej wykorzystywanej w celu wykonywania działalności w zakresie wydobywania kopaliny ze złoża dokonuje się metodą:",
        "odpowiedzi": {
            "A": "obliczenie zryczałtowanej wartości informacji geologicznej;",
            "B": "obliczenie kosztu pozyskania informacji geologicznej, zgodnie z zakresem i technologią prac geologicznych, które posłużyły do jej pozyskania, wyrażonego w cenach stosowanych dla tego typu prac w roku wykonywania szacowania;",
            "C": "obliczenie kosztu pozyskania informacji geologicznej, wyrażonego w nominalnych cenach z roku jej pozyskania i zrewaloryzowanego do poziomu cen z roku poprzedzającego rok wykonywania szacowania;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Przepisy wykonawcze ws. wyceny informacji geologicznej",
        "tresc_artykulu": "Określa szczegółowe metody wyceny informacji geologicznej na podstawie kosztów jej pozyskania zrewaloryzowanych do cen aktualnych z roku wyceny."
    },
    {
        "id": 71,
        "pytanie": "Do kosztów pozyskania informacji geologicznej wlicza się nakłady poniesione na:",
        "odpowiedzi": {
            "A": "projektowanie prac geologicznych;",
            "B": "wykonywanie prac geologicznych;",
            "C": "próbki geologiczne trwałego przechowywania;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 100 ust. 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wysokość wynagrodzenia ustala się na podstawie wyceny określającej koszty projektowania, wykonywania i dokumentowania prac geologicznych."
    },
    {
        "id": 72,
        "pytanie": "Do kosztów pozyskania informacji geologicznej wlicza się nakłady poniesione na",
        "odpowiedzi": {
            "A": "przedstawienie wyników prac geologicznych;",
            "B": "gromadzenie i przetwarzanie informacji geologicznej;",
            "C": "archiwizowanie dokumentacji geologicznych, które są źródłem informacji geologicznej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 100 ust. 4 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wysokość wynagrodzenia ustala się na podstawie wyceny określającej koszty projektowania, wykonywania i dokumentowania prac geologicznych."
    },
    {
        "id": 73,
        "pytanie": "W przypadku szacowania wartości informacji geologicznej wykorzystywanej w celu wykonywania działalności w zakresie wydobywania kopaliny ze złoża, wycena wymaga przedstawienia:",
        "odpowiedzi": {
            "A": "historii badań i eksploatacji złoża oraz wykazu materiałów archiwalnych wykorzystanych do wykonania szacowania;",
            "B": "oraz granicami obszaru, którego dotyczy informacja geologiczną objęta wnioskiem.",
            "C": "załączników graficznych z zaznaczonymi granicami złoża"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Przepisy wykonawcze ws. wyceny informacji geologicznej",
        "tresc_artykulu": "Określa wymaganą treść operatu wyceny, w tym historię badań złoża i materiały źródłowe."
    },
    {
        "id": 74,
        "pytanie": "Wartość informacji geologicznej wykorzystywanej w celu wydobywania wód leczniczych podlega obniżeniu o:",
        "odpowiedzi": {
            "A": "80% obliczonej wartości informacji;",
            "B": "95% obliczonej wartości informacji;",
            "C": "90% obliczonej wartości informacji;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Przepisy wykonawcze ws. wyceny informacji geologicznej",
        "tresc_artykulu": "Ustala wskaźniki redukcyjne dla wartości informacji geologicznej dotyczącej wód leczniczych do 90%."
    },
    {
        "id": 75,
        "pytanie": "W przypadku szacowania wartości informacji geologicznej przy użyciu więcej niż jednej z metod wyceny, jako podstawę do ustalenia wartości wynagrodzenia przyjmuje się:",
        "odpowiedzi": {
            "A": "najwyższy z uzyskanych wyników",
            "B": "najniższy z uzyskanych wyników",
            "C": "średnią z uzyskanych wyników"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Przepisy wykonawcze ws. wyceny informacji geologicznej",
        "tresc_artykulu": "Zasady ustalania wynagrodzenia w przypadku zastosowania alternatywnych metod szacowania wartości."
    },
    {
        "id": 76,
        "pytanie": "Szacowania wartości informacji geologicznej wykorzystywanej w celu wykonywania działalności w zakresie, w jakim jest wymagane pozwolenie wodnoprawne, dokonuje się metodą:",
        "odpowiedzi": {
            "A": "obliczenie zryczałtowanej wartości informacji geologicznej;",
            "B": "obliczenie kosztu pozyskania informacji geologicznej, zgodnie z zakresem i technologią prac geologicznych, które posłużyły do jej pozyskania, wyrażonego w cenach stosowanych dla tego typu prac w roku wykonywania szacowania;",
            "C": "obliczenie kosztu pozyskania informacji geologicznej, wyrażonego w nominalnych cenach z roku jej pozyskania i zrewaloryzowanego do poziomu cen z roku poprzedzającego rok wykonywania szacowania;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Przepisy wykonawcze ws. wyceny informacji geologicznej",
        "tresc_artykulu": "Określa procedury ustalania opłat za korzystanie z danych w sprawach hydrogeologicznych."
       }
    ],
    
    "BAZA PYTAŃ - CZĘŚĆ 3 (Pojęcia ogólne, własność górnicza, koncesje, kwalifikacje geologiczne)": [
        {
        "id": 1,
        "pytanie": "Ustawa Prawo geologiczne i górnicze określa zasady i warunki podejmowania, wykonywania oraz zakończenia działalności w zakresie:",
        "odpowiedzi": {
            "A": "naziemnego składowania odpadów;",
            "B": "wytwarzania, przetwarzania, magazynowania, przesyłania, dystrybucji i obrotu paliwami i energią;",
            "C": "bezzbiornikowego magazynowania substancji;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 1 ust. 1 pkt 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ustawa określa zasady i warunki podejmowania, wykonywania oraz zakończenia działalności w zakresie: (...) 3) bezzbiornikowego magazynowania substancji w górotworze, w tym w podziemnych wyrobiskach górniczych."
    },
    {
        "id": 2,
        "pytanie": "Ustawy Prawo geologiczne i górnicze nie stosuje się do:",
        "odpowiedzi": {
            "A": "drążenia tuneli z zastosowaniem techniki górniczej;",
            "B": "bezzbiornikowego magazynowania substancji w górotworze;",
            "C": "wydobywania kruszywa do wykonania pilnych prac zabezpieczających przed powodzią w czasie klęski żywiołowej;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 3 pkt 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ustawy nie stosuje się do: (...) 6) pozyskiwania drewna i kruszywa do wykonania pilnych prac zabezpieczających przed powodzią w czasie stanu klęski żywiołowej."
    },
    {
        "id": 3,
        "pytanie": "Kiedy konieczne będzie uzyskanie koncesji na wydobycie piasku i żwiru?",
        "odpowiedzi": {
            "A": "Piasek będzie wydobyty przez Jana Kowalskiego z nieruchomości stanowiącej jego własność w ilości 8 m³ jednorazowo oraz sprzedany firmie ABC sp. z o.o.,",
            "B": "Piasek będzie wydobywany przez Jana Kowalskiego w celu wykonania podmurówki jednorazowo w ilości ok. 5 m³ w roku, z nieruchomości stanowiącej jego własność;",
            "C": "Piasek będzie wydobywany przez ABC sp. z o.o. oraz wykorzystany w celu wykonania podmurówki w ilości ok. 5 m³ z nieruchomości stanowiącej jej własność,"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 4 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Robić bez koncesji wydobycie może tylko osoba fizyczna, z nieruchomości własnej, do 10 m³ w roku kalendarzowym, bez prawa rozporządzania (sprzedaży) wydobytą kopaliną i przeznaczając ją wyłącznie na własne potrzeby."
    },
    {
        "id": 4,
        "pytanie": "Za kopaliny uważa się:",
        "odpowiedzi": {
            "A": "Wody lecznicze, wody termalne i solanki",
            "B": "Tylko wody lecznicze;",
            "C": "Wody pochodzące z odwadniania kopalń"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 5 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Nie są kopalinami wody, z wyjątkiem wód leczniczych, wód termalnych i solanek."
    },
    {
        "id": 5,
        "pytanie": "Wodą termalną jest:",
        "odpowiedzi": {
            "A": "Każda woda podziemna o zawartości rozpuszczonych składników mineralnych nie mniejszej niż 35g/dm³;",
            "B": "Woda podziemna, która na wypływie z ujęcia ma temperaturę nie mniejszą niż 20°C;",
            "C": "Woda podgrzana w termie elektrycznej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 5 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wodą termalną jest woda podziemna, która na wypływie z ujęcia ma temperaturę nie mniejszą niż 20°C."
    },
    {
        "id": 6,
        "pytanie": "Informacją geologiczną w rozumieniu ustawy Prawo geologiczne i górnicze są:",
        "odpowiedzi": {
            "A": "Dane geologiczne;",
            "B": "Próbki geologiczne;",
            "C": "Opracowania danych geologicznych, w szczególności w dokumentacjach geologicznych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 6 ust. 1 pkt 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Informacja geologiczna to dane geologiczne, w tym próbki geologiczne, jak również opracowania danych geologicznych, w szczególności zawarte w dokumentacjach geologicznych."
    },
    {
        "id": 7,
        "pytanie": "Obszar górniczy to:",
        "odpowiedzi": {
            "A": "Przestrzeń w górotworze powstała w wyniku robót górniczych;",
            "B": "Przestrzeń, w granicach której przedsiębiorca jest uprawniony do wydobywania kopaliny oraz prowadzenia robót górniczych związanych z wykonywaniem koncesji;",
            "C": "Przestrzeń objęta przewidywanymi szkodliwymi wpływami robót górniczych zakładu górniczego;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 6 ust. 1 pkt 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Obszar górniczy – przestrzeń, w granicach której przedsiębiorca jest uprawniony do wydobywania kopaliny, podziemnego magazynowania substancji, podziemnego składowania odpadów oraz prowadzenia robót górniczych związanych z wykonywaniem koncesji."
    },
    {
        "id": 8,
        "pytanie": "Własnością górniczą objęte są złoża:",
        "odpowiedzi": {
            "A": "Węglowodorów;",
            "B": "metanu występującego jako kopalina towarzysząca,",
            "C": "Granitu;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 10 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoża węglowodorów, węgla kamiennego, metanu występującego jako kopalina towarzysząca (...) są objęte własnością górniczą."
    },
    {
        "id": 9,
        "pytanie": "Własnością górniczą objęte są złoża:",
        "odpowiedzi": {
            "A": "wód leczniczych,",
            "B": "wód termalnych,",
            "C": "Solanek;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 10 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoża wód leczniczych, wód termalnych i solanek są objęte własnością górniczą."
    },
    {
        "id": 10,
        "pytanie": "Własnością górniczą objęte są złoża:",
        "odpowiedzi": {
            "A": "węgla kamiennego,",
            "B": "rud pierwiastków promieniotwórczych,",
            "C": "gipsu i anhydrytu"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 10 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoża węgla kamiennego, rud pierwiastków promieniotwórczych (...) stanowią przedmiot własności górniczej."
    },
    {
        "id": 11,
        "pytanie": "Własnością górniczą nie są objęte złoża:",
        "odpowiedzi": {
            "A": "siarki rodzimej,",
            "B": "wapieni,",
            "C": "soli kamiennej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 10 ust. 1 i 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoża kopalin niewymienionych w ust. 1 i 2 (m.in. wapienie, gipsy, kruszywa) są objęte prawem własności nieruchomości gruntowej."
    },
    {
        "id": 12,
        "pytanie": "Własnością górniczą objęte są:",
        "odpowiedzi": {
            "A": "złoża rud metali z wyjątkiem darniowych rud żelaza,",
            "B": "części górotworu położone poza granicami przestrzennymi nieruchomości gruntowej, w szczególności znajdujące się w granicach obszarów morskich Rzeczypospolitej Polskiej,",
            "C": "nieruchomości gruntowe;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 10 ust. 1 i 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Własnością górniczą objęte są złoża rud metali z wyjątkiem darniowych rud żelaza oraz części górotworu położone poza granicami przestrzennymi nieruchomości gruntowej."
    },
    {
        "id": 13,
        "pytanie": "Prawo własności górniczej przysługuje:",
        "odpowiedzi": {
            "A": "Skarbowi Państwa,",
            "B": "właścicielom nieruchomości gruntowych,",
            "C": "marszałkom województw;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 10 ust. 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawo własności górniczej przysługuje Skarbowi Państwa."
    },
    {
        "id": 14,
        "pytanie": "Ustanowienie użytkowania górniczego następuje w drodze:",
        "odpowiedzi": {
            "A": "decyzji administracyjnej organu koncesyjnego,",
            "B": "umowy zawartej na piśmie pod rygorem nieważności,",
            "C": "zatwierdzenia dokumentacji geologicznej złoża kopaliny"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 13 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ustanowienie użytkowania górniczego następuje w drodze umowy zawartej na piśmie pod rygorem nieważności."
    },
    {
        "id": 15,
        "pytanie": "Aby żądać ustanowienia użytkowania górniczego z pierwszeństwem przed innymi, przedsiębiorca powinien:",
        "odpowiedzi": {
            "A": "rozpoznać złoże kopaliny, stanowiące przedmiot własności górniczej,",
            "B": "udokumentować złoże kopaliny w stopniu umożliwiającym sporządzenie projektu zagospodarowania złoża,",
            "C": "uzyskać decyzję zatwierdzającą dokumentację geologiczną złoża kopaliny;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 15 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ten, kto poszukiwał lub rozpoznał złoże kopaliny (...) i udokumentował je w stopniu umożliwiającym sporządzenie PZZ oraz uzyskał decyzję zatwierdzającą dokumentację geologiczną, może żądać ustanowienia użytkowania górniczego z pierwszeństwem przed innymi."
    },
    {
        "id": 16,
        "pytanie": "Aby żądać ustanowienia użytkowania górniczego z pierwszeństwem przed innymi, przedsiębiorca powinien:",
        "odpowiedzi": {
            "A": "rozpoznać złoże kopaliny, stanowiące przedmiot własności górniczej,",
            "B": "udokumentować złoże kopaliny w stopniu umożliwiającym sporządzenie projektu zagospodarowania złoża,",
            "C": "utworzyć fundusz likwidacji zakładu górniczego;"
        },
        "poprawne": ["A","B"],
        "podstawa_prawna": "Art. 15 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podstawą żądania pierwszeństwa jest udokumentowanie złoża w stopniu umożliwiającym sporządzenie PZZ."
    },
    {
        "id": 17,
        "pytanie": "Żądanie ustanowienia użytkowania górniczego z pierwszeństwem przed innymi wygasa z upływem:",
        "odpowiedzi": {
            "A": "5 lat od dnia doręczenia decyzji zatwierdzającej dokumentację geologiczną złoża kopaliny,",
            "B": "3 lat od dnia doręczenia decyzji zatwierdzającej dokumentację geologiczną złoża kopaliny,",
            "C": "4 lat od dnia doręczenia dokumentacji geologicznej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 15 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prawo żądania ustanowienia użytkowania górniczego wygasa z upływem 5 lat od dnia doręczenia decyzji zatwierdzającej dokumentację geologiczną złoża kopaliny."
    },
    {
        "id": 18,
        "pytanie": "Jeżeli cudza nieruchomość lub jej część jest niezbędna do wykonywania działalności regulowanej ustawą Prawo geologiczne i górnicze przedsiębiorca może żądać umożliwienia korzystania z tej nieruchomości lub jej części:",
        "odpowiedzi": {
            "A": "przez czas nieoznaczony, bezpłatnie,",
            "B": "przez czas nieoznaczony, za wynagrodzeniem,",
            "C": "przez czas oznaczony, za wynagrodzeniem;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 18 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Jeżeli cudza nieruchomość (...) jest niezbędna do wykonywania działalności (...) przedsiębiorca może żądać umożliwienia korzystania z tej nieruchomości lub jej części przez czas oznaczony, za wynagrodzeniem."
    },
    {
        "id": 19,
        "pytanie": "Korzystanie z wód kopalnianych dla zaspokojenia potrzeb zakładu górniczego jest:",
        "odpowiedzi": {
            "A": "płatne,",
            "B": "bezpłatne,",
            "C": "zabronione;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 20 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Korzystanie z wód pochodzących z odwodnienia wyrobisk górniczych dla potrzeb zakładu górniczego jest bezpłatne."
    },
    {
        "id": 20,
        "pytanie": "Prawem własności nieruchomości gruntowej objęte są złoża:",
        "odpowiedzi": {
            "A": "piasku i żwiru,",
            "B": "wapieni,",
            "C": "gipsu i anhydrytu"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 10 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoża kopalin niewymienionych w ust. 1 i 2 (m.in. piaski, żwiry, wapienie, gipsy i anhydryty) są objęte prawem własności nieruchomości gruntowej."
    },
    {
        "id": 21,
        "pytanie": "Obiekty, urządzenia oraz instalacje wzniesione w przestrzeni objętej użytkowaniem górniczym stanowią własność:",
        "odpowiedzi": {
            "A": "Skarbu Państwa,",
            "B": "użytkownika górniczego,",
            "C": "organu koncesyjnego."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 16 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Obiekty, urządzenia oraz instalacje wzniesione w przestrzeni objętej użytkowaniem górniczym stanowią własność użytkownika górniczego."
    },
    {
        "id": 22,
        "pytanie": "W przypadku likwidacji zakładu górniczego, w całości lub w części, przedsiębiorca jest obowiązany:",
        "odpowiedzi": {
            "A": "zabezpieczyć lub zlikwidować wyrobiska górnicze oraz urządzenia, instalacje i obiekty zakładu górniczego,",
            "B": "zabezpieczyć niewykorzystaną część złoża kopaliny,",
            "C": "zabezpieczyć sąsiednie złoża kopalin;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 129 ust. 1 pkt 1, 2, 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku likwidacji zakładu górniczego przedsiębiorca jest obowiązany: zabezpieczyć lub zlikwidować wyrobiska, zabezpieczyć niewykorzystaną część złoża oraz zabezpieczyć sąsiednie złoża."
    },
    {
        "id": 23,
        "pytanie": "W przypadku likwidacji zakładu górniczego, w całości lub w części, przedsiębiorca jest obowiązany:",
        "odpowiedzi": {
            "A": "zabezpieczyć niewykorzystaną część złoża kopaliny,",
            "B": "zabezpieczyć sąsiednie złoża kopalin,",
            "C": "przedsięwziąć niezbędne środki chroniące wyrobiska sąsiednich zakładów górniczych"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 129 ust. 1 pkt 2, 3, 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca likwidujący zakład górniczy zabezpiecza niewykorzystane i sąsiednie złoża oraz podejmuje kroki w celu ochrony wyrobisk sąsiednich zakładów górniczych."
    },
    {
        "id": 24,
        "pytanie": "W przypadku likwidacji zakładu górniczego, w całości lub w części, przedsiębiorca jest obowiązany:",
        "odpowiedzi": {
            "A": "przedsięwziąć niezbędne środki chroniące wyrobiska sąsiednich zakładów górniczych,",
            "B": "zabezpieczyć sąsiednie złoża kopalin,",
            "C": "przedsięwziąć niezbędne środki w celu ochrony środowiska oraz rekultywacji gruntów po działalności górniczej"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 129 ust. 1 pkt 3, 4, 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Obowiązki przy likwidacji obejmują ochronę wyrobisk sąsiednich zakładów, zabezpieczenie sąsiednich złóż oraz ochronę środowiska i rekultywację."
    },
    {
        "id": 25,
        "pytanie": "W przypadku likwidacji zakładu górniczego, w całości lub w części, przedsiębiorca jest obowiązany:",
        "odpowiedzi": {
            "A": "zabezpieczyć lub zlikwidować wyrobiska górnicze oraz urządzenia, instalacje i obiekty zakładu górniczego,",
            "B": "zabezpieczyć niewykorzystaną część złoża kopaliny,",
            "C": "sporządzić dokumentację hydrogeologiczną;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 129 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wśród ustawowych obowiązków likwidacji zakładu wymieniono zabezpieczenie/likwidację wyrobisk oraz zabezpieczenie niewykorzystanej części złoża."
    },
    {
        "id": 25,
        "pytanie": "Plan ruchu likwidowanego zakładu górniczego wymaga uzgodnienia z:",
        "odpowiedzi": {
            "A": "wójtem (burmistrzem, prezydentem),",
            "B": "marszałkiem województwa,",
            "C": "starostą;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 108 ust. 5 (Art 129 ust. 5 uchylony) Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Plan ruchu likwidowanego zakładu górniczego wymaga uzgodnienia z właściwym wójtem (burmistrzem, prezydentem miasta)."
    },
    {
        "id": 26,
        "pytanie": "Do rekultywacji gruntów po działalności górniczej stosuje się przepisy:",
        "odpowiedzi": {
            "A": "ustawy o ochronie gruntów rolnych i leśnych,",
            "B": "Kodeksu postępowania administracyjnego,",
            "C": "ustawy o swobodzie działalności gospodarczej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 129 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do rekultywacji gruntów po działalności górniczej stosuje się przepisy o ochronie gruntów rolnych i leśnych."
    },
    {
        "id": 27,
        "pytanie": "Obowiązek przeznaczania środków na fundusz likwidacji zakładu górniczego powstaje w przypadku wydobywania kopalin ze złóż:",
        "odpowiedzi": {
            "A": "od dnia udzielenia koncesji na wydobywanie kopaliny,",
            "B": "od dnia wymagalności opłaty eksploatacyjnej,",
            "C": "od dnia wydania decyzji o zatwierdzeniu dokumentacji geologicznej złoża kopaliny;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 128 ust. 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Obowiązek tworzenia funduszu likwidacji zakładu górniczego powstaje od dnia powstania obowiązku uiszczania opłaty eksploatacyjnej."
    },
    {
        "id": 28,
        "pytanie": "Która, z wymienionych obok działalności wymaga uzyskania koncesji:",
        "odpowiedzi": {
            "A": "Poszukiwanie i rozpoznawanie złóż gipsu i anhydrytu,",
            "B": "Poszukiwanie i rozpoznawanie złóż wód leczniczych",
            "C": "Poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 21 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Działalność w zakresie poszukiwania lub rozpoznawania złóż kopalin objętych własnością górniczą (m.in. wód leczniczych) wymaga koncesji."
    },
    {
        "id": 29,
        "pytanie": "Która, z wymienionych obok działalności wymaga uzyskania koncesji:",
        "odpowiedzi": {
            "A": "Poszukiwanie i rozpoznawanie złóż rud miedzi;",
            "B": "Poszukiwanie i rozpoznawanie złóż solanek;",
            "C": "Podziemne składowanie odpadów"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 21 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesji wymaga poszukiwanie/rozpoznawanie złóż stanowiących własność górniczą (rudy miedzi, solanki) oraz podziemne składowanie odpadów."
    },
    {
        "id": 30,
        "pytanie": "Która, z wymienionych obok działalności wymaga uzyskania koncesji:",
        "odpowiedzi": {
            "A": "Poszukiwanie i rozpoznawanie złóż soli potasowo – magnezowej;",
            "B": "Wydobywanie złóż soli potasowo – magnezowej ze złoża;",
            "C": "Poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 21 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesji wymaga poszukiwanie, rozpoznawanie oraz wydobywanie kopalin ze złóż objętych własnością górniczą (m.in. soli potasowo-magnezowych)."
    },
    {
        "id": 31,
        "pytanie": "Która, z wymienionych obok działalności wymaga uzyskania koncesji:",
        "odpowiedzi": {
            "A": "Wydobywanie kopalin ze złóż",
            "B": "Podziemne bezzbiornikowe magazynowanie substancji",
            "C": "Poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 21 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesji wymaga wydobywanie kopalin ze złóż oraz podziemne bezzbiornikowe magazynowanie substancji."
    },
    {
        "id": 32,
        "pytanie": "Koncesji udziela się na czas:",
        "odpowiedzi": {
            "A": "Nie dłuższy niż 50 lat",
            "B": "Nie dłuższy niż 10 lat",
            "C": "Bez ograniczeń w czasie"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 21 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesji udziela się na czas oznaczony, nie krótszy niż 3 lata i nie dłuższy niż 50 lat, chyba że wnioskodawca wnosi o udzielenie koncesji na czas krótszy."
    },
    {
        "id": 33,
        "pytanie": "Minister środowiska udziela koncesji na:",
        "odpowiedzi": {
            "A": "Poszukiwanie złóż węgla brunatnego",
            "B": "Poszukiwanie i rozpoznawanie złóż wód termalnych",
            "C": "Podziemne składowanie odpadów"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 22 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister właściwy do spraw środowiska udziela koncesji na poszukiwanie/rozpoznawanie złóż objętych własnością górniczą, podziemne magazynowanie substancji oraz podziemne składowanie odpadów."
    },
    {
        "id": 34,
        "pytanie": "Minister środowiska udziela koncesji na:",
        "odpowiedzi": {
            "A": "Wydobywanie soli kamiennej;",
            "B": "Wydobywanie kruszywa naturalnego z dna Morza Bałtyckiego w granicach obszarów morskich RP;",
            "C": "Wydobywanie wapieni z użyciem środków strzałowych"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 22 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Minister udziela koncesji na wydobywanie kopalin ze złóż objętych własnością górniczą (soli kamiennej) oraz wydobywanie kopalin w granicach obszarów morskich RP."
    },
    {
        "id": 35,
        "pytanie": "Starosta udziela koncesji na wydobywanie kopalin ze złóż, jeżeli spełnione są jednocześnie trzy wymagania. Wskaż, które muszą być spełnione aby koncesji mógł udzielić starosta (które nie dyskwalifikują starostę jako organ koncesyjny):",
        "odpowiedzi": {
            "A": "Obszar udokumentowanego złoża objętego własnością górniczą nie przekracza 2 ha;",
            "B": "Wydobycie kopaliny ze złoża w roku kalendarzowym nie przekroczy 20 000 m³;",
            "C": "Działalność będzie prowadzona metodą głębinową, bez użycia środków strzałowych;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Starosta udziela koncesji na wydobywanie kopalinii, jeżeli obszar złoża nieobjętego własnością górniczą nie przekracza 2 ha, wydobycie w roku nie przekroczy 20 000 m³, a prace prowadzone są metodą odkrywkową bez środków strzałowych."
    },
    {
        "id": 36,
        "pytanie": "Starosta udziela koncesji na wydobywanie kopalin ze złóż, jeżeli spełnione są jednocześnie trzy wymagania. Wskaż, które muszą być spełnione aby koncesji mógł udzielić starosta (które nie dyskwalifikują starostę jako organ koncesyjny):",
        "odpowiedzi": {
            "A": "Obszar udokumentowanego złoża nieobjętego własnością górniczą nie przekracza 2 ha;",
            "B": "Wydobycie kopaliny ze złoża nie przekroczy 20 000 m³ kwartalnie, i wyniesie nie więcej niż 80 000 m³ rocznie;",
            "C": "Działalność będzie prowadzona metodą odkrywkową, bez użycia środków strzałowych;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kryteria właściwości starosty to: złoże nieobjęte własnością górniczą do 2 ha, odkrywka bez użycia środków strzałowych oraz limit roczny wydobycia do 20 000 m³."
    },
    {
        "id": 37,
        "pytanie": "Starosta udziela koncesji na wydobywanie kopalin ze złóż, jeżeli spełnione są jednocześnie trzy wymagania. Wskaż, które muszą być spełnione aby koncesji mógł udzielić starosta (które nie dyskwalifikują starostę jako organ koncesyjny):",
        "odpowiedzi": {
            "A": "Obszar udokumentowanego złoża nieobjętego własnością górniczą nie przekracza 2 ha;",
            "B": "Wydobycie kopaliny ze złoża w roku kalendarzowym nie przekroczy 20 000 m³;",
            "C": "Działalność będzie prowadzona metodą odkrywkową, z użyciem środków strzałowych;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wymagania dla starosty obejmują obszar do 2 ha oraz roczne wydobycie do 20 000 m³ (użycie środków strzałowych dyskwalifikuje starostę)."
    },
    {
        "id": 38,
        "pytanie": "Koncesji na wydobywanie granitu, jeżeli wydobycie w roku kalendarzowym wyniesie 15 000 m³ udziela:",
        "odpowiedzi": {
            "A": "Minister właściwy do spraw środowiska;",
            "B": "Marszałek województwa;",
            "C": "Starosta"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Granit nie podlega własności górniczej. Jeżeli spełnia warunki metody odkrywkowej bez materiałów wybuchowych oraz progu do 20 000 m³/rok, organem jest starosta."
    },
    {
        "id": 39,
        "pytanie": "Koncesji na wydobywanie kaolinu, jeżeli obszar udokumentowanego złoża wynosi 20 ha, udziela:",
        "odpowiedzi": {
            "A": "Marszałek województwa;",
            "B": "Minister właściwy do spraw środowiska;",
            "C": "Starosta"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Ponieważ powierchnia złoża przekracza 2 ha (wynosi 20 ha), właściwym organem koncesyjnym staje się marszałek województwa."
    },
    {
        "id": 40,
        "pytanie": "Koncesji na wydobywanie siarki rodzimej, jeżeli obszar udokumentowanego złoża wynosi 350 ha, udziela:",
        "odpowiedzi": {
            "A": "Minister właściwy do spraw środowiska;",
            "B": "Marszałek województwa;",
            "C": "Starosta"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 22 ust. 1 pkt 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Siarka rodzima objęta jest własnością górniczą, dlatego koncesji na jej wydobywanie udziela Minister właściwy do spraw środowiska."
    },
    {
        "id": 41,
        "pytanie": "Koncesji na wydobywanie marmuru, jeżeli eksploatacja będzie prowadzona z użyciem środków strzałowych, udziela:",
        "odpowiedzi": {
            "A": "Marszałek województwa;",
            "B": "Minister właściwy do spraw środowiska;",
            "C": "Starosta"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Użycie środków strzałowych wyklucza właściwość starosty, przekazując kompetencje marszałkowi województwa."
    },
    {
        "id": 42,
        "pytanie": "Udzielenie koncesji na wydobywanie złóż węgla kamiennego wymaga uzgodnienia z:",
        "odpowiedzi": {
            "A": "Ministrem właściwym do spraw gospodarki;",
            "B": "Ministrem spraw wewnętrznych;",
            "C": "Ministrem rozwoju regionalnego"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 23 ust. 1 pkt 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Udzielenie koncesji na wydobywanie węgla kamiennego wymaga uzgodnienia z ministrem właściwym do spraw gospodarki."
    },
    {
        "id": 43,
        "pytanie": "Opinia Prezesa Państwowej Agencji Atomistyki wymagana jest przed udzieleniem koncesji na:",
        "odpowiedzi": {
            "A": "Poszukiwanie lub rozpoznawanie rud pierwiastków promieniotwórczych;",
            "B": "Wydobywanie rud pierwiastków promieniotwórczych ze złóż;",
            "C": "Podziemne składowanie odpadów promieniotwórczych;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 23 ust. 2 pkt 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Udzielenie koncesji na poszukiwanie, rozpoznawanie lub wydobywanie rud pierwiastków promieniotwórczych wymaga opinii Prezesa Państwowej Agencji Atomistyki."
    },
    {
        "id": 44,
        "pytanie": "Udzielenie koncesji na wydobywanie kopalin z obszaru bezpośredniego lub potencjalnego zagrożenia powodzią wymaga:",
        "odpowiedzi": {
            "A": "Uzgodnienia z organem odpowiedzialnym za utrzymanie wód;",
            "B": "Opinii organu właściwego do wydania pozwolenia wodnoprawnego;",
            "C": "Uzgodnienia z ministrem właściwym do spraw gospodarki morskiej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 23 ust. 1 pkt 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Udzielenie koncesji na obszarach zagrożenia powodziowego wymaga uzgodnienia z organem odpowiedzialnym za utrzymanie wód (Wody Polskie)."
    },
    {
        "id": 45,
        "pytanie": "We wniosku o udzielenie koncesji, poza wymaganiami przewidzianymi przepisami z zakresu ochrony środowiska i działalności gospodarczej, określa się m. in.:",
        "odpowiedzi": {
            "A": "Stan prawny nieruchomości, w granicach których ma być wykonywana zamierzona działalność;",
            "B": "Czas, na jaki koncesja ma być udzielona, bez wskazania terminu rozpoczęcia działalności;",
            "C": "Sposób przeciwdziałania ujemnym wpływom zamierzonej działalności na środowisko;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 24 ust. 1 pkt 1, 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wniosek o udzielenie koncesji zawiera stan prawny nieruchomości oraz proponowane sposoby przeciwdziałania ujemnym wpływom na środowisko."
    },
    {
        "id": 46,
        "pytanie": "We wniosku o udzielenie koncesji na poszukiwanie i rozpoznawanie węglowodorów, poza wymaganiami przewidzianymi przepisami z zakresu ochrony środowiska i działalności gospodarczej, określa się m. in.:",
        "odpowiedzi": {
            "A": "Stan prawny nieruchomości, w granicach których ma być wykonywana zamierzona działalność;",
            "B": "Środki, jakimi wnioskodawca dysponuje w celu zapewnienia prawidłowego wykonywania zamierzonej działalności;",
            "C": "Sposób przeciwdziałania ujemnym wpływom zamierzonej działalności na środowisko;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 24 ust. 1 oraz Art. 24a Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wniosek obejmuje stan prawny gruntów, środki finansowe/techniczne oraz metody ochrony środowiska."
    },
    {
        "id": 47,
        "pytanie": "We wniosku o udzielenie koncesji na wydobywanie miedzi, poza wymaganiami przewidzianymi przepisami z zakresu ochrony środowiska i działalności gospodarczej, określa się m. in.:",
        "odpowiedzi": {
            "A": "Stan prawny nieruchomości, w granicach których ma być wykonywana zamierzona działalność;",
            "B": "Czas, na jaki koncesja ma być udzielona, ze wskazaniem terminu rozpoczęcia działalności;",
            "C": "Sposób przeciwdziałania ujemnym wpływom zamierzonej działalności na rynkowe ceny miedzi;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 24 ust. 1 pkt 1, 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wniosek o koncesję na wydobywanie kopaliny określa stan prawny nieruchomości oraz czas trwania koncesji ze wskazaniem terminu rozpoczęcia działalności."
    },
    {
        "id": 48,
        "pytanie": "Do wniosku o udzielenie koncesji na poszukiwanie lub rozpoznawanie złoża kopaliny, w przypadku zamierzonego wykonywania robót geologicznych, dołącza się:",
        "odpowiedzi": {
            "A": "2 egzemplarze projektu robót geologicznych;",
            "B": "Kopię decyzji zatwierdzającej projekt robót geologicznych;",
            "C": "Projekt zagospodarowania złoża;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 25 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do wniosku o udzielenie koncesji na poszukiwanie lub rozpoznawanie złoża kopaliny dołącza się projekt robót geologicznych w 2 egzemplarzach."
    },
    {
        "id": 49,
        "pytanie": "Do wniosku o udzielenie koncesji na wydobywanie kopalin ze złóż dołącza się:",
        "odpowiedzi": {
            "A": "2 egzemplarze projektu robót geologicznych;",
            "B": "Dowody istnienia prawa do korzystania z informacji geologicznej, jakie w zakresie niezbędnym do prowadzenia zamierzonej działalności przysługuje wnioskodawcy",
            "C": "Kopię decyzji zatwierdzającej dokumentację geologiczną"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 26 ust. 1 pkt 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do wniosku o koncesję wydobywczą dołącza się dowód prawa do informacji geologicznej oraz projekt zagospodarowania złoża."
    },
    {
        "id": 50,
        "pytanie": "Do wniosku o udzielenie koncesji przez starostę na wydobywanie kopalin ze złóż dołącza się:",
        "odpowiedzi": {
            "A": "Dowody istnienia prawa do korzystania z informacji geologicznej, jakie w zakresie niezbędnym do prowadzenia zamierzonej działalności przysługuje wnioskodawcy",
            "B": "Kopię decyzji zatwierdzającej dokumentację geologiczną",
            "C": "Projekt zagospodarowania złoża"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 26 ust. 1 i 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Niezależnie od organu, do wniosku dołącza się dowód prawa do informacji geologicznej oraz projekt zagospodarowania złoża."
    },
    {
        "id": 51,
        "pytanie": "Organ koncesyjny odmawia udzielenia koncesji jeżeli:",
        "odpowiedzi": {
            "A": "Zamierzona działalność sprzeciwia się interesowi publicznemu, w szczególności związanemu z bezpieczeństwem państwa,",
            "B": "Zamierzona działalność sprzeciwia się interesowi publicznemu, w szczególności związanemu z racjonalną gospodarką złożami kopalin;",
            "C": "Zamierzona działalność uniemożliwiłaby wykorzystanie nieruchomości zgodnie z przeznaczeniem określonym przez miejscowy plan zagospodarowania przestrzennego;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 29 ust. 1 pkt 1, 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Organ odmawia koncesji, gdy działalność sprzeciwia się interesowi publicznemu lub uniemożliwia wykorzystanie nieruchomości wg MPZP."
    },
    {
        "id": 52,
        "pytanie": "Odmowa udzielenia koncesji na podziemne składowanie odpadów następuje w przypadku gdy:",
        "odpowiedzi": {
            "A": "istnieje uzasadniona technicznie, ekologicznie lub ekonomicznie możliwość ich (odpadów) odzysku;",
            "B": "istnieje możliwość unieszkodliwienia odpadów w inny sposób niż przez ich składowanie;",
            "C": "Zamierzona działalność sprzeciwia się interesowi publicznemu, w szczególności związanemu z bezpieczeństwem państwa;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 29 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Odmowa udzielenia koncesji na składowanie odpadów następuje, gdy istnieje możliwość ich odzysku lub unieszkodliwienia w inny sposób, albo gdy sprzeciwia się to interesowi publicznemu."
    },
    {
        "id": 53,
        "pytanie": "Koncesja określa m.in.:",
        "odpowiedzi": {
            "A": "Rodzaj i sposób wykonywania zamierzonej działalności;",
            "B": "Przestrzeń, w granicach której ma być wykonywana zamierzona działalność;",
            "C": "Czas obowiązywania koncesji;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 30 ust. 1 pkt 1, 2, 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja określa rodzaj i sposób wykonywania działalności, przestrzeń wykonywania oraz czas jej obowiązywania."
    },
    {
        "id": 54,
        "pytanie": "Koncesja określa m.in.:",
        "odpowiedzi": {
            "A": "Termin rozpoczęcia działalności określonej koncesją, a w razie potrzeby – przesłanki, których spełnienie oznacza rozpoczęcie działalności;",
            "B": "Rodzaj i sposób wykonywania zamierzonej działalności;",
            "C": "Przestrzeń, w granicach której ma być wykonywana zamierzona działalność;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 30 ust. 1 pkt 1, 2, 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja określa m.in. termin rozpoczęcia działalności, rodzaj i sposób prac oraz granice przestrzenne."
    },
    {
        "id": 55,
        "pytanie": "Koncesja na poszukiwanie lub rozpoznawanie złoża kopaliny określa m.in.:",
        "odpowiedzi": {
            "A": "Cel, zakres i rodzaj zamierzonych prac geologicznych;",
            "B": "Zakres i harmonogram przekazywania informacji geologicznych i próbek uzyskanych w wyniku wykonywania robót geologicznych;",
            "C": "Wysokość opłaty za działalność określoną w koncesji;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 31 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja na poszukiwanie/rozpoznawanie określa cel, zakres i rodzaj prac, harmonogram przekazywania informacji oraz opłatę."
    },
    {
        "id": 56,
        "pytanie": "Koncesja na poszukiwanie lub rozpoznawanie złoża kopaliny określa m.in.:",
        "odpowiedzi": {
            "A": "Cel, zakres i rodzaj zamierzonych prac geologicznych;",
            "B": "Zakres i harmonogram przekazywania informacji geologicznych i próbek uzyskanych w wyniku wykonywania robót geologicznych;",
            "C": "Minimalny stopień wykorzystania zasobów złoża;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 31 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja poszukiwawcza zawiera cel, zakres i harmonogram prac (stopień wykorzystania dotyczy koncesji wydobywczej)."
    },
    {
        "id": 57,
        "pytanie": "Maksymalna powierzchnia terenu objętego koncesją na poszukiwanie lub rozpoznawanie złoża kopaliny wynosi:",
        "odpowiedzi": {
            "A": "1200 km²",
            "B": "2400 km²",
            "C": "Nie ma górnej granicy powierzchni terenu objętego koncesją na poszukiwanie lub rozpoznawanie złoża kopaliny"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 31 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Powierzchnia terenu objętego koncesją na poszukiwanie lub rozpoznawanie złoża kopaliny nie może przekraczać 1200 km²."
    },
    {
        "id": 58,
        "pytanie": "Granice obszaru i terenu górniczego wyznaczane są w koncesji:",
        "odpowiedzi": {
            "A": "na poszukiwanie lub rozpoznawanie złoża kopaliny",
            "B": "Na podziemne bezzbiornikowe magazynowanie substancji do górotworu",
            "C": "Na wydobywanie kopaliny ze złoża"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 32 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Obszar i teren górniczy wyznacza się w koncesji na wydobywanie kopaliny, magazynowanie substancji lub składowanie odpadów."
    },
    {
        "id": 59,
        "pytanie": "Koncesja na wydobywanie kopaliny ze złoża może określać:",
        "odpowiedzi": {
            "A": "Minimalny stopień wykorzystywania zasobów złoża;",
            "B": "Warunki wtłaczania wód pochodzących z odwodnienia wyrobisk górniczych;",
            "C": "Przedsięwzięcia niezbędne w zakresie racjonalnej gospodarki złożem;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 32 ust. 2, 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja wydobywcza może określać minimalne wykorzystanie zasobów, racjonalną gospodarkę oraz warunki wtłaczania wód z odwodnień."
    },
    {
        "id": 60,
        "pytanie": "Koncesja na podziemne składowanie odpadów określa m.in.:",
        "odpowiedzi": {
            "A": "Typ podziemnego składowiska;",
            "B": "Rodzaj i ilość odpadów dopuszczonych do składowania,",
            "C": "Zakres i sposób monitorowania składowiska;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 32 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja na składowanie odpadów określa ich typ, rodzaj i ilość oraz metody monitorowania."
    },
    {
        "id": 61,
        "pytanie": "Przedsiębiorca jest obowiązany niezwłocznie złożyć wniosek o dokonanie zmiany koncesji, jeżeli:",
        "odpowiedzi": {
            "A": "Rzeczywiste szkodliwe wpływy robót górniczych zakładu górniczego przekroczą wyznaczone w koncesji granice terenu górniczego;",
            "B": "Rzeczywiste szkodliwe wpływy robót górniczych zakładu górniczego przekroczą wyznaczone w koncesji granice obszaru górniczego;",
            "C": "Rzeczywiste szkodliwe wpływy robót górniczych zakładu górniczego przekroczą wyznaczone w koncesji granice obszaru poszukiwań złóż;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 34 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku gdy przewidywane szkodliwe wpływy robót przekroczą granice terenu górniczego, przedsiębiorca niezwłocznie wnioskuje o zmianę koncesji."
    },
    {
        "id": 62,
        "pytanie": "Rejestr obszarów górniczych prowadzi:",
        "odpowiedzi": {
            "A": "państwowa służba geologiczna;",
            "B": "Prezes Wyższego Urzędu Górniczego;",
            "C": "Minister właściwy do spraw gospodarki nieruchomościami;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 167 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Rejestr obszarów górniczych prowadzi państwowa służba geologiczna (PIG-PIB)."
    },
    {
        "id": 63,
        "pytanie": "Rejestr obszarów górniczych prowadzi:",
        "odpowiedzi": {
            "A": "państwowa służba geologiczna;",
            "B": "okręgowe urzędy górnicze",
            "C": "Minister właściwy do spraw administracji;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 167 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Rejestr obszarów górniczych prowadzi państwowa służba geologiczna."
    },
    {
        "id": 64,
        "pytanie": "Koncesja wygasa:",
        "odpowiedzi": {
            "A": "Z upływem czasu, na jaki została udzielona;",
            "B": "Jeżeli stała się bezprzedmiotowa",
            "C": "W przypadku jej zrzeczenia się;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 38 ust. 1 pkt 1, 2, 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesja wygasa: z upływem czasu, gdy stała się bezprzedmiotowa lub w przypadku jej zrzeczenia się."
    },
    {
        "id": 65,
        "pytanie": "Koncesja wygasa:",
        "odpowiedzi": {
            "A": "Z upływem czasu, na jaki została udzielona;",
            "B": "W przypadku śmierci przedsiębiorcy będącego osobą fizyczną",
            "C": "W przypadku likwidacji przedsiębiorcy innego niż osoba fizyczna;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 38 ust. 1 pkt 1, 4, 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przyczynami wygaśnięcia koncesji są: upływ czasu, śmierć przedsiębiorcy będącego osobą fizyczną oraz likwidacja podmiotu."
    },
    {
        "id": 66,
        "pytanie": "Wskaż warunki, które musi spełnić podmiot, aby koncesja mogła być przeniesiona na jego rzecz:",
        "odpowiedzi": {
            "A": "W zakresie niezbędnym do wykonywania zamierzonej działalności podmiot musi wykazać się prawem do korzystania z informacji geologicznej;",
            "B": "Podmiot musi wykazać, iż jest w stanie spełnić wymagania związane z wykonywaniem zamierzonej działalności;",
            "C": "Podmiot musi wyrazić zgodę na przyjęcie wszystkich warunków określonych w koncesji;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 36 ust. 1 pkt 1, 2, 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przeniesienie koncesji wymaga akceptacji warunków koncesji, wykazania możliwości spełnienia wymogów oraz prawa do informacji geologicznej."
    },
    {
        "id": 67,
        "pytanie": "Wskaż dokumenty, które są podstawą wyznaczenia granic obszaru górniczego:",
        "odpowiedzi": {
            "A": "Projekt robót geologicznych;",
            "B": "Dokumentacja geologiczna;",
            "C": "Projekt zagospodarowania złoża"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 32 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Granice obszaru i terenu górniczego wyznacza się na podstawie dokumentacji geologicznej i projektu zagospodarowania złoża."
    },
    {
        "id": 68,
        "pytanie": "Zgodnie z Prawem geologicznymi i górniczym zabronione jest:",
        "odpowiedzi": {
            "A": "Poszukiwanie lub rozpoznawanie kopalin w granicach obszarów morskich;",
            "B": "Poszukiwanie lub rozpoznawanie złóż kopalin objętych własnością górniczą bez koncesji;",
            "C": "Poszukiwanie lub rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 21 ust. 1 pkt 1 w zw. z Art. 177 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Wykonywanie działalności w zakresie poszukiwania lub rozpoznawania złóż stanowiących własność górniczą bez wymaganej koncesji jest zabronione i karalne."
    },
    {
        "id": 69,
        "pytanie": "Zgodnie z Prawem geologicznym i górniczym zakazane oraz zagrożone karą pozbawienia wolności lub grzywny jest:",
        "odpowiedzi": {
            "A": "Niezastosowanie się do decyzji organu nakazującej wstrzymanie wydobywania kopalin ze złóż;",
            "B": "Kierowanie pracami geologicznymi bez wymaganych kwalifikacji;",
            "C": "Podziemne bezzbiornikowe magazynowanie substancji bez koncesji;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 176 i Art. 177 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prowadzenie magazynowania bez koncesji oraz nieprzestrzeganie decyzji o wstrzymaniu wydobycia stanowią czyn zabroniony zagrożony karą."
    },
    {
        "id": 70,
        "pytanie": "W przypadku naruszenia przez przedsiębiorcę obowiązków określonych w koncesji na wydobywanie kopalin ze złoża oraz wyrządzenia poważnej szkody w środowisku organ koncesyjny:",
        "odpowiedzi": {
            "A": "zakazuje przedsiębiorcy prowadzenia działalności polegającej na wydobywaniu kopalin na okres od 3 do 10 lat;",
            "B": "wzywa do niezwłocznego usunięcia naruszeń pod rygorem cofnięcia koncesji lub ograniczenia jej zakresu bez odszkodowania;",
            "C": "Zawiadamia o nieprawidłowości Państwową Inspekcję Geologiczną;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 37 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku naruszenia warunków koncesji organ wzywa do usunięcia uchybień, a w przypadku braku reakcji cofa koncesję lub ogranicza jej zakres bez odszkodowania."
    },
    {
        "id": 71,
        "pytanie": "Właściciel nieruchomości znajdującej się w pobliżu zakładu górniczego:",
        "odpowiedzi": {
            "A": "Może skutecznie dochodzić przed sądem powszechnym nałożenia na zakład górniczy zakazu prowadzenia działalności;",
            "B": "Nie może sprzeciwić się zagrożeniom spowodowanym ruchem zakładu górniczego, jeżeli jest prowadzony zgodnie z ustawą;",
            "C": "Może żądać naprawienia szkody wyrządzonej ruchem zakładu górniczego;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 144 ust. 1 i Art. 145 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Właściciel nie może sprzeciwić się działaniom zgodnym z ustawą, lecz przysługuje mu roszczenie o naprawienie szkody."
    },
    {
        "id": 72,
        "pytanie": "Zasady odpowiedzialności zakładów górniczych za szkody wyrządzone w związku z ich ruchem określa:",
        "odpowiedzi": {
            "A": "Ustawa z dnia 9 czerwca 2011 r. Prawo geologiczne i górnicze;",
            "B": "Kodeks postępowania administracyjnego, w zakresie neuregulowanym w ustawie Prawo geologiczne i górnicze;",
            "C": "Kodeks cywilny, w zakresie nieuregulowanym w ustawie Prawo geologiczne i górnicze;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 144 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Do odpowiedzialności za szkody stosuje się przepisy PGiG, a w sprawach nieuregulowanych – przepisy Kodeksu cywilnego."
    },
    {
        "id": 73,
        "pytanie": "Odpowiedzialność za szkodę spowodowaną ruchem zakładu górniczego ponosi:",
        "odpowiedzi": {
            "A": "Właściciel nieruchomości, na której znajduje się zakład górniczy, z którego działalnością związane jest powstanie szkody;",
            "B": "Przedsiębiorca prowadzący ruch zakładu górniczego;",
            "C": "Skarb Państwa, gdy nie istnieje przedsiębiorca odpowiedzialny za szkodę ani jego następca prawny;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 146 ust. 1 i ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Za szkodę odpowiada przedsiębiorca prowadzący ruch zakładu, a pomocniczo Skarb Państwa w przypadku braku przedsiębiorcy lub jego następcy."
    },
    {
        "id": 74,
        "pytanie": "Kto odpowiada za szkodę spowodowaną ruchem zakładu górniczego, gdy nie można ustalić, kto wyrządził szkodę?",
        "odpowiedzi": {
            "A": "Przedsiębiorca, który w dniu ujawnienia się szkody ma prawo prowadzić w obszarze górniczym, w granicach którego wystąpiła szkoda, działalność;",
            "B": "Właściwa gmina;",
            "C": "Właściwy organ nadzoru górniczego;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 146 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Jeżeli nie można ustalić, kto wyrządził szkodę, odpowiada przedsiębiorca, który w dniu ujawnienia szkody ma prawo prowadzić działalność w danym obszarze."
    },
    {
        "id": 75,
        "pytanie": "W jakim terminie przedawnia się roszczenie o naprawienie szkody górniczej?",
        "odpowiedzi": {
            "A": "W terminie 5 lat od wyrządzenia szkody;",
            "B": "W terminie 5 lat od dowiedzenia się o szkodzie;",
            "C": "W ogóle się nie przedawnia;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 149 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Roszczenie o naprawienie szkody przedawnia się z upływem 5 lat od dnia dowiedzenia się o szkodzie."
    },
    {
        "id": 76,
        "pytanie": "Naprawienie szkody wyrządzonej przez ruch zakładu górniczego może nastąpić przez:",
        "odpowiedzi": {
            "A": "Przywrócenie stanu poprzedniego, w szczególności dostarczenie gruntów tego samego rodzaju;",
            "B": "Zapłatę odpowiedniej sumy pieniężnej;",
            "C": "Rekultywację terenu zdegradowanego;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 147 ust. 1 i 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Naprawienie szkody następuje przez przywrócenie stanu poprzedniego lub zapłatę odszkodowania pieniężnego."
    },
    {
        "id": 77,
        "pytanie": "Opłata za uzyskanie koncesji na poszukiwanie złóż kopalin:",
        "odpowiedzi": {
            "A": "Jest uiszczana do 31 marca każdego roku przez okres trwania koncesji - w stałej wysokości wynikającej z koncesji;",
            "B": "Jest uiszczana do 31 marca każdego roku przez okres trwania koncesji w pierwszym roku w wysokości wynikającej z koncesji, a w kolejnych latach z waloryzacją;",
            "C": "Jest uiszczana jednorazowo w terminie 14 dni, od dnia, kiedy koncesja stanie się ostateczna;"
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 133 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłatę za działalność poszukiwawczą/rozpoznawczą wnosi się jednorazowo w terminie 14 dni od dnia, w którym koncesja stała się ostateczna."
    },
    {
        "id": 78,
        "pytanie": "Opłata za uzyskanie koncesji na poszukiwanie złóż kopalin stanowi:",
        "odpowiedzi": {
            "A": "Iloczyn wyrażonej w kilometrach kwadratowych powierzchni terenu objętej koncesją oraz okresu obowiązywania koncesji;",
            "B": "Iloczyn odpowiedniej stawki opłaty oraz wyrażonej w kilometrach kwadratowych powierzchni terenu objętej koncesją;",
            "C": "Iloczyn odpowiedniej stawki opłaty oraz okresu obowiązywania koncesji;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 133 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłata stanowi iloczyn stawki opłaty oraz powierzchni terenu wyrażonej w kilometrach kwadratowych."
    },
    {
        "id": 79,
        "pytanie": "W przypadku koncesji na poszukiwanie lub rozpoznawanie opłata jest ustalana:",
        "odpowiedzi": {
            "A": "Zawsze jednorazowo w treści koncesji, bez względu ewentualne późniejsze przedłużenie czasu trwania koncesji;",
            "B": "Jednorazowo w treści koncesji, z zastrzeżeniem, że w przypadku wydłużenia czasu obowiązywania koncesji, organ ponowne ustala opłatę;",
            "C": "Za każdy rok obowiązywania koncesji w wysokości wynikającej z rozporządzenia;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 133 ust. 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłatę ustala się jednorazowo w koncesji; w przypadku przedłużenia terminu jej obowiązywania, organ ponownie ustala opłatę."
    },
    {
        "id": 80,
        "pytanie": "Stawka opłaty za działalność w zakresie poszukiwania oraz rozpoznawania złóż kopalin stanowi:",
        "odpowiedzi": {
            "A": "Iloczyn odpowiedniej stawki opłaty oraz okresu trwania koncesji;",
            "B": "Iloczyn odpowiedniej stawki opłaty oraz wyrażonej w kilometrach kwadratowych powierzchni terenu objętej koncesją;",
            "C": "Dwukrotność iloczynu odpowiedniej stawki oraz powierzchni"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 133 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłata jest wyliczana jako iloczyn ustalonej stawki i powierzchni terenu w km²."
    },
    {
        "id": 81,
        "pytanie": "Przedsiębiorca, który uzyskał koncesję na wydobywanie kopaliny wnosi opłatę eksploatacyjną ustaloną jako:",
        "odpowiedzi": {
            "A": "Iloczyn wydobytej kopaliny oraz stawki właściwej opłaty wynikającej z załącznika do ustawy;",
            "B": "Iloczyn wydobytej kopaliny oraz stałej stawki właściwej opłaty ustalonej kwotowo w koncesji;",
            "C": "Iloczyn powierzchni obszaru górniczego oraz stawki z załącznika"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 134 ust. 1, 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłata eksploatacyjna stanowi iloczyn ilości kopaliny wydobytej ze złoża i stawki opłaty."
    },
    {
        "id": 82,
        "pytanie": "Wysokość opłaty eksploatacyjnej za wydobyty gaz ziemny wysokometanowy jest uzależniona od:",
        "odpowiedzi": {
            "A": "Ilości tys. m³ wydobytego gazu;",
            "B": "Ilości ton wydobytego gazu;",
            "C": "Ilości kilogramów wydobytego gazu;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Załącznik do Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Stawki opłat eksploatacyjnych dla gazu ziemnego wyrażane są w odniesieniu do tysiąca metrów sześciennych (1000 m³)."
    },
    {
        "id": 83,
        "pytanie": "Opłata eksploatacyjna za działalność podziemnego bezzbiornikowego magazynowania substancji jest ustalana jako:",
        "odpowiedzi": {
            "A": "Iloczyn stawki opłaty oraz wyrażonej w kilometrach kwadratowych powierzchni terenu;",
            "B": "Iloczyn stawki opłaty oraz ilości substancji, która w okresie rozliczeniowym została wprowadzona do górotworu;",
            "C": "Iloraz stawki opłaty oraz ilości substancji"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 135 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłata za magazynowanie stanowi iloczyn stawki opłaty oraz ilości substancji wprowadzonej do górotworu w okresie rozliczeniowym."
    },
    {
        "id": 84,
        "pytanie": "Okresem rozliczeniowym z tytułu opłaty eksploatacyjnej za kopalinę wydobytą jest:",
        "odpowiedzi": {
            "A": "Półrocze;",
            "B": "Kwartal;",
            "C": "Rok;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 137 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Okresem rozliczeniowym dla opłaty eksploatacyjnej jest półrocze."
    },
    {
        "id": 85,
        "pytanie": "Wysokość opłaty eksploatacyjnej ustala:",
        "odpowiedzi": {
            "A": "Organ koncesyjny, każdorazowo w decyzji;",
            "B": "Organ koncesyjny w sytuacji, gdy przedsiębiorca nie dokonał wpłaty lub dokonał wpłaty w niewłaściwej wysokości;",
            "C": "Samodzielnie przedsiębiorca;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 137 ust. 3 oraz Art. 138 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca sam ustala wysokość opłaty eksploatacyjnej, a organ ustala ją decyzją dopiero w przypadku uchylania się lub podania błędnych kwot."
    },
    {
        "id": 86,
        "pytanie": "Przedsiębiorca posiadający koncesję na wydobycie kopaliny ma obowiązek:",
        "odpowiedzi": {
            "A": "Samodzielnego ustalenia wysokość opłaty eksploatacyjnej;",
            "B": "Przedstawienia organowi koncesyjnemu, gminie oraz NFOŚiGW informacji dot. rodzaju, ilości kopaliny i przyjętej stawki;",
            "C": "Zapłaty opłaty eksploatacyjnej, jeżeli jej wysokość wynosi co najmniej 300 zł;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 137 ust. 1, 3, 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Przedsiębiorca samodzielnie ustala opłatę, przedkłada informacje organom oraz dokonuje wpłaty (jeżeli jej kwota przekracza 300 zł)."
    },
    {
        "id": 87,
        "pytanie": "W przypadku, gdy przedsiębiorca nie prowadził w ogóle w okresie rozliczeniowym wydobycia kopaliny:",
        "odpowiedzi": {
            "A": "Nie powstaje obowiązek zapłaty opłaty eksploatacyjnej;",
            "B": "Nie powstaje obowiązek przesłania organowi koncesyjnemu, gminie oraz NFOŚiGW informacji o braku wydobycia;",
            "C": "Organ Koncesyjny stwierdza cofnięcie koncesji;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 137 ust. 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku braku wydobycia opłata nie występuje, jednak należy przedłożyć informację ze wskaźnikiem zerowym."
    },
    {
        "id": 88,
        "pytanie": "Opłatę dodatkową ustala się w przypadku:",
        "odpowiedzi": {
            "A": "Wydobywania kopaliny towarzyszącej oraz współwystępującej;",
            "B": "Prowadzenia działalności z rażącym naruszeniem warunków określonych w koncesji lub zatwierdzonym projekcie robót geologicznych;",
            "C": "Przedłużenie o dodatkowy okres obowiązywania koncesji;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 139 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Prowadzenie działalności z rażącym naruszeniem warunków koncesji lub projektu robót skutkuje wymierzeniem opłaty dodatkowej."
    },
    {
        "id": 89,
        "pytanie": "Kto ustala wysokość opłaty dodatkowej?",
        "odpowiedzi": {
            "A": "Organ koncesyjny lub organ, który zatwierdził projekt robót geologicznych;",
            "B": "Przedsiębiorca samodzielnie;",
            "C": "Prezes Narodowego Funduszu Ochrony Środowiska i Gospodarki Wodnej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 139 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłatę dodatkową ustala, w drodze decyzji, właściwy organ koncesyjny lub organ administracji geologicznej."
    },
    {
        "id": 90,
        "pytanie": "Opłatę dodatkową za wydobywanie kopaliny bez wymaganej koncesji ustala się w wysokości:",
        "odpowiedzi": {
            "A": "Pięciu milionów złotych;",
            "B": "Pięciokrotnej stawki opłaty eksploatacyjnej dla danego rodzaju kopaliny, pomnożonej przez ilość wydobytej w ten sposób kopaliny;",
            "C": "Pięciokrotnej stawki opłaty dla danego rodzaju kopaliny za każdy kilometr kwadratowy;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 139 ust. 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Opłata dodatkowa wynosi pięciokrotność stawki opłaty eksploatacyjnej pomnożoną przez ilość wydobytej kopaliny."
    },
    {
        "id": 91,
        "pytanie": "Robotą geologiczną jest:",
        "odpowiedzi": {
            "A": "wykonywanie w ramach prac geologicznych wszelkich czynności poniżej powierzchni terenu;",
            "B": "Likwidacja wyrobisk po czynnościach wykonywanych w ramach prac geologicznych poniżej powierzchni terenu;",
            "C": "Analiza próbek geologicznych w laboratorium;"
        },
        "poprawne": ["A", "B"],
        "podstawa_prawna": "Art. 6 ust. 1 pkt 11 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Robotą geologiczną jest wykonywanie w ramach prac geologicznych wszelkich czynności poniżej powierzchni terenu, w tym wyrobisk i likwidacji wyrobisk."
    },
    {
        "id": 92,
        "pytanie": "Węglowodorami w rozumieniu ustawy Prawo geologiczne i górnicze są:",
        "odpowiedzi": {
            "A": "Metan występujący w złożach węgla kamiennego;",
            "B": "Ropa naftowa;",
            "C": "Gaz ziemny;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 6 ust. 1 pkt 16 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Węglowodory – ropa naftowa, gaz ziemny oraz ich naturalne pochodne."
    },
    {
        "id": 93,
        "pytanie": "Złożem kopaliny w rozumieniu ustawy Prawo geologiczne i górnicze jest:",
        "odpowiedzi": {
            "A": "Każde nagromadzenie minerałów, skał oraz innych substancji niezależnie od tego, czy jej wydobywanie jest ekonomicznie opłacalne;",
            "B": "Naturalne nagromadzenie minerałów, skał oraz innych substancji, których wydobywanie może przynieść korzyść gospodarczą;",
            "C": "Wyłącznie te złoże, które zostało uwzględnione w miejscowym planie zagospodarowania przestrzennego;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 6 ust. 1 pkt 8 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Złoże kopaliny – naturalne nagromadzenie minerałów, skał oraz innych substancji, których wydobywanie może przynieść korzyść gospodarczą."
    },
    {
        "id": 94,
        "pytanie": "Organem administracji geologicznej uprawnionym do wydania koncesji na wydobywanie kopaliny ze złóż w ilości do 20.000m³ w roku z obszaru nie większego niż 2 ha, bez użycia środków strzałowych, metodą odkrywkową jest:",
        "odpowiedzi": {
            "A": "Starosta powiatowy;",
            "B": "Burmistrz miasta;",
            "C": "Prezydent Miasta na prawach powiatu;"
        },
        "poprawne": ["A", "C"],
        "podstawa_prawna": "Art. 22 ust. 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Koncesji w tych przypadkach udziela starosta (funkcję starosty w miastach na prawach powiatu sprawuje prezydent miasta)."
    },
    {
        "id": 95,
        "pytanie": "Podejmowanie działalności polegającej na wydobywaniu kopaliny ze złoża jest dozwolone wówczas gdy:",
        "odpowiedzi": {
            "A": "Nie naruszy przeznaczenia nieruchomości określonego w miejscowym planie zagospodarowania przestrzennego oraz w odrębnych przepisach;",
            "B": "Nie naruszy sposobu wykorzystywania nieruchomości ustalonego w studium uwarunkowań i kierunków zagospodarowania przestrzennego gminy oraz w odrębnych przepisach;",
            "C": "Treść miejscowego planu zagospodarowania przestrzennego nie ma w ogóle wpływu na udzielenie koncesji na wydobycie kopalin;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 7 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Podejmowanie działalności regulowanej ustawą nie może naruszać przeznaczenia nieruchomości określonego w MPZP."
    },
    {
        "id": 96,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. I są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "poszukiwanie i rozpoznawanie złóż węglowodorów;",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych własnością górniczą (z pewnymi wyjątkami);",
            "C": "poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria I obejmuje poszukiwanie i rozpoznawanie złóż węglowodorów."
    },
    {
        "id": 97,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. II są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "poszukiwanie i rozpoznawanie złóż węglowodorów;",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych własnością górniczą, z wyjątkiem złóż ropy naftowej i gazu ziemnego, wód leczniczych, wód termalnych i solanek...",
            "C": "określanie warunków geologiczno-inżynierskich..."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 2 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria II dotyczy poszukiwania i rozpoznawania złóż kopalin objętych własnością górniczą (oprócz ropy, gazu, wód leczniczych, termalnych i solanek) oraz złoża gruntowego."
    },
    {
        "id": 98,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. III są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych własnością górniczą...",
            "C": "poszukiwanie i rozpoznawanie złóż węglowodorów;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 3 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria III obejmuje poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej."
    },
    {
        "id": 99,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. IV są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "poszukiwanie i rozpoznawanie zasobów wód podziemnych, w tym wód leczniczych, wód termalnych i solanek, określanie warunków hydrogeologicznych...",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;",
            "C": "poszukiwanie i rozpoznawanie złóż węglowodorów;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 4 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria IV dotyczy poszukiwania i rozpoznawania wód podziemnych, solanek, wód leczniczych i termalnych oraz sprawowania hydrogeologii."
    },
    {
        "id": 100,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. V są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "określanie warunków geologiczno-inżynierskich na potrzeby zagospodarowania przestrzennego, posadawiania obiektów budowlanych...",
            "B": "poszukiwanie i rozpoznawanie zasobów wód podziemnych...",
            "C": "wykonywanie prac kartografii geologicznej..."
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 5 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria V obejmuje zakresem hydrogeologię, czyli m.in.: poszukiwanie i rozpoznawanie zasobów wód podziemnych (z wyłączeniem solanek, wód leczniczych i termalnych) oraz określanie warunków hydrogeologicznych."
    },
    {
        "id": 101,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. VI są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "wykonywanie prac kartografii geologicznej wraz z projektowaniem i dokumentowaniem tych prac...",
            "B": "poszukiwanie i rozpoznawanie zasobów wód podziemnych...",
            "C": "określanie warunków geologiczno-inżynierskich na potrzeby zagospodarowania przestrzennego..."
        },
        "poprawne": ["C"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 6 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria VI obejmuje określanie warunków geologiczno-inżynierskich m.in. na potrzeby zagospodarowania przestrzennego oraz posadawiania obiektów budowlanych."
    },
    {
        "id": 102,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. VII są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "określanie warunków geologiczno-inżynierskich na potrzeby zagospodarowania przestrzennego, posadawiania obiektów budowlanych, z wyjątkiem posadawiania obiektów budowlanych zakładów górniczych oraz budownictwa wodnego;",
            "B": "określanie warunków geologiczno-inżynierskich na potrzeby... zakładów górniczych i budownictwa wodnego;",
            "C": "poszukiwanie i rozpoznawanie złóż kopalin..."
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 7 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria VII obejmuje geologię inżynierską ograniczoną (z wyłączeniem budownictwa wodnego i zakładów górniczych)."
    },
    {
        "id": 103,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. VIII są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "wykonywanie prac kartografii geologicznej wraz z projektowaniem i dokumentowaniem tych prac, z wyjątkiem map sporządzanych w ramach pozostałych kategorii kwalifikacji;",
            "B": "poszukiwanie i rozpoznawanie złóż kopalin objętych własnością górniczą...",
            "C": "poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;"
        },
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 8 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria VIII obejmuje kartografię geologiczną (zakres uzupełniający)."
    },
    {
        "id": 104,
        "pytanie": "Kwalifikacje w zakresie wykonywania, dozorowania i kierowania pracami geologicznymi kat. IX są zdefiniowane jako:",
        "odpowiedzi": {
            "A": "kierowanie i wykonywanie w terenie badań geofizycznych wraz z projektowaniem i dokumentowaniem tych badań, z wyjątkiem badań sejsmicznych i geofizyki wiertniczej;",
            "B": "kierowanie i wykonywanie w terenie badań geofizycznych, w tym badań sejsmicznych i geofizyki wiertniczej, także przy użyciu środków strzałowych...",
            "C": "poszukiwanie i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 50 ust. 2 pkt 9 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Kategoria IX obejmuje badania geofizyczne pełnego zakresu (w tym sejsmikę i geofizykę wiertniczą)."
    },
    {
        "id": 105,
        "pytanie": "Stwierdzenie posiadanych kwalifikacji w zakresie kategorii XIII tj. kierowanie w terenie robotami geologicznymi wykonywanymi poza granicami obszaru górniczego, wykonywanymi bez użycia środków strzałowych albo gdy projektowana głębokość wyrobiska nie przekracza 100 m. następuje w drodze świadectwa wydanego przez:",
        "odpowiedzi": {
            "A": "Ministra właściwego ds. środowiska;",
            "B": "marszałka województwa;",
            "C": "wojewodę"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 58 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Stwierdzenia kwalifikacji kategorii XIII dokonuje właściwy marszałek województwa."
    },
    {
        "id": 106,
        "pytanie": "Marszałek województwa stwierdza kwalifikacje osób w zakresie:",
        "odpowiedzi": {
            "A": "poszukiwania i rozpoznawanie złóż kopalin objętych prawem własności nieruchomości gruntowej;",
            "B": "kierowania w terenie robotami geologicznymi wykonywanymi poza granicami obszaru górniczego, wykonywanymi bez użycia środków strzałowych albo gdy projektowana głębokość wyrobiska nie przekracza 100 m;",
            "C": "wykonywania czynności dozoru geologicznego nad pracami geologicznymi, z wyjątkiem badań geofizycznych;"
        },
        "poprawne": ["B", "C"],
        "podstawa_prawna": "Art. 58 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "Marszałek województwa jest organem właściwym do nadawania kwalifikacji kategorii XI oraz XII."
    },
    {
        "id": 107,
        "pytanie": "W stosunku do osoby, która wykonuje czynności polegające na wykonywaniu, dozorowaniu i kierowaniu pracami geologicznymi z rażącym niedbalstwem, z naruszeniem ustawy lub rażącym naruszeniem wydanych na jej podstawie przepisów można orzec zakaz ich wykonywania na okres do:",
        "odpowiedzi": {
            "A": "5 lat;",
            "B": "2 lat;",
            "C": "nie ma takiej możliwości"
        },
        "poprawne": ["B"],
        "podstawa_prawna": "Art. 68 ust. 1 Ustawy Prawo geologiczne i górnicze",
        "tresc_artykulu": "W przypadku stwierdzenia niedbalstwa przy pracach geologicznych można orzec zakaz wykonywania tych czynności na okres do 2 lat."
    }
],  
        "BAZA PYTAŃ - CZĘŚĆ 4 (Projekty robót, dokumentacje geologiczne, inne dokumentacje, operaty ewidencyjne, projekty zagospodarowania złóż)": [
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
}
# ==============================================================================
# INICJALIZACJA STANU SESJI I MOTYWÓW
# ==============================================================================
if 'theme' not in st.session_state:
    st.session_state.theme = "Ciemny"

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

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
if 'czas_konca' not in st.session_state:
    st.session_state.czas_konca = None
if 'test_zakonczony' not in st.session_state:
    st.session_state.test_zakonczony = False

# Konfiguracja układu strony
st.set_page_config(
    page_title="Aplikacja Testowa - Prawo Geologiczne i Górnicze",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stylizacja CSS
if st.session_state.theme == "Jasny":
    st.markdown("""
    <style>
        .stApp { background-color: #f8f9fa; color: #212529; }
        section[data-testid="stSidebar"] { background-color: #f1f3f5 !important; }
        section[data-testid="stSidebar"] * { color: #212529 !important; }
        input, textarea, select, div[role="combobox"], div[data-baseweb="select"] {
            background-color: #ffffff !important; color: #212529 !important; border: 1px solid #ced4da !important;
        }
        div[data-baseweb="select"] * { background-color: #ffffff !important; color: #212529 !important; }
        .stButton>button, .stFormSubmitButton>button {
            background-color: #e9ecef !important; color: #212529 !important; border: 1px solid #ced4da !important; width: 100% !important;
        }
        .stButton>button:hover, .stFormSubmitButton>button:hover { background-color: #dee2e6 !important; border-color: #adb5bd !important; }
        label, .stRadio p, .stCheckbox p, p { color: #212529 !important; }
        .main-header { font-size: 22px; font-weight: bold; color: #0d6efd; border-bottom: 2px solid #dee2e6; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ced4da; margin-bottom: 15px; color: #212529; }
        .legal-box { background-color: #e7f1ff; padding: 15px; border-radius: 6px; border: 1px solid #b6d4fe; margin-top: 15px; margin-bottom: 15px; color: #084298; }
        .card-blue, .card-yellow, .card-green, .card-red {
            padding: 20px; border-radius: 8px; height: 220px; display: flex; flex-direction: column; justify-content: flex-start; margin-bottom: 20px; box-sizing: border-box;
        }
        .card-blue { background-color: #cfe2ff; color: #084298; border: 1px solid #b6d4fe; }
        .card-yellow { background-color: #ffe5d0; color: #7c2d12; border: 1px solid #ffbb99; }
        .card-green { background-color: #d1e7dd; color: #0f5132; border: 1px solid #badbcc; }
        .card-red { background-color: #f8d7da; color: #842029; border: 1px solid #f5c2c7; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        section[data-testid="stSidebar"] { background-color: #161b22 !important; }
        section[data-testid="stSidebar"] * { color: #ffffff !important; }
        input, textarea, select, div[role="combobox"], div[data-baseweb="select"] {
            background-color: #21262d !important; color: #ffffff !important; border: 1px solid #30363d !important;
        }
        div[data-baseweb="select"] * { background-color: #21262d !important; color: #ffffff !important; }
        .stButton>button, .stFormSubmitButton>button { width: 100% !important; }
        label, .stRadio p, .stCheckbox p, p { color: #ffffff !important; }
        .main-header { font-size: 22px; font-weight: bold; color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #161b22; padding: 15px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; color: #ffffff; }
        .legal-box { background-color: #0d1117; padding: 15px; border-radius: 6px; border: 1px solid #238636; margin-top: 15px; margin-bottom: 15px; color: #e6edf3; }
        .card-blue, .card-yellow, .card-green, .card-red {
            padding: 20px; border-radius: 8px; height: 220px; display: flex; flex-direction: column; justify-content: flex-start; margin-bottom: 20px; box-sizing: border-box;
        }
        .card-blue { background-color: #1f364d; color: #58a6ff; border: 1px solid #30363d; }
        .card-yellow { background-color: #452800; color: #ffbc54; border: 1px solid #633800; }
        .card-green { background-color: #1b3a2b; color: #3fb950; border: 1px solid #238636; }
        .card-red { background-color: #421e22; color: #f85149; border: 1px solid #da3633; }
    </style>
    """, unsafe_allow_html=True)

# Pomocnicze funkcje sesyjne
def start_sesji(tryb, limit_pytan=None, z_calej_bazy=False):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.odpowiedzi_egzamin = {}
    st.session_state.test_zakonczony = False
    
    if z_calej_bazy:
        pula = []
        for baza in st.session_state.bazy.values():
            pula.extend(baza)
        random.shuffle(pula)
        if limit_pytan:
            pula = pula[:limit_pytan]
        st.session_state.pytania_sesji = pula
        st.session_state.czas_konca = time.time() + (30 * 60) # 30 minut
    else:
        pula = list(st.session_state.bazy[st.session_state.wybrana_baza])
        if "Losowo" in tryb or "Egzamin" in tryb:
            random.shuffle(pula)
        if limit_pytan:
            pula = pula[:limit_pytan]
        st.session_state.pytania_sesji = pula
        st.session_state.czas_konca = None

def powrot_do_wyboru():
    st.session_state.wybrana_baza = None
    st.session_state.aktywny_tryb = None
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.test_zakonczony = False
    st.session_state.czas_konca = None

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
            <p style="margin:0;">Wybierz część bazy, ustal tryb nauki, egzaminu lub uruchom test z całej bazy.</p>
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
    if st.session_state.wybrana_baza is None and st.session_state.aktywny_tryb is None:
        st.markdown("<div class='main-header'>Wybierz tryb testowy lub bazę pytań</div>", unsafe_allow_html=True)
        
        if st.button("🚀 Uruchom Egzamin z CAŁEJ BAZY (50 pytań / 30 min)", use_container_width=True, type="primary"):
            start_sesji("Tryb Egzaminu z CAŁEJ BAZY (50 pytań / 30 min)", limit_pytan=50, z_calej_bazy=True)
            st.rerun()
            
        st.markdown("---")
        st.write("Lub wybierz pojedynczą część bazy danych:")
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
            start_sesji("Tryb Nauki (Kolejno + Podpowiedzi)", limit_pytan=None)
            st.rerun()

        if st.button("Tryb Nauki (Losowo – 30 pytań + Podpowiedzi)", use_container_width=True):
            start_sesji("Tryb Nauki (Losowo – 30 pytań + Podpowiedzi)", limit_pytan=30)
            st.rerun()

        if st.button("Tryb Egzaminu (Losowo – 35 pytań, wynik na końcu)", use_container_width=True):
            start_sesji("Tryb Egzaminu (Losowo – 35 pytań)", limit_pytan=35)
            st.rerun()

        st.write("")
        if st.button("← Powrót do wyboru baz", use_container_width=True):
            powrot_do_wyboru()
            st.rerun()

    else:
        # Pasek czasu dla egzaminu
        if st.session_state.czas_konca is not None and not st.session_state.test_zakonczony:
            pozostaly_czas = int(st.session_state.czas_konca - time.time())
            if pozostaly_czas <= 0:
                st.session_state.test_zakonczony = True
                st.rerun()
            else:
                mins, secs = divmod(pozostaly_czas, 60)
                st.markdown(f"""
                <div style="font-size: 18px; font-weight: bold; color: #ff4b4b; background-color: #1f2937; padding: 10px; border-radius: 8px; margin-bottom: 15px; text-align: center;">
                    ⏱️ Pozostały czas egzaminu: {mins:02d}:{secs:02d}
                </div>
                """, unsafe_allow_html=True)

        st.markdown(f"<div class='main-header'>{st.session_state.aktywny_tryb}</div>", unsafe_allow_html=True)
        lista = st.session_state.pytania_sesji
        idx = st.session_state.indeks

        if st.button("← Przerwij i wróć do menu"):
            powrot_do_wyboru()
            st.rerun()

        st.markdown("---")

        if idx < len(lista) and not st.session_state.test_zakonczony:
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
                    if st.button("🏁 Zakończ Test / Egzamin"):
                        st.session_state.test_zakonczony = True
                        st.rerun()
        else:
            st.balloons()
            st.success("🎉 Zakończyłeś test / egzamin!")
            
            if "Egzamin" in st.session_state.aktywny_tryb:
                punkty = 0
                for i, q in enumerate(lista):
                    user_ans = set(st.session_state.odpowiedzi_egzamin.get(i, []))
                    correct_ans = set(q["poprawne"])
                    if user_ans == correct_ans:
                        punkty += 1
                st.markdown(f"### Twój Wynik Egzaminu: **{punkty} / {len(lista)}** ({(punkty/len(lista)*100):.1f}%)")

            if st.button("🔄 Rozpocznij ponownie"):
                powrot_do_wyboru()
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
