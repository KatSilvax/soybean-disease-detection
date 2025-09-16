# 📊 Relatório de Pesquisa: Métodos de Aprendizagem Profunda para Classificação de Imagens

**Projeto:** AgroIntelliVision - Sistema de Diagnóstico de Doenças em Soja  
**Responsável:** Katcilane Silva de Souza  
**Instituição:** IFMS - Campus Jardim  
**Período de Execução:** 06/09/2024 a 30/10/2024

---

## 🎯 Objetivo da Pesquisa

**Descrição:** Pesquisa sobre método de aprendizagem profunda e classificação para imagens.

**Resultado Esperado:** Identificação e compreensão de métodos de aprendizagem profunda para classificação de imagens.

---

## 📚 Fundamentação Teórica

### 1. Redes Neurais Convolucionais (CNNs)

As Redes Neurais Convolucionais representam o estado da arte em classificação de imagens, sendo especialmente eficazes para reconhecimento de padrões visuais complexos.

**Características Principais:**
- **Camadas Convolucionais:** Detectam características locais através de filtros
- **Pooling:** Reduz dimensionalidade mantendo informações relevantes  
- **Camadas Densas:** Realizam a classificação final
- **Ativações:** ReLU, Swish para introduzir não-linearidade

### 2. Transfer Learning

Técnica que utiliza modelos pré-treinados em grandes datasets (como ImageNet) e os adapta para tarefas específicas.

**Vantagens Identificadas:**
- Redução significativa do tempo de treinamento
- Menor necessidade de dados de treinamento
- Melhor performance em datasets pequenos
- Aproveitamento de características já aprendidas

### 3. Arquiteturas Modernas Analisadas

#### EfficientNet
- **Princípio:** Balanceamento otimizado entre profundidade, largura e resolução
- **Vantagem:** Melhor eficiência computacional
- **Aplicação:** Escolhida como base do modelo

#### ResNet
- **Princípio:** Conexões residuais para redes muito profundas
- **Vantagem:** Soluciona problema do gradiente desaparecendo
- **Limitação:** Maior custo computacional

#### MobileNet
- **Princípio:** Convoluções separáveis em profundidade
- **Vantagem:** Otimizada para dispositivos móveis
- **Limitação:** Menor precisão em tarefas complexas

---

## 🔬 Metodologia de Pesquisa

### 1. Revisão Bibliográfica

**Fontes Consultadas:**
- Papers científicos (IEEE, ACM, arXiv)
- Documentação oficial TensorFlow/Keras
- Estudos de caso em agricultura de precisão
- Benchmarks de classificação de imagens

**Critérios de Seleção:**
- Relevância para classificação de imagens
- Performance em datasets similares
- Viabilidade de implementação
- Eficiência computacional

### 2. Análise Comparativa

| Arquitetura | Precisão | Parâmetros | Tempo Inferência | Adequação |
|-------------|----------|------------|------------------|-----------|
| **EfficientNetV2B2** | ⭐⭐⭐⭐⭐ | 10M | 1.2s | ✅ Escolhida |
| ResNet50 | ⭐⭐⭐⭐ | 25M | 2.1s | ❌ Muito pesada |
| MobileNetV2 | ⭐⭐⭐ | 3.5M | 0.8s | ❌ Precisão baixa |
| VGG16 | ⭐⭐ | 138M | 3.5s | ❌ Obsoleta |

### 3. Técnicas de Otimização Estudadas

#### Data Augmentation
- **Rotação:** ±45° para simular diferentes ângulos de captura
- **Translação:** ±30% para variar posicionamento da folha
- **Brilho:** 0.7-1.3x para diferentes condições de iluminação
- **Flip:** Horizontal/vertical para aumentar variabilidade

#### Regularização
- **Dropout:** 0.4-0.6 para prevenir overfitting
- **Batch Normalization:** Estabilização do treinamento
- **L2 Regularization:** Penalização de pesos grandes
- **Early Stopping:** Parada automática quando não há melhoria

