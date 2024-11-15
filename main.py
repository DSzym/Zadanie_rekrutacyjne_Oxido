from openai import OpenAI
import os

client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY"))
prompt = ""

text_file = open("Zadanie dla Junior AI Developera - tresc artykulu.txt", "r", encoding="utf-8")
text = text_file.read()
print(text)

prompt1 = "Podany tekst przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML dla nagłówków i zwykłego tekstu."
prompt2 = "Podany tekst przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML dla nagłówków i zwykłego tekstu. Nie dodawaj nowych nagłówków. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg."
prompt3 = "Podany tekst przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML do strukturyzacji treści. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg. Do każdej grafiki dodaj atrybut alt z promptem do wygenerowania grafiki. Pod grafikami umieść podpisy używając odpowiednich tagów."
prompt4 = "Podaną treść artykułu przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML do strukturyzacji treści artykułu. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg. Do każdej grafiki dodaj atrybut alt z promptem do wygenerowania grafiki. Pod grafikami umieść podpisy używając odpowiednich tagów."
prompt5 = "Podany tekst przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML do strukturyzacji treści artykułu. Nie dodawaj nowych nagłówków. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg. Do każdej grafiki dodaj atrybut alt z promptem do wygenerowania grafiki. Pod grafikami umieść podpisy używając odpowiednich tagów."

def text_to_html():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": text},
            {"role": "user", "content": prompt5}
        ]
    )

    message = completion.choices[0].message.content
    message = message[7:-4]
    #print(message)
    return message

#text_to_html()

text_file.close()

html_file = open("artykul.html", "w")
html_file.write(text_to_html())
html_file.close()
