# genAI

# Para criar um ambiente virtual do python

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

```

+ Groq API

```bash

#Install the Groq Python library
pip install groq

#Set API key
export GROQ_API_KEY=<your-api-key-here>

#Performing a Chat Completion
import os

from groq import Groq

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

