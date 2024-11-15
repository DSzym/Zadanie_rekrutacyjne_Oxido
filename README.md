# Zadanie rekrutacyjne Oxido - Junior AI Developer

## Opis działania
Zadaniem programu jest, za pomocą OpenAI, przekształcenie treści artykułu zapisanego w formie pliku .txt na plik HTML z odpowiednimi tagami, wskazaniem miejsc na grafiki i opisaniem ich. 
Program wczytuje plik tekstowy, następnie jego treść wraz promptem opisującym sposób przekształcenia treści prekazuje do OpenAI; na koniec odpowiedź od OpenAI, czyli kod HTML artykułu, zapisuje w pliku HTML.  

## Wymagania
- Python 3.10
- biblioteka openai

## Instrukcja uruchomienia
Aby program nawiązał połączenie z API OpenAI należy ustawić zmienną środowiskową OPENAI_API_KEY z kluczem do API OprenAI jako wartość.
1. Sklonuj repozytorium.
2. Uruchom program main.py
