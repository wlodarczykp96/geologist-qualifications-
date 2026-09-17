import streamlit as st
import random
import time
import datetime
import streamlit.components.v1 as components

# W app.py pobieramy dane z osobnego pliku bazy_danych.py:
from baza_danych import BAZY_PYTAN

# I inicjalizujemy je w sesji w ten sposób:
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
    st.session_state.statystyki = {
        "Piotrek": [],
        "Edyta": [],
        "Gość": []
    }

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

# Przypisanie zaimportowanych baz do stanu sesji
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

    .question-box {{
        background-color: var(--bg-sec) !important;
        padding: 18px;
        border-radius: 8px;
        border: 1px solid var(--border-color);
        margin-bottom: 15px;
    }}

    .legal-box {{
        background-color: var(--bg-sec) !important;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #0d6efd;
        margin: 15px 0;
        border: 1px solid var(--border-color);
    }}

    .main-header {{
        font-size: 22px;
        font-weight: bold;
        border-bottom: 2px solid var(--border-color);
        padding-bottom: 8px;
        margin-bottom: 15px;
    }}
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
        # Pytania wielokrotne to te, które mają 2 (lub więcej) poprawnych odpowiedzi
        return [p for p in pula if len(p.get("poprawne", [])) >= 2]
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
    st.session_state.statystyki[user].append(wpis)

# ==============================================================================
# 5. EKRAN LOGOWANIA
# ==============================================================================
if st.session_state.zalogowany_uzytkownik is None:
    st.markdown("<div class='main-header'>🔒 Aplikacja - Prawo Górnicze i Geologiczne</div>", unsafe_allow_html=True)
    
    col_login, _ = st.columns([1, 1])
    with col_login:
        wybrany_user = st.selectbox("Wybierz użytkownika:", options=list(USERS_PIN.keys()))
        wymaga_pin = USERS_PIN[wybrany_user] is not None
        
        podany_pin = st.text_input("Podaj swój PIN:", type="password") if wymaga_pin else None

        if st.button("Zaloguj się", type="primary", use_container_width=True):
            if not wymaga_pin or podany_pin == USERS_PIN[wybrany_user]:
                st.session_state.zalogowany_uzytkownik = wybrany_user
                aktualizuj_pamiec_sesji(user=wybrany_user)
                st.success(f"Pomyślnie zalogowano jako {wybrany_user}!")
                st.rerun()
            else:
                st.error("Błędny PIN! Spróbuj ponownie.")

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
    st.subheader("📊 Twoje Statystyki Egzaminów")
    st.metric("Łącznie podejść", len(user_stats))

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
        if idx < len(lista) and not st.session_state.test_zakonczony:
            p = lista[idx]
            st.markdown(f"**Pytanie {idx + 1} z {len(lista)}** (ID: {p['id']})")
            st.markdown(f"<div class='question-box'><h3>{p['pytanie']}</h3></div>", unsafe_allow_html=True)

            with st.form(key=f"form_pyt_{idx}"):
                wybrane = []
                for k, v in p["odpowiedzi"].items():
                    if st.checkbox(f"**{k}**: {v}", key=f"cb_{idx}_{k}"):
                        wybrane.append(k)
                zatwierdz = st.form_submit_button("Zatwierdź / Sprawdź")

            if zatwierdz:
                st.session_state.sprawdzono_odpowiedz = True

            if st.session_state.sprawdzono_odpowiedz:
                poprawne = set(p["poprawne"])
                zaznaczone = set(wybrane)
                if zaznaczone == poprawne:
                    st.success("✅ Poprawna odpowiedź!")
                else:
                    st.error(f"❌ Błąd! Poprawne odpowiedzi to: {', '.join(p['poprawne'])}")

                st.info(f"Podstawa prawna: {p.get('podstawa_prawna', 'Brak')} \n\n {p.get('tresc_artykulu', '')}")

            if st.button("Następne pytanie ➡️"):
                if idx < len(lista) - 1:
                    st.session_state.indeks += 1
                    st.session_state.sprawdzono_odpowiedz = False
                    st.rerun()
                else:
                    st.session_state.test_zakonczony = True
                    st.rerun()
        else:
            st.success("🎉 Koniec testu!")
            if st.button("Rozpocznij od nowa"):
                powrot_do_wyboru()
                st.rerun()

# ==============================================================================
# 9. POZOSTAŁE ZAKŁADKI (Dodaj Pytanie, Przegląd, Admin, Ustawienia)
# ==============================================================================
elif menu_glowne == "➕ Dodaj Pytanie":
    st.markdown("<div class='main-header'>Dodaj Pytanie</div>", unsafe_allow_html=True)
    st.write("Formularz dodawania pytań (możesz dopisać logikę zapisu do pliku bazy, jeśli chcesz zachować trwałość na dysku).")

elif menu_glowne == "🔍 Przegląd Bazy":
    st.markdown("<div class='main-header'>Przegląd Bazy</div>", unsafe_allow_html=True)
    for dzial, pytania in st.session_state.bazy.items():
        st.subheader(dzial)
        for p in pytania:
            st.write(f"- ID {p['id']}: {p['pytanie']}")

elif menu_glowne == "🔑 Panel Administratora":
    st.markdown("<div class='main-header'>Panel Administratora</div>", unsafe_allow_html=True)
    st.info("Zarządzanie bazą i podgląd statystyk.")

elif menu_glowne == "⚙️ Ustawienia / Motyw":
    st.markdown("<div class='main-header'>Ustawienia</div>", unsafe_allow_html=True)
    nowy_motyw = st.radio("Motyw:", ["Ciemny", "Jasny"], index=0 if st.session_state.theme == "Ciemny" else 1)
    if nowy_motyw != st.session_state.theme:
        st.session_state.theme = nowy_motyw
        aktualizuj_pamiec_sesji(theme=nowy_motyw)
        st.rerun()
