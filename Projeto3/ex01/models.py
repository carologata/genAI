import os
import ollama
from groq import Groq
import google.generativeai as genai


""" PROMPT """
PROMPT:str = ("Sua tarefa é ler a descrição de uma vaga e estruturá-lo dentro dos quatro itens em inglês abaixo."
              "Na resposta não inclua nenhum outro item além dos itens informados abaixo."
                "- Name of role:"
                "- Working hours:"
                "- Country:"
                "- Tech skills:"
                "Segue abaixo um exemplo de como organizar a mensagem de retorno:"
                "Name of role: Pleno Software Engineer (BackEnd)"
                "Working hours: 8-5 (Monday to Friday)"
                "Country: United States"
                "Tech skills: Python, Java, C#, programming methodologies and frameworks"

                "Abaixo se encontra a descrição da vaga que será sua base para construir sua informação."
            )

def format_prompt(job_description: str):
    prompt:str = PROMPT + job_description
    return prompt


""" OLLAMA """
def query_ollama(formatted_prompt):
    print("Consultando Ollama...")
    try:
        response = ollama.chat(model='qwen2:1.5bd', messages=[
            {
                'role': 'user',
                'content': formatted_prompt,
            },
        ])
    except Exception as error:
        return {"Error": str(error)}
    return {"Qwen2 1.5B": response['message']['content']}

""" GROQ """
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def query_groq(formatted_prompt):
    print("Consultando Groq...")
    try:
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_prompt,
            }
        ],
        model="llama3-8b-8192")
    except Exception as error:
        return {"Error": str(error)}
    return {"Llama 3 8B": chat_completion.choices[0].message.content}


""" GEMINI """
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def query_gemini(formatted_prompt):
    print("Consultando Gemini...")
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(formatted_prompt)
    except Exception as error:
        return {"Error": str(error)}
    return {"Gemini 1.5 Flash": response.text}


""" ALL MODELS """
def query_all_models(formatted_prompt):
    results_gemini = query_gemini(formatted_prompt)
    results_groq = query_groq(formatted_prompt)
    results_ollama = query_ollama(formatted_prompt)
    results = {}
    results.update(results_ollama)
    results.update(results_groq)
    results.update(results_gemini)
    return results


def main():
    with open("job_description.txt", "r") as file:
        job_description = file.read()

    formatted_prompt = format_prompt(job_description)
    results = query_all_models(formatted_prompt)

    for model, response in results.items():
        print(f"\nAnálise do {model}:")
        print(response)
        print("-" * 50)

if __name__ == "__main__":
    main()