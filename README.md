# Cyber Log Analysis Project

## Overview / Esittely
This project is a simple cybersecurity log analyzer that detects suspicious activity such as brute force login attempts, high traffic IPs, and endpoint scanning behavior.

It is designed as a lightweight SOC-style monitoring tool for learning and demonstration purposes.

## Project Structure / Projektin rakenne

```text
📁 cyber-log-analysis-python
│
├── data/
│   └── input_logs/ # Input log files
│
├── outputs/
│   └── report.xlsx  # Generated reports
│
├── src/
│   └── log_analyzer.py  # Analysis scripts
│
├── README.md
└── requirements.txt
```

## Features / Ominaisuudet

- Failed login detection
- Brute force attack detection
- Top IP analysis
- Endpoint activity monitoring
- Export report to Excel
## Usage / Käyttö
Run the analyzer ( log_analyzer.py) 
Output will be generated in: outputs/reports.xlsx
