import streamlit as st
import random
import time
import datetime
import json
import os
import streamlit.components.v1 as components
from github import Github

# ==============================================================================
# IMPORT BAZ JAKO MODUŁÓW PYTHONA (.py)
# ==============================================================================
try:
    from Baza_1_v2 import BAZY_PYTAN as b1
    baza_1_lista = list(b1.values())[0] if b1 else []
except ImportError:
    baza_1_lista = []

try:
    from Baza_2_v2 import BAZY_PYTAN as b2
    baza_2_lista = list(b2.values())[0] if b2 else []
except ImportError:
    baza_2_lista = []

try:
    from Baza_3_v2 import BAZY_PYTAN as b3
    baza_3_lista = list(b3.values())[0] if b3 else []
except ImportError:
    baza_3_lista = []

try:
    from Baza_4_v2 import BAZY_PYTAN as b4
    baza_4_lista = list(b4.values())[0] if b4 else []
except ImportError:
    baza_4_lista = []

try:
    from Baza_5_v1 import BAZY_PYTAN as b5
    baza_5_lista = b5.get("BAZA PYTAŃ - CZĘŚĆ 5 (Wiedz ogólna o Prawie Górniczym i geologicznym [...])", [])
except ImportError:
    baza_5_lista = []

PLIKI_BAZ = {
    "Baza 1": "Baza_1_v2.py",
    "Baza 2": "Baza_2_v2.py",
    "Baza 3": "Baza_3_v2.py",
    "Baza 4": "Baza_4_v2.py",
    "Baza 5": "Baza_5_v1.py"
}

if 'bazy' not in st.session_state:
    st.session_state.bazy = {
        "Baza 1": baza_1_lista,
        "Baza 2": baza_2_lista,
        "Baza 3": baza_3_lista,
        "Baza 4": baza_4_lista,
        "Baza 5": baza_5_lista
    }
    
