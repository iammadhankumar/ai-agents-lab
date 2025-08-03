# 🧠 LLM Environment Setup: Ollama
This guide explains how to install and run large language models locally using [Ollama](https://ollama.com/).

Ollama allows you to run open-source models like `mistral`, `llama3`, and `gemma` entirely on your system.

## ⚙️ Requirements

- ✅ macOS, Linux, or Windows (WSL 2)
- ✅ 8 GB+ RAM (16 GB recommended for larger models)
- ✅ Python (for integration tools)
- ✅ Internet (only for model download)

## 🛠️ Step-by-Step Setup
### 1. Install Ollama

Choose your OS and follow instructions:
- **macOS**  
  ```bash
  brew install ollama
  ```
- **Linux** 
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
- **Windows**
Download and install from: https://ollama.com/download.
On Windows, Ollama runs inside WSL2 (automatically handled during setup).

### 2. Start Ollama
Start the Ollama server in your terminal:
```bash
ollama serve
```
💡 You can also run this in the background or as a service.

### 3. Pull a Model
Download the base model you want to use. For example:
```bash
ollama pull mistral
```

| Model   | Command               | Use Case                   |
| ------- | --------------------- | -------------------------- |
| Mistral | `ollama pull mistral` | Fast, general-purpose      |
| LLaMA 3 | `ollama pull llama3`  | Meta's open LLM            |
| Gemma   | `ollama pull gemma`   | Google’s open-source model |
| Phi-3   | `ollama pull phi3`    | Lightweight & fast         |

🧠 All models run locally. No cloud calls.

### 4. Run a Model
To start an interactive session:
```bash
ollama run mistral
```
### 5. Test API Access
Ollama exposes a local API at:
```ardunio
http://localhost:11434
```
Test it with a simple curl command:
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "mistral",
  "prompt": "Explain what transformers are in AI.",
  "stream": false
}'
```
If you get a proper response, you're good to go!

`
