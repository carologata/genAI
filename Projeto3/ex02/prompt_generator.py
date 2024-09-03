import os
import google.generativeai as genai

role = "especialista em métodos de educação inovadores em tecnologia"
task = "explicar o conceito e a abordagem única da École 42 para interessados em educação em tecnologia"
topic = "École 42 e seu método de ensino"
specific_question = "O que é a École 42 e como seu método de ensino difere das faculdades tradicionais de computação?"

def create_prompt(role, task, topic, specific_question):
    prompt = (f"Você é um {role} e sua função é ${task} sobre o seguinte tópico {topic}." 
        "Você precisa responder a questão {specific_question}."
        "Separe a sua resposta em 5 módulos mas não mostre as tags:"
            f"<prompt>"
            f"<role>{role}</role>"
            f"<task>{task}</task>"
            f"<topic>{topic}</topic>"
            f"<specific_question>{specific_question}</specific_question>"
            f"<modules>"
            f"<conceito>Explicação básica do conceito</conceito>"
            f"<cotidiano>Analogia do cotidiano</cotidiano>"
            f"<pergunta>Solução passo a passo da pergunta</pergunta>"
            f"<exemplo>Exemplo detalhado</exemplo>"
            f"<dica>Dica prática para iniciantes</dica>"
            f"</modules>"
            f"</prompt>"
    )
    return prompt
    
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def send_to_gemini(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return (response.text)

def main():
    prompt = create_prompt(role, task, topic, specific_question)
    response = send_to_gemini(prompt)
    print("\nResposta do Gemini 1.5 Flash:")
    print(response)

if __name__ == "__main__":
    main()

