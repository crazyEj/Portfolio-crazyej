# Erick James Sibayan | Portfolio

A polished personal portfolio for Erick James Sibayan, built as a lightweight static website with a cinematic landing page and a detailed projects/experience section.

## Overview

This project presents:

- a bold home page with animated background visuals and an intro experience
- a second page highlighting projects, experience, services, and skills
- responsive layouts for desktop and mobile
- subtle motion and transitions for a modern portfolio feel
- no build tools or framework dependency required

## Tech Stack

- HTML5 for structure and content
- CSS for layout, visual design, responsive behavior, and animation
- Vanilla JavaScript for interactivity and UI effects
- Google Fonts for typography
- Three.js for the 3D-style hero treatment on the home page

## Project Structure

```text
.
├── index.html          # Home page with hero, navigation, and contact modal
├── projects.html       # Projects, experience, services, and skills
├── profile.jpg         # Portfolio profile image
├── Resume.pdf          # Resume document
├── README.md           # Project documentation
└── .git/              # Git metadata
```

## Features

- immersive full-screen landing experience
- animated line background and layered visual effects
- project cards with preview interactions
- experience timeline and service overview
- contact modal with a Formspree-ready form setup
- smooth page transitions using the View Transition API when supported

## Run Locally

From the project directory, start a local web server:

```powershell
py -m http.server 8000
```

Then open:

```text
http://localhost:8000/index.html
```

A local server is recommended rather than opening the files directly from the filesystem.

## Customize the Portfolio

Edit the content in these files:

- [index.html](index.html) for the hero section, navigation, contact modal, and home-page text
- [projects.html](projects.html) for projects, experience, services, and skills
- [profile.jpg](profile.jpg) for the profile photo
- [Resume.pdf](Resume.pdf) for the downloadable resume

## Contact Form

The site includes a contact form that is wired for Formspree. You will need to replace the placeholder endpoint in [index.html](index.html) with your own Formspree form ID before submissions will work.

## Notes

- The website is static and does not require Node.js or package installation.
- Some visuals use external CDNs, so an internet connection is needed for the fonts and 3D assets.
- The design is intentionally minimal, modern, and dark-themed to match the portfolio aesthetic.

## License

This project is for personal portfolio use. If you intend to reuse or adapt it, make sure you have permission for any branding, personal content, résumé details, or media included in the site.
