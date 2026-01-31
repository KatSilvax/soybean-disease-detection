#!/bin/bash

# AgroIntelliVision - Script de Execução (Linux/macOS)
# Autores: Katcilane Silva, Kaue Ribeiro

echo "========================================"
echo "   AgroIntelliVision - Iniciando..."
echo "========================================"
echo

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python 3 não encontrado!"
    echo "Por favor, instale o Python 3.8+ antes de continuar."
    exit 1
fi

# Verificar versão do Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "[ERRO] Python $python_version encontrado, mas é necessário Python $required_version ou superior"
    exit 1
fi

# Tentar ativar ambiente virtual
if [ -d "venv" ]; then
    echo "[INFO] Ativando ambiente virtual venv..."
    source venv/bin/activate
else
    echo "[AVISO] Nenhum ambiente virtual encontrado."
    echo "[INFO] Criando novo ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Verificar se o modelo existe
if [ ! -f "models/saved_models/modelo_soja.h5" ]; then
    echo "[ERRO] Modelo não encontrado!"
    echo "Verifique se o arquivo modelo_soja.h5 existe em models/saved_models/"
    exit 1
fi

# Instalar dependências
echo "[INFO] Verificando dependências..."
pip install -r requirements.txt --quiet

# Iniciar servidor
echo "[INFO] Iniciando servidor Flask..."
echo "[INFO] Acesse: http://127.0.0.1:5000"
echo
python3 app.py

echo
echo "[INFO] Servidor encerrado."