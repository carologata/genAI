import os
import google.generativeai as genai

from github_comments import github_comments
from github_examples import github_examples

""" GEMINI API """
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def send_to_gemini(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
    except Exception as e:
        return (f"Error: {e}")
    return (response.text)


def call_llm(text):
    try:
        prompt = ("<Instrução> Preciso criar um sistema de classificação de sentimentos para comentários do Github."
                "Todo texto contém um comentário do Github e preciso que com base nos exemplos"
                "você retorne o sentimento relacionado ao comentário. </Instrução> Exemplos:\n")
        for example in github_examples:
            text_example = example["text"]
            sentiment_example = example["sentiment"]
            prompt += f"<example>\n<text>{text_example}</text>\n<sentiment>{sentiment_example}</sentiment>\n</example>\n"
        prompt += (f"Baseado na instrução e nos exemplos anteriores, qual é o sentimento associado ao texto abaixo? "
                "Responda apenas se o sentimento associado ao texto é Positivo, Negativo ou Neutro. Texto:\n"
                f"{text}")
        response = send_to_gemini(prompt)
    except Exception as e:
        return (f"Error: {e}")
    return (response)

def parse_llm_response(response):
    if response.find("Positivo") != -1:
        return ("Positivo")
    elif response.find("Negativo") != -1:
        return ("Negativo")
    elif response.find("Neutro") != -1:
        return ("Neutro")
    else:
        return (f"Erro ao identificar o sentimento: {response}")
    
def analyze_sentiments(comments):
    for comment in comments:
        llm_response = call_llm(comment["text"])
        comment["sentiment"] = parse_llm_response(llm_response)

analyze_sentiments(github_comments)

for comment in github_comments:
    print(f"Texto: {comment['text']}")
    print(f"Sentimento: {comment['sentiment']}")
    print("-" * 50)