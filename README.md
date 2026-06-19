# EduTrack — School Management System

> 🎓 A beautiful, lightweight school management system built with Python & Streamlit.

EduTrack lets you register students and teachers, assign and track grades, and view detailed profiles through a clean, responsive Streamlit UI. Data is persisted locally using JSON files so the app is easy to run, inspect, and back up.

---

## Table of contents

- [Features](#features)
- [Demo / Quickstart](#demo--quickstart)
- [Installation](#installation)
- [Usage](#usage)
- [Data storage](#data-storage)
- [Configuration](#configuration)
- [Development](#development)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

---

## Features

- Register, edit, and view student profiles
- Register, edit, and view teacher profiles
- Assign, edit, and view grades per student
- Search and filter records in the UI
- Local JSON-based storage for portability and manual inspection
- Built with Streamlit for fast iteration and an interactive web UI

---

## Demo / Quickstart

Run the app locally in a few minutes:

1. Clone the repository

   git clone https://github.com/CodeXRudy/School-Management-Project.git
   cd School-Management-Project

2. (Optional) Create and activate a virtual environment

   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .\.venv\Scripts\activate  # Windows (PowerShell)

3. Install dependencies

   pip install -r requirements.txt

4. Run the Streamlit app

   streamlit run app.py

Open http://localhost:8501 in your browser (Streamlit usually opens it automatically).

Note: Replace `app.py` above with the actual entrypoint filename if it's different.

---

## Installation

Prerequisites

- Python 3.8 or newer
- pip

If there is no requirements.txt, the main dependency is Streamlit — install it with:

   pip install streamlit

Add any other dependencies listed in the repository.

---

## Usage

- Use the web UI to add students and teachers, and to assign grades.
- Export/import capabilities may be present in the UI (or available as a future enhancement).
- Data is stored in JSON files in the project (see [Data storage](#data-storage)).

If the UI file names or routes differ, consult the project files for the exact Streamlit script name.

---

## Data storage

EduTrack uses JSON files stored locally (commonly in a `data/` directory) to persist:

- students.json — student records
- teachers.json — teacher records
- grades.json — grades and assignments

Behavior

- If JSON files are missing, the app typically creates them when saving the first record.
- Back up these files if you want to preserve data before code changes.
- The format is plain JSON; you can edit it manually but be careful to keep valid JSON structure.

---

## Configuration

- Streamlit configuration (port, browser, server settings) can be provided via the Streamlit CLI or `~/.streamlit/config.toml`.
- Environment variables may be used by the app for toggles (inspect the code to find any `os.environ` usage).

---

## Development

- The codebase is Python-first and Streamlit-driven. Run the app locally and make UI changes in the Streamlit script(s).
- When adding dependencies, add them to `requirements.txt`.
- Keep JSON schema changes backwards compatible where possible (add new fields with defaults).

Suggested git workflow

1. Create a feature branch: `git checkout -b feat/your-feature`
2. Make changes and test locally: `streamlit run app.py`
3. Commit and push: `git push origin feat/your-feature`
4. Open a pull request with a clear description and testing steps

---

## Contributing

Contributions are welcome — open an issue to discuss significant changes first.

When submitting a pull request, include:

- A clear title and description of changes
- Screenshots or brief notes if the UI changed
- Steps to reproduce and test the changes

Small fixes can be sent as direct PRs. For larger features, open an issue first to align on design.

---

## Troubleshooting

- Streamlit not starting: ensure Python version and dependencies are correct.
- JSON read/write errors: check file permissions and ensure the `data/` directory exists and is writable.
- Port conflicts: run Streamlit with `--server.port <port>` to change the port.

---

## Roadmap / Ideas

- Import/export (CSV / Excel)
- Optional SQLite or remote backend for larger deployments
- Simple role-based auth for teacher/admin access
- Unit tests for core data-handling logic

---

## License

Add a LICENSE file to this repository to document the project's license. If no license is present, contact the maintainer for permission before using the code in other projects.

---

## Contact

Maintainer: CodeXRudy

Repository: https://github.com/CodeXRudy/School-Management-Project

Feel free to open issues or pull requests.
