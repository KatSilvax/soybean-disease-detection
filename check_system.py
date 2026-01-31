#!/usr/bin/env python3
"""
Script de Verificação do Sistema AgroIntelliVision

Este script verifica se todos os componentes necessários estão instalados
e configurados corretamente.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é adequada."""
    print("🐍 Verificando versão do Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Necessário Python 3.8+")
        return False

def check_dependencies():
    """Verifica se as dependências estão instaladas."""
    print("\n📦 Verificando dependências...")
    
    required_packages = [
        'flask', 'flask-cors', 'tensorflow', 'numpy', 'pillow'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"   ✅ {package} - Instalado")
        except ImportError:
            print(f"   ❌ {package} - Não encontrado")
            missing_packages.append(package)
    
    return len(missing_packages) == 0, missing_packages

def check_model_file():
    """Verifica se o arquivo do modelo existe."""
    print("\n🧠 Verificando modelo de IA...")
    model_path = Path("models/saved_models/modelo_soja.h5")
    
    if model_path.exists():
        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ Modelo encontrado ({size_mb:.1f} MB)")
        return True
    else:
        print("   ❌ Modelo não encontrado em models/saved_models/modelo_soja.h5")
        return False

def check_html_files():
    """Verifica se os arquivos HTML existem."""
    print("\n🌐 Verificando arquivos da interface...")
    
    html_files = ['index.html', 'index_professional.html', 'index_simple.html']
    found_files = []
    
    for html_file in html_files:
        if Path(html_file).exists():
            print(f"   ✅ {html_file} - Encontrado")
            found_files.append(html_file)
        else:
            print(f"   ⚠️  {html_file} - Não encontrado")
    
    return len(found_files) > 0

def check_directories():
    """Verifica se os diretórios necessários existem."""
    print("\n📁 Verificando estrutura de diretórios...")
    
    required_dirs = [
        'models/saved_models',
        'assets',
        'data',
        'utils'
    ]
    
    all_exist = True
    
    for directory in required_dirs:
        if Path(directory).exists():
            print(f"   ✅ {directory}/ - Existe")
        else:
            print(f"   ❌ {directory}/ - Não encontrado")
            all_exist = False
    
    return all_exist

def install_missing_dependencies(missing_packages):
    """Instala dependências faltantes."""
    if not missing_packages:
        return True
    
    print(f"\n🔧 Instalando dependências faltantes: {', '.join(missing_packages)}")
    
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', '--upgrade'
        ] + missing_packages)
        print("   ✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("   ❌ Erro ao instalar dependências")
        return False

def main():
    """Função principal de verificação."""
    print("=" * 50)
    print("🌱 AgroIntelliVision - Verificação do Sistema")
    print("=" * 50)
    
    checks_passed = 0
    total_checks = 5
    
    # Verificar Python
    if check_python_version():
        checks_passed += 1
    
    # Verificar dependências
    deps_ok, missing = check_dependencies()
    if deps_ok:
        checks_passed += 1
    else:
        print(f"\n🔧 Tentando instalar dependências faltantes...")
        if install_missing_dependencies(missing):
            checks_passed += 1
    
    # Verificar modelo
    if check_model_file():
        checks_passed += 1
    
    # Verificar HTML
    if check_html_files():
        checks_passed += 1
    
    # Verificar diretórios
    if check_directories():
        checks_passed += 1
    
    # Resultado final
    print("\n" + "=" * 50)
    print(f"📊 Resultado: {checks_passed}/{total_checks} verificações passaram")
    
    if checks_passed == total_checks:
        print("🎉 Sistema pronto para uso!")
        print("💡 Execute 'run.bat' (Windows) ou './run.sh' (Linux/macOS) para iniciar")
        return True
    else:
        print("⚠️  Alguns problemas foram encontrados.")
        print("📖 Consulte o GUIA_INSTALACAO.md para mais informações")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)