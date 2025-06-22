import ollama
import zipfile
import os

preface = "Here is the the CSV content:\n"
prepare = "\n\nPlease think about an plan and all the steps necessary to extract the follow information of CSV. Execute the plan and return just the answer of the question in silent:"

questions = [
    "How many lines exists in following CSV spreadsheet? ",
    "Which is the sum of all 'VALOR NOTA FISCAL' column values in following CSV spreadsheet? ",
    "Which is the major and maximum value of all 'VALOR NOTA FISCAL' column in following CSV spreadsheet? "+
    "After that response which is the value of the 'CPF/CNPJ Emitente' of the same line that have the previous founded value (major and maximum value of all 'VALOR NOTA FISCAL' column). ",
    "What is the sum of all values of 'VALOR NOTA FISCAL' column?",
    "Calculate and respond these two following proposals:\n"+
    "1. Select, reserve and tell how many lines exists in the CSV with value 378257000181 on 'CPF/CNPJ Emitente' column?\n"+
    "2. Using just only the lines selected by the first proposal, filter and calcule the sum of values of 'VALOR NOTA FISCAL' column",
    "What is the value of 'CPF/CNPJ Emitente' at the second line at the original CSV content?",
]

with zipfile.ZipFile('202401_NFs.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

with open("202401_NFs_Cabecalho.csv", "rb") as f:
    cabecalho = f.read()
    
with open("202401_NFs_Itens.csv", "rb") as f:
    itens = f.read()

def chat(preface, cabecalho, prepare, question):
    response = ollama.chat(
        model='qwen2.5vl:3b',
        stream=True,
        messages=[
            {
                'role': 'user',
                'content': preface+"\n###START HEADER CSV FILE###\n"+cabecalho.decode('utf-8')+"\n###END HEADER CSV FILE###\n\n###START ITEMS CSV FILE###\n"+itens.decode('utf-8')+"\n###END ITEMS CSV FILE###\n"+prepare+question,
                'options': {
                    'num_gpu': 999,
                    'num_ctx ': 65536,
                    'temperature': 0.7,
                    'num_predict': 1000,
                    'keep_alive':-1,
                },
                'stream': False,
                'format': 'json',
            },
        ]
    )
    print("\nOllama Chat Response about CSV files:")
    for line in response:
        print(line['message']['content'], end='', flush=True)

os.system('cls')

for question in questions:
    print("\n\n"+question)
    chat(preface, cabecalho, prepare, question)
    
while True:
    question = input('\nInput Q to quit or Type your question: ')
    if question.lower() == 'q':
        break
    else:
        chat(preface, cabecalho, prepare, question)