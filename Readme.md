# Instructions to setup environment
- Initialize a virtual environment via:
- Conda:
```bash
conda create --name rag-bot python=3.10
```
- virtualenv
```bash
virtualenv -p python3.10 rasaenv
```
- Install langchain-community and other dependencies
```bash
pip install -r requirements.txt
```
- Install Rasa
```bash
pip install uv
uv pip install rasa
```

## 🧪 Testing
- Pull Qwen2.5 model from ollama(make sure you have ollama application)
```bash
ollama pull qwen2.5
```
- Train RAG model
```bash
python .\rag\populate_db.py 
```
- Train bot
```
rasa train
```
- start `rasa` server
```bash
rasa run --enable-api --cors "*" --debug[Optional] -p {PORT}[optional]
```
- start `actions` server
```
rasa run actions
```