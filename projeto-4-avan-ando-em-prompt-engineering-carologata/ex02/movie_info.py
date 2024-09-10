import os
import json
import google.generativeai as genai
from groq import Groq


movie_titles = ["The Matrix", "Inception", "Pulp Fiction"]

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

def get_response(model, user_prompt):
    if model == "gemini":
        return query_gemini(user_prompt)
    elif model == "groq":
        return query_groq(user_prompt)

def get_movie_info(movie_title):
    user_prompt = f"""
        Provide information about the movie "{movie_title}" in JSON format.
        Do not write in your answer that you're giving information in JSON format.
        The answer should be just the information in JSON format.
        Start your response with:
        {{
        "title": "{movie_title}",
        """
    try:
        response = get_response("gemini", user_prompt)
        response_json = json.loads(response)
        response_expected = response.strip("{}")
        return {movie_title: response_expected}, None
    except Exception as error:
        return None, str(error)

def main():
    for title in movie_titles:
        print(f"\nAnalyzing: {title}")
        result, error = get_movie_info(title)
        if result:
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print(f"Error: {error}")
        print("-" * 50)

if __name__ == "__main__":
    main()