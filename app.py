import random
import streamlit as st

# Podstawowa konfiguracja widoku na telefonie
st.set_page_config(
    page_title="Test Kwalifikacyjny", page_icon="📝", layout="centered"
)

AUTOR = "Jan Kowalski"  # <-- Wpisz swoje imię i nazwisko / nick

# ==========================================
# TUTAJ BAZY PYTAŃ (Uzupełnij swoimi danymi)
# ==========================================
PYTANIA_CZ1 = [
    {
        "id": 1,
        "pytanie": "Przykładowe pytanie z części 1?",
        "odpowiedzi": {"A": "Opcja A", "B": "Opcja B", "C": "Opcja C"},
        "poprawne": ["A"],
        "podstawa_prawna": "Art. 1 Ust. 1",
    }
]

PYTANIA_CZ2 = [
    # Wklej pytania z części 2
]

# ==============================================================================
# INICJALIZACJA ZMIENNYCH STANU (Session State)
# ==============================================================================
if "krok" not in st.session_state:
    st.session_state.krok = "WYBOR_CZESCI"
if "baza_zrodlowa" not in st.session_state:
    st.session_state.baza_zrodlowa = []
if "pula_pytan" not in st.session_state:
    st.session_state.pula_pytan = []
if "indeks" not in st.session_state:
    st.session_state.indeks = 0
if "tryb_nauki" not in st.session_state:
    st.session_state.tryb_nauki = True
if "odpowiedzial" not in st.session_state:
    st.session_state.odpowiedzial = False
if "wynik_poprawne" not in st.session_state:
    st.session_state.wynik_poprawne = 0
if "wynik_bledne" not in st.session_state:
    st.session_state.wynik_bledne = 0
if "bledne_pytania" not in st.session_state:
    st.session_state.bledne_pytania = []


# ==============================================================================
# EKRAN 1: WYBÓR CZĘŚCI BAZY
# ==============================================================================
if st.session_state.krok == "WYBOR_CZESCI":
    st.title("📱 System Testowy")
    st.caption("Wybierz część bazy pytań, aby rozpocząć.")

    btn_cz1 = st.button(f"Część 1 ({len(PYTANIA_CZ1)} pytań)", use_container_width=True)
    btn_cz2 = st.button(f"Część 2 ({len(PYTANIA_CZ2)} pytań)", use_container_width=True)
    btn_obu = st.button(f"Połączone Części ({len(PYTANIA_CZ1) + len(PYTANIA_CZ2)} pytań)", use_container_width=True)

    if btn_cz1:
        if not PYTANIA_CZ1:
            st.warning("Baza Części 1 jest pusta!")
        else:
            st.session_state.baza_zrodlowa = list(PYTANIA_CZ1)
            st.session_state.krok = "WYBOR_TRYBU"
            st.rerun()

    if btn_cz2:
        if not PYTANIA_CZ2:
            st.warning("Baza Części 2 jest pusta!")
        else:
            st.session_state.baza_zrodlowa = list(PYTANIA_CZ2)
            st.session_state.krok = "WYBOR_TRYBU"
            st.rerun()

    if btn_obu:
        razem = PYTANIA_CZ1 + PYTANIA_CZ2
        if not razem:
            st.warning("Połączona baza jest pusta!")
        else:
            st.session_state.baza_zrodlowa = list(razem)
            st.session_state.krok = "WYBOR_TRYBU"
            st.rerun()


# ==============================================================================
# EKRAN 2: WYBÓR TRYBU ROZWIAZYWANIA
# ==============================================================================
elif st.session_state.krok == "WYBOR_TRYBU":
    st.title("⚙️ Wybierz Tryb")
    st.caption(f"Wybrana baza liczy: {len(st.session_state.baza_zrodlowa)} pytań")

    if st.button("Tryb Nauki (Kolejno + Podpowiedzi)", use_container_width=True):
        st.session_state.pula_pytan = list(st.session_state.baza_zrodlowa)
        st.session_state.tryb_nauki = True
        st.session_state.krok = "QUIZ"
        st.session_state.indeks = 0
        st.session_state.wynik_poprawne = 0
        st.session_state.wynik_bledne = 0
        st.session_state.bledne_pytania = []
        st.session_state.odpowiedzial = False
        st.rerun()

    if st.button("Tryb Nauki (Losowa kolejność + Podpowiedzi)", use_container_width=True):
        st.session_state.pula_pytan = list(st.session_state.baza_zrodlowa)
        random.shuffle(st.session_state.pula_pytan)
        st.session_state.tryb_nauki = True
        st.session_state.krok = "QUIZ"
        st.session_state.indeks = 0
        st.session_state.wynik_poprawne = 0
        st.session_state.wynik_bledne = 0
        st.session_state.bledne_pytania = []
        st.session_state.odpowiedzial = False
        st.rerun()

    if st.button("Tryb Egzaminu (Losowo, Wynik na końcu)", use_container_width=True):
        st.session_state.pula_pytan = list(st.session_state.baza_zrodlowa)
        random.shuffle(st.session_state.pula_pytan)
        st.session_state.tryb_nauki = False
        st.session_state.krok = "QUIZ"
        st.session_state.indeks = 0
        st.session_state.wynik_poprawne = 0
        st.session_state.wynik_bledne = 0
        st.session_state.bledne_pytania = []
        st.session_state.odpowiedzial = False
        st.rerun()

    st.write("")
    if st.button("← Powrót do wyboru części", use_container_width=True):
        st.session_state.krok = "WYBOR_CZESCI"
        st.rerun()


