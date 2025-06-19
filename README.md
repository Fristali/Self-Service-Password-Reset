# Self-Service Password Reset Portal

A modern Flask-based web portal for secure, self-service password resets for on-premises Active Directory (AD) users. Designed for both demonstration and production use, with clear separation between mock/demo and real AD integration.

---

## Features

- **User self-service password reset** (mock/demo by default; real AD optional)
- **Security questions** (3 per user, customizable)
- **Password policy enforcement** (length, complexity, etc.)
- **Account lockout** after multiple failed attempts (configurable, default: 3 attempts, 15 min lockout)
- **Audit logging** to JSON files (ELK-ready)
- **Bootstrap UI** for a clean, responsive user experience
- **Sample users** and data for easy testing
- **Pytest test suite** and GitHub Actions CI

---

## Demo/Mock vs. Production-Ready Modes

- **Demo/Mock Mode (default):**
  - All password resets are simulated; no changes are made to real AD accounts.
  - Uses local CSV and SQLite for user data and lockout tracking.
  - Safe for local testing, training, and demonstration.
  - See `scripts/reset_password.ps1` (stub) and sample logs in `elk/sample_logs/`.

- **Production-Ready AD Integration (optional):**
  - Run the app on a Windows Server joined to your domain.
  - Set up a service account with delegated rights to reset passwords and unlock accounts (never use Domain Admin).
  - Configure the app to call `scripts/real_ad_reset_password.ps1` for real password resets.
  - See the script and README section below for security and deployment notes.

---

## Setup Instructions

### Prerequisites
- Windows 10/11 or Server (for AD integration)
- Python 3.11+
- PowerShell 5.1+
- (Optional) ELK stack for log analysis

### Quickstart (Demo/Mock Mode)
1. Clone this repository.
2. Install Python dependencies:
   ```
   pip install -r app/requirements.txt
   ```
3. Run the Flask app:
   ```
   python -m flask --app app run
   ```
4. Open http://localhost:5000 in your browser.

### Testing
- Run all tests:
  ```
  pytest tests/
  ```

### ELK Integration (Optional)
- Use Filebeat and the provided `filebeat.yml` to ship logs in `elk/sample_logs/` to your ELK stack.
- Sample Kibana dashboards are included in `elk/kibana_export.ndjson`.

---

## Usage

1. Enter your username on the portal home page.
2. Answer your three security questions.
3. Enter and confirm your new password (must meet policy).
4. If successful, your password is reset (simulated in demo mode; real in AD mode if enabled).
5. All attempts are logged for auditing.

---

## Security Notes

- **No real secrets or certificates** are included in this repository.
- All demo data is local and for demonstration only.
- **Never run production scripts as Domain Admin.** Always use least-privilege service accounts.
- Protect credentials, scripts, and logs from unauthorized access.
- All actions are logged for auditing and compliance.
- Test thoroughly in a non-production environment before enabling real AD integration.

---

## Active Directory Integration (Optional)

By default, this portal runs in mock/demo mode for safe local testing. No real Active Directory changes are made.

To enable real Active Directory password resets:

1. **Run the app on a Windows server joined to your domain.**
2. **Create a service account** with delegated rights to reset passwords and unlock accounts for your user population. _Never use a Domain Admin account._
3. **Configure the app** to call the script at `/scripts/real_ad_reset_password.ps1` for password reset operations.
4. **Review and secure** the script and log files. Only authorized personnel should have access.

**Security Caveats:**
- Never run as Domain Admin. Always use least-privilege service accounts.
- Protect credentials, scripts, and logs from unauthorized access.
- Test thoroughly in a non-production environment before enabling in production.

The `/scripts/real_ad_reset_password.ps1` script is provided as a ready-to-use starting point for secure AD integration. Review and adapt it to your environment as needed.

---

## Project Structure

- `app/` – Flask app, templates, static files, config
- `infra/` – user data, lockout DB, DSC stub
- `scripts/` – PowerShell scripts (demo and production), Filebeat config
- `elk/` – sample logs, Kibana dashboards
- `docs/` – documentation, setup, architecture, issues, resume bullets, planned features
- `tests/` – pytest test suite
- `.github/workflows/` – CI pipeline

---

## Future Plans

- Azure MFA integration
- Email notifications for password changes
- User self-enrollment for security questions
- Admin dashboard for lockout management
- Enhanced reporting and analytics

---

## Credits

- Designed and implemented by Ali Aldhalimi.

---

## License

This project is for demonstration and educational use. No warranty is provided. Use at your own risk.
