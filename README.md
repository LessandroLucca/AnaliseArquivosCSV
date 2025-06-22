# Agentes Autônomos – Análise de Arquivos CSV

Nesse repositório existem os seguintes arquivos:

* N8N_Workflow.json
* run_N8N.bat
* run_python.py

# N8N_Workflow.json
Arquivo JSON de um workflow, de um agente criado no N8N, o qual usa Ollama juntamente com o modelo o LLM qwen2.5vl:3b, para permitir que sejam inseridas perguntas acerca das planilhas de NF-Es, contidas no arquivo ZIP denominado 202401_NFs.zip.

Essa pipeline está programada para ser acionada a partir de três tipos diferentes de gatilhos: 

* Ao realizar o upload para diretório E:\shared (existe um listener que fica monitorando essa pasta)
* Ao acessar a URL do Web (P.Ex.: http://localhost:5678/webhook-test/14f459ae-8728-4551-813d-8cd6ae91f1c3)
* Ao receber uma chamada externa (P.Ex. Comando executado a partir da linha de comando: bash, shell ou CMD)

OBS: O arquivo ZIP deve estar previamente presente na pasta E:\shared, para a execução do 2º ou 3º gatilho

# run_N8N.bat
Script BAT que serve meramente como interface para a entrada das perguntas ao agente da pipeline criada no workflow N8N acima.
Depende dos seguintes utilitários (comandos) instalados no sistema:
* nodeJs
* N8N
* 7z
* grep
* sfk

OBS: Altere a seguinte linha do arquivo BAT com o ID do workflow cadastrado no N8N, para poder executar o agente corretamente.

> SET WORKFLOW=1idwoT5UOdXBor3Q

# run_python.py
Script de agente escrito na linguagem python, o qual usa Ollama juntamente com o modelo o LLM qwen2.5vl:3b, para permitir que sejam inseridas perguntas acerca das planilhas de NF-Es, contidas no arquivo ZIP denominado 202401_NFs.zip, presente no mesmo diretório que for executado o comando:

> python run_ollama.py
