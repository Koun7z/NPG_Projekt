# <p align=center> :keyboard: Mistrz Klawiatury :keyboard: </p>
Witaj w grze **Mistrz Klawiatury**! Jest to gra mająca na celu usprawnienie szybkiego i precyzyjnego pisania na klawiaturze. Przetestuj swoje umiejętności i zostań prawdziwym Mistrzem Klawiatury.

## Spis treści

- [O grze](#o-grze)
- [Instalacja](#instalacja)
- [Przyszłe implementacje](#przyszłe-implementacje)
- [Źródła](#źródła)

## O grze
Mistrz Klawiatury to gra w której zadaniem gracza jest możliwie jak najszybsze, ale jednocześnie dokładne przepisanie wyświetlonego na ekranie tekstu. Dzięki obecności różnych poziomów trudności oraz trybów, gra skierowana jest zarówno do osób rozpoczynających naukę szybkiego pisania, jak i do bardziej zaawansowanych graczy chcących udoskonalić swoje umiejętności, czy też szukających wyzwania. 

### Funkcje gry

- **Tryb gry**: wybieraj spośród trzech trybów gry
  
  - Tryb klasyczny - podstawowy tryb gry, polegający na przepisywaniu wyświetlanego tekstu zdanie po zdaniu.
  - Tryb Spadające Literki - tryb skupiony na szybkości reakcji gracza. Naciśnij odpowiedni klawisz zanim literka spadnie na dół ekranu, zakańczając grę.
  - Tryb Wyzwanie -
    
- **Poziom trudności**: graj w każdy z trybów na trzech poziomach trudności
  
- **Ranking**: zapisuj swoje najlepsze wyniki w systemie rankingowym
## Link do zaaktualizowanych diagramów na platformie drawio
https://aghedupl-my.sharepoint.com/:u:/g/personal/kmazur_student_agh_edu_pl/EekcssABLj5CjMfLzjRKH0wB3MjTKACfrfj7tJBcMupAlA?e=hb0ayo
## Instalacja
W celu urochomienia gry należy pobrać najnowsze wydanie z zakładki releases i uruchomić plik .exe

### Komilacja kodu źródłowego
W celu własnoręczne zbudowania aplikacji należy sklonować repozytorium lub pobrać kod źródłowy jednej ze staszych wersji.

Po uruchomieniu gry wybierz tryb oraz pozion trudności w menu głównym. Podążaj za wyświetlanymi na ekranie instrukcjami. W prawym górnym rogu ekranu możesz sprawdzić aktualny procent ukończenia poziomu oraz czas gry. Twój wynik zostanie wyświetlony po zakończeniu poziomu, a jeżeli jest on jednym z twoich najwyższych wyników, pojawi się możliwość jego zapisu.

Wewnątrz sklonowanego repozytorium należy utworzyć nowe venv pythona o wersji 3.11
  ```bash
  python -m venv .venv
  ```
Po uruchomieniu wirtualnego środowiska należy popbrać niezbędne zależności opisane w pliku pyproject.toml
```bash
pip install .
```

## Zależności
Biblioteki i narzedzia niezbędne do działania programu
| Biblioteka | Wersja |
| --- | --- |
| Python | >= 3.11 |
| Pygame-ce | >= 2.4 |
| pygame_gui | == 0.6.10 |


## Przyszłe implementacje

## Źródła
Do stworzenia grzy urzyto następujących tekstów:


