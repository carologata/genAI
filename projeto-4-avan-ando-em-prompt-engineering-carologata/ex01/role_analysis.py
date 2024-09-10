import os
import google.generativeai as genai
from groq import Groq

models = ["gemini", "groq"]

roles = {
    "Educador tradicional": "Você é um educador tradicional com anos de experiência em universidades convencionais. Analise a École 42 de uma perspectiva acadêmica.",
    "Estudante de tecnologia": "Você é um estudante de tecnologia ansioso para aprender programação. Analise a École 42 do ponto de vista de um potencial aluno.",
    "Recrutador de tecnologia": "Você é um recrutador de profissionais de uma grande empresa de tecnologia. Avalie a École 42 considerando as habilidades que você busca em candidatos."
}

user_prompt = "Descreva a École 42 e seu método de ensino. Destaque os pontos principais que seriam relevantes para sua perspectiva."

""" GEMINI """
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def query_gemini(system_prompt, user_prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    response = chat.send_message(f"{system_prompt}\n\n{user_prompt}")
    print(response.text)
    return response.text


""" GROQ """
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def query_groq(system_prompt, user_prompt):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        stream=False,
    )
    return (completion.choices[0].message.content)

def get_response(model, system_prompt, user_prompt):
    if model == "gemini":
        return query_gemini(system_prompt, user_prompt)
    elif model == "groq":
        return query_groq(system_prompt, user_prompt)
    
def main():
    for model in models:
        print(f"=== Análises usando {model.upper()} ===\n\n")
        for key, value in roles.items():
            print(f"--- Análise da perspectiva de {key} ---\n")
            response = get_response(model, value, user_prompt)
            print(response)
            print("\n")
        print("\n")

if __name__ == "__main__":
    main()