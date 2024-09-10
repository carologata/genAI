__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import os
import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from tqdm import tqdm
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        #PdfReader is used to open and read PDF files.
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def process_pdf_directory(pdf_directory, collection):
    #tqdm is a Python library that provides a progress bar for iterators. 
    for filename in tqdm(os.listdir(pdf_directory)):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            text = extract_text_from_pdf(pdf_path)
            collection.add(
                        documents=[text],
                        metadatas=[{"source": filename}],
                        ids=[filename]
                    )

def interactive_query_loop(collection):
    while True:
        query = input("\nConsulta (digite 'sair' para finalizar): ")
        if query.lower() == 'sair':
            break
        
        results = collection.query(
            query_texts=[query],
            n_results=10,
            include=["documents", "metadatas"]
        )
        
        print("\nResultados:\n")
        if len(results['documents'][0]) == 0:
            print("Nenhum resultado encontrado\n")
        else:
            for document, metadata in zip(results['documents'][0], results['metadatas'][0]):
                print(f"Documento: {metadata['source']}")
                print(f"Trecho: {document[:200]}...") # Apenas os 200 primeiros caracteres
                print("\n")  # Add a blank line between results for readability

def main():
    persist_directory = "./chroma_data"
    pdf_directory = "./pdfs"
    # Configurar ChromaDB com persistência local
    chroma_client = chromadb.PersistentClient(path=persist_directory)
    # Criar embedding function
    # Nota: Tente outro modelo, como "paraphrase-multilingual-MiniLM-L12-v2"
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    # Criar ou obter uma coleção existente
    collection = chroma_client.get_or_create_collection(name="curriculos", embedding_function=embedding_function)
    # Processar diretório de PDFs
    process_pdf_directory(pdf_directory, collection)
    # Iniciar loop de consulta interativa
    interactive_query_loop(collection)

main()