# Testování hlavni_menu

## Pozitivní testy

-----------------------------------------------------------
TC01
Popis: Ověření, že po zvolení "1" se otevře funkce pridat_ukol.

Vstupní podmínky: Zobrazené hlavní_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter

Očekávaný výsledek: Spustí se funkce pridat_ukol a program se zeptá na název úkolu.

Skutečný výsledek: Program vypíše "Zadejte název úkolu: " a čeká na zadání názvu.

Stav: Pass

Poznámky: Důležité pro ověření funkce hlavního menu

-----------------------------------------------------------
TC02
Popis: Ověření, že po zvolení "2" se otevře funkce zobrazit_ukoly.

Vstupní podmínky: Zobrazené hlavní_menu, seznam úkolů je prázdný

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 2 a zmáčknu Enter

Očekávaný výsledek: Spustí se funkce zobrazit_ukoly, vypíše, že nejsou žádné úkoly, a vrátí se do menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "Žádné úkoly nejsou zadány.", pak další prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Důležité pro ověření funkce hlavního menu

-----------------------------------------------------------
TC03
Popis: Ověření, že po zvolení "3" se otevře funkce odstranit_ukol.

Vstupní podmínky: Zobrazené hlavní_menu, seznam úkolů je prázdný

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 3 a zmáčknu Enter

Očekávaný výsledek: Spustí se funkce odstranit_ukol, vypíše, že nejsou žádné úkoly, nepožaduje číslo a vrátí se do menu.

Skutečný výsledek: Program vypíše prázdný řádek, "Seznam úkolů:" a "Žádné úkoly nejsou zadány.", nepožádá o číslo úkolu, vypíše prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Důležité pro ověření funkce hlavního menu

-----------------------------------------------------------
TC04
Popis: Ověření, že po zvolení "4" se program ukončí

Vstupní podmínky: Zobrazené hlavní_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 4 a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Konec programu." a ukončí se.

Skutečný výsledek: Program vypíše "Konec programu." a ukončí se.

Stav: Pass

Poznámky: Důležité pro ověření funkce hlavního menu

-----------------------------------------------------------

## Negativní testy

-----------------------------------------------------------
TC05
Popis: Zadání jiného čísla než v nabídce

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 9 a zmáčknu Enter

Očekávaný výsledek: Program vypíše "Neplatná volba, zkus to znovu." a vrátí mě zpátky do hlavního menu s inputem.

Skutečný výsledek: Program vypíše "Neplatná volba, zkus to znovu.", prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověření funkčnosti inputu

-----------------------------------------------------------
TC06
Popis: Zadání mezery nebo prázdného pole

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Nechám pole prázdné a zmáčknu Enter
             4. Zadám mezeru a zmáčknu Enter

Očekávaný výsledek: Program po obou vstupech vypíše "Neplatná volba, zkus to znovu." a vrátí mě zpátky do hlavního menu s inputem.

Skutečný výsledek: Program po prázdném vstupu i po mezeře vypíše "Neplatná volba, zkus to znovu.", prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověření funkčnosti inputu

-----------------------------------------------------------
TC07
Popis: Zadání písmene nebo speciálního znaku

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám písmeno "a" a zmáčknu Enter
             4. Zadám speciální znak @ a zmáčknu Enter

Očekávaný výsledek: Program po obou vstupech vypíše "Neplatná volba, zkus to znovu." a vrátí mě zpátky do hlavního menu s inputem.

Skutečný výsledek: Program po písmeni i po znaku @ vypíše "Neplatná volba, zkus to znovu.", prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověření funkčnosti inputu

-----------------------------------------------------------
TC08
Popis: Volba s mezerami

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Zadám " 1 " (s mezerami) a zmáčknu Enter

Očekávaný výsledek: Program volbu odmítne, protože v hlavním menu se vstup neořezává.

Skutečný výsledek: Program volbu odmítne, vypíše "Neplatná volba, zkus to znovu.", prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověřuje přesné porovnávání textu.
