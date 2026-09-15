import random
import streamlit as st

# Konfiguracja strony Streamlit
st.set_page_config(
    page_title="Aplikacja Testowa - Prawo Geologiczne i Górnicze",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS dopasowane do oryginalnego wyglądu
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-header {
        font-size: 20px;
        font-weight: bold;
        color: #58a6ff;
        border-bottom: 2px solid #30363d;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    .question-box {
        background-color: #161b22;
        padding: 15px;
        border-radius: 6px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
    }
    .legal-box {
        background-color: #0d1117;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #238636;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# BAZA PYTAŃ - CZĘŚĆ 1 & CZĘŚĆ 2
# ==============================================================================
PYTANIA_CZ1 = [
    {
        "id": 1,
        "pytanie": "W jakim terminie przedsiębiorca powinien przedłożyć organowi koncesyjnemu aktualny dowód istnienia zabezpieczenia roszczeń mogących powstać wskutek wykonywania działalności objętej koncesją na podziemne składowanie odpadów:",
        "odpowiedzi": {
            "A": "raz na kwartał,",
            "B": "corocznie, w terminie do końca stycznia,",
            "C": "nie później niż w terminie dwóch tygodni od dnia otrzymania wezwania ze strony organu koncesyjnego.",
        },
        "poprawne": ["B"],
    },
    {
        "id": 2,
        "pytanie": "Koncesji na jaką działalność udziela się zawsze pod warunkiem ustanowienia zabezpieczenia roszczeń mogących powstać wskutek wykonywania działalności nią objętą:",
        "odpowiedzi": {
            "A": "koncesji na podziemne składowanie odpadów,",
            "B": "koncesji na podziemne bezzbiornikowe magazynowanie substancji,",
            "C": "koncesji na wydobywanie kopaliny prowadzone metodą podziemną.",
        },
        "poprawne": ["A"],
    },
    {
        "id": 3,
        "pytanie": "We wniosku o udzielenie koncesji na podziemne składowanie odpadów określa się:",
        "odpowiedzi": {
            "A": "technologię składowania,",
            "B": "projektowane położenie obszaru i terenu górniczego,",
            "C": "rodzaj, ilość oraz charakterystykę odpadów.",
        },
        "poprawne": ["A", "B", "C"],
    }
]

PYTANIA_CZ2 = [
    {
        "id": 1,
        "pytanie": "Miejscowy plan zagospodarowania przestrzennego, sporządzany dla terenu górniczego w sytuacji, gdy w wyniku zamierzonej działalności określonej w koncesji przewiduje się istotne skutki dla środowiska powienien zapewniać integrację wszelkich działań podejmowanych w granicach terenu górniczego w celu:",
        "odpowiedzi": {
            "A": "Wykonania działalności określonej w koncesji;",
            "B": "Zapewnienia bezpieczeństwa powszechnego;",
            "C": "Ochrony środowiska, w tym obiektów budowlanych;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 104 ust. 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Miejscowy plan zagospodarowania przestrzennego dla terenu górniczego sporządza się dla terenu górniczego..."
    },
    {
        "id": 2,
        "pytanie": "Miejscowy plan zagospodarowania przestrzennego, sporządzany dla terenu górniczego w sytuacji, gdy w wyniku zamierzonej działalności określonej w koncesji przewiduje się istotne skutki dla środowiska, może określić:",
        "odpowiedzi": {
            "A": "Obiekty, dla których wyznacza się filar ochronny;",
            "B": "obszary, dla których wyznacza się filar ochronny;",
            "C": "Obszary wyłączone z zabudowy;"
        },
        "poprawne": ["A", "B", "C"],
        "podstawa_prawna": "Art. 104 ust. 2 pkt 1 Prawo geologiczne i górnicze",
        "tresc_artykulu": "Miejscowy plan zagospodarowania przestrzennego dla terenu górniczego może w szczególności określić obszary..."
    }
]

# ==============================================================================
# INICJALIZACJA STANUSESSION
# ==============================================================================
if 'bazy' not in st.session_state:
    st.session_state.bazy = {
        "Część 1 (Projekty, hydrogeologia, geologia)": PYTANIA_CZ1,
        "Część 2 (Planowanie, ruch zakładu, przepisy)": PYTANIA_CZ2
    }

if 'wybrana_baza' not in st.session_state:
    st.session_state.wybrana_baza = None
if 'aktywny_tryb' not in st.session_state:
    st.session_state.aktywny_tryb = None
if 'pytania_sesji' not in st.session_state:
    st.session_state.pytania_sesji = []
if 'indeks' not in st.session_state:
    st.session_state.indeks = 0
if 'odpowiedzi_egzamin' not in st.session_state:
    st.session_state.odpowiedzi_egzamin = {}

def start_sesji(tryb):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.odpowiedzi_egzamin = {}
    
    pula = list(st.session_state.bazy[st.session_state.wybrana_baza])
    if "Losow" in tryb or "Egzamin" in tryb:
        random.shuffle(pula)
    st.session_state.pytania_sesji = pula

def powrot_do_wyboru():
    st.session_state.wybrana_baza = None
    st.session_state.aktywny_tryb = None
    st.session_state.indeks = 0

# ==============================================================================
# NAWIGACJA BOCZNA
# ==============================================================================
st.sidebar.title("📌 Menu Główne")
menu_glowne = st.sidebar.radio(
    "Nawigacja:",
    ["🎮 Testy i Nauka", "➕ Dodaj Pytanie", "🔍 Przegląd Bazy"]
)

# ==============================================================================
# WIDOK 1: TESTY I NAUKA (Z WIDOKIEM MENU Z OBRAZKA)
# ==============================================================================
if menu_glowne == "🎮 Testy i Nauka":
    
    # KROK 1: Wybór części bazy
    if st.session_state.wybrana_baza is None:
        st.markdown("<div class='main-header'>Wybierz część bazy pytań</div>", unsafe_allow_html=True)
        for nazwa_bazy in st.session_state.bazy.keys():
            if st.button(f"📁 {nazwa_bazy}", use_container_width=True):
                st.session_state.wybrana_baza = nazwa_bazy
                st.rerun()

    # KROK 2: Wybór trybu rozwiązywania (Ekran z obrazka)
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

    # KROK 3: Ekran rozwiązywania pytań
    else:
        st.markdown(f"<div class='main-header'>{st.session_state.aktywny_tryb} - {st.session_state.wybrana_baza}</div>", unsafe_allow_html=True)
        
        lista = st.session_state.pytania_sesji
        idx = st.session_state.indeks

        # Przycisk szybkiego wyjścia
        if st.button("← Zmień tryb / powrót"):
            st.session_state.aktywny_tryb = None
            st.rerun()

        st.markdown("---")

        if idx < len(lista):
            p = lista[idx]
            st.markdown(f"**Pytanie {idx + 1} z {len(lista)}** (ID: {p['id']})")
            st.markdown(f"<div class='question-box'><h3>{p['pytanie']}</h3></div>", unsafe_allow_html=True)

            # --- TRYBY NAUKI ---
            if "Nauki" in st.session_state.aktywny_tryb:
                with st.form(key=f"form_nauka_{idx}"):
                    wybrane = []
                    for k, v in p["odpowiedzi"].items():
                        if st.checkbox(f"**{k}**: {v}", key=f"cb_nauka_{idx}_{k}"):
                            wybrane.append(k)
                    
                    sprawdz = st.form_submit_button("Sprawdź odpowiedź")

                if sprawdz:
                    poprawne = set(p["poprawne"])
                    zaznaczone = set(wybrane)
                    if zaznaczone == poprawne:
                        st.success("✅ Poprawna odpowiedź!")
                    else:
                        st.error(f"❌ Błąd! Poprawne odpowiedzi to: {', '.join(p['poprawne'])}")

                    if "podstawa_prawna" in p or "tresc_artykulu" in p:
                        st.markdown(f"""
                        <div class='legal-box'>
                            <strong>📜 Podstawa prawna:</strong> {p.get('podstawa_prawna', 'Brak danych')}<br><br>
                            <em>{p.get('tresc_artykulu', '')}</em>
                        </div>
                        """, unsafe_allow_html=True)

            # --- TRYB EGZAMINU ---
            else:
                poprzednie_wybory = st.session_state.odpowiedzi_egzamin.get(idx, [])
                wybrane = []
                for k, v in p["odpowiedzi"].items():
                    zaznaczone = k in poprawnie_zaznaczone if 'poprawnie_zaznaczone' in locals() else k in poprzednie_wybory
                    if st.checkbox(f"**{k}**: {v}", value=zaznaczone, key=f"cb_egz_{idx}_{k}"):
                        wybrane.append(k)
                
                st.session_state.odpowiedzi_egzamin[idx] = wybrane

            col_p, col_n = st.columns([1, 1])
            with col_p:
                if st.button("⬅️ Poprzednie") and idx > 0:
                    st.session_state.indeks -= 1
                    st.rerun()
            with col_n:
                if idx < len(lista) - 1:
                    if st.button("Następne ➡️"):
                        st.session_state.indeks += 1
                        st.rerun()
                else:
                    if st.button("🏁 Zakończ Test"):
                        st.session_state.indeks += 1
                        st.rerun()

        # Ekran podsumowania po zakończeniu
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
# WIDOK 2: DODAJ PYTANIE
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
                st.error("Uzupełnij polach i wybierz co najmniej jedną poprawną odpowiedź!")

# ==============================================================================
# WIDOK 3: PRZEGLĄD BAZY
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
