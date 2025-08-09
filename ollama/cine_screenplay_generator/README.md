# Screenplay Genie

**AI-powered offline screenplay generator using Ollama**  
_Output: Markdown format only._

Screenplay Genie is a small CLI tool that renders Jinja prompt templates and runs a local Ollama model to generate feature-length, three-act screenplays in Markdown. It’s designed for offline usage (no cloud API required) and integrates cleanly into writer workflows and automated pipelines.

---

## Features

- Render Jinja templates for repeatable, production-grade prompts  
- Run local Ollama models (e.g., `mistral`) to generate screenplay drafts  
- Output is saved as a Markdown (`.md`) screenplay file ready to version or edit  
- Minimal, scriptable CLI suitable for batch runs or integration in CI

---

## Requirements
**Ollama:**
Make sure ollama is installed and the model you will use is available.

**Python 3.8+**
- [Ollama](https://ollama.com/) installed and accessible in `PATH` (local model runner)
- At least one Ollama model installed (default: `mistral`)
- `jinja2` Python package

**Install dependencies:** (Install the dependencies below if not already installed)
```bash
pip install jinja2
```
---
**Usage:**
Run the script and follow interactive prompts:
```bash
python cineprompt.py
```
Simple interactive flow:
```bash
🎬 Welcome to CinePrompt - AI Screenplay Generator (Markdown only)

💡 Enter your story idea:               (e.g., An exiled detective must stop a city-wide blackout)
🎭 Enter the style (e.g., Tarantino, Nolan) [default: standard]: Nolan
📄 Prompt template file [default: screenplay_prompt.jinja]: screenplay_prompt.jinja
📝 Enter output filename (without extension): my_screenplay( give whatever name you want)
```
After generation the script prints a preview and saves the full screenplay to current location.

---

                         Happy Learning