# ==============================================================================
# EKRAN 3: QUIZ / INTERFEJS PYTANIA
# ==============================================================================
elif st.session_state.krok == "QUIZ":
    pytanie = st.session_state.pula_pytan[st.session_state.indeks]
    razem = len(st.session_state.pula_pytan)

    st.progress((st.session_state.indeks + 1) / razem)
    
    col_top1, col_top2 = st.columns([2, 1])
    with col_top1:
        st.caption(f"Pytanie {st.session_state.indeks + 1} z {razem} (ID: {pytanie.get('id', '-')})")
    with col_top2:
        if st.button("Menu 🏠", key="top_menu"):
            st.session_state.krok = "WYBOR_CZESCI"
            st.rerun()

    st.markdown(f"### {pytanie['pytanie']}")

    wybrane = []
    for k, v in pytanie["odpowiedzi"].items():
        if st.checkbox(f"**{k}.** {v}", key=f"q_{st.session_state.indeks}_{k}"):
            wybrane.append(k)

    st.write("")

    if not st.session_state.odpowiedzial:
        if st.button("Sprawdź / Zatwierdź", use_container_width=True):
            if not wybrane:
                st.warning("Zaznacz co najmniej jedną odpowiedź!")
            else:
                st.session_state.odpowiedzial = True
                czy_poprawne = set(wybrane) == set(pytanie["poprawne"])

                if czy_poprawne:
                    st.session_state.wynik_poprawne += 1
                    st.session_state.ostatnia_poprawna = True
                else:
                    st.session_state.wynik_bledne += 1
                    st.session_state.ostatnia_poprawna = False
                    st.session_state.bledne_pytania.append((pytanie, wybrane))

                if not st.session_state.tryb_nauki:
                    st.session_state.indeks += 1
                    st.session_state.odpowiedzial = False
                    if st.session_state.indeks >= razem:
                        st.session_state.krok = "WYNIK"
                    st.rerun()
                else:
                    st.rerun()
    else:
        if st.session_state.ostatnia_poprawna:
            st.success("✅ DOKŁADNIE TAK! Odpowiedź poprawna.")
        else:
            st.error(f"❌ BŁĄD!\nTwoja odpowiedź: {', '.join(wybrane)} | Poprawna: {', '.join(pytanie['poprawne'])}")

        if "podstawa_prawna" in pytanie or "tresc_artykulu" in pytanie:
            with st.expander("📖 Wyjaśnienie / Podstawa prawna", expanded=True):
                if "podstawa_prawna" in pytanie:
                    st.markdown(f"**Podstawa:** {pytanie['podstawa_prawna']}")
                if "tresc_artykulu" in pytanie:
                    st.write(pytanie['tresc_artykulu'])

        if st.button("Następne pytanie ➔", use_container_width=True):
            st.session_state.indeks += 1
            st.session_state.odpowiedzial = False
            if st.session_state.indeks >= razem:
                st.session_state.krok = "WYNIK"
            st.rerun()


# ==============================================================================
# EKRAN 4: PODSUMOWANIE I WYNIKI
# ==============================================================================
elif st.session_state.krok == "WYNIK":
    st.title("🎉 Koniec Testu!")

    razem = len(st.session_state.pula_pytan)
    poprawne = st.session_state.wynik_poprawne
    bledne = st.session_state.wynik_bledne
    procent = (poprawne / razem) * 100 if razem > 0 else 0

    st.metric(label="Mój Wynik", value=f"{poprawne} / {razem}", delta=f"{procent:.1f}%")

    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.success(f"Poprawne: **{poprawne}**")
    with col_m2:
        st.error(f"Błędne: **{bledne}**")

    if st.session_state.bledne_pytania:
        st.write("---")
        st.subheader("Podsumowanie popełnionych błędów:")

        for py, wybrane in st.session_state.bledne_pytania:
            with st.expander(f"❌ [ID: {py.get('id','-')}] {py['pytanie'][:60]}..."):
                st.write(f"**Pytanie:** {py['pytanie']}")
                st.write(f"**Twoja odpowiedź:** {', '.join(wybrane)}")
                st.write(f"**Poprawna odpowiedź:** {', '.join(py['poprawne'])}")
                if "podstawa_prawna" in py:
                    st.caption(f"Podstawa: {py['podstawa_prawna']}")

    st.write("")
    if st.button("Powrót do Menu Głównego", use_container_width=True):
        st.session_state.krok = "WYBOR_CZESCI"
        st.rerun()


# ==============================================================================
# STOPKA Z AUTOREM
# ==============================================================================
st.write("---")
st.caption(f"Autor programu: **{AUTOR}**")
