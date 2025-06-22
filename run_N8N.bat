@echo off

SET WORKFLOW=1idwoT5UOdXBor3Q
SET ZIP=202401_NFs.zip
SET HEADER=202401_NFs_Cabecalho.csv
SET ITEMS=202401_NFs_Itens.csv

SET N8N_RUNNERS_ENABLED=true

if NOT "%1"=="" (
	sfk replace ./resposta.txt -spat -bylist .\pattern_nto.txt -yes
	cls
	echo Processamento finalizado!
	echo:
	echo Pergunta digitada: %question%
	echo:
	echo Resposta:
	echo:
	cat resposta.txt | grep -v obj|grep "final_response"|uniq
	echo:
	pause
	del /Q E:\E.zip
	del /Q E:\shared\E.zip
	del /Q teste0.txt
	del /Q teste1.csv
	del /Q teste2.csv
	del /Q %HEADER%
	del /Q %ITEMS%
	run_N8N.bat
)
del /Q E:\E.zip
del /Q E:\shared\E.zip
del /Q teste0.txt
del /Q teste1.csv
del /Q teste2.csv
del /Q resposta.txt
del /Q %HEADER%
del /Q %ITEMS%
7z -y e %ZIP%
copy /Y %HEADER% teste1.csv
copy /Y %ITEMS% teste2.csv
:ASK
cls
set question=
set /P question=Pergunta (Pressione ENTER para encerrar):
if "%question%"=="" GOTO EXIT
echo %question%>teste0.txt
echo ===>>teste0.txt
echo ===>>teste1.csv
sfk replace ./teste0.txt -spat -bylist .\pattern_crlf.txt -yes
7z a E:\E.zip teste0.txt teste1.csv teste2.csv
copy /Y E.zip E:\shared\E.zip
cls
echo Pergunta digitada: %question%
echo:
pause
echo:
echo Processando a resposta. Aguarde...
n8n execute --id %WORKFLOW% > resposta.txt && run_N8N.bat resultado
:EXIT
exit /b 0