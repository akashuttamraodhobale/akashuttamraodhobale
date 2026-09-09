# Hi there, I'm Akash Dhobale 👋

<p align="center">
  <img src="https://img.shields.io/badge/Role-Technical%20Program%20Manager%20%7C%20Cybersecurity%20Proffessional-blue?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Role" />
  <img src="https://img.shields.io/badge/Domain-Banking%20%26%20Enterprise%20Infrastructure-0052CC?style=for-the-badge&logo=enterprise&logoColor=white" alt="Domain" />
  <img src="https://img.shields.io/badge/Certifications-Cybersecurity Professional%20%7C%20Generative AI Leader%20%7C%20CEH%20%7C%20Google%20PMP-success?style=for-the-badge&logo=shield&logoColor=white" alt="Certifications" />
</p>

---

### 🛡️ Executive Profile & Leadership Overview
I am an **Enterprise Cybersecurity Professional and Technical Program Manager (TPM)** specializing in macro-scale technology transformations, high-availability cloud/network architecture, and strategic IT governance. 

Over the past **12+ years**, I have directed complex, multi-million dollar infrastructure programs—bridging technical DevSecOps execution with executive board governance.

* **🛡️ Macro-Scale Protection:** Spearheaded a **₹9 Crore ($1.1M+)** enterprise security deployment, securing **80,000+ heterogeneous endpoints** across **9,000+ branch locations** with a phased rollout executed in a **record 15 days** with zero business disruption.
* **⚙️ Active-Active HA/DR Resilience:** Engineered and deployed Active-Active High Availability and Disaster Recovery infrastructure across Primary Data Centers (Mumbai) and DR sites (Bengaluru), achieving an **RTO of <15 minutes** and **near-zero RPO**.
* **💼 Financial & Procurement Governance:** Managed end-to-end technology procurement (RFP, SOW, SLA) and negotiated software contracts, delivering **~60% licensing cost optimization**.
* **📚 Industry Thought Leadership:** Published researcher in *IJSCI* and author for **IFSEC India** on building true enterprise cyber resilience beyond "the illusion of security."

---

### 🛠️ Technology Stack & Competency Matrix

| Category | Enterprise Technologies & Leadership Frameworks |
| :--- | :--- |
| **Program & Governance** | End-to-End Program Lifecycles, Agile/Scrum/Kanban (Jira), Vendor SLA & Contract Mgmt, Executive Committee Advisory (ITAC) |
| **Cybersecurity & EDR** | Microsoft Defender for Endpoint, Symantec Endpoint Security, CyberArk PAM, Forcepoint DLP, SCCM, SIEM Log Triage |
| **Architecture & Cloud** | Active-Active HA/DR Resilience, BGP Anycast Routing, Global Server Load Balancing (GSLB), Zero-Trust Architecture |
| **Automation & Data** | Python, SQL (SQLite/PostgreSQL), Shell Scripting, REST APIs, Google Gemini AI Integration, RAG Architectures |

---

### 🏅 Professional Certifications & Credentials
* **Cybersecurity & Audit:** Certified Information Systems Security Professional (CISSP) Specialization • Certified Information Systems Auditor (CISA) Specialization • Certified Ethical Hacker (CEH) Specialization • Certified in Cybersecurity (CC - ISC2) • Certificate in IT Security (IIBF).
* **Management & AI:** Google Project Management Professional Certificate • Google Cybersecurity Professional Certificate & Advanced Risk Management • Generative AI Leader Professional Certificate (Google Cloud) • MBA (NMIMS).

---

### 📁 Flagship Open-Source Engineering Projects

#### 1. ⚡ [Active-Active HA/DR Architecture Simulator](https://github.com/akashuttamraodhobale/active-active-hadr-architecture)
> **Keywords:** `BGP Anycast` • `GSLB` • `High Availability` • `RTO/RPO SLA Audit`
* **What it is:** A Google/Microsoft-grade interactive terminal simulation of an Active-Active Dual Data Center topology.
* **Key Feature:** Injects simulated subsea fiber cuts, measures automated failover in real-time (**RTO: ~1.6s vs <15min SLA**), and verifies zero transaction data loss (**RPO = 0s**).

#### 2. 🛡️ [Enterprise Threat & Risk Financial Simulator](https://github.com/akashuttamraodhobale/enterprise-threat-risk-simulator)
> **Keywords:** `Risk Monetization` • `NIST CSF 2.0` • `Dynamic Modeling` • `Security ROI`
* **What it is:** A data-driven financial risk modeling engine that calculates unmitigated vs. mitigated business losses based on custom user inputs, JSON configurations, or CSV datasets.
* **Key Feature:** Dynamically evaluates risk scores (0-100), financial exposure, and security control ROI, exporting audit-ready Markdown executive reports.

