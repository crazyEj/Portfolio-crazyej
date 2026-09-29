# Erick James Sibayan Portfolio

A static, two-page portfolio focused on data analysis, ecommerce, product engineering, and automation. Built with HTML, CSS, and JavaScript; no framework or package installation is required.

## Pages

- `index.html` - home page with the hero, animated background, navigation, and contact modal.
- `projects.html` - project previews, experience timeline, and services and skills.

## Features

- Responsive layouts for desktop and mobile.
- Native cross-page fade transitions in browsers that support the View Transition API; navigation still works in other browsers.
- Project and service cards with an interactive preview panel.
- Experience timeline and profile portrait (`profile.jpg`).
- Three.js and Google Fonts are loaded from CDNs, so those visual assets require an internet connection.

## Run locally

From the portfolio folder, start a local server in PowerShell:

```powershell
py -m http.server 8000
```

Then open [http://localhost:8000/index.html](http://localhost:8000/index.html) in your browser. Serving the files over HTTP is recommended over opening them directly, especially for external scripts and page transitions.

## Contact form setup

The home page form posts to Formspree, but its endpoint currently contains the placeholder `MY_FORM_ID`. Replace it with your Formspree form ID in `index.html` before expecting submissions to work.

## Customize

Edit the HTML files directly:

- Hero copy, navigation, and contact form in `index.html`.
- Project cards, experience entries, services, and skills in `projects.html`.
- Colors, spacing, and motion in the embedded CSS in each page.
- Social and resume links in the navigation and footer.

## Files

```text
index.html
projects.html
profile.jpg
Resume.pdf
README.md
```
