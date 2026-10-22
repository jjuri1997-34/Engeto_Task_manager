# Testování pridat_ukol

## Pozitivní testy

-----------------------------------------------------------
TC01
Popis: Přidání úkolu, test pro funkčnost a ukládání našich úkolů

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Zadám název "Test" a zmáčknu Enter
             6. Zadám popis "Test123" a zmáčknu Enter

Očekávaný výsledek: Úkol se přidá do seznamu, program vypíše "Úkol 'Test' byl přidán." a vrátí se do menu.

Skutečný výsledek: Program se po názvu zeptá "Zadejte popis úkolu: ", po popisu vypíše "Úkol 'Test' byl přidán.", prázdný řádek a znovu hlavní menu s inputem "Vyberte možnost (1-4):".

Stav: Pass

Poznámky: Ověřuje ukládání názvu i popisu

-----------------------------------------------------------
TC02
Popis: Ořezání mezer by mělo správně fungovat a úkol přidat bez mezer

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Zadám název " Test " (s mezerami) a zmáčknu Enter
             6. Zadám popis " Test123 " (s mezerami) a zmáčknu Enter

Očekávaný výsledek: Úkol se přidá bez okrajových mezer, program vypíše "Úkol 'Test' byl přidán." a vrátí se do menu.

Skutečný výsledek: Program okrajové mezery odstraní, vypíše "Úkol 'Test' byl přidán." (název bez mezer), prázdný řádek a znovu hlavní menu.

Stav: Pass

Poznámky: Ověřuje .strip()

-----------------------------------------------------------
TC03
Popis: Diakritika a speciální znaky by měly být platný input a úkol by se měl přidat

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Zadám název " Účty@" a zmáčknu Enter
             6. Zadám popis " &test!" a zmáčknu Enter

Očekávaný výsledek: Úkol se přidá, program vypíše "Úkol 'Účty@' byl přidán." a vrátí se do menu.

Skutečný výsledek: Program vypíše "Úkol 'Účty@' byl přidán.", prázdný řádek a znovu hlavní menu.

Stav: Pass

Poznámky: Ověřuje správné zadání speciálních znaků

-----------------------------------------------------------

## Negativní testy

-----------------------------------------------------------
TC04
Popis: Prázdný název

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Název nechám zadat jako mezeru a zmáčknu Enter
             6. Zadám popis "Test123" a zmáčknu Enter
             7. Po chybové hlášce zadám název "Test" a popis "Test123"

Očekávaný výsledek: Program vypíše chybu, nechá mě zadat název i popis znovu a po platném zadání úkol přidá.

Skutečný výsledek: Program vypíše "Název i popis úkolu musí být vyplněny. Zadejte je prosím znovu." a prázdný řádek, pak se znovu zeptá "Zadejte název úkolu: " a "Zadejte popis úkolu: ". Úkol z prvního pokusu se nepřidá. Po platném zadání vypíše "Úkol 'Test' byl přidán.", prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje správné zadání úkolu

-----------------------------------------------------------
TC05
Popis: Prázdný popis by měl vypsat chybu

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Zadám název "Test123" a zmáčknu Enter
             6. Popis zadám jako mezeru a zmáčknu Enter
             7. Po chybové hlášce zadám název "Test123" a popis "Test123"

Očekávaný výsledek: Program vypíše chybu, nechá mě zadat název i popis znovu a po platném zadání úkol přidá.

Skutečný výsledek: Program vypíše "Název i popis úkolu musí být vyplněny. Zadejte je prosím znovu." a prázdný řádek, pak se znovu zeptá "Zadejte název úkolu: " a "Zadejte popis úkolu: " (původní název se nezachová). Po platném zadání vypíše "Úkol 'Test123' byl přidán.", prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje správné zadání úkolu

-----------------------------------------------------------
TC06
Popis: Prázdný název i popis by měl vypsat chybu

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Název zadám jako mezeru a zmáčknu Enter
             6. Popis zadám jako mezeru a zmáčknu Enter
             7. Po chybové hlášce zadám název "Test" a popis "Test123"

Očekávaný výsledek: Program vypíše chybu, nechá mě zadat název i popis znovu a po platném zadání úkol přidá.

Skutečný výsledek: Program vypíše "Název i popis úkolu musí být vyplněny. Zadejte je prosím znovu." a prázdný řádek, pak se znovu zeptá "Zadejte název úkolu: " a "Zadejte popis úkolu: ". Po platném zadání vypíše "Úkol 'Test' byl přidán.", prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Ověřuje správné zadání úkolu

-----------------------------------------------------------

## Hraniční testy

-----------------------------------------------------------
TC07
Popis: Dlouhý text v inputech, ověření zda nám dlouhý text bude správně fungovat

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Do názvu zadám 201 znaků A a zmáčknu Enter
             6. Do popisu zadám 201 znaků B a zmáčknu Enter

Očekávaný výsledek: Úkol se přidá, program vypíše celý název v potvrzení a vrátí se do menu.

Skutečný výsledek: Program úkol přidá a vypíše "Úkol '" s celým názvem (201× A) a "' byl přidán.", nic nezkrátí a nevypíše chybu. Pak vypíše prázdný řádek a hlavní menu.

Stav: Pass

Poznámky: Testuje hranice délky

-----------------------------------------------------------
TC08
Popis: Duplicita úkolů, chceme ověřit, zda se nám duplicitní úkoly správně přidají

Vstupní podmínky: Zobrazené hlavni_menu

Kroky testu: 1. Spustím program
             2. Spustí se funkce hlavni_menu s nabídkou a inputem
             3. Zadám číslo 1 a zmáčknu Enter
             4. Otevře se funkce pridat_ukol
             5. Do názvu zadám "test" a zmáčknu Enter
             6. Do popisu zadám "test" a zmáčknu Enter
             7. Znovu zadám číslo 1 a zmáčknu Enter
             8. Do názvu zadám "test" a zmáčknu Enter
             9. Do popisu zadám "test" a zmáčknu Enter

Očekávaný výsledek: Oba úkoly se přidají, po každém program vypíše "Úkol 'test' byl přidán." a vrátí se do menu.

Skutečný výsledek: Program po prvním i po druhém zadání vypíše "Úkol 'test' byl přidán.", prázdný řádek a hlavní menu. Duplicitu nehlídá, takže se přidají oba úkoly.

Stav: Pass

Poznámky: Testuje duplicitu úkolů a zda je možné přidat dva stejné úkoly
