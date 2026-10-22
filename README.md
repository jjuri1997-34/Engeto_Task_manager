# Správce úkolů

Jednoduchá konzolová aplikace pro správu seznamu úkolů. Úkoly se drží pouze v paměti a po ukončení programu se ztratí.

## Požadavky

- Python 3.9 nebo novější (vyvíjeno a testováno na Pythonu 3.14)
- Žádné externí knihovny

Verzi zjistíte příkazem:

```powershell
python --version
```

Na Windows lze použít i `py --version`.

## Spuštění

1. Otevřete terminál ve složce projektu.
2. Spusťte program:

   ```powershell
   python task_manager.py
   ```

   Na Windows lze použít i `py task_manager.py`.

3. V hlavním menu zadejte číslo volby (1–4).

## Funkce

| Volba | Akce |
|-------|------|
| 1 | Přidat nový úkol (název a popis jsou povinné) |
| 2 | Zobrazit všechny úkoly |
| 3 | Odstranit úkol podle čísla |
| 4 | Konec programu |

Při neplatném čísle nebo vstupu při odstraňování se program zeptá znovu.

## Testovací scénáře

Popis testů jednotlivých funkcí je v souborech [hlavni_menu.md](hlavni_menu.md), [pridat_ukol.md](pridat_ukol.md), [zobrazit_ukoly.md](zobrazit_ukoly.md) a [odstranit_ukol.md](odstranit_ukol.md).