# ==============================================================================
# 1. KONFIGURACJA STRONY
# ==============================================================================
st.set_page_config(
    page_title="Aplikacja - Prawo Górnicze i Geologiczne",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
if 'wynik_zapisany' not in st.session_state:
    st.session_state.wynik_zapisany = False

# --- ZMIENNE DLA TRYBU INTELIGENTNEJ NAUKI (QUIZLET / DUOLINGO) ---
if 'smart_pula_calkowita' not in st.session_state:
    st.session_state.smart_pula_calkowita = []
if 'smart_nieopanowane' not in st.session_state:
    st.session_state.smart_nieopanowane = []
if 'smart_kolejka_rundy' not in st.session_state:
    st.session_state.smart_kolejka_rundy = []
if 'smart_opanowane_ids' not in st.session_state:
    st.session_state.smart_opanowane_ids = set()
if 'smart_bledne_w_rundzie' not in st.session_state:
    st.session_state.smart_bledne_w_rundzie = set()
if 'smart_nr_rundy' not in st.session_state:
    st.session_state.smart_nr_rundy = 1
if 'smart_ostatni_wynik' not in st.session_state:
    st.session_state.smart_ostatni_wynik = None
if 'smart_krok' not in st.session_state:
    st.session_state.smart_krok = 0

def aktualizuj_pamiec_sesji(user=None, theme=None):
    if user is not None:
        if user is False:
            if "user" in st.query_params:
                del st.query_params["user"]
        else:
            st.query_params["user"] = user

    if theme is not None:
        st.session_state.theme = theme
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
    [data-testid="stCheckbox"] p, [data-testid="stCheckbox"] span, [data-testid="stCheckbox"] label,
    [data-testid="stRadio"] p, [data-testid="stRadio"] span, [data-testid="stRadio"] label,
    [data-testid="stWidgetLabel"] p, [data-testid="stMarkdownContainer"] p {{
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
# 2. OBSŁUGA TRWAŁEGO ZAPISU DANYCH (JSON / GITHUB)
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

def zapisz_konkretna_baze(nazwa_bazy):
    if nazwa_bazy not in PLIKI_BAZ:
        return
    
    plik = PLIKI_BAZ[nazwa_bazy]
    dane_bazy = st.session_state.bazy[nazwa_bazy]

    try:
        if plik.endswith(".py"):
            zapisywana_tresc = f"BAZY_PYTAN = {{\n    \"BAZA PYTAŃ - CZĘŚĆ\": " + json.dumps(dane_bazy, ensure_ascii=False, indent=4) + "\n}"
            with open(plik, "w", encoding="utf-8") as f:
                f.write(zapisywana_tresc)
        else:
            with open(plik, "w", encoding="utf-8") as f:
                json.dump(dane_bazy, f, ensure_ascii=False, indent=4)
    except Exception as e:
        st.error(f"❌ Błąd lokalnego zapisu bazy {nazwa_bazy}: {e}")

    try:
        if "GITHUB_TOKEN" not in st.secrets or "GITHUB_REPO" not in st.secrets:
            return

        token = st.secrets["GITHUB_TOKEN"].strip()
        if token.startswith("gghp_"):
            token = token[1:]

        repo_name = st.secrets["GITHUB_REPO"].strip().replace("https://github.com/", "").strip("/")

        g = Github(token)
        repo = g.get_repo(repo_name)

        if plik.endswith(".py"):
            nowa_tresc = f"BAZY_PYTAN = {{\n    \"BAZA PYTAŃ - CZĘŚĆ\": " + json.dumps(dane_bazy, ensure_ascii=False, indent=4) + "\n}"
        else:
            nowa_tresc = json.dumps(dane_bazy, ensure_ascii=False, indent=4)

        try:
            contents = repo.get_contents(plik)
            repo.update_file(
                path=contents.path,
                message=f"Auto-update bazy pytań: {nazwa_bazy}",
                content=nowa_tresc,
                sha=contents.sha
            )
        except Exception:
            repo.create_file(
                path=plik,
                message=f"Utworzenie pliku bazy pytań: {nazwa_bazy}",
                content=nowa_tresc
            )

        st.cache_data.clear()
        st.success(f"✅ Baza '{nazwa_bazy}' została pomyślnie zsynchronizowana z GitHubem!")

    except Exception as e:
        st.error(f"❌ Błąd synchronizacji bazy {nazwa_bazy} z GitHub: {e}")

def zapisz_json(sciezka, dane):
    try:
        with open(sciezka, "w", encoding="utf-8") as f:
            json.dump(dane, f, ensure_ascii=False, indent=4)
    except Exception as e:
        st.error(f"❌ Błąd zapisu lokalnego: {e}")

    try:
        if "GITHUB_TOKEN" not in st.secrets or "GITHUB_REPO" not in st.secrets:
            st.error("❌ BRAK KLUCZY w Streamlit Secrets!")
            return

        token = st.secrets["GITHUB_TOKEN"].strip()
        if token.startswith("gghp_"):
            token = token[1:]

        repo_name = st.secrets["GITHUB_REPO"].strip()
        repo_name = repo_name.replace("https://github.com/", "").strip("/")

        g = Github(token)
        repo = g.get_repo(repo_name)

        nowa_tresc = json.dumps(dane, ensure_ascii=False, indent=4)

        try:
            contents = repo.get_contents(sciezka)
            repo.update_file(
                path=contents.path,
                message="Auto-update statystyk egzaminu",
                content=nowa_tresc,
                sha=contents.sha
            )
        except Exception:
            repo.create_file(
                path=sciezka,
                message="Utworzenie pliku statystyk",
                content=nowa_tresc
            )

        st.cache_data.clear()
        st.success("✅ Zapisano i zsynchronizowano z GitHubem!")

    except Exception as e:
        st.error(f"❌ Błąd synchronizacji z GitHub: {e}")

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
# 5. FUNKCJE POMOCNICZE
# ==============================================================================
def pobierz_pytania_z_bazy(nazwa_bazy, tylko_wielokrotne=False):
    if nazwa_bazy == "Egzamin mieszany (40 Baza 1 + 10 reszta)":
        b1 = list(st.session_state.bazy.get("Baza 1", []))
        reszta = []
        for k, v in st.session_state.bazy.items():
            if k != "Baza 1":
                reszta.extend(v)
        
        if tylko_wielokrotne:
            b1 = [p for p in b1 if len(p.get("poprawne", [])) in [1, 2]]
            reszta = [p for p in reszta if len(p.get("poprawne", [])) in [1, 2]]
            
        random.shuffle(b1)
        random.shuffle(reszta)
        
        pula = b1[:40] + reszta[:10]
        random.shuffle(pula)
        return pula

    elif nazwa_bazy == "Cała baza (wszystkie pytania)":
        pula = []
        for nazwa_b, b in st.session_state.bazy.items():
            for p in b:
                p_copy = dict(p)
                p_copy["_uid"] = f"{nazwa_b}_{p['id']}"
                pula.append(p_copy)
    else:
        pula = []
        for p in st.session_state.bazy.get(nazwa_bazy, []):
            p_copy = dict(p)
            p_copy["_uid"] = f"{nazwa_bazy}_{p['id']}"
            pula.append(p_copy)
    
    if tylko_wielokrotne:
        return [p for p in pula if len(p.get("poprawne", [])) in [1, 2]]
    return pula

def start_sesji(tryb, baza_nazwa, limit_pytan=None, tylko_wielokrotne=False):
    st.session_state.aktywny_tryb = tryb
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.odpowiedzi_egzamin = {}
    st.session_state.test_zakonczony = False
    st.session_state.wynik_zapisany = False
    st.session_state.id_obecnej_sesji = time.time()
    
    pula = pobierz_pytania_z_bazy(baza_nazwa, tylko_wielokrotne=tylko_wielokrotne)
    
    if baza_nazwa != "Egzamin mieszany (40 Baza 1 + 10 reszta)":
        if "Losowo" in tryb or "Egzamin" in tryb:
            random.shuffle(pula)
        if limit_pytan:
            pula = pula[:limit_pytan]
        
    st.session_state.pytania_sesji = pula
    if "20 min" in tryb:
        st.session_state.czas_konca = time.time() + (20 * 60)
    else:
        st.session_state.czas_konca = None

def start_inteligentna_nauka(baza_nazwa, tylko_wielokrotne=False, rozmiar_partii=20):
    st.session_state.aktywny_tryb = "Inteligentna Nauka (1/2)" if tylko_wielokrotne else "Inteligentna Nauka (1/2/3)"
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.smart_ostatni_wynik = None
    st.session_state.smart_krok = 0
    
    pula = pobierz_pytania_z_bazy(baza_nazwa, tylko_wielokrotne=tylko_wielokrotne)
    random.shuffle(pula)
    
    st.session_state.smart_pula_calkowita = pula
    st.session_state.smart_opanowane_ids = set()
    st.session_state.smart_nr_rundy = 1
    st.session_state.smart_bledne_w_rundzie = set()
    
    # Wydzielenie pierwszej partii (20 pytań) i reszty nieopanowanych
    st.session_state.smart_kolejka_rundy = pula[:rozmiar_partii]
    st.session_state.smart_nieopanowane = pula[rozmiar_partii:]

def zaladuj_kolejna_partie_smart(rozmiar_partii=20):
    st.session_state.smart_nr_rundy += 1
    st.session_state.smart_bledne_w_rundzie = set()
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.smart_ostatni_wynik = None
    st.session_state.smart_krok += 1
    
    random.shuffle(st.session_state.smart_nieopanowane)
    st.session_state.smart_kolejka_rundy = st.session_state.smart_nieopanowane[:rozmiar_partii]
    st.session_state.smart_nieopanowane = st.session_state.smart_nieopanowane[rozmiar_partii:]

def powrot_do_wyboru():
    st.session_state.wybrana_baza = None
    st.session_state.aktywny_tryb = None
    st.session_state.indeks = 0
    st.session_state.sprawdzono_odpowiedz = False
    st.session_state.test_zakonczony = False
    st.session_state.wynik_zapisany = False
    st.session_state.czas_konca = None

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
        "📚 Testy i Nauka", 
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
            <p style="margin:0;">Wybierz część bazy, ustal tryb nauki (w tym inteligentne powtórki) lub uruchom egzamin.</p>
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
elif menu_glowne == "📚 Testy i Nauka":
    if st.session_state.wybrana_baza is None and st.session_state.aktywny_tryb is None:
        st.markdown("<div class='main-header'>Wybierz tryb testowy lub bazę pytań</div>", unsafe_allow_html=True)
        
        st.subheader("📚 PEŁNE BAZY I EGZAMINY")
        if st.button("🎯 Uruchom Egzamin WIELOKROTNEGO WYBORU (1/2/3) (40 Baza 1 + 10 reszta | 50 pytań / 20 min)", use_container_width=True, type="primary"):
            st.session_state.wybrana_baza = "Wszystkie"
            start_sesji("Egzamin (Losowo – 50 pytań / 20 min)", "Egzamin mieszany (40 Baza 1 + 10 reszta)", limit_pytan=50, tylko_wielokrotne=False)
            st.rerun()

        if st.button("🎯 Uruchom Egzamin WIELOKROTNEGO WYBORU (1/2) (40 Baza 1 + 10 reszta | 50 pytań / 20 min)", use_container_width=True, type="primary"):
            st.session_state.wybrana_baza = "Wszystkie"
            start_sesji("Egzamin (Losowo – 50 pytań / 20 min)", "Egzamin mieszany (40 Baza 1 + 10 reszta)", limit_pytan=50, tylko_wielokrotne=True)
            st.rerun()

        if st.button("🧠 Cała baza (wszystkie pytania) – Tryby Nauki i Powtórek", use_container_width=True):
            st.session_state.wybrana_baza = "Cała baza (wszystkie pytania)"
            st.rerun()

        st.markdown("---")
        st.subheader("📁 Wybierz Rozdział Bazy")
        for nazwa_bazy in st.session_state.bazy.keys():
            if nazwa_bazy == "Baza 1":
                if st.button(f"📁 {nazwa_bazy}", use_container_width=True, type="primary"):
                    st.session_state.wybrana_baza = nazwa_bazy
                    st.rerun()
            else:
                if st.button(f"📁 {nazwa_bazy}", use_container_width=True):
                    st.session_state.wybrana_baza = nazwa_bazy
                    st.rerun()

    elif st.session_state.aktywny_tryb is None:
        nazwa_bary = st.session_state.wybrana_baza
        wszystkie = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=False)
        wielokrotne = pobierz_pytania_z_bazy(nazwa_bary, tylko_wielokrotne=True)

        st.markdown(f"**Wybrana baza:** {nazwa_bary}")
        st.markdown(f"* Wszystkie pytania WIELOKROTNEGO WYBORU (1/2/3): **{len(wszystkie)}**")
        st.markdown(f"* Wszystkie pytania WIELOKROTNEGO WYBORU (1/2): **{len(wielokrotne)}**")
        st.write("")

        st.subheader("Wybierz wariant testu:")
        
        col_w1, col_w2 = st.columns(2)
        
        with col_w1:
            st.markdown("### 🎯 WIELOKROTNY WYBÓR (1/2/3)")
            if st.button("🧠 Inteligentna Nauka (Powtórki jak Quizlet - partie po 20)", key="smart_w", type="primary", use_container_width=True):
                start_inteligentna_nauka(nazwa_bary, tylko_wielokrotne=False, rozmiar_partii=20)
                st.rerun()
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
            if st.button("🧠 Inteligentna Nauka (Powtórki jak Quizlet - partie po 20)", key="smart_f", type="primary", use_container_width=True):
                start_inteligentna_nauka(nazwa_bary, tylko_wielokrotne=True, rozmiar_partii=20)
                st.rerun()
            if st.button("Tryb Nauka (Kolejno)", key="n_f_k", use_container_width=True):
                start_sesji("Tryb Nauki (Kolejno)", nazwa_bary, limit_pytan=None, tylko_wielokrotne=True)
                st.rerun()
            if st.button("Tryb Nauki (Losowo – 30 pytań)", key="n_f_l", use_container_width=True):
                start_sesji("Tryb Nauki (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=True)
                st.rerun()
            if st.button("Egzamin (Losowo – 30 pytań)", key="e_f_l", use_container_width=True):
                start_sesji("Egzamin (Losowo – 30 pytań)", nazwa_bary, limit_pytan=30, tylko_wielokrotne=True)
                st.rerun()
        st.write("")
        if st.button("← Powrót do wyboru baz", use_container_width=True):
            powrot_do_wyboru()
            st.rerun()

    # ==========================================================================
    # OBSŁUGA NOWEGO TRYBU: INTELIGENTNA NAUKA (QUIZLET / DUOLINGO)
    # ==========================================================================
    elif "Inteligentna Nauka" in st.session_state.aktywny_tryb:
        st.markdown(f"<div class='main-header'>🧠 {st.session_state.aktywny_tryb} — {
