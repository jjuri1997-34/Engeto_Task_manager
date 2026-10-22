#region hlavni menu

def hlavni_menu() -> None:
    """Zobrazí hlavní menu a zpracovává volby uživatele."""
    ukoly = []
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        volba = input("Vyberte možnost (1-4):")

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            odstranit_ukol(ukoly)
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkus to znovu.\n")

#endregion

#region přidat úkol
def pridat_ukol(ukoly: list[dict[str, str]]) -> None:
    """Vyžádá údaje a přidá úkol do seznamu."""
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        if nazev and popis:
            break
        print("Název i popis úkolu musí být vyplněny. Zadejte je prosím znovu.\n")

    ukol = {
        "nazev": nazev,
        "popis": popis
    }

    ukoly.append(ukol)
    print(f"Úkol '{nazev}' byl přidán.\n")
    
#endregion

#region zobrazit úkoly

def zobrazit_ukoly(ukoly: list[dict[str, str]]) -> None:
    """Vypíše seznam uložených úkolů."""
    print("\nSeznam úkolů:")

    if not ukoly:
        print("Žádné úkoly nejsou zadány.\n")
    else:
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
        print()

#endregion

#region odstranit úkol
def odstranit_ukol(ukoly: list[dict[str, str]]) -> None:
    """Vyžádá číslo a odstraní odpovídající úkol ze seznamu."""
    zobrazit_ukoly(ukoly)
    if not ukoly:
        return
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odstraneny_ukol = ukoly.pop(cislo - 1)
                print(f"Úkol '{odstraneny_ukol['nazev']}' byl odstraněn.\n")
                return
            print("Neplatné číslo úkolu.\n")
        except ValueError:
            print("Neplatný vstup.\n")

#endregion

if __name__ == "__main__":
    hlavni_menu()
