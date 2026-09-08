import os
import sys
import json
import urllib.request
import urllib.error
import time
from datetime import datetime

def main():
    # 1. Verify API Key is Present
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY environment variable is not set.")
        print("[INFO] Please add GEMINI_API_KEY as an Actions Secret in your GitHub Repo settings.")
        sys.exit(1)

    # 2. Craft a Strategic, High-Impact Engineering Prompt
    prompt = (
        "You are an expert, elite DevSecOps and Cybersecurity AI agent. Your mission is to write a highly innovative, "
        "practical, and production-ready cybersecurity micro-tool or security automation script (written in Python, Bash, or SQL), "
        "OR a modern, highly technical cloud infrastructure security blueprint/threat audit checklist (e.g., AWS/GCP IAM hardening, "
        "Kubernetes configuration auditing, or secure CI/CD pipeline automation).\n\n"
        "Format your entire response in beautiful, clean Markdown. Do NOT wrap your entire response in a single global code block, "
        "only the code blocks themselves. The content must include:\n"
        "1. A professional, catchy title (e.g., '🛡️ Week X: Automated Kubernetes RBAC Privilege Auditor').\n"
        "2. The Enterprise Security Problem (the exact operational or regulatory threat this solves).\n"
        "3. The complete, production-grade, and beautifully commented code snippet or audit matrix.\n"
        "4. Practical Execution Steps (how a developer runs it in 1 line).\n"
        "5. An Enterprise-Grade Engineering takeaway (why this architecture is resilient and secure).\n\n"
        "Make it unique, highly advanced, and directly designed to impress senior recruiters at top-tier companies like Google or Amazon."
    )

    # 3. Model Cascade List (High-Availability Fallback Strategy)
    # If the brand-new gemini-3.8-flash is experiencing high load or 503 errors, 
    # the script will automatically roll back to other stable endpoints.
    models_to_try = [
        "gemini-3.8-flash",      # Flagship 2026 Model (First Choice)
        "gemini-3.5-flash-lite", # Efficient Gemini 3 Series Fallback
        "gemini-2.5-flash",      # Reliable Gemini 2.5 Series Fallback
        "gemini-flash-latest"    # Google's Dynamic Redirection Alias
    ]

    generated_text = None

    for model in models_to_try:
        print(f"[*] Attempting to contact Google Gemini API using model: {model}...")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        # Retry logic: Retry up to 3 times with exponential backoff for transient errors (e.g., 503)
        retries = 3
        backoff_delay = 2

        for attempt in range(1, retries + 1):
            req = urllib.request.Request(
                url, 
                data=json.dumps(payload).encode("utf-8"), 
                headers=headers, 
                method="POST"
            )

            try:
                with urllib.request.urlopen(req) as response:
                    res_data = json.loads(response.read().decode("utf-8"))
                    generated_text = res_data['candidates'][0]['content']['parts'][0]['text']
                    break # Success! Break out of retry loop
            except urllib.error.HTTPError as e:
                # If it's a transient server error (500, 502, 503, 504), wait and retry
                if e.code in [500, 502, 503, 504]:
                    print(f"    [!] HTTP Error {e.code} (Service Unavailable/Server Error) on attempt {attempt}/{retries}.")
                    if attempt < retries:
                        print(f"    [*] Waiting {backoff_delay} seconds before retrying...")
                        time.sleep(backoff_delay)
                        backoff_delay *= 2 # Double the wait time
                    else:
                        print(f"    [!] All retries exhausted for model '{model}'.")
                else:
                    # If it's a 404 or 400, retrying won't help. Move directly to next model.
                    print(f"    [!] HTTP Error {e.code} on model '{model}'. Skipping to fallback models.")
                    break
            except Exception as e:
                print(f"    [!] Unexpected error: {e}")
                break

        if generated_text:
            print(f"[SUCCESS] Successfully retrieved content using model: {model}!")
            break
        else:
            print(f"[-] Model '{model}' failed or was unavailable. Moving to next fallback...")

    if not generated_text:
        print("[CRITICAL ERROR] All models and retries failed. Google Gemini API is completely unreachable at this moment.")
        sys.exit(1)

    # 4. Read and Update README.md with Sliding Window Injection
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("[!] README.md not found. Generating a basic structure...")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("# Security Engineering Portfolio\n\n<!-- WEEKLY-UPDATE-START -->\n<!-- WEEKLY-UPDATE-END -->\n")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- WEEKLY-UPDATE-START -->"
    end_marker = "<!-- WEEKLY-UPDATE-END -->"

    if start_marker in content and end_marker in content:
        print("[*] Found placeholders. Injecting new automated security showcase...")
        before = content.split(start_marker)[0] + start_marker
        after = end_marker + content.split(end_marker)[1]
        
        injection = f"\n### 🤖 Weekly Automated Security Showcase (Generated: {datetime.now().strftime('%Y-%m-%d')})\n\n{generated_text}\n"
        new_content = before + injection + after
    else:
        print("[!] Placeholders not found. Appending to the end of README.md...")
        new_content = content + f"\n\n## 🤖 Weekly Automated Security Showcase (Generated: {datetime.now().strftime('%Y-%m-%d')})\n\n{generated_text}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("[SUCCESS] README.md successfully updated with this week's custom security showcase!")

if __name__ == "__main__":
    main()
