# Portfolio

Personal portfolio for Erick James Sibayan, focused on data analysis, ecommerce, product engineering, and automation.

## Pages

- `Index.html` - landing page with the hero section, animated background, navigation menu, and contact modal.
- `projects.html` - project highlights, experience timeline, services, skills, and work details.

This portfolio is built with plain HTML, CSS, and JavaScript. It does not require a framework or package install.

## Current features

- Full-screen menu overlay with hover scaling effects
- Smooth horizontal page transition between the home page and projects page
- Project cards that open a preview panel before redirecting to GitHub
- Contact modal with a form submission flow
- Profile image placed in the projects page portrait frame (`profile.jpg`)
- Responsive styling for desktop and smaller screens

## Run locally

Open `Index.html` directly in a browser or serve the folder with a local web server:

```powershell
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000/Index.html
```

## Customize

Update the following sections directly in the HTML files:

- Hero text and intro details in `Index.html`
- Navigation labels and the overlay menu in `Index.html`
- Project cards, timeline items, and services in `projects.html`
- Social links, resume link, and contact links throughout the site
- Colors, spacing, and motion in each file's embedded CSS block

## Profile image

The portrait used in the projects page is stored as:

```text
profile.jpg
```

It is referenced in `projects.html` and is used in the profile frame near the top of the project timeline page.

## Files

```text
Index.html
projects.html
profile.jpg
Resume.pdf
README.md
```
