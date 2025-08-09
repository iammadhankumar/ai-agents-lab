"""CinePrompt - AI-powered offline screenplay generator using Ollama. Output: Markdown format only."""

import os
import subprocess
import sys
import logging
from typing import Dict
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_prompt(template_name: str, context: Dict[str, str]) -> str:
    """Loads and renders a Jinja2 prompt with the given context."""
    prompt_dir = os.path.join(os.path.dirname(__file__), "prompt")
    env = Environment(loader=FileSystemLoader(prompt_dir))
    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        raise FileNotFoundError(f"❌ Prompt template '{template_name}' not found in 'prompt/' folder.")
    return template.render(context)

def generate_screenplay(prompt_text: str, model: str = "mistral") -> str:
    """Runs the Ollama model with the prompt text and returns the generated screenplay."""
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt_text.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"❌ Ollama execution failed:\n{e.stderr.decode('utf-8')}")

def ask_questions() -> Dict[str, str]:
    """Prompts the user for input values: idea, style, template, and output file."""
    print("\n🎬 Welcome to CinePrompt - AI Screenplay Generator (Markdown only)\n")

    idea = input("💡 Enter your story idea: ").strip()
    if not idea:
        logging.error("Story idea is required. Exiting.")
        sys.exit(1)

    style = input("🎭 Enter the style (e.g., Tarantino, Nolan) [default: standard]: ").strip() or "standard"
    template = input("📄 Prompt template file [default: screenplay_prompt.jinja]: ").strip() or "screenplay_prompt.jinja"
    output_file = input("📝 Enter output filename (without extension): ").strip()

    if not output_file:
        logging.error("Output filename is required. Exiting.")
        sys.exit(1)

    return {
        "idea": idea,
        "style": style,
        "template": template,
        "model": "mistral",
        "output_file": output_file + ".md",
    }

def save_markdown(content: str, filepath: str) -> None:
    """Saves the screenplay content to a markdown (.md) file."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"✅ Screenplay saved to '{filepath}'")
    except Exception as e:
        logging.error(f"❌ Failed to save file: {e}")

def main() -> None:
    """Main program flow: collects inputs, generates screenplay, saves output as Markdown."""
    try:
        user_input = ask_questions()

        context = {
            "idea": user_input["idea"],
            "style": user_input["style"],
        }

        prompt_text = load_prompt(user_input["template"], context)
        screenplay_output = generate_screenplay(prompt_text, model=user_input["model"])

        print("\n🎥 Generated Screenplay (Markdown Preview):\n")
        print(screenplay_output[:1000], "...\n")

        save_markdown(screenplay_output, user_input["output_file"])

    except (FileNotFoundError, RuntimeError) as err:
        logging.error(err)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n❗ Interrupted by user. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
