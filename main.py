import openai

openai.api_key = ""
prompt = ""

f = open("Zadanie dla Junior AI Developera - tresc artykulu.txt", "r")
text = f.read()


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