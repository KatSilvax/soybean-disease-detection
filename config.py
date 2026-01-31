"""
Configurações do AgroIntelliVision

Este arquivo centraliza todas as configurações do sistema para facilitar
manutenção e modificações futuras.
"""

import os

# Configurações do Modelo
MODEL_CONFIG = {
    'path': 'models/saved_models/modelo_soja.h5',
    'input_size': (64, 64),
    'classes': [
        'antracnose', 'crestamento_foliar_cercospora', 'ferrugem_asiatica',
        'mancha_alvo', 'mancha_olho_de_ra', 'mildio', 'oidio', 'classe_7',
        'classe_8', 'classe_9', 'classe_10', 'classe_11', 'classe_12',
        'saudavel', 'classe_14', 'classe_15'
    ],
    'confidence_threshold': 0.65
}

# Configurações do Servidor Flask
SERVER_CONFIG = {
    'host': '127.0.0.1',
    'port': 5000,
    'debug': True
}

# Configurações de Upload
UPLOAD_CONFIG = {
    'max_file_size': 5 * 1024 * 1024,  # 5MB
    'allowed_extensions': {'png', 'jpg', 'jpeg'},
    'upload_folder': 'uploads'
}

# Configurações de Logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'logs/app.log'
}

# Mapeamento de nomes de classes para exibição
CLASS_DISPLAY_NAMES = {
    'saudavel': 'Folha Saudável',
    'antracnose': 'Antracnose',
    'crestamento_foliar_cercospora': 'Crestamento Foliar de Cercospora',
    'ferrugem_asiatica': 'Ferrugem Asiática',
    'mancha_alvo': 'Mancha Alvo',
    'mancha_olho_de_ra': 'Mancha Olho-de-Rã',
    'mildio': 'Míldio',
    'oidio': 'Oídio'
}

# Informações do Projeto
PROJECT_INFO = {
    'name': 'AgroIntelliVision',
    'version': '1.0.0',
    'description': 'Sistema de detecção de doenças em folhas de soja',
    'authors': ['Katcilane Silva', 'Kaue Ribeiro'],
    'coordinator': 'Patrick Ola Bressan',
    'institution': 'IFMS Campus Jardim',
    'year': 2024
}

# Caminhos importantes
PATHS = {
    'models': 'models/saved_models/',
    'assets': 'assets/',
    'logs': 'logs/',
    'data': 'data/',
    'uploads': 'uploads/'
}

# Criar diretórios se não existirem
def create_directories():
    """Cria os diretórios necessários se não existirem."""
    for path in PATHS.values():
        os.makedirs(path, exist_ok=True)

if __name__ == '__main__':
    create_directories()
    print("Diretórios criados com sucesso!")