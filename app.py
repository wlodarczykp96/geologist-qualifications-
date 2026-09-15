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
    st.session_state.bazy = {
        "Część 1 (Projekty, hydrogeologia, geologia)": [
            {
                "id": 1,
                "pytanie": "W jakim terminie przedsiębiorca powinien przedłożyć organowi koncesyjnemu aktualny dowód istnienia zabezpieczenia roszczeń mogących powstać wskutek wykonywania działalności objętej koncesją na podziemne składowanie odpadów:",
                "odpowiedzi": {
                    "A": "raz na kwartał,",
                    "B": "corocznie, w terminie do końca stycznia,",
                    "C": "nie później niż w terminie dwóch tygodni od dnia otrzymania wezwania ze strony organu koncesyjnego.",
                },
                "poprawne": ["B"],
                "podstawa_prawna": "Art. 28a ust. 2 Prawo geologiczne i górnicze",
                "tresc_artykulu": "Przedsiębiorca jest obowiązany przedkładać organowi koncesyjnemu aktualny dowód istnienia zabezpieczenia roszczeń corocznie, w terminie do końca stycznia danego roku."
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
                "podstawa_prawna": "Art. 28a ust. 1 Prawo geologiczne i górnicze",
                "tresc_artykulu": "Koncesji na podziemne składowanie odpadów udziela się pod warunkiem ustanowienia zabezpieczenia roszczeń mogących powstać wskutek wykonywania działalności objętej tą koncesją."
            }
        ],
        "Część 2 (Planowanie, ruch zakładu, przepisy)": [
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
            }
        ]
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

# Konfiguracja układu strony
st.set_page_config(
    page_title="Aplikacja Testowa - Prawo Geologiczne i Górnicze",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dynamiczne wstrzykiwanie poprawionego motywu CSS
if st.session_state.theme == "Jasny":
    st.markdown("""
    <style>
        .stApp { background-color: #f8f9fa; color: #212529; }
        .main-header { font-size: 22px; font-weight: bold; color: #0d6efd; border-bottom: 2px solid #dee2e6; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ced4da; margin-bottom: 15px; color: #212529; }
        .legal-box { background-color: #e7f1ff; padding: 15px; border-radius: 6px; border: 1px solid #b6d4fe; margin-top: 15px; margin-bottom: 15px; color: #084298; }
        /* Poprawka widoczności etykiet tekstowych w jasnym motywie */
        label, .stRadio p, .stCheckbox p { color: #212529 !important; }
    </style>
    """, unsafe_allow_html=True)
elif st.session_state.theme in ["Cciemny", "Ciemny"]:
    st.markdown("""
    <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        .main-header { font-size: 22px; font-weight: bold; color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 5px; margin-bottom: 15px; }
        .question-box { background-color: #161b22; padding: 15px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; color: #ffffff; }
        .legal-box { background-color: #0d1117; padding: 15px; border-radius: 6px; border: 1px solid #238636; margin-top: 15px; margin-bottom: 15px; color: #e6edf3; }
        label, .stRadio p, .stCheckbox p { color: #ffffff !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        @media (prefers-color-scheme: dark) {
            .stApp { background-color: #0e1117; color: #ffffff; }
            .main-header { font-size: 22px; font-weight: bold; color: #58a6ff; border-bottom: 2px solid #30363d; padding-bottom: 5px; margin-bottom: 15px; }
            .question-box { background-color: #161b22; padding: 15px; border-radius: 6px; border: 1px solid #30363d; margin-bottom: 15px; color: #ffffff; }
            .legal-box { background-color: #0d1117; padding: 15px; border-radius: 6px; border: 1px solid #238636; margin-top: 15px; margin-bottom: 15px; color: #e6edf3; }
            label, .stRadio p, .stCheckbox p { color: #ffffff !important; }
        }
        @media (prefers-color-scheme: light) {
            .stApp { background-color: #f8f9fa; color: #212529; }
            .main-header { font-size: 22px; font-weight: bold; color: #0d6efd; border-bottom: 2px solid #dee2e6; padding-bottom: 5px; margin-bottom: 15px; }
            .question-box { background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ced4da; margin-bottom: 15px; color: #212529; }
            .legal-box { background-color: #e7f1ff; padding: 15px; border-radius: 6px; border: 1px solid #b6d4fe; margin-top: 15px; margin-bottom: 15px; color: #084298; }
            label, .stRadio p, .stCheckbox p { color: #212529 !important; }
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
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("### 🎮 Rozwiązywanie Testów\nWybierz część bazy, ustal tryb nauki lub spróbuj sił w symulacji egzaminu.")
        st.success("### 🔍 Baza Pytań\nPrzeglądaj pytania razem z przypisanymi podstawami prawnymi oraz tekstami artykułów.")
    with col2:
        st.warning("### ➕ Dodawanie Pytań\nRozszerzaj bazę testową o własne pytania i odpowiedzi.")
        st.error("### 🔑 Tryb Administratora\nPozwala edytować oraz usuwać dowolne pytania w bazie po podaniu hasła.")

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
