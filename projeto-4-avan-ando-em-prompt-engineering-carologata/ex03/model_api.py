import os
import google.generativeai as genai
from groq import Groq

""" GEMINI """
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def query_gemini(formatted_prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(formatted_prompt)
    except Exception as error:
        return {"Error": str(error)}
    return (response.text)

""" GROQ """
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def query_groq(formatted_prompt):
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
    return (chat_completion.choices[0].message.content)

def get_response(formatted_prompt):
    response = query_groq(formatted_prompt)
    return response