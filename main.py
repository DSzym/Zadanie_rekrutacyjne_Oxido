from openai import OpenAI
import os


# Stworzenie połączenia z API OpenAI
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))

def pass_long_text_and_prompt_to_openai(prompt, text):
    """
    Funkcja, która przekazuje treść artykułu wraz z promptem do OpenAI i zwraca odpowiedź
    :param prompt: zawiera treść prompta.
    :param text: zawiera wczytaną treść artykułu.
    """

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": text},
            {"role": "user", "content": prompt}
        ]
    )

    message = completion.choices[0].message.content
    message = message[7:-4]

    return message


#Wczytanie pliku tekstowego z artykułem
text_file = open("Zadanie dla Junior AI Developera - tresc artykulu.txt", "r", encoding="utf-8")
txt = text_file.read()

prmpt = "Podany tekst przekształć na kod HTML, który można umieścić między tagami <body> i </body> (nie dołączaj tych znaczników). Użyj odpowiednich tagów HTML do strukturyzacji treści artykułu. Nie dodawaj nowych nagłówków. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg. Do każdej grafiki dodaj atrybut alt z promptem do wygenerowania grafiki. Pod grafikami umieść podpisy używając odpowiednich tagów."

# Zapisanie odpowiedzi (artykułu) jako plik HTML
html_file = open("artykul.html", "w")
html_file.write(pass_long_text_and_prompt_to_openai(prmpt, txt))
html_file.close()
text_file.close()
