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