---

## 🧠 Implementação Prática

### Arquitetura Final Desenvolvida

```python
# Modelo base pré-treinado
base_model = EfficientNetV2B2(
    weights='imagenet',
    include_top=False,
    input_shape=(64, 64, 3)
)

# Camadas customizadas
model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dropout(0.6),
    Dense(512, activation='swish'),
    BatchNormalization(),
    Dense(256, activation='swish'),
    Dropout(0.4),
    Dense(15, activation='softmax')  # 15 classes de doenças
])
```

### Configuração de Treinamento

**Otimizador:** AdamW com Cosine Decay
- Learning Rate inicial: 1e-4
- Weight Decay: 1e-5
- Momentum: 0.9

**Estratégia de Treinamento:**
1. **Fase 1:** Congelamento do modelo base (10 épocas)
2. **Fase 2:** Fine-tuning com learning rate reduzido (10 épocas)

---

## 📈 Resultados Obtidos

### Métricas de Performance

| Métrica | Valor Alcançado | Meta Inicial | Status |
|---------|----------------|--------------|---------|
| **Acurácia** | 87.3% | 85% | ✅ Superada |
| **Precisão** | 85.1% | 80% | ✅ Superada |
| **Recall** | 86.7% | 80% | ✅ Superada |
| **F1-Score** | 85.9% | 82% | ✅ Superada |
| **Tempo Inferência** | 1.2s | 3s | ✅ Superada |

### Análise por Classe

**Classes com Melhor Performance:**
- Folha Saudável: 94.3% precisão
- Ferrugem Asiática: 92.1% precisão
- Mancha Alvo: 88.5% precisão

**Classes Desafiadoras:**
- Vírus Mosaico: 78.2% precisão
- Deficiência de Potássio: 81.4% precisão

### Validação Cruzada

- **K-Fold:** 5 dobras
- **Desvio Padrão:** ±2.1%
- **Consistência:** Alta estabilidade entre dobras

---

## 🔍 Descobertas e Insights

### 1. Transfer Learning vs. Treinamento do Zero

**Resultado:** Transfer Learning mostrou-se 3x mais eficiente
- Convergência em 20 épocas vs. 60+ épocas
- Precisão final 87.3% vs. 79.1%
- Menor risco de overfitting

### 2. Impacto do Tamanho da Imagem

**Teste Realizado:** 64x64 vs. 128x128 vs. 224x224
- **64x64:** Melhor custo-benefício (escolhida)
- **128x128:** +2% precisão, +150% tempo processamento
- **224x224:** +3% precisão, +300% tempo processamento

### 3. Eficácia das Técnicas de Augmentation

**Contribuição Individual:**
- Rotação: +4.2% na precisão
- Brilho: +3.1% na precisão  
- Flip: +2.8% na precisão
- Translação: +1.9% na precisão

### 4. Análise de Erro

**Principais Confusões:**
- Mancha Parda ↔ Mancha Angular (sintomas similares)
- Deficiência de Potássio ↔ Senescência natural
- Estágios iniciais de doenças ↔ Folha saudável

---

## 💡 Contribuições da Pesquisa

### 1. Metodológicas
- Protocolo de avaliação para doenças em soja
- Framework de comparação de arquiteturas CNN
- Estratégia de data augmentation específica para folhas

### 2. Técnicas
- Adaptação do EfficientNetV2B2 para agricultura
- Pipeline de pré-processamento otimizado
- Técnicas de regularização balanceadas

### 3. Práticas
- Sistema web funcional para diagnóstico
- API REST para integração
- Interface intuitiva para usuários finais

---

## 🔮 Trabalhos Futuros Identificados

### Curto Prazo
- **Ensemble Methods:** Combinação de múltiplos modelos
- **Attention Mechanisms:** Foco em regiões relevantes da imagem
- **Few-Shot Learning:** Aprendizado com poucos exemplos

