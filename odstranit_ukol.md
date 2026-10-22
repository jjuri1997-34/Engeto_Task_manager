# Testování odstranit_ukol

## Pozitivní testy

-----------------------------------------------------------
TC01
Popis: Odstranění jediného úkolu

Vstupní podmínky: V seznamu je jeden úkol Test (popis Test123).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám číslo 1 a zmáčknu Enter

Očekávaný výsledek: Program potvrdí odstranění úkolu Test a vrátí se do menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:", "1. Test - Test123" a prázdný řádek, zeptá se "Zadejte číslo úkolu, který chcete odstranit: ", po zadání 1 vypíše "Úkol 'Test' byl odstraněn.", prázdný řádek a vrátí se do hlavního menu. Seznam je pak prázdný.

Stav: Pass

Poznámky: Ověřuje odstranění.

-----------------------------------------------------------
TC02
Popis: Odstranění prostředního úkolu

Vstupní podmínky: V seznamu jsou tři různé úkoly (Nákup - Mléko, Úklid - Byt, Telefonát - Lékař).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám 2 a zmáčknu Enter

Očekávaný výsledek: Odstraní se pouze druhý úkol (Úklid), první a třetí zůstanou a přečíslují se.

Skutečný výsledek: Program vypíše seznam "1. Nákup - Mléko", "2. Úklid - Byt", "3. Telefonát - Lékař", po zadání 2 vypíše "Úkol 'Úklid' byl odstraněn.", prázdný řádek a vrátí se do hlavního menu. Zůstanou úkoly Nákup a Telefonát, které se přečíslují na 1 a 2.

Stav: Pass

Poznámky: Ověřuje správné přečíslování úkolů

-----------------------------------------------------------

## Negativní testy

-----------------------------------------------------------
TC03
Popis: Odstranění z prázdného seznamu

Vstupní podmínky: Seznam úkolů je prázdný.

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu

Očekávaný výsledek: Program vypíše "Žádné úkoly nejsou zadány.", nepožaduje číslo a vrátí se do menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "Žádné úkoly nejsou zadány.", nepožádá o číslo úkolu, vypíše prázdný řádek a vrátí se do hlavního menu.

Stav: Pass

Poznámky: Ověřuje chování bez úkolů.

-----------------------------------------------------------
TC04
Popis: Neexistující číslo úkolu

Vstupní podmínky: V seznamu jsou dva úkoly (Test - Test123, Úkol2 - Popis2).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám číslo 3, které není v seznamu, a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Neplatné číslo úkolu.", žádný úkol nesmaže a znovu požádá o číslo úkolu.

Skutečný výsledek: Program vypíše "Neplatné číslo úkolu.", prázdný řádek a znovu se zeptá "Zadejte číslo úkolu, který chcete odstranit: ". Seznam se nezmění a program zůstane ve funkci odstranit_ukol.

Stav: Pass

Poznámky: Ověřuje číslo nad rozsahem.

-----------------------------------------------------------
TC05
Popis: Písmena místo čísla

Vstupní podmínky: V seznamu je úkol Test (popis Test123).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám písmeno A a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Neplatný vstup.", nespadne a znovu požádá o číslo úkolu.

Skutečný výsledek: Program nespadne, vypíše "Neplatný vstup.", prázdný řádek a znovu se zeptá "Zadejte číslo úkolu, který chcete odstranit: ". Seznam se nezmění.

Stav: Pass

Poznámky: Ověřuje zachycení špatného vstupu

-----------------------------------------------------------
TC06
Popis: Prázdné číslo

Vstupní podmínky: V seznamu je úkol Test (popis Test123).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Nechám pole prázdné a zmáčknu Enter
             6. Zadám mezeru a zmáčknu Enter

Očekávaný výsledek: Program po obou vstupech vypíše "Neplatný vstup.", žádný úkol nesmaže a znovu požádá o číslo úkolu.

Skutečný výsledek: Program po prázdném vstupu i po mezeře vypíše "Neplatný vstup.", prázdný řádek a znovu se zeptá "Zadejte číslo úkolu, který chcete odstranit: ". Seznam se nezmění.

Stav: Pass

Poznámky: Ověřuje prázdný vstup.

-----------------------------------------------------------
TC07
Popis: Číslo s mezerami

Vstupní podmínky: V seznamu jsou tři různé úkoly (Nákup - Mléko, Úklid - Byt, Telefonát - Lékař).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám " 1 " (s mezerami) a zmáčknu Enter

Očekávaný výsledek: Program odstraní první úkol (Nákup).

Skutečný výsledek: Program mezery ignoruje, vypíše "Úkol 'Nákup' byl odstraněn.", prázdný řádek a vrátí se do hlavního menu.

Stav: Pass

Poznámky: Ověřuje číslo s mezerami jako platný vstup

-----------------------------------------------------------

## Hraniční testy

-----------------------------------------------------------
TC08
Popis: Odstranění posledního úkolu

Vstupní podmínky: V seznamu jsou tři různé úkoly (Nákup - Mléko, Úklid - Byt, Telefonát - Lékař).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám číslo 3 a zmáčknu Enter

Očekávaný výsledek: Odstraní se poslední úkol (Telefonát) a ostatní zůstanou.

Skutečný výsledek: Program vypíše "Úkol 'Telefonát' byl odstraněn.", prázdný řádek a vrátí se do hlavního menu. Úkoly Nákup a Úklid zůstanou.

Stav: Pass

Poznámky: Ověřuje horní platnou hranici.

-----------------------------------------------------------
TC09
Popis: Číslo nula

Vstupní podmínky: V seznamu jsou dva úkoly (Test - Test123, Úkol2 - Popis2).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám číslo 0 a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Neplatné číslo úkolu.", žádný úkol nesmaže a znovu požádá o číslo úkolu.

Skutečný výsledek: Program vypíše "Neplatné číslo úkolu.", prázdný řádek a znovu se zeptá "Zadejte číslo úkolu, který chcete odstranit: ". Seznam se nezmění.

Stav: Pass

Poznámky: Ověřuje dolní neplatnou hranici.

-----------------------------------------------------------
TC10
Popis: Záporné číslo

Vstupní podmínky: V seznamu jsou dva úkoly (Test - Test123, Úkol2 - Popis2).

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter
             4. Spustí se funkce odstranit_ukol a zobrazí se mi úkoly v seznamu
             5. Zadám číslo -1 a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Neplatné číslo úkolu.", žádný úkol nesmaže a znovu požádá o číslo úkolu.

Skutečný výsledek: Program vypíše "Neplatné číslo úkolu.", prázdný řádek a znovu se zeptá "Zadejte číslo úkolu, který chcete odstranit: ". Seznam se nezmění.

Stav: Pass

Poznámky: Ověřuje záporný index.
