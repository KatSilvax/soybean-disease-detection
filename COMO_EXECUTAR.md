# Como Executar o AgroIntelliVision

> 📋 **Para usuários iniciantes:** Consulte o [Guia de Instalação Completo](GUIA_INSTALACAO.md)

## 🚀 Execução Rápida

### Windows
```cmd
run.bat
```

### Linux/macOS
```bash
chmod +x run.sh && ./run.sh
```

## 🔧 Execução Manual

1. **Ativar ambiente virtual:**
   ```cmd
   # Windows
   venv_new\Scripts\activate
   
   # Linux/macOS
   source venv_new/bin/activate
   ```

2. **Instalar dependências:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Executar servidor:**
   ```cmd
   python app.py
   ```

4. **Acessar aplicação:**
   - Navegador: `http://127.0.0.1:5000`

## ✅ Verificações

- ✅ Python 3.8+ instalado
- ✅ Modelo: `models/saved_models/modelo_soja.h5`
- ✅ Dependências: `requirements.txt`
- ✅ Interface: `index.html`

## ⚠️ Solução de Problemas

| Problema | Solução |
|----------|----------|
| Python não encontrado | Instalar Python 3.8+ |
| Modelo não encontrado | Verificar `models/saved_models/modelo_soja.h5` |
| Erro de dependências | `pip install -r requirements.txt` |
| Página não carrega | Verificar se servidor está rodando |

---

*Para instruções detalhadas, consulte o [Guia de Instalação Completo](GUIA_INSTALACAO.md)*