import os
import sys
import json
import urllib.request
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

    # 3. Call the Google Gemini API using Native urllib (zero dependency, lightning fast)
    # LATEST 2026 MODEL: Switched to Google's newly released GA model: gemini-3.8-flash (Released Sept 2, 2026)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    print("[*] Contacting Google Gemini API for this week's technical showcase (using gemini-3.8-flash)...")
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
    except Exception as e:
        print(f"[ERROR] Failed to query Gemini API: {e}")
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