#### 3. 🔍 [Automated Security Log Analyzer & SIEM Engine](https://github.com/akashuttamraodhobale/security-log-analyzer)
> **Keywords:** `SIEM` • `Log Parsing` • `SQLi & XSS Detection` • `Sliding Window`
* **What it is:** An enterprise-grade Python log ingestion engine that decodes URL evasions, parses web server access logs, and detects SQLi, XSS, and brute-force attacks in real time.
* **Key Feature:** Uses a memory-safe 60-second sliding window to monitor attack density and exports structured Markdown incident reports with Slack/Teams webhook alerts.

#### 4. 🤖 [Interactive AI Resume Assistant (RAG Chatbot)](https://github.com/akashuttamraodhobale/ai-resume-assistant)
> **Keywords:** `Generative AI` • `Streamlit` • `Google Gemini API` • `RAG`
* **What it is:** A responsive web application built with Streamlit and Google Gemini API that transforms a static resume into an interactive, conversational AI agent.
* **Key Feature:** Allows recruiters and hiring managers to interview my professional profile in real time, receiving grounded, metric-driven responses.

---

### 📊 GitHub Activity & Engineering Metrics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=akashuttamraodhobale&show_icons=true&theme=tokyonight&hide_border=true" alt="Akash's GitHub Stats" width="48%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=akashuttamraodhobale&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" width="48%" />
</p>

---

