import openai

openai.api_key = ""
prompt = ""

f = open("Zadanie dla Junior AI Developera - tresc artykulu.txt", "r")
text = f.read()

prompt1 = "Podany dokument przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML dla nagłówków i zwykłego tekstu."
prompt2 = "Podany dokument przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML dla nagłówków i zwykłego tekstu. Nie dodawaj nowych nagłówków. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg."
prompt3 = "Podany dokument przekształć na kod HTML, który można umieścić między tagami <body> i </body>. Użyj odpowiednich tagów HTML do strukturyzacji treści. Wyznacz miejsca, w których warto wstawić grafiki i oznacz je tagiem <img> z atrybutem src=image_placeholder.jpg. Do każdej grafiki dodaj atrybut alt z promptem do wygenerowania grafiki. Pod grafikami umieść podpisy używając odpowiednich tagów."

"""def text_to_html():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},  # Send the long text first
            {"role": "user", "content": prompt}    # Follow up with the specific question
        ]
    )
    # Extract the response content
    message = response['choices'][0]['message']['content']
    return message"""

f.close()