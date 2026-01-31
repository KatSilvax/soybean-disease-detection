@echo off
chcp 65001 >nul
echo ========================================
echo    AgroIntelliVision - Iniciando...
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado!
    echo Por favor, instale o Python 3.8+ antes de continuar.
    pause
    exit /b 1
)

REM Tentar ativar ambiente virtual
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Ativando ambiente virtual venv...
    call venv\Scripts\activate.bat
) else (
    echo [AVISO] Nenhum ambiente virtual encontrado.
    echo [INFO] Usando Python global...
)

REM Verificar se o modelo existe
if not exist "models\saved_models\modelo_soja.h5" (
    echo [ERRO] Modelo não encontrado!
    echo Verifique se o arquivo modelo_soja.h5 existe em models/saved_models/
    pause
    exit /b 1
)

REM Instalar dependências se necessário
echo [INFO] Verificando dependências...
pip install -r requirements.txt --quiet

REM Iniciar servidor
echo [INFO] Iniciando servidor Flask...
echo [INFO] Acesse: http://127.0.0.1:5000
echo.
python app.py

echo.
echo [INFO] Servidor encerrado.
pause