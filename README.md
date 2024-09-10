# genAI

# Criar um ambiente virtual do python

```bash
#Crie uma pasta 
mkdir .venv

#Crie o ambiente virtual nessa pasta (atenção para a versão do python utilizada)
python -m venv .venv

#Ative o ambiente virtual
source <venv_path>/bin/activate

#mova as dependências instaladas para o arquivo requirement.txt
pip freeze > requirements.txt

#Se existir o arquivo requirement.txt com todas as dependências necessárias, instale no seu ambiente virtual
pip install -r requirements.txt

#Desative o ambiente virtual
deactivate
```


# Configurar APIs

+ Gemini API

```bash

#Install the Gemini API SDK
pip install -q -U google-generativeai

#Set up API key
export API_KEY=<YOUR_API_KEY>

#Import the library
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

#Make request
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)
```
Source: https://ai.google.dev/gemini-api/docs/quickstart?lang=python


+ Groq API

```bash

#Install the Groq Python library
pip install groq

#Set up API key
export GROQ_API_KEY=<your-api-key-here>

#Import the library
import os

from groq import Groq

#Make request
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
```
Source: https://console.groq.com/docs/quickstart

# Configurar ChromaDB

```bash
#Install ChromaDB Libray
pip install chromadb
``
