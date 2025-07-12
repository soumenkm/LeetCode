

import os
import sys
import google.generativeai as genai
from pathlib import Path
os.environ["GOOGLE_API_KEY"] = "AIzaSyB1hEv88gKks5OhnV2rkjagg7vvod-kWzI"


# --- Configuration ---
# The script assumes it is located in the parent directory of 'LeetCode'
# e.g., /path/to/your/repo/run_script.py
#       /path/to/your/repo/LeetCode/
SCRIPT_DIR = Path(__file__).parent.resolve()
LEETCODE_ROOT_DIR = SCRIPT_DIR / "LeetCode"

# --- Main Logic ---

def generate_explanation(code_content: str, readme_content: str) -> tuple[str, str]:
    """
    Constructs a prompt and uses the Gemini API to generate a code explanation.

    Args:
        code_content: The Python code from the solution file.
        readme_content: The content of the README.md (problem statement).

    Returns:
        A tuple containing (prompt_text, explanation_text).
        Returns an empty tuple ("", "") on error.
    """
    # Configure the Gemini API key.
    try:
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            print("\nERROR: The 'GOOGLE_API_KEY' environment variable is not set.")
            sys.exit(1)
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring Gemini: {e}")
        return "", ""

    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    # This is the prompt template that will be sent to the AI
    prompt_template = f"""
You are an expert programming coach specializing in LeetCode solutions. Your task is to analyze the following Python code submission and generate a detailed explanation in Markdown format.

Use the provided "Problem Statement" to understand the problem statement, but base your final code analysis strictly on the provided "User's Code".

VERY IMPORTANT: Your entire analysis must be based *strictly* on the provided code. Explain the user's specific logic, their variable names, and their coding style. Do not suggest your own code or alternative implementations.

Please structure your explanation using the following Markdown headers:

### Code Explanation

#### Key Concepts
Identify the main algorithms or coding patterns or data structures used (e.g., Dijkstra's Algorithm, Two Pointers, Dynamic Programming, BFS etc.).

#### Identification of Algorithm
Explain the intuition or logic or pattern behind thinking a particular algorithm or data structure for this problem. For example, if the problem demands to find minimum path in a graph then it is a sign that BFS can be used instead of DFS.

#### Intuition and Logic
Explain the core idea behind the user's approach. Why does their solution work? Walk through the logic step-by-step, referencing their variable names (e.g., `adjList`, `Q`, `dist` etc.).

#### "Gotcha" Points and Tricks
Highlight any clever tricks, non-obvious steps, or common pitfalls that the user's code successfully handles. For example, handling edge cases, or the specific way they handle state.

#### Potential Errors and Pitfalls
Based on the provided code, where might a developer commonly make a mistake? For example, off-by-one errors, forgetting to handle a specific case, or misunderstanding a data structure's behavior.

---
**Problem Statment:**
```markdown
{readme_content}
```
---
**User's Code (for analysis):**
```python
{code_content}
```
"""

    # try:
    #     print("   Generating explanation with Gemini...")
    #     response = model.generate_content(prompt_template)
    #     # Return both the prompt and the generated text
    #     return prompt_template, response.text
    # except Exception as e:
    #     print(f"   An error occurred while calling the Gemini API: {e}")
    #     return prompt_template, ""
    return prompt_template, ""

def process_solution_file(solution_path: Path):
    """
    Processes a single LeetCode solution file. It generates a prompt and a
    solution explanation, saving them into the problem's directory.
    It will skip directories that already contain 'prompt.md' and 'solution.md'.

    Args:
        solution_path: A pathlib.Path object pointing to the solution .py file.
    """
    folder_path = solution_path.parent
    readme_path = folder_path / "README.md"
    prompt_output_path = folder_path / "prompt.md"
    solution_output_path = folder_path / "solution.md"

    print(f"\nProcessing: {folder_path.relative_to(LEETCODE_ROOT_DIR.parent)}")

    # --- New Idempotency Check ---
    # If both files already exist, skip this folder entirely.
    if solution_output_path.exists():
        print("   'solution.md' already exist. Skipping.")
        return

    # Ensure the problem statement (README.md) exists
    if not readme_path.exists():
        print(f"   'README.md' not found in {folder_path.name}. Skipping.")
        return

    try:
        readme_content = readme_path.read_text(encoding='utf-8')
    except IOError as e:
        print(f"   Could not read README.md: {e}. Skipping.")
        return

    try:
        code_content = solution_path.read_text(encoding='utf-8')
    except IOError as e:
        print(f"   Could not read solution file '{solution_path.name}': {e}. Skipping.")
        return

    if not code_content.strip():
        print(f"   Solution file '{solution_path.name}' is empty. Skipping.")
        return

    # Get the prompt and the explanation from the AI model
    prompt_text, explanation_text = generate_explanation(code_content, readme_content)

    # If the generation was successful, write the new files
    if prompt_text:
        try:
            text = prompt_text + "\n\n---\n\n" + explanation_text
            # prompt_output_path.write_text(prompt_text, encoding='utf-8')
            solution_output_path.write_text(text, encoding='utf-8')
            print(f"   Successfully created 'prompt.md' and 'solution.md' in {folder_path.name}")
        except IOError as e:
             print(f"   Could not write output files: {e}")

def main():
    """Main function to run the documentation process."""
    print(f"Script starting in: {SCRIPT_DIR}")
    print(f"Scanning target directory: {LEETCODE_ROOT_DIR}\n")

    # Sanity check: Ensure the target LeetCode directory exists.
    if not LEETCODE_ROOT_DIR.is_dir():
        print(f"FATAL: The target directory '{LEETCODE_ROOT_DIR}' was not found.")
        print("Please make sure this script is in the correct location and the")
        print("'LeetCode' sub-directory exists.")
        return

    # Find all Python solution files within the LeetCode directory structure.
    solution_files = sorted(list(LEETCODE_ROOT_DIR.rglob("*.py")))

    if not solution_files:
        print("No Python solution files (.py) were found to process. Exiting.")
        return

    for solution_file in solution_files:
        # Exclude common non-solution files like '__init__.py'
        if solution_file.name.startswith('__'):
            continue
        process_solution_file(solution_file)

    print("\n-------------------------------------")
    print("Documentation process complete!")
    print("Check the 'prompt.md' and 'solution.md' files inside each problem folder.")
    print("-------------------------------------")

if __name__ == "__main__":
    main()
