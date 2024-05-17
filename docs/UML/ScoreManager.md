![UML](img/ScoreManager.jpg)

# ScoreManager

 
_num_of_correct_chars: int - ostateczna ilość poprawnych znaków obliczona w GameManager

calculate_score(mode, counter) - oblicza ilość punktów w zależności od trybu i czasu, wynik umieszcza w polu _score

rank_score(storagemanager) - nadaje nowemu wynikowi pozycję w rankingu porównując go z poprzednimi wynikami

ask_if_save() - wyświetla komunikat pytający użytkownika czy chce zapisać swój wynik, jeżeli tak to wywołuje save_score() ze StorageManager, jeżeli nie to wywołuje destruktor

update_top_10(storagemanegar) - w przypadku gdy wynik zostaje oceniony jako jeden z 10 najwyższych, aktualizuje listę 10 najlepszych wyników

__del__() - destruktor, zwraca czy pomyślnie usunięty

## Score
_id: int - składowa statyczna, w momencie inicjalizacji obiektu zwiększa się o 1

input_player_name() - wprowadza nazwę gracza z klawiatury