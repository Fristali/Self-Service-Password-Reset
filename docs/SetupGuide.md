# Setup Guide

## Prerequisites

- Windows 10/11
- Python 3.11
- PowerShell 5.1+
- (Optional) ELK stack for log analysis

## Steps

1. Clone the repo.
2. Install Python dependencies:
   ```
   pip install -r app/requirements.txt
   ```
3. Run the Flask app:
   ```
   python -m flask --app app run
   ```
4. Browse to http://localhost:5000

5. (Optional) To simulate password reset, see `scripts/reset_password.ps1`.

6. (Optional) To test ELK logs, run Filebeat with `scripts/filebeat.yml`.

## Notes

- No real AD integration or secrets in this demo.
- All data is local and for demonstration only.
