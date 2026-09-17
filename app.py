import streamlit as st
import random
import time
import datetime
import streamlit.components.v1 as components
# ==============================================================================
# HASŁO ADMINISTRATORA
# ==============================================================================
ADMIN_PASSWORD = "admin123"
PLIK_STATYSTYK = "statystyki.json"

# ==============================================================================
# FUNKCJE DO OBSŁUGI TRWAŁYCH STATYSTYK (JSON)
# ==============================================================================
def wczytaj_statystyki():
    if os.path.exists(PLIK_STATYSTYK):
        try:
            with open(PLIK_STATYSTYK, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"Piotrek": [], "Edyta": [], "Gość": []}

def zapisz_statystyki_do_pliku(stats):
    try:
        with open(PLIK_STATYSTYK, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=4)
    except:
        pass

# ==============================================================================
# INICJALIZACJA STANUSESSION I MOTYWÓW
# ==============================================================================
from baza_danych import BAZY_PYTAN

if 'bazy' not in st.session_state:
    st.session_state.bazy = BAZY_PYTAN
    
# ==============================================================================
# 1. KONFIGURACJA STRONY
# ==============================================================================
st.set_page_config(
    page_title="Aplikacja - Prawo Górnicze i Geologiczne",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. MECHANIZM TRWAŁEJ SESJI
# ==============================================================================
USERS_PIN = {
    "Piotrek": "1671",
    "Edyta": "3538",
    "Gość": None
}

query_params = st.query_params

if 'zalogowany_uzytkownik' not in st.session_state:
    st.session_state.zalogowany_uzytkownik = query_params.get("user", None)

if 'theme' not in st.session_state:
    st.session_state.theme = query_params.get("theme", "Ciemny")

if 'admin_logged_in' not in st.session_state:
    st.session_state.admin_logged_in = False

if 'statystyki' not in st.session_state:
    st.session_state.statystyki = wczytaj_statystyki()

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

if 'bazy' not in st.session_state:
    st.session_state.bazy = BAZY_PYTAN

def aktualizuj_pamiec_sesji(user=None, theme=None):
    if user is not None:
        if user is False:
            if "user" in st.query_params:
                del st.query_params["user"]
        else:
            st.query_params["user"] = user

    if theme is not None:
        st.query_params["theme"] = theme

# ==============================================================================
# 3. GLOBALNY MOTYW CSS
# ==============================================================================
if st.session_state.theme == "Jasny":
    bg_main = "#f8f9fa"
    bg_sec = "#ffffff"
    text_main = "#111827"
    border_color = "#d1d5db"
    btn_bg = "#ffffff"
    btn_text = "#111827"
    btn_border = "#cccccc"
    box_bg = "#ffffff"
    box_text = "#111827"
else:
    bg_main = "#0e1117"
    bg_sec = "#161b22"
    text_main = "#ffffff"
    border_color = "rgba(255, 255, 255, 0.15)"
    btn_bg = "#21262d"
    btn_text = "#ffffff"
    btn_border = "#363b42"
    box_bg = "#21262d"
    box_text = "#ffffff"

st.markdown(f"""
<style>
    :root {{
        --bg-main: {bg_main};
        --bg-sec: {bg_sec};
        --text-main: {text_main};
        --border-color: {border_color};
        --btn-bg: {btn_bg};
        --btn-text: {btn_text};
        --btn-border: {btn_border};
        --box-bg: {box_bg};
        --box-text: {box_text};
    }}

    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {{
        background-color: var(--bg-main) !important;
        color: var(--text-main) !important;
    }}
    
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {{
        background-color: var(--bg-sec) !important;
        border-right: 1px solid var(--border-color) !important;
    }}

    p, span, label, div, h1, h2, h3, h4, h5, h6, 
    [data-testid="stCheckbox"] p, [data-testid="stRadio"] p, [data-testid="stWidgetLabel"] p, [data-testid="stMarkdownContainer"] p {{
        color: var(--text-main) !important;
    }}

    div[data-baseweb="select"] > div {{
        background-color: var(--box-bg) !important;
        color: var(--box-text) !important;
        border-color: var(--border-color) !important;
    }}

    div.stButton > button {{
        background-color: var(--btn-bg) !important;
        color: var(--btn-text) !important;
        border: 1px solid var(--btn-border) !important;
        border-radius: 6px !important;
        transition: all 0.2s ease-in-out !important;
    }}

    div.stButton > button:hover {{
        border-color: #ff4b4b !important;
        color: #ff4b4b !important;
    }}

    div.stButton > button[kind="primary"] {{
        background-color: #ff4b4b !important;
        color: #ffffff !important;
        border: none !important;
    }}

    div.stButton > button[kind="primary"]:hover {{
        background-color: #e03e3e !important;
        color: #ffffff !important;
    }}

    input, textarea {{
        background-color: var(--bg-sec) !important;
        color: var(--text-main) !important;
        border-color: var(--border-color) !important;
    }}

    [data-testid="stExpander"] {{
        background-color: var(--bg-sec) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 6px !important;
    }}

    .question-box {{
        background-color: var(--bg-sec) !important;
        padding: 18px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        margin-bottom: 15px;
    }}

    .main-header {{
        font-size: 22px;
        font-weight: bold;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 8px;
        margin-bottom: 15px;
    }}

    .card-blue, .card-yellow, .card-green, .card-red {{
        padding: 20px;
        border-radius: 8px;
        height: 160px;
        margin-bottom: 15px;
    }}
    .card-blue {{ background-color: rgba(13, 110, 253, 0.12); border: 1px solid rgba(13, 110, 253, 0.3); }}
    .card-yellow {{ background-color: rgba(255, 193, 7, 0.12); border: 1px solid rgba(255, 193, 7, 0.3); }}
    .card-green {{ background-color: rgba(25, 135, 84, 0.12); border: 1px solid rgba(25, 135, 84, 0.3); }}
    .card-red {{ background-color: rgba(220, 53, 69, 0.12); border: 1px solid rgba(220, 53, 69, 0.3); }}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. FUNKCJE POMOCNICZE
# ==============================================================================
def pobierz_pytania_z_bazy(nazwa_bazy, tylko_wielokrotne=False):
    if nazwa_bazy == "Cała baza (wszystkie pytania)":
        pula = []
        for b in st.session_state.bazy.values():
            pula.extend(b)
    else:
        pula = list(st.session_state.bazy.get(nazwa_bazy, []))
    
    if tylko_wielokrotne:
        return [p for p in pula if len(p.get("poprawne", [])) > 1]
    return pula

def start_sesji(tryb, baza_nazwa, limit_pytan=None, tylko_wielokrotne=False):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.odpowiedzi_egzamin = {}
    st.session_state.test_zakonczony = False
    
    pula = pobierz_pytania_z_bazy(baza_nazwa, tylko_wielokrotne=tylko_wielokrotne)
    
    if "Losowo" in tryb or "Egzamin" in tryb:
        random.shuffle(pula)
    if limit_pytan:
        pula = pula[:limit_pytan]
        
    st.session_state.pytania_sesji = pula
    if "30 min" in tryb:
        st.session_state.czas_konca = time.time() + (30 * 60)
    else:
        st.session_state.czas_konca = None

def powrot_do_wyboru():
    st.session_state.wybrana_baza = None
    st.session_state.aktywny_tryb = None
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.test_zakonczony = False
    st.session_state.czas_konca = None
    st.session_state.odpowiedzi_egzamin = {}

def zapisz_wynik_egzaminu(user, tryb, baza, punkty, max_punkty):
    procent = (punkty / max_punkty) * 100 if max_punkty > 0 else 0
    zdane = procent >= 75.0
    
    wpis = {
        'data': datetime.date.today().strftime("%Y-%m-%d"),
        'tryb': tryb,
        'baza': baza if baza else "Wszystkie",
        'zdane': zdane,
        'wynik_str': f"{punkty}/{max_punkty}",
        'procent': procent
    }
    
    if user not in st.session_state.statystyki:
        st.session_state.statystyki[user] = []
        
    # Zapobiegaj wielokrotnemu zapisywaniu dokładnie tego samego wyniku w jednej sesji
    if not st.session_state.statystyki[user] or st.session_state.statystyki[user][-1] != wpis:
        st.session_state.statystyki[user].append(wpis)
        zapisz_statystyki_do_pliku(st.session_state.statystyki)

# ==============================================================================
# 5. EKRAN LOGOWANIA
# ==============================================================================
if st.session_state.zalogowany_uzytkownik is None:
    st.markdown("<div class='main-header'>🔒 Aplikacja - Prawo Górnicze i Geologiczne</div>", unsafe_allow_html=True)
    
    col_login, _ = st.columns([1, 1])
    with col_login:
        wybrany_user = st.selectbox(
            "Wybierz użytkownika:",
            options=list(USERS_PIN.keys()),
            key="login_user_select"
        )
        
        wymaga_pin = USERS_PIN[wybrany_user] is not None
        
        if wymaga_pin:
            podany_pin = st.text_input("Podaj swój PIN:", type="password", key="login_pin_input")
        else:
            st.info("Konto Gościa nie wymaga podawania PIN-u.")
            podany_pin = None

        if st.button("Zaloguj się", type="primary", use_container_width=True):
            if not wymaga_pin or podany_pin == USERS_PIN[wybrany_user]:
                st.session_state.zalogowany_uzytkownik = wybrany_user
                aktualizuj_pamiec_sesji(user=wybrany_user)
                st.success(f"Pomyślnie zalogowano jako {wybrany_user}!")
                st.rerun()
            else:
                st.error("Błędny PIN! Spróbuj ponownie.")

        st.markdown("---")
        opcje_motywu = ["Ciemny", "Jasny"]
        idx = opcje_motywu.index(st.session_state.theme) if st.session_state.theme in opcje_motywu else 0
        zmien_motyw = st.radio("Motyw ekranu:", opcje_motywu, index=idx, key="login_theme_radio", horizontal=True)
        if zmien_motyw != st.session_state.theme:
            st.session_state.theme = zmien_motyw
            aktualizuj_pamiec_sesji(theme=zmien_motyw)
            st.rerun()

    st.stop()

# ==============================================================================
# 6. MENU BOCZNE
# ==============================================================================
st.sidebar.title(f"👤 Zalogowany: {st.session_state.zalogowany_uzytkownik}")
if st.sidebar.button("🚪 Wyloguj"):
    st.session_state.zalogowany_uzytkownik = None
    aktualizuj_pamiec_sesji(user=False)
    st.rerun()

st.sidebar.markdown("---")
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
# 7. STRONA GŁÓWNA
# ==============================================================================
if menu_glowne == "🏠 Strona Główna":
    st.markdown("<div class='main-header'>Aplikacja - Prawo Górnicze i Geologiczne</div>", unsafe_allow_html=True)
    st.write(f"Zalogowany profil: **{st.session_state.zalogowany_uzytkownik}**")
    
    user_stats = st.session_state.statystyki.get(st.session_state.zalogowany_uzytkownik, [])
    dzisiaj_str = datetime.date.today().strftime("%Y-%m-%d")
    
    egz_dzisiaj = [s for s in user_stats if s['data'] == dzisiaj_str]
    egz_calosc = [s for s in user_stats if s['baza'] == "Wszystkie"]
    egz_czesc = [s for s in user_stats if s['baza'] != "Wszystkie"]
    
    calosc_pozytywne = sum(1 for s in egz_calosc if s['zdane'])
    calosc_negatywne = len(egz_calosc) - calosc_pozytywne
    
    czesc_pozytywne = sum(1 for s in egz_czesc if s['zdane'])
    czesc_negatywne = len(egz_czesc) - czesc_pozytywne

    st.subheader("📊 Twoje Statystyki Egzaminów")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    col_stat1.metric("Egzaminy dzisiaj", len(egz_dzisiaj))
    col_stat2.metric("Łącznie podejść", len(user_stats))
    col_stat3.metric("Całościowe (Pozytywne / Negatywne)", f"{calosc_pozytywne} / {calosc_negatywne}")
    col_stat4.metric("Z części (Pozytywne / Negatywne)", f"{czesc_pozytywne} / {czesc_negatywne}")

    if user_stats:
        st.write("### 📈 Wykresy Wyników Egzaminów")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.markdown("**Rozkład wyników (Zdane vs Niezdane)**")
            wszystkie_zdane = sum(1 for s in user_stats if s['zdane'])
            wszystkie_niezdane = len(user_stats) - wszystkie_zdane
            st.bar_chart({"Wyniki": {"Pozytywne": wszystkie_zdane, "Negatywne": wszystkie_niezdane}})
            
        with col_chart2:
            st.markdown("**Procentowe wyniki w kolejnych próbach (%)**")
            procenty = [s['procent'] for s in user_stats]
            st.line_chart(procenty)
    else:
        st.info("Brak zarejestrowanych wyników egzaminów. Rozwiąż egzamin, aby zobaczyć swoje statystyki!")

    st.markdown("---")
    
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
# 8. TESTY I NAUKA
# ==============================================================================
elif menu_glowne == "🎮 Testy i Nauka":
    if st.session_state.wybrana_baza is None and st.session_state.aktywny_tryb is None:
        st.markdown("<div class='main-header'>Wybierz tryb testowy lub bazę pytań</div>", unsafe_allow_html=True)
        
        if st.button("🚀 Uruchom Egzamin z CAŁEJ BAZY (50 pytań / 30 min)", use_container_width=True, type="primary"):
            st.session_state.wybrana_baza = "Cała baza (wszystkie pytania)"
            start_sesji("Tryb Egzaminu z CAŁEJ BAZY (50 pytań / 30 min)", "Cała baza (wszystkie pytania)", limit_pytan=50, tylko_wielokrotne=False)
            st.rerun()

        st.markdown("---")
        for nazwa_bazy in st.session_state.bazy.keys():
            if st.button(f"📁 {nazwa_bazy}", use_container_width=True):
                st.session_state.wybrana_baza = nazwa_bazy
                st.rerun()

    elif st.session_state.aktywny_tryb is None:
        nazwa_bary = st.session_state.wybrana_baza
        wszystkie = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=False)
        wielokrotne = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=True)

        st.markdown(f"**Wybrana baza:** {nazwa_bary}")
        st.markdown(f"* Wszystkie pytania w bazie: **{len(wszystkie)}**")
        st.markdown(f"* Pytania wielokrotnego wyboru: **{len(wielokrotne)}**")
        st.write("")

        col_w1, col_w2 = st.columns(2)
        
        with col_w1:
            st.markdown("### 🌐 Wszystkie Pytania")
            if st.button("Tryb Nauki (Kolejno)", key="n_w_k", use_container_width=True):
                start_sesji("Tryb Nauki (Wszystkie – Kolejno)", nazwa_bary, limit_pytan=None, tylko_wielokrotne=False)
                st.rerun()
            if st.button("Tryb Egzaminu (Losowo – 35 pytań)", key="e_w_l", use_container_width=True):
                start_sesji("Tryb Egzaminu (Wszystkie – Losowo 35)", nazwa_bary, limit_pytan=35, tylko_wielokrotne=False)
                st.rerun()

        with col_w2:
            st.markdown("### 🎯 Pytania Wielokrotnego Wyboru")
            if st.button("Tryb Nauki (Kolejno)", key="n_m_k", use_container_width=True):
                start_sesji("Tryb Nauki (Wielokrotne – Kolejno)", nazwa_bary, limit_pytan=None, tylko_wielokrotne=True)
                st.rerun()
            if st.button("Tryb Egzaminu (Losowo – 35 pytań)", key="e_m_l", use_container_width=True):
                start_sesji("Tryb Egzaminu (Wielokrotne – Losowo 35)", nazwa_bary, limit_pytan=35, tylko_wielokrotne=True)
                st.rerun()

        st.write("")
        if st.button("← Powrót do wyboru baz", use_container_width=True):
            powrot_do_wyboru()
            st.rerun()

    else:
        st.markdown(f"<div class='main-header'>{st.session_state.aktywny_tryb}</div>", unsafe_allow_html=True)
        lista = st.session_state.pytania_sesji
        idx = st.session_state.indeks

        if st.button("← Przerwij i wróć do menu"):
            powrot_do_wyboru()
            st.rerun()

        st.markdown("---")
        
        # Ekran trwania testu/nauki
        if idx < len(lista) and not st.session_state.test_zakonczony:
            p = lista[idx]
            st.markdown(f"**Pytanie {idx + 1} z {len(lista)}** (ID: {p['id']})")
            st.markdown(f"<div class='question-box'><h3>{p['pytanie']}</h3></div>", unsafe_allow_html=True)

            domyslne_zaznaczenia = st.session_state.odpowiedzi_egzamin.get(idx, [])

            with st.form(key=f"form_pyt_{idx}"):
                wybrane = []
                for k, v in p["odpowiedzi"].items():
                    czy_zaznaczone = k in domyslne_zaznaczenia
                    if st.checkbox(f"**{k}**: {v}", value=czy_zaznaczone, key=f"cb_{idx}_{k}"):
                        wybrane.append(k)
                zatwierdz = st.form_submit_button("Zatwierdź odpowiedź")

            if zatwierdz:
                st.session_state.odpowiedzi_egzamin[idx] = wybrane
                st.session_state.sprawdzono_odpowiedz = True

            if st.session_state.sprawdzono_odpowiedz:
                poprawne = set(p["poprawne"])
                zaznaczone = set(wybrane)
                if zaznaczone == poprawne:
                    st.success("✅ Twoja odpowiedź jest poprawna!")
                else:
                    st.error(f"❌ Twoja odpowiedź jest błędna. Poprawne to: {', '.join(p['poprawne'])}")

                st.info(f"**Podstawa prawna:** {p.get('podstawa_prawna', 'Brak')} \n\n {p.get('tresc_artykulu', '')}")

            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if idx > 0:
                    if st.button("⬅️ Poprzednie pytanie"):
                        st.session_state.indeks -= 1
                        st.session_state.sprawdzono_odpowiedz = (idx - 1) in st.session_state.odpowiedzi_egzamin
                        st.rerun()
            with col_btn2:
                if idx < len(lista) - 1:
                    if st.button("Następne pytanie ➡️"):
                        st.session_state.indeks += 1
                        st.session_state.sprawdzono_odpowiedz = st.session_state.indeks in st.session_state.odpowiedzi_egzamin
                        st.rerun()
                else:
                    if st.button("🏁 Zakończ i zobacz wynik", type="primary"):
                        st.session_state.test_zakonczony = True
                        st.rerun()

        # Ekran podsumowania po zakończeniu testu / egzaminu
        else:
            st.markdown("<div class='main-header'>📋 Podsumowanie Wyników Testu</div>", unsafe_allow_html=True)
            
            punkty = 0
            max_punkty = len(lista)
            
            for i, p in enumerate(lista):
                odp_uzytkownika = set(st.session_state.odpowiedzi_egzamin.get(i, []))
                poprawne_odpowiedzi = set(p["poprawne"])
                if odp_uzytkownika == poprawne_odpowiedzi:
                    punkty += 1

            procent = (punkty / max_punkty) * 100 if max_punkty > 0 else 0
            
            col_m1, col_m2 = st.columns(2)
            col_m1.metric("Wynik punktowy", f"{punkty} / {max_punkty}")
            col_m2.metric("Skuteczność", f"{procent:.1f}%")
            
            # Zapis do trwałego pliku statystyk
            zapisz_wynik_egzaminu(
                user=st.session_state.zalogowany_uzytkownik,
                tryb=st.session_state.aktywny_tryb,
                baza=st.session_state.wybrana_baza,
                punkty=punkty,
                max_punkty=max_punkty
            )

            st.markdown("---")
            st.subheader("🔍 Szczegółowy przegląd odpowiedzi:")

            for i, p in enumerate(lista):
                odp_uzytkownika = sorted(st.session_state.odpowiedzi_egzamin.get(i, []))
                poprawne_odpowiedzi = sorted(p["poprawne"])
                czy_ok = (set(odp_uzytkownika) == set(poprawne_odpowiedzi))
                
                status_ikonka = "✅" if czy_ok else "❌"
                
                with st.expander(f"{status_ikonka} Pytanie {i+1}: {p['pytanie']}"):
                    st.write(f"**Twoja odpowiedź:** {', '.join(odp_uzytkownika) if odp_uzytkownika else 'Brak odpowiedzi'}")
                    st.write(f"**Poprawna odpowiedź:** {', '.join(poprawne_odpowiedzi)}")
                    st.markdown(f"**Podstawa prawna:** {p.get('podstawa_prawna', 'Brak')}")
                    if p.get('tresc_artykulu'):
                        st.markdown(f"> *{p.get('tresc_artykulu')}*")

            st.write("")
            if st.button("🔄 Rozpocznij nowy test", type="primary", use_container_width=True):
                powrot_do_wyboru()
                st.rerun()

# ==============================================================================
# 9. DODAJ PYTANIE
# ==============================================================================
elif menu_glowne == "➕ Dodaj Pytanie":
    st.markdown("<div class='main-header'>Dodaj nowe pytanie do bazy</div>", unsafe_allow_html=True)
    baza_docelowa = st.radio("Wybierz bazę:", list(st.session_state.bazy.keys()), horizontal=True)

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
# 10. PRZEGLĄD BAZY
# ==============================================================================
elif menu_glowne == "🔍 Przegląd Bazy":
    st.markdown("<div class='main-header'>Przegląd Bazy Pytań</div>", unsafe_allow_html=True)
    
    opcje_przegladu = ["Cała baza (wszystkie pytania)", "Cała baza (tylko wielokrotne)"] + list(st.session_state.bazy.keys())
    wybrana = st.radio("Wybierz bazę do przeglądu:", opcje_przegladu, horizontal=True)
    
    if wybrana == "Cała baza (wszystkie pytania)":
        lista_do_wyswietlenia = pobierz_pytania_z_bazy("Cała baza (wszystkie pytania)", tylko_wielokrotne=False)
    elif wybrana == "Cała baza (tylko wielokrotne)":
        lista_do_wyswietlenia = pobierz_pytania_z_bazy("Cała baza (wszystkie pytania)", tylko_wielokrotne=True)
    else:
        lista_do_wyswietlenia = st.session_state.bazy[wybrana]
        
    st.caption(f"Wyświetlono pytań: {len(lista_do_wyswietlenia)}")

    for item in lista_do_wyswietlenia:
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
# 11. PANEL ADMINISTRATORA
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
        st.subheader("📊 Podgląd Wyników i Statystyk Wszystkich Użytkowników")
        
        for u_name in USERS_PIN.keys():
            st.markdown(f"### Użytkownik: **{u_name}**")
            u_stats = st.session_state.statystyki.get(u_name, [])
            
            if u_stats:
                u_zdane = sum(1 for s in u_stats if s['zdane'])
                u_niezdane = len(u_stats) - u_zdane
                
                c1, c2, c3 = st.columns(3)
                c1.metric("Podejścia ogółem", len(u_stats))
                c2.metric("Egzaminy ZDANE", u_zdane)
                c3.metric("Egzaminy NIEZDANE", u_niezdane)
                
                col_chart1, col_chart2 = st.columns(2)
                with col_chart1:
                    st.bar_chart({"Wyniki": {"Pozytywne": u_zdane, "Negatywne": u_niezdane}})
                with col_chart2:
                    st.line_chart([s['procent'] for s in u_stats])
            else:
                st.info(f"Brak zapisanych wyników dla użytkownika {u_name}.")
            st.markdown("---")

        st.subheader("✏️ Edycja oraz zarządzanie pytaniami w bazie")
        wybrana_baza_admin = st.radio("Wybierz część bazy do edycji:", list(st.session_state.bazy.keys()), key="admin_baza_select", horizontal=True)
        lista_pytan = st.session_state.bazy[wybrana_baza_admin]

        if not lista_pytan:
            st.warning("Wybrana baza nie posiada żadnych pytań.")
        else:
            opcje_pytan = [f"ID {p['id']}: {p['pytanie'][:60]}..." for p in lista_pytan]
            wybrane_pytanie_str = st.radio("Wybierz pytanie do edycji/usunięcia:", opcje_pytan)
            
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
# 12. USTAWIENIA I MOTYW
# ==============================================================================
elif menu_glowne == "⚙️ Ustawienia / Motyw":
    st.markdown("<div class='main-header'>Ustawienia i Personalizacja</div>", unsafe_allow_html=True)
    
    st.subheader("🎨 Wybór motywu wizualnego")
    
    opcje_motywu = ["Ciemny", "Jasny"]
    wybrany_index = opcje_motywu.index(st.session_state.theme) if st.session_state.theme in opcje_motywu else 0

    nowy_motyw = st.radio(
        "Wybierz preferowany motyw:",
        opcje_motywu,
        index=wybrany_index,
        key="settings_theme_radio"
    )

    if nowy_motyw != st.session_state.theme:
        st.session_state.theme = nowy_motyw
        aktualizuj_pamiec_sesji(theme=nowy_motyw)
        st.success(f"Zmieniono tryb na: {nowy_motyw}")
        st.rerun()
