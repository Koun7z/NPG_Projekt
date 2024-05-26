
# Progress

__init() - tworzy UILabel, ustawia _current_num_of_chars i _num_of_target_chars na 0

set_num_of_target_chars() - wywołuje get_target_text(), zlicza ilość znaków, zmienia pole _num_of_target_chars

update() - aktualizuje ilość znaków wprowadzonych przez gracza (_current_num_of_chars)

calculate_percentage() - oblicza _current_num_of_chars/_num_of_target_chars i zamienia go 
liczbę całkowitą która będzie wyśweitlona na ekranie

reset() - ustawia _current_num_of_chars i _num_of_target_chars na 0, zwraca czy udało się to zrobić