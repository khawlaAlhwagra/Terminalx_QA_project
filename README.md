# Terminalx_QA_project
 
## Overview
This repository contains UI automation tests for the TerminalX website.
 
## Tech Stack
- **Python**
- **Selenium WebDriver**
- **webdriver-manager** (auto-downloads the matching ChromeDriver)
- **unittest** (tests are written as `unittest.TestCase`)
- **pytest** (optional runner; convenient for discovery/output)
 
## Project Structure
- **`infra/`**
  - `browser_wrapper.py`: creates a Chrome WebDriver instance and navigates to a given URL.
  - `base_page.py`: a small base page object.
- **`logic/`**
  - Page Objects / flows used by the tests (login, signup, product page actions, etc.).
- **`test/`**
  - Test cases (e.g. login, add to cart, favorites, signup).
 
## Prerequisites
- **Python 3.10+** recommended
- **Google Chrome** installed
- Internet access (TerminalX is a live website; tests depend on network and site availability)
 
## Setup
Create and activate a virtual environment:
 
```bash
python3 -m venv .venv
source .venv/bin/activate
```
 
Install dependencies:
 
```bash
pip install -U pip
pip install selenium webdriver-manager pytest
```
 
## Running the Tests
From the repository root:
 
### Option A: Run with pytest (recommended)
```bash
pytest -q
```
 
Run a single test file:
```bash
pytest -q test/test_logo_terminalx.py
```
 
### Option B: Run with unittest
```bash
python -m unittest discover -s test -p "test_*.py"
```
 
## Notes / Known Caveats
- Some tests include `time.sleep(...)` and depend on UI timing; they may be flaky on slow networks.
- Some flows may require a valid account.
- If credentials are used in a test file, avoid committing real credentials to git.
 
## Troubleshooting
- **ChromeDriver issues**
  - `webdriver-manager` downloads drivers automatically. If it fails, ensure Chrome is installed and up to date.
- **Tests fail intermittently**
  - Prefer explicit waits (`WebDriverWait`) over `sleep` where possible.
- **Windows users**
  - Activate venv with: `.venv\\Scripts\\activate`
