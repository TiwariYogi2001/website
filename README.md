# Yogesh Tiwari — portfolio

Personal site: <https://tiwariyogi2001.github.io/website/>

A static site — plain HTML, CSS and JavaScript, hosted on GitHub Pages. No framework, no build tools beyond Python.

## Editing content

All copy lives in **`build.py`**: projects, experience, skills, certifications, contact details. Edit it, then regenerate the pages:

```bash
python build.py
```

That rewrites every `.html` file (including `work/*.html`), `sitemap.xml` and `robots.txt`. Don't edit the `.html` files directly — the next build overwrites them.

Design lives in `assets/css/style.css`; behaviour (menu, filters, lightbox, SQL highlighting, contact form) in `assets/js/main.js`.

## Preview locally

```bash
python -m http.server 5174
```

Then open <http://localhost:5174>.

## Adding a project

Add an entry to the `PROJECTS` list in `build.py`. Each one becomes its own case-study page at `work/<slug>.html` and a card on `work.html`. The `thumb` field takes one of:

- `{"type": "img", "src": "assets/img/projects/name.webp", "w": 1280, "h": 720}` — a dashboard screenshot
- `{"type": "code", "lines": ["SELECT …", "FROM …"]}` — a few lines of SQL
- `{"type": "funnel"}` or `{"type": "glyph", "label": "VR"}` — decorative

Dashboard screenshots go in `assets/img/projects/` as WebP, ~1280px wide.

## Deploying

Push to `main` — GitHub Pages serves the repo root. `deploy.bat` builds, commits and pushes in one step.

## Contact form

Uses EmailJS (service, template and public key are in `assets/js/main.js`). Manage it at <https://www.emailjs.com>.
