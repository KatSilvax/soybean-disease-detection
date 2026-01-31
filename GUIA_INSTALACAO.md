# 🌱 AgroIntelliVision - Guia de Instalação Completo

> **Sistema inteligente para detecção de doenças em folhas de soja**

---

## 📋 O que você precisa ter instalado

### 1. Python (Obrigatório)
- **Versão:** Python 3.8 ou superior
- **Download:** https://www.python.org/downloads/
- **Durante a instalação:** ✅ Marque "Add Python to PATH"

### 2. Git (Recomendado)
- **Download:** https://git-scm.com/downloads
- **Para que serve:** Baixar o projeto do GitHub

---

## 🚀 Como instalar e executar

### Opção 1: Download Direto (Mais Fácil)

1. **Baixe o projeto:**
   - Acesse: https://github.com/seu-usuario/AgroIntelliVision
   - Clique no botão verde "Code" → "Download ZIP"
   - Extraia o arquivo ZIP em uma pasta de sua escolha

2. **Execute o programa:**
   - Abra a pasta extraída
   - Clique duas vezes no arquivo `run.bat`
   - Aguarde o programa inicializar

### Opção 2: Usando Git (Para usuários avançados)

1. **Abra o Prompt de Comando:**
   - Pressione `Windows + R`
   - Digite `cmd` e pressione Enter

2. **Navegue até onde quer salvar o projeto:**
   ```cmd
   cd C:\Users\SeuNome\Desktop
   ```

3. **Baixe o projeto:**
   ```cmd
   git clone https://github.com/seu-usuario/AgroIntelliVision.git
   cd AgroIntelliVision
   ```

4. **Execute o programa:**
   ```cmd
   run.bat
   ```

---

## 🖥️ Como usar o sistema

### 1. Iniciando o programa
- Execute o arquivo `run.bat`
- Aguarde aparecer a mensagem: "Servidor iniciado em http://127.0.0.1:5000"
- **NÃO FECHE** a janela do prompt de comando

### 2. Acessando a interface
- Abra seu navegador (Chrome, Firefox, Edge, etc.)
- Digite na barra de endereços: `http://127.0.0.1:5000`
- Pressione Enter

### 3. Analisando uma folha
1. **Prepare sua imagem:**
   - Tire uma foto clara da folha de soja
   - Formatos aceitos: JPG, JPEG, PNG
   - Tamanho recomendado: até 5MB

2. **Envie a imagem:**
   - Arraste a foto para a área indicada, OU
   - Clique em "Selecione o arquivo" e escolha a imagem

3. **Veja o resultado:**
   - O sistema mostrará se a folha está saudável ou doente
   - Também mostrará o nível de confiança da análise

---

## ❗ Solucionando problemas comuns

### "Python não encontrado"
- **Solução:** Instale o Python do site oficial
- **Importante:** Durante a instalação, marque "Add Python to PATH"

### "Modelo não encontrado"
- **Causa:** O arquivo do modelo de IA não está na pasta correta
- **Solução:** Verifique se existe o arquivo `modelo_soja.h5` em `models/saved_models/`

### "Erro ao conectar ao servidor"
- **Causa:** O servidor não está rodando
- **Solução:** 
  1. Execute novamente o `run.bat`
  2. Aguarde a mensagem de confirmação
  3. Não feche a janela do prompt

### "Página não carrega"
- **Soluções:**
  1. Verifique se digitou corretamente: `http://127.0.0.1:5000`
  2. Tente outro navegador
  3. Desative temporariamente o antivírus/firewall

### "Erro de dependências"
- **Solução:** Execute no prompt de comando:
  ```cmd
  pip install -r requirements.txt
  ```

---

## 🔧 Configuração avançada (Opcional)

### Criando um ambiente virtual
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Executando manualmente
```cmd
python app.py
```

---

## 📱 Dicas de uso

### Para melhores resultados:
- ✅ Use fotos com boa iluminação
- ✅ Foque apenas na folha
- ✅ Evite fotos borradas ou muito escuras
- ✅ Tire fotos de perto, mas sem cortar a folha

### Formatos de imagem aceitos:
- JPG / JPEG
- PNG
- Tamanho máximo recomendado: 5MB

---

## 🆘 Precisa de ajuda?

### Contatos dos desenvolvedores:
- **Katcilane Silva** - Especialista em IA
- **Kaue Ribeiro** - Especialista em Sistemas

### Coordenador do projeto:
- **Patrick Ola Bressan** - IFMS Campus Jardim

---

## 📄 Informações técnicas

### Requisitos mínimos do sistema:
- **Sistema:** Windows 7/8/10/11
- **RAM:** 4GB (recomendado: 8GB)
- **Espaço:** 2GB livres
- **Internet:** Necessária apenas para instalação

### Tecnologias utilizadas:
- Python 3.8+
- TensorFlow (Inteligência Artificial)
- Flask (Servidor web)
- HTML/CSS/JavaScript (Interface)

---

*© 2024 AgroIntelliVision - IFMS Campus Jardim*