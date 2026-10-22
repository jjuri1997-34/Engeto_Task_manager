# Testování zobrazit_ukoly

## Pozitivní testy

-----------------------------------------------------------
TC01
Popis: Zobrazení jednoho úkolu

Vstupní podmínky: V seznamu je úkol Test s popisem Test123.

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Zobrazí se "1. Test - Test123" a následně hlavní menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "1. Test - Test123", pak prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověřuje výpis názvu, popisu a číslování.

-----------------------------------------------------------
TC02
Popis: Zobrazení více úkolů

Vstupní podmínky: V seznamu jsou tři různé úkoly (Nákup - Mléko, Úklid - Byt, Telefonát - Lékař).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Vypíšou se všechny tři úkoly ve správném pořadí pod čísly 1, 2 a 3.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a pod sebe, bez prázdných řádků mezi nimi, "1. Nákup - Mléko", "2. Úklid - Byt" a "3. Telefonát - Lékař". Za posledním úkolem vypíše prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověřuje průchod seznamem.

-----------------------------------------------------------
TC03
Popis: Opakované zobrazení

Vstupní podmínky: V seznamu je úkol Test s popisem Test123.

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter
             4. Znovu zadám 2 a zmáčknu Enter

Očekávaný výsledek: Oba výpisy obsahují stejné úkoly a funkce data nemění.

Skutečný výsledek: Po obou zadáních 2 program vypíše prázdný řádek, "Seznam úkolů:" a "1. Test - Test123", pak prázdný řádek a hlavní menu. Oba výpisy jsou stejné a seznam se nezměnil.

Stav: Pass

Poznámky: Ověřuje, že zobrazení neupravuje seznam.

-----------------------------------------------------------
TC04
Popis: Zobrazení po odstranění

Vstupní podmínky: V seznamu jsou dva úkoly (Test - Test123, Úkol2 - Popis2).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Zadám číslo 1 a zmáčknu Enter (odstraním první úkol)
             5. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Zobrazí se pouze zbývající úkol pod číslem 1.

Skutečný výsledek: Po odstranění program vypíše "Úkol 'Test' byl odstraněn." a vrátí se do hlavního menu. Po zadání 2 vypíše prázdný řádek, "Seznam úkolů:" a "1. Úkol2 - Popis2", pak prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje aktualizaci výpisu po odstranění.

-----------------------------------------------------------

## Negativní testy

-----------------------------------------------------------
TC05
Popis: Zobrazení prázdného seznamu

Vstupní podmínky: Seznam úkolů je prázdný.

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Žádné úkoly nejsou zadány." a vrátí se do menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "Žádné úkoly nejsou zadány.", pak prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověřuje chování prázdného seznamu

-----------------------------------------------------------
TC06
Popis: Zobrazení po smazání všech úkolů

Vstupní podmínky: V seznamu je jeden úkol (Test - Test123).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Zadám číslo 1 a zmáčknu Enter (odstraním poslední úkol)
             5. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Program vypíše, že žádné úkoly nejsou zadány.

Skutečný výsledek: Po odstranění program vypíše "Úkol 'Test' byl odstraněn." a vrátí se do hlavního menu. Po zadání 2 vypíše prázdný řádek, "Seznam úkolů:" a "Žádné úkoly nejsou zadány.", pak prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje prázdný seznam po mazání.

-----------------------------------------------------------

## Hraniční testy

-----------------------------------------------------------
TC07
Popis: Dlouhý text v seznamu

Vstupní podmínky: V seznamu je úkol s názvem (201 znaků A) a popisem (201 znaků B).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Zobrazí se celý uložený název a popis.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a na jednom řádku "1. " následované celým názvem (201× A), " - " a celým popisem (201× B), nic se nezkrátí. Pak vypíše prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje výpis dlouhých úkolů.

-----------------------------------------------------------
TC08
Popis: Speciální znaky

Vstupní podmínky: V seznamu je úkol s názvem "Účty@" a popisem "&test!".

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Program zobrazí správné znaky v názvu i popisu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "1. Účty@ - &test!", pak prázdný řádek a hlavní menu. Diakritika i speciální znaky se zobrazí správně.

Stav: Pass

Poznámky: Ověřuje správné zobrazení textu.
