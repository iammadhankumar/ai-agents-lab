import requests
import sys
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"
PROMPT_DIR = "prompts"
PROMPT_FILE = "md_blog_prompt.jinja"


def load_prompt(template_name: str, context: dict) -> str:
    """
    Load and render a Jinja2 prompt template with the given context.
    """
    try:
        env = Environment(loader=FileSystemLoader(PROMPT_DIR))
        template = env.get_template(template_name)
        return template.render(context)
    except TemplateNotFound:
        raise FileNotFoundError(f"Prompt file '{template_name}' not found in '{PROMPT_DIR}/'.")
    except Exception as e:
        raise RuntimeError(f"Failed to load or render prompt: {e}")


def generate_blog_content(prompt: str, model: str = MODEL_NAME) -> str:
    """
    Send the prompt to Ollama and return the generated response.
    """
    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Connection error with Ollama: {e}")
    except KeyError:
        raise RuntimeError("Unexpected response format from Ollama.")


def save_markdown_file(content: str, topic: str):
    """
    Save generated blog content to a markdown file with a clean filename.
    """
    safe_topic = "".join(c for c in topic if c.isalnum() or c in (" ", "-", "_")).strip()
    slug = safe_topic.replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{slug}_{timestamp}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Blog saved successfully to: {filename}")


def main():
    """
    Main script entry point.
    """
    try:
        topic = input("📘 Enter a blog topic: ").strip()
        if not topic:
            print("❌ Error: Topic cannot be empty.")
            sys.exit(1)

        print("⏳ Preparing prompt...")
        prompt = load_prompt(PROMPT_FILE, {"topic": topic})

        print("🤖 Generating content using Ollama...\n")
        content = generate_blog_content(prompt)

        save_markdown_file(content, topic)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
