# Erick James Sibayan | Portfolio

A responsive, two-page portfolio presenting work in data analysis, ecommerce, product engineering, and automation. The site is implemented with static HTML, CSS, and JavaScript and has no build step or package dependencies.

## Technical Overview

- **Markup:** semantic HTML5 for page structure, navigation, forms, and content.
- **Styling:** CSS custom properties, Grid and Flexbox layouts, responsive media queries, transitions, and reduced-motion handling.
- **Client-side behavior:** vanilla JavaScript for navigation, modal controls, card previews, pointer interactions, and scroll-triggered reveals.
- **Browser APIs:** Canvas 2D and `requestAnimationFrame` for animated line backgrounds; `IntersectionObserver` for reveal effects; `ResizeObserver` for canvas sizing; the View Transition API for progressive cross-page transitions.
- **3D rendering:** Three.js renders the EJS lettering on the home page.

## Pages

- `index.html` - hero, animated background, navigation menu, and contact modal.
- `projects.html` - project cards, experience timeline, services, and skills.

Project and service cards open an in-page preview panel. The preview provides a path to the related GitHub destination where available. Cross-page transitions use the View Transition API when supported; ordinary link navigation remains the fallback.

## Run Locally

Python 3 can serve the static files over HTTP. From the project directory, run this in PowerShell:

```powershell
py -m http.server 8000
```

Open [http://localhost:8000/index.html](http://localhost:8000/index.html). Using a local server is recommended over opening the HTML files with `file://`.

## External Resources

The site loads Google Fonts and Three.js from CDNs, so an internet connection is needed for those resources. The home page also loads its 3D font from the Three.js examples CDN.

## Contact Form Configuration

The contact form submits using `fetch` to Formspree. Its current endpoint contains the placeholder `MY_FORM_ID`, so submissions will not work until it is replaced with the form ID from a configured Formspree form in `index.html`.

## Updating the Site

- Edit the hero text, navigation, and contact form in `index.html`.
- Edit project cards, experience entries, services, and skills in `projects.html`.
- Update social and resume destinations in the relevant page links.
- Adjust design tokens, responsive layouts, and motion in each page's embedded CSS.

## Project Files

```text
index.html       Home page
projects.html    Projects, experience, services, and skills
profile.jpg      Portrait image
Resume.pdf       Resume document
README.md        Project documentation
```
