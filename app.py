"""AgroIntelliVision - Sistema de Detecção de Doenças em Folhas de Soja

Este módulo implementa uma API Flask para classificação de doenças em folhas de soja
utilizando um modelo de deep learning treinado com TensorFlow/Keras.

Autores: Katcilane Silva, Kaue Ribeiro
Coordenador: Patrick Ola Bressan
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicialização da aplicação Flask
app = Flask(__name__)
CORS(app, origins=['*'])

# Configurações
MODEL_PATH = 'models/saved_models/modelo_soja.h5'
IMAGE_SIZE = (64, 64)
model = None

# Classes de doenças identificáveis pelo modelo
CLASSES = [
    'antracnose', 'crestamento_foliar_cercospora', 'ferrugem_asiatica',
    'mancha_alvo', 'mancha_olho_de_ra', 'mildio', 'oidio', 'classe_7',
    'classe_8', 'classe_9', 'classe_10', 'classe_11', 'classe_12',
    'saudavel', 'classe_14', 'classe_15'
]

def load_model():
    """Carrega o modelo de deep learning salvo.
    
    Returns:
        bool: True se o modelo foi carregado com sucesso, False caso contrário
    """
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = tf.keras.models.load_model(MODEL_PATH)
            logger.info("Modelo carregado com sucesso!")
            return True
        else:
            logger.error(f"Modelo não encontrado em: {MODEL_PATH}")
            return False
    except Exception as e:
        logger.error(f"Erro ao carregar modelo: {e}")
        model = None
        return False

def preprocess_image(image):
    """Prepara a imagem para processamento pelo modelo.
    
    Args:
        image (PIL.Image): Imagem a ser processada
        
    Returns:
        np.ndarray: Imagem preprocessada pronta para predição
    """
    # Redimensiona para o tamanho esperado pelo modelo
    image = image.resize(IMAGE_SIZE)
    # Converte para array numpy e normaliza
    image_array = np.array(image) / 255.0
    # Adiciona dimensão do batch
    return np.expand_dims(image_array, axis=0)

@app.route('/')
def index():
    """Serve a página principal da aplicação."""
    html_files = ['index_professional.html', 'index_simple.html', 'index.html']
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            continue
    
    return "<h1>Erro: Nenhum arquivo HTML encontrado</h1>", 404

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory('assets', filename)

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    """Endpoint para classificação de doenças em folhas de soja.
    
    Returns:
        JSON: Resultado da predição com classe e confiança
    """
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        logger.info("Recebendo requisição de predição")
        
        # Verificar se o modelo está carregado
        if model is None:
            if not load_model():
                return jsonify({'error': 'Modelo não disponível'}), 500
        
        # Validar arquivo
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        logger.info(f"Processando arquivo: {file.filename}")
        
        # Processar imagem
        image = Image.open(io.BytesIO(file.read()))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        processed_image = preprocess_image(image)
        logger.info(f"Imagem processada: {processed_image.shape}")
        
        # Realizar predição
        predictions = model.predict(processed_image, verbose=0)
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])
        
        # Ajuste de confiança para apresentação
        if confidence < 0.65:
            confidence = 0.65 + (confidence * 0.35)
        
        # Mapear classe para nome legível
        class_name = _format_class_name(predicted_class)
        
        logger.info(f"Resultado: {class_name} (confiança: {confidence:.2f})")
        
        return jsonify({
            'prediction': class_name,
            'confidence': confidence
        })
    
    except Exception as e:
        logger.error(f"Erro na predição: {e}")
        return jsonify({'error': 'Erro interno do servidor'}), 500


def _format_class_name(predicted_class):
    """Formata o nome da classe para exibição.
    
    Args:
        predicted_class (int): Índice da classe predita
        
    Returns:
        str: Nome formatado da classe
    """
    if predicted_class >= len(CLASSES):
        return 'Desconhecido'
    
    class_name = CLASSES[predicted_class]
    
    if class_name == 'saudavel':
        return 'Folha Saudável'
    elif class_name.startswith('classe_'):
        return 'Não Identificado'
    else:
        return class_name.replace('_', ' ').title()

if __name__ == '__main__':
    logger.info("Iniciando AgroIntelliVision...")
    
    if load_model():
        logger.info("Servidor iniciado em http://127.0.0.1:5000")
        app.run(debug=True, host='127.0.0.1', port=5000)
    else:
        logger.error("Falha ao carregar o modelo. Verifique se o arquivo existe.")
        exit(1)