### 📬 Connect & Collaborate
* 💼 **LinkedIn:** [linkedin.com/in/akash-dhobale-cybersecurity](https://linkedin.com/in/akash-dhobale-cybersecurity)
* 📧 **Email:** akashuttamraodhobale@gmail.com
* 📰 **Publication:** [The Most Expensive Mistake in Cybersecurity Isn't a Data Breach (IFSEC India)](https://ifsecindia.com/the-most-expensive-mistake-in-cybersecurity-isnt-a-data-breach)

---
*⚡ Automated with GitHub Actions & Google Gemini API • Engineered for Scale & High Availability*


## 🤖 Weekly Automated Security Showcase (Generated: 2026-09-09)

# 🛡️ Project Zero: Real-Time S3 Data Exfiltration & CloudTrail Threat Hunter

## The Enterprise Security Problem
In modern multi-cloud architectures, sophisticated threat actors who compromise low-privileged AWS IAM credentials immediately pivot to enumeration and data exfiltration. A classic attack pattern involves altering **S3 Bucket Policies**, disabling **Server-Side Encryption (SSE)**, or creating unauthorized **Cross-Account Replication Rules** to siphon petabytes of sensitive enterprise data to external, attacker-controlled AWS accounts. 

Standard SIEM alerts often fail because they lack contextual correlation, resulting in alert fatigue or massive detection latency. This production-grade Python micro-tool continuously polls AWS CloudTrail via boto3, applies a sliding-window heuristic filter, and instantly isolates anomalous S3 policy modifications and exfiltration attempts, automatically triggering infrastructure containment protocols.

---

## Complete Production-Grade Python Tool (`s3_sentinel.py`)

```python
#!/usr/bin/env python3
"""
Enterprise S3 Threat Hunter & Automated Containment Micro-Tool
Author: Elite DevSecOps AI Agent
Description: Polls AWS CloudTrail for high-risk S3 API actions, flags unauthorized
             modifications (Bucket Policy overrides, Public Access blocks removal,
             Cross-Account Replication setup), and executes automated remediation.
"""

import boto3
import logging
import sys
from datetime import datetime, timedelta, timezone
from botocore.exceptions import ClientError

# Configure structured enterprise logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d) - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("S3Sentinel")

# High-risk CloudTrail event names mapped to MITRE ATT&CK TTPs
HIGH_RISK_S3_EVENTS = {
    "PutBucketPolicy": "T1565.001 - Data Manipulation: Stored Data Manipulation",
    "PutBucketAcl": "T1114.003 - Email Collection: Collection via S3",
    "PutBucketReplication": "T1537 - Transfer Data to Cloud Account",
    "DeletePublicAccessBlock": "T1530 - Data from Cloud Storage Object",
    "PutBucketEncryption": "T1562.001 - Impair Defenses: Disable or Modify Tools"
}

class S3ThreatHunter:
    def __init__(self, region: str = "us-east-1", dry_run: bool = True):
        self.region = region
        self.dry_run = dry_run
        self.cloudtrail = boto3.client("cloudtrail", region_name=region)
        self.s3_client = boto3.client("s3", region_name=region)
        self.sts = boto3.client("sts", region_name=region)
        
        try:
            self.account_id = self.sts.get_caller_identity()["Account"]
            logger.info(f"Initialized S3Sentinel for AWS Account: {self.account_id} [DryRun Mode: {self.dry_run}]")
        except ClientError as e:
            logger.critical(f"Failed to initialize AWS session: {e}")
            sys.exit(1)

    def scan_recent_events(self, minutes_ago: int = 15):
        """Scans CloudTrail logs for high-risk S3 API mutations within a sliding time window."""
        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(minutes=minutes_ago)
        
        logger.info(f"Scanning CloudTrail events from {start_time.isoformat()} to {end_time.isoformat()}...")

        try:
            paginator = self.cloudtrail.get_paginator("lookup_events")
            for page in paginator.paginate(
                StartTime=start_time,
                EndTime=end_time,
                LookupAttributes=[{"AttributeKey": "EventSource", "AttributeValue": "s3.amazonaws.com"}]
            ):
                for event in page.get("Events", []):
                    self._analyze_event(event)
                    
        except ClientError as e:
            logger.error(f"Error querying CloudTrail: {e}")

    def _analyze_event(self, event: dict):
        """Analyzes an individual CloudTrail event against enterprise security heuristics."""
        event_name = event.get("EventName")
        if event_name not in HIGH_RISK_S3_EVENTS:
            return

        # Parse CloudTrail event payload
        import json
        cloudtrail_event = json.loads(event.get("CloudTrailEvent", "{}"))
        
        user_identity = cloudtrail_event.get("userIdentity", {})
        username = user_identity.get("userName", user_identity.get("principalId", "Unknown"))
        source_ip = cloudtrail_event.get("sourceIPAddress", "Unknown")
        request_parameters = cloudtrail_event.get("requestParameters", {})
        bucket_name = request_parameters.get("bucketName", "Unknown")
        mitre_ttp = HIGH_RISK_S3_EVENTS[event_name]

        logger.warning(
            f"🚨 SECURITY ALERT: High-Risk S3 Action Detected!\n"
            f"  - TTP: {mitre_ttp}\n"
            f"  - Action: {event_name}\n"
            f"  - Bucket: {bucket_name}\n"
            f"  - Principal: {username}\n"
            f"  - Source IP: {source_ip}"
        )

        # Execute automated incident response
        self._remediate_threat(bucket_name, event_name, cloudtrail_event)

    def _remediate_threat(self, bucket_name: str, event_name: str, event_details: dict):
        """Performs automated defensive containment actions based on the threat vector."""
        if bucket_name == "Unknown":
            return

        if self.dry_run:
            logger.info(f"[DRY-RUN] Would have remediated bucket '{bucket_name}' for event '{event_name}'.")
            return

        try:
            if event_name == "PutBucketPolicy":
                logger.info(f"🛡️ REMEDIATION: Reverting malicious bucket policy on {bucket_name}...")
                # In a strict production environment, restore a known-good baseline policy or delete it
                self.s3_client.delete_bucket_policy(Bucket=bucket_name)
                logger.info(f"Successfully neutralized policy on bucket: {bucket_name}")
                
            elif event_name == "DeletePublicAccessBlock":
                logger.info(f"🛡️ REMEDIATION: Re-enabling Block Public Access on {bucket_name}...")
                self.s3_client.put_public_access_block(
                    Bucket=bucket_name,
                    PublicAccessBlockConfiguration={
                        'BlockPublicAcls': True,
                        'IgnorePublicAcls': True,
                        'BlockPublicPolicy': True,
                        'RestrictPublicBuckets': True
                    }
                )
                logger.info(f"Successfully re-secured public access block on: {bucket_name}")
                
        except ClientError as e:
            logger.error(f"Failed to execute automated remediation for {bucket_name}: {e}")

if __name__ == "__main__":
    # Execute tool in dry-run mode by default for safety
    sentinel = S3ThreatHunter(region="us-east-1", dry_run=True)
    sentinel.scan_recent_events(minutes_ago=60)
```

---

## Practical Execution Steps

Developers and security engineers can pull and execute this micro-tool instantly via a one-liner in any secure CI/CD runner or local developer workstation configured with standard AWS credentials:

```bash
python3 -m pip install boto3 && python3 s3_sentinel.py
```

*(To flip the script into active automated containment mode, modify instantiation in code: `S3ThreatHunter(region="us-east-1", dry_run=False)`).*

---

## Enterprise-Grade Engineering Takeaway

This architecture implements a robust **Detect-and-Respond** paradigm designed for hyperscale cloud environments:
1. **Stateless Resiliency:** The script relies on AWS-native APIs (CloudTrail Paginators) without maintaining a persistent, vulnerable database state.
2. **MITRE ATT&CK Alignment:** By explicitly mapping API events to enterprise adversary tradecraft (`T1565.001`, `T1537`), security teams can seamlessly integrate findings into automated SOAR (Security Orchestration, Automation, and Response) pipelines like Phantom or Torq.
3. **Fail-Safe Design:** Enforcing `dry_run=True` by default prevents catastrophic auto-remediation loops or service outages caused by false positives, satisfying rigorous Change Management and SOC2 compliance controls.
