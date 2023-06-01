lodówka(chłodziarko-zamrażarka).
lodówka(chłodziarka).

funkcja_lodówki(regulacja_temperatury).
funkcja_lodówki(alarm_otwarcia_drzwi).
funkcja_lodówki(panel_dotykowy).
funkcja_lodówki(regulowana_wysokość_półek).
funkcja_lodówki(oświetlenie_wnętrza).
funkcja_lodówki(tryb_oszczędzania_energii).
funkcja_lodówki(filtrowanie_wody).

typ_lodówki(_, wolnostojąca).
typ_lodówki(_, do_zabudowy).
typ_lodówki(chłodziarko-zamrażarka, z_zamrażarką_u_góry).
typ_lodówki(chłodziarko-zamrażarka, z_zamrażarką_u_dołu).
typ_lodówki(chłodziarko-zamrażarka, side_by_side).
typ_lodówki(_, przemysłowa).
typ_lodówki(_, mini_lodowka).

element_lodówki(_, zasilacz).
element_lodówki(_, chłodziarka).
element_lodówki(chłodziarko-zamrażarka, zamrażarka).
element_lodówki(_, drzwi).
element_lodówki(_, termostat).
element_lodówki(_, kompresor).
element_lodówki(_, półki).

wypisz_typy_lodówki(L) :-
    lodówka(L),
    typ_lodówki(L, Typ),
    write(Typ), nl.
wypisz_typy_lodówki(lodówka).

/*	sprawdza czy podane lodówki zawierają ten sam element konstrukcyjny	*/
zawiera_ten_sam_element(L1, L2, Element) :-
    element_lodówki(L1, Element),
    element_lodówki(L2, Element).

/*	sprawdza czy podane lodówki oferują ten sam typ*/
oferuje_ten_sam_typ(L1, L2, Typ) :-
    typ_lodówki(L1, Typ),
    typ_lodówki(L2, Typ).

ma_zamrażarkę(L) :-
    lodówka(L),
    L = chłodziarko-zamrażarka.
    


/*	diagnozowanie	*/
problem(lodówka_nie_działa).
problem(lodówka_nie_osiąga_odpowiedniej_temperatury).
problem(lodówka_chłodzi_zbyt_silnie).
problem(nieprzyjemny_zapach).
problem(szron_wokół_otworów_wentylacyjnych).
problem(szron_na_ściankach_wewnątrz).
problem(na_ściankach_wewnątrz_tworzą_się_skropliny).

możliwa_przyczyna_problemu(lodówka_nie_działa, przewód_zasilacz_nie_jest_prawidłowo_podłączony).
możliwa_przyczyna_problemu(lodówka_nie_osiąga_odpowiedniej_temperatury, temperature_nie_jest_prawidłowo_ustawiona).
możliwa_przyczyna_problemu(lodówka_nie_osiąga_odpowiedniej_temperatury, lodówka_znajduje_się_blisko_źródła_ciepła).
możliwa_przyczyna_problemu(lodówka_nie_osiąga_odpowiedniej_temperatury, niewystarczający_odstęp_pomiędzy_lodówką_i_przedmiotami_po_bokach_lub_z_tyłu).
możliwa_przyczyna_problemu(lodówka_nie_osiąga_odpowiedniej_temperatury, został_włączony_tryb_wakacyjny).
możliwa_przyczyna_problemu(lodówka_nie_osiąga_odpowiedniej_temperatury, produkty_żywnościowe_blokują_otwory_wentylacyjne).
możliwa_przyczyna_problemu(lodówka_chłodzi_zbyt_silnie, temperatura_nie_jest_prawidłowo_ustawiona).
możliwa_przyczyna_problemu(nieprzyjemny_zapach, zepsute_produkty_żywnościowe).
możliwa_przyczyna_problemu(nieprzyjemny_zapach, produkty_żywnościowe_o_silnym_zapachu).
możliwa_przyczyna_problemu(szron_wokół_otworów_wentylacyjnych, produkty_żywnościowe_blokują_otwory_wentylacyjne).
możliwa_przyczyna_problemu(szron_na_ściankach_wewnątrz, drzwi_nie_są_prawidłowo_zamknięte).
możliwa_przyczyna_problemu(na_ściankach_wewnątrz_tworzą_się_skropliny, do_wnętrza_lodówki_przedostaje_się_wilgoć_przez_otwarte_drzwi).
możliwa_przyczyna_problemu(na_ściankach_wewnątrz_tworzą_się_skropliny, produkty_żywnościowe_o_dużej_wilgoci).

możliwa_naprawa_problemu(przewód_zasilacz_nie_jest_prawidłowo_podłączony, podłącz_prawidłowo_przewód_zasilający).
możliwa_naprawa_problemu(temperature_nie_jest_prawidłowo_ustawiona, ustaw_niższą_temperature).
możliwa_naprawa_problemu(lodówka_znajduje_się_blisko_źródła_ciepła, ustwa_lodówkę_z_dala_od_miejsc_ciepła).
możliwa_naprawa_problemu(niewystarczający_odstęp_pomiędzy_lodówką_i_przedmiotami_po_bokach_lub_z_tyłu, zapewnij_co_najmniej_5_cm_odstępu_z_tyłu_i_po_bokach).
możliwa_naprawa_problemu(został_włączony_tryb_wakacyjny, wyłącz_tryb_wakacyjny).
możliwa_naprawa_problemu(temperatura_nie_jest_prawidłowo_ustawiona, ustaw_wyższą_temperaturę).
możliwa_naprawa_problemu(zepsute_produkty_żywnościowe, wyczyść_lodówkę_i_usuń_zepsute_produkty_żywnościowe).
możliwa_naprawa_problemu(produkty_żywnościowe_o_silnym_zapachu, upewnij_się_że_żywność_o_intensywnym_zapach_jest_szczelnie_zapakowana).
możliwa_naprawa_problemu(produkty_żywnościowe_blokują_otwory_wentylacyjne, upewnij_się_że_produkty_żywnościowe_nie_blokują_otworów_wentylacyjnych).
możliwa_naprawa_problemu(drzwi_nie_są_prawidłowo_zamknięte, upewnij_się_że_produkty_żywnościowe_nie_blokują_drzwi).
możliwa_naprawa_problemu(do_wnętrza_lodówki_przedostaje_się_wilgoć_przez_otwarte_drzwi, usuń_wilgoć_i_nie_otwieraj_drzwi_na_dłuższy_czas).
możliwa_naprawa_problemu(produkty_żywnościowe_o_dużej_wilgoci, upewnij_się_że_żywność_jest_szczelnie_zapakowana).

rozwiązanie_problemu(Problem) :-
    problem(Problem),
    możliwa_przyczyna_problemu(Problem, Przyczyna),
    możliwa_naprawa_problemu(Przyczyna, Rozwiązanie),
    write(Rozwiązanie), nl.
