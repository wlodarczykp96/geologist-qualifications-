import streamlit as st
import random
import time
import datetime
import json
import os
import streamlit.components.v1 as components
from github import Github

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
# 2. OBSŁUGA TRWAŁEGO ZAPISU DANYCH (JSON)
# ==============================================================================
PLIK_STATYSTYK = "statystyki.json"

def wczytaj_statystyki():
    try:
        with open("statystyki.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"Piotrek": [], "Edyta": [], "Gość": []}

if "statystyki" not in st.session_state:
    st.session_state.statystyki = wczytaj_statystyki()

def zapisz_wynik_egzaminu(user, tryb, baza, punkty, max_punkty):
    st.info("🔄 Rozpoczynam próbę zapisu do GitHuba...")
    
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
    
    # Wysyłanie do GitHub API
    try:
        if "GITHUB_TOKEN" not in st.secrets or "GITHUB_REPO" not in st.secrets:
            st.error("❌ Brak kluczy GITHUB_TOKEN lub GITHUB_REPO w Streamlit Secrets!")
            return

        token = st.secrets["GITHUB_TOKEN"]
        repo_name = st.secrets["GITHUB_REPO"]
        
        g = Github(token)
        repo = g.get_repo(repo_name)
        
        contents = repo.get_contents("statystyki.json")
        nowa_tresc = json.dumps(st.session_state.statystyki, ensure_ascii=False, indent=4)
        
        repo.update_file(
            path=contents.path,
            message=f"Auto-update statystyk: {user}",
            content=nowa_tresc,
            sha=contents.sha
        )
        st.success("✅ Zamieszczono nowy commit w repozytorium GitHub!")
    except Exception as e:
        st.error(f"❌ Błąd GitHub API: {e}")
# ==============================================================================
# 3. MECHANIZM TRWAŁEJ SESJI I INICJALIZACJA
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
    st.session_state.statystyki = wczytaj_json(PLIK_STATYSTYK, {"Piotrek": [], "Edyta": [], "Gość": []})

if 'bazy' not in st.session_state:
    st.session_state.bazy = wczytaj_json(PLIK_BAZY, DOMYSLNA_BAZA)

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
# 4. GLOBALNY MOTYW CSS
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

    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {{
        background-color: var(--box-bg) !important;
    }}

    li[role="option"] {{
        background-color: var(--box-bg) !important;
        color: var(--box-text) !important;
    }}

    li[role="option"]:hover {{
        background-color: rgba(255, 75, 75, 0.2) !important;
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
# 5. FUNKCJE POMOCNICZE
# ==============================================================================
def pobierz_pytania_z_bazy(nazwa_bazy, tylko_wielokrotne=False):
    if nazwa_bazy == "Cała baza (wszystkie pytania)":
        pula = []
        for b in st.session_state.bazy.values():
            pula.extend(b)
    else:
        pula = list(st.session_state.bazy.get(nazwa_bazy, []))
    
    if tylko_wielokrotne:
        return [p for p in pula if len(p.get("poprawne", [])) in [1, 2]]
    return pula

def start_sesji(tryb, baza_nazwa, limit_pytan=None, tylko_wielokrotne=False):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.odpowiedzi_egzamin = {}
    st.session_state.test_zakonczony = False
    st.session_state.id_obecnej_sesji = time.time()  # Unikalny identyfikator nowej sesji
    
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
    zapisz_json(PLIK_STATYSTYK, st.session_state.statystyki)

# ==============================================================================
# 6. EKRAN LOGOWANIA
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
# 7. MENU BOCZNE
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
# 8. STRONA GŁÓWNA
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
# 9. TESTY I NAUKA
# ==============================================================================
elif menu_glowne == "🎮 Testy i Nauka":
    if st.session_state.wybrana_baza is None and st.session_state.aktywny_tryb is None:
        st.markdown("<div class='main-header'>Wybierz tryb testowy lub bazę pytań</div>", unsafe_allow_html=True)
        
        st.subheader("📚 PEŁNE BAZY")
        if st.button("🚀 Uruchom Egzamin WIELOKTOTNEGO WYBROU (1/2/3) (Wszystkie pytania | 50 pytań / 30 min)", use_container_width=True, type="primary"):
            st.session_state.wybrana_baza = "Cała baza (wszystkie pytania)"
            start_sesji("Egzamin (Losowo – 50 pytań)", "Cała baza (wszystkie pytania)", limit_pytan=50, tylko_wielokrotne=False)
            st.rerun()

        if st.button("🎯 Uruchom Egzamin WIELOKTOTNEGO WYBROU (1/2) (Wszystkie pytania | 50 pytań / 30 min)", use_container_width=True):
            st.session_state.wybrana_baza = "Cała baza (wszystkie pytania)"
            start_sesji("Egzamin (Losowo – 50 pytań)", "Cała baza (wszystkie pytania)", limit_pytan=50, tylko_wielokrotne=True)
            st.rerun()

        st.markdown("---")
        st.subheader("📁 Wybierz Rozdział Bazy")
        for nazwa_bazy in st.session_state.bazy.keys():
            if st.button(f"📁 {nazwa_bazy}", use_container_width=True):
                st.session_state.wybrana_baza = nazwa_bazy
                st.rerun()

    elif st.session_state.aktywny_tryb is None:
        nazwa_bary = st.session_state.wybrana_baza
        wszystkie = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=False)
        wielokrotne = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=True)

        st.markdown(f"**Wybrana baza:** {nazwa_bary}")
        st.markdown(f"* Wszystkie pytania WIELOKTORNEGO WYBORU (1/2/3): **{len(wszystkie)}**")
        st.markdown(f"* Wszystkie pytania WIELOKTORNEGO WYBORU (1/2) **{len(wielokrotne)}**")
        st.write("")

        st.subheader("Wybierz wariant testu:")
        
        col_w1, col_w2 = st.columns(2)
        
        with col_w1:
            st.markdown("### 🌐 WIELOKROTNY WYBÓR (1/2/3)")
            if st.button("Tryb Nauki (Kolejno)", key="n_w_k", use_container_width=True):
                start_sesji("Tryb Nauki (Wszystkie – Kolejno)", nazwa_bary, limit_pytan=None, tylko_wielokrotne=False)
                st.rerun()
            if st.button("Tryb Nauki (Losowo – 30 pytań)", key="n_w_l", use_container_width=True):
                start_sesji("Tryb Nauki (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=False)
                st.rerun()
            if st.button("Egzamin (Losowo – 30 pytań)", key="e_w_l", use_container_width=True):
                start_sesji("Egzamin (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=False)
                st.rerun()

        with col_w2:
            st.markdown("### 🎯 WIELOKROTNY WYBÓR (1/2)")
            if st.button("Tryb Nauki (Kolejno)", key="n_f_k", use_container_width=True):
                start_sesji("Tryb Nauki (Kolejno)", nazwa_bary, limit_pytan=None, tylko_wielokrotne=True)
                st.rerun()
            if st.button("Tryb Nauki (Losowo – 30 pytań)", key="n_f_l", use_container_width=True):
                start_sesji("Tryb Nauki (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=True)
                st.rerun()
            if st.button("Egzaminu (Losowo – 30 pytań)", key="e_f_l", use_container_width=True):
                start_sesji("Egzaminu (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=True)
                st.rerun()
        st.write("")
        if st.button("← Powrót do wyboru baz", use_container_width=True):
            powrot_do_wyboru()
            st.rerun()

    else:
        if st.session_state.czas_konca is not None and not st.session_state.test_zakonczony:
            pozostaly_czas_ms = int((st.session_state.czas_konca - time.time()) * 1000)
            if pozostaly_czas_ms <= 0:
                st.session_state.test_zakonczony = True
                st.rerun()
            else:
                timer_html = """
                <div style="font-size: 18px; font-weight: bold; color: #ff4b4b; background-color: var(--bg-sec); padding: 10px; border-radius: 8px; margin-bottom: 15px; text-align: center; border: 1px solid var(--border-color);">
                    ⏱️ Pozostały czas egzaminu: <span id="countdown">--:--</span>
                </div>
                <script>
                    var endTime = new Date().getTime() + """ + str(pozostaly_czas_ms) + """;
                    var x = setInterval(function() {
                        var now = new Date().getTime();
                        var distance = endTime - now;
                        
                        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                        
                        minutes = minutes < 10 ? "0" + minutes : minutes;
                        seconds = seconds < 10 ? "0" + seconds : seconds;
                        
                        document.getElementById("countdown").innerHTML = minutes + ":" + seconds;
                        
                        if (distance < 0) {
                            clearInterval(x);
                            document.getElementById("countdown").innerHTML = "00:00";
                            window.parent.location.reload();
                        }
                    }, 1000);
                </script>
                """
                components.html(timer_html, height=60)

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
                        
                        if "Egzamin" in st.session_state.aktywny_tryb:
                            punkty = sum(
                                1 for i, q in enumerate(lista) 
                                if set(st.session_state.odpowiedzi_egzamin.get(i, [])) == set(q["poprawne"])
                            )
                            zapisz_wynik_egzaminu(
                                st.session_state.zalogowany_uzytkownik,
                                st.session_state.aktywny_tryb,
                                st.session_state.wybrana_baza,
                                punkty,
                                len(lista)
                            )
                        st.rerun()
        else:
            st.balloons()
            st.success("🎉 Zakończyłeś test / egzamin!")
            
            if "Egzamin" in st.session_state.aktywny_tryb:
                punkty = 0
                szczegoly_wynikow = []
                for i, q in enumerate(lista):
                    user_ans = set(st.session_state.odpowiedzi_egzamin.get(i, []))
                    correct_ans = set(q["poprawne"])
                    is_correct = (user_ans == correct_ans)
                    if is_correct:
                        punkty += 1
                    szczegoly_wynikow.append({
                        "id": q["id"],
                        "pytanie": q["pytanie"],
                        "odpowiedzi": q["odpowiedzi"],
                        "user_ans": sorted(list(user_ans)),
                        "correct_ans": sorted(list(correct_ans)),
                        "is_correct": is_correct,
                        "podstawa": q.get("podstawa_prawna", "Brak"),
                        "artykul": q.get("tresc_artykulu", "Brak")
                    })
                
                procent = (punkty / len(lista)) * 100 if len(lista) > 0 else 0
                zdane = procent >= 75.0

                st.markdown("### 📊 Statystyki i Podsumowanie Egzaminu")
                col_res1, col_res2, col_res3 = st.columns(3)
                col_res1.metric("Uzyskany wynik", f"{punkty} / {len(lista)}")
                col_res2.metric("Skuteczność", f"{procent:.1f}%")
                col_res3.metric("Status egzaminu", "POZYTYWNY (ZDANE)" if zdane else "NEGATYWNY (NIEZDANE)")
                
                st.markdown("---")
                st.subheader("📝 Szczegółowa Analiza Odpowiedzi")
                
                filtr_odp = st.radio(
                    "Filtruj pytania:",
                    ["Wszystkie", "Tylko poprawne ✅", "Tylko błędne ❌"],
                    horizontal=True,
                    key="filtr_odp_egzamin"
                )

                for i, res in enumerate(szczegoly_wynikow):
                    if filtr_odp == "Tylko poprawne ✅" and not res["is_correct"]:
                        continue
                    if filtr_odp == "Tylko błędne ❌" and res["is_correct"]:
                        continue

                    status_str = "✅ POPRAWNA" if res["is_correct"] else "❌ BŁĘDNA"
                    u_ans_str = ", ".join(res["user_ans"]) if res["user_ans"] else "Brak odpowiedzi"
                    c_ans_str = ", ".join(res["correct_ans"])

                    with st.expander(f"Pytanie {i+1} [ID: {res['id']}] - {status_str} | Twoja odp: {u_ans_str} (Poprawna: {c_ans_str})"):
                        st.markdown(f"**Treść pytania:** {res['pytanie']}")
                        for k, v in res["odpowiedzi"].items():
                            st.write(f"**{k}**: {v}")
                        
                        st.markdown("---")
                        st.write(f"👉 **Twoja odpowiedź:** {u_ans_str}")
                        st.write(f"✅ **Poprawna odpowiedź:** {c_ans_str}")
                        
                        if res["podstawa"] != "Brak" or res["artykul"] != "Brak":
                            st.markdown(f"""
                            <div class='legal-box'>
                                <strong>📜 Podstawa prawna:</strong> {res['podstawa']}<br><br>
                                <strong>📖 Treść artykułu:</strong><br>
                                <em>{res['artykul']}</em>
                            </div>
                            """, unsafe_allow_html=True)

            if st.button("🔄 Rozpocznij ponownie"):
                powrot_do_wyboru()
                st.rerun()

# ==============================================================================
# 10. DODAJ PYTANIE
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
                zapisz_json(PLIK_BAZY, st.session_state.bazy)
                st.success(f"Dodano pytanie o ID {nowe_id} i zapisano baze na stałe!")
            else:
                st.error("Uzupełnij pola i wybierz co najmniej jedną poprawną odpowiedź!")

# ==============================================================================
# 11. PRZEGLĄD BAZY
# ==============================================================================
elif menu_glowne == "🔍 Przegląd Bazy":
    st.markdown("<div class='main-header'>Przegląd Bazy Pytań</div>", unsafe_allow_html=True)
    
    opcje_przegladu = ["Cała baza (wszystkie pytania)", "Cała baza (pytania wielokrotnego wyboru)"] + list(st.session_state.bazy.keys())
    wybrana = st.radio("Wybierz bazę do przeglądu:", opcje_przegladu, horizontal=True)
    
    if wybrana == "Cała baza (wszystkie pytania)":
        lista_do_wyswietlenia = pobierz_pytania_z_bazy("Cała baza (wszystkie pytania)", tylko_wielokrotne=False)
    elif wybrana == "Cała baza (pytania wielokrotnego wyboru)":
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
# 12. PANEL ADMINISTRATORA
# ==============================================================================
elif menu_glowne == "🔑 Panel Administratora":
    st.markdown("<div class='main-header'>🔑 Panel Administratora</div>", unsafe_allow_html=True)

    if not st.session_state.admin_logged_in:
        with st.form("admin_login_form"):
            pass_input = st.text_input("Podaj hasło administratora:", type="password")
            btn_login = st.form_submit_button("Zaloguj się")
            if btn_login:
                if pass_input == "admin123":
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
                    zapisz_json(PLIK_BAZY, st.session_state.bazy)
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

                        zapisz_json(PLIK_BAZY, st.session_state.bazy)
                        st.success("Zmiany zostały pomyślnie zapisane!")
                        st.rerun()
                    else:
                        st.error("Pola pytania/odpowiedzi nie mogą być puste, oraz co najmniej jedna odpowiedź musi być zaznaczona jako poprawna!")

# ==============================================================================
# 13. USTAWIENIA I MOTYW
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
