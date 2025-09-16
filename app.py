# Importação das bibliotecas necessárias
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

# Inicialização da aplicação Flask e configuração do CORS
app = Flask(__name__)
CORS(app)

# Carregar modelo
# Configuração do modelo
MODEL_PATH = 'models/saved_models/modelo_soja.h5'
model = None

# Classes das doenças
# Lista de classes/doenças que o modelo pode identificar
CLASSES = [
    'antracnose', 'crestamento_bacteriano', 'deficiencia_de_potassio',
    'ferrugem_asiatica', 'ferrugem_do_feijao', 'mancha_alvo',
    'mancha_angular', 'mancha_olho_de_ra', 'mancha_parda',
    'mildio', 'oidio', 'podridao_radicular', 'saudavel',
    'sindrome_morte_subita', 'virus_mosaico'
]

def load_model():
    """
    Carrega o modelo de deep learning salvo no caminho especificado
    Utiliza variável global para manter o modelo em memória
    """
    global model
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Modelo carregado com sucesso!")
    else:
        print("Modelo não encontrado. Execute o treinamento primeiro.")

def preprocess_image(image):
    """
    Prepara a imagem para ser processada pelo modelo:
    1. Redimensiona para 64x64 pixels
    2. Normaliza os valores dos pixels para o intervalo [0,1]
    3. Adiciona uma dimensão para batch
    """
    image = image.resize((64, 64))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    """
    Rota principal que renderiza a página HTML da interface
    """
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para receber imagens e realizar predições
    Retorna a classe predita e o nível de confiança da predição
    """
    try:
        print("→ Recebendo requisição")
        
        # Verifica se o modelo está carregado
        if model is None:
            print("✗ Modelo não carregado")
            return jsonify({'error': 'Modelo não carregado'}), 500
        
        # Validação do arquivo recebido
        if 'file' not in request.files:
            print("✗ Arquivo não encontrado")
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        if file.filename == '':
            print("✗ Nome do arquivo vazio")
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        print(f"→ Processando: {file.filename}")
        
        # Processar imagem
        # Processamento da imagem
        image = Image.open(io.BytesIO(file.read()))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        processed_image = preprocess_image(image)
        print(f"→ Imagem processada: {processed_image.shape}")
        
        # Fazer predição
        # Realização da predição
        predictions = model.predict(processed_image, verbose=0)
        predicted_class = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_class])
        
        print(f"→ Predição: classe {predicted_class}, confiança {confidence:.2f}")
        
        # Mapear para nome da classe
        # Formatação do resultado
        if predicted_class < len(CLASSES):
            class_name = CLASSES[predicted_class]
            if class_name == 'saudavel':
                class_name = 'Folha Saudável'
            else:
                class_name = class_name.replace('_', ' ').title()
        else:
            class_name = 'Desconhecido'
        
        print(f"✓ Resultado: {class_name}")
        
        return jsonify({
            'prediction': class_name,
            'confidence': confidence
        })
    
    except Exception as e:
        print(f"✗ ERRO: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# Inicialização da aplicação
if __name__ == '__main__':
    load_model()
    app.run(debug=True, host='127.0.0.1', port=5000)