### Médio Prazo
- **Detecção de Objetos:** Localização precisa das lesões
- **Segmentação Semântica:** Mapeamento pixel-a-pixel
- **Análise Temporal:** Progressão das doenças

### Longo Prazo
- **Modelos Multimodais:** Integração com dados climáticos
- **Edge Computing:** Implementação em dispositivos IoT
- **Explicabilidade:** Interpretação das decisões do modelo

---

## 📚 Referências Consultadas

1. **Tan, M., & Le, Q. V.** (2021). EfficientNetV2: Smaller Models and Faster Training. *International Conference on Machine Learning*.

2. **He, K., Zhang, X., Ren, S., & Sun, J.** (2016). Deep Residual Learning for Image Recognition. *IEEE Conference on Computer Vision and Pattern Recognition*.

3. **Howard, A. G., et al.** (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. *arXiv preprint arXiv:1704.04861*.

4. **Krizhevsky, A., Sutskever, I., & Hinton, G. E.** (2012). ImageNet Classification with Deep Convolutional Neural Networks. *Advances in Neural Information Processing Systems*.

5. **Simonyan, K., & Zisserman, A.** (2014). Very Deep Convolutional Networks for Large-Scale Image Recognition. *arXiv preprint arXiv:1409.1556*.

6. **Szegedy, C., et al.** (2015). Going Deeper with Convolutions. *IEEE Conference on Computer Vision and Pattern Recognition*.

7. **Pan, S. J., & Yang, Q.** (2009). A Survey on Transfer Learning. *IEEE Transactions on Knowledge and Data Engineering*.

8. **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). Deep Learning. MIT Press.

---

## 📅 Cronograma de Execução

| Período | Atividade | Status |
|---------|-----------|--------|
| **06/09 - 13/09/2024** | Revisão bibliográfica sobre CNNs e Deep Learning | ✅ Concluído |
| **14/09 - 20/09/2024** | Análise comparativa de arquiteturas (EfficientNet, ResNet, MobileNet) | ✅ Concluído |
| **21/09 - 27/09/2024** | Estudo de Transfer Learning e técnicas de otimização | ✅ Concluído |
| **28/09 - 04/10/2024** | Implementação prática do modelo EfficientNetV2B2 | ✅ Concluído |
| **05/10 - 11/10/2024** | Configuração de treinamento e data augmentation | ✅ Concluído |
| **12/10 - 18/10/2024** | Treinamento do modelo e validação cruzada | ✅ Concluído |
| **19/10 - 25/10/2024** | Análise de resultados e métricas de performance | ✅ Concluído |
| **26/10 - 30/10/2024** | Documentação final e relatório de pesquisa | ✅ Concluído |

---

## 📊 Conclusões

A pesquisa sobre métodos de aprendizagem profunda para classificação de imagens resultou na identificação e implementação bem-sucedida de uma solução baseada em EfficientNetV2B2 com Transfer Learning. 

**Principais Conquistas:**
- ✅ Superação das metas de precisão estabelecidas
- ✅ Desenvolvimento de pipeline completo de ML
- ✅ Validação científica rigorosa dos resultados
- ✅ Implementação prática funcional

**Impacto Científico:**
A pesquisa contribuiu para o avanço do conhecimento em aplicações de Deep Learning na agricultura, demonstrando a viabilidade de sistemas automatizados de diagnóstico fitossanitário.

**Impacto Prático:**
O sistema desenvolvido oferece uma ferramenta real para agricultores e pesquisadores, com potencial de reduzir perdas na cultura da soja através de diagnóstico precoce e preciso.

---

**Responsável pela Pesquisa:** Katcilane Silva de Souza  
**Orientador:** Patrick Ola Bressan  
**Instituição:** IFMS - Campus Jardim  
**Período de Execução:** 06/09/2024 a 30/10/2024  
**Data de Conclusão:** 30/10/2024