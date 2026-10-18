#!/usr/bin/env python3
"""Genera index.html (ES) y en/index.html (EN) a partir del contenido de este archivo.

Uso:  python3 tools/build.py

Cada texto vive junto a su traducción mediante tr(es, en). Para actualizar el
sitio, edita el contenido aquí, ejecuta el script y publica los HTML generados.
"""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://vladimirjon.github.io/JohannPasquel_PersonalWebsite/"
EMAIL = "johannpasquel@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/johannpasquel"
GITHUB = "https://github.com/Vladimirjon"

LANG = "es"


def tr(es, en):
    return es if LANG == "es" else en


def e(text):
    return escape(text, quote=True)


ICON = {
    "arrow": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11 11 5M6 5h5v5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"/></svg>',
    "down": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3v8m0 0L4.5 7.5M8 11l3.5-3.5M3 13.5h10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"/></svg>',
    "to": '<svg class="icon to" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"/></svg><span class="sr-only">, </span>',
    "copy": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M5.5 5.5h7v8h-7zM3.5 10.5v-8h7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square"/></svg>',
}


# ---------------------------------------------------------------- contenido

def results():
    return [
        (tr("<strong>Cinco tablas de calificaciones</strong> unificadas en un único modelo relacional.",
            "<strong>Five grade tables</strong> unified into a single relational model."),
         tr("Conservatorio Nacional de Música", "National Conservatory of Music")),
        (tr("<strong>Doble digitación eliminada:</strong> informes PDF y Excel generados de forma automática.",
            "<strong>Double data entry eliminated:</strong> PDF and Excel reports generated automatically."),
         "Abimatik Medical Instruments"),
        (tr("<strong>Entorno institucional de datos recuperado</strong> y validado sobre AlmaLinux.",
            "<strong>Institutional data environment recovered</strong> and validated on AlmaLinux."),
         "ARCONEL"),
        (tr("<strong>99,50 % mAP50</strong> en visión por computadora para reconstruir partidas de Amazons.",
            "<strong>99.50% mAP50</strong> in computer vision to reconstruct Amazons games."),
         tr("Investigación aplicada · 2025", "Applied research · 2025")),
    ]


def experience():
    return [
        dict(
            org=tr("Conservatorio Nacional de Música", "National Conservatory of Music"),
            role=tr("Desarrollador full-stack · Sistema de gestión académica",
                    "Full-stack developer · Academic management system"),
            period=tr("ago. – oct. 2026", "Aug – Oct 2026"),
            points=[
                tr("Participé en la migración y evolución de la plataforma en cuatro repositorios de frontend y backend: sistema anterior (Angular, Express/Sequelize) y nuevo (Next.js, NestJS/TypeORM).",
                   "Worked on the migration and evolution of the platform across four frontend and backend repositories: the legacy system (Angular, Express/Sequelize) and the new one (Next.js, NestJS/TypeORM)."),
                tr("Unifiqué cinco tablas de calificaciones en un modelo académico único y desarrollé servicios REST para consulta, cálculo y registro de notas (MySQL).",
                   "Unified five grade tables into a single academic model and built REST services to query, calculate and record grades (MySQL)."),
                tr("Implementé módulos de estudiantes, representantes y matrículas, reportes y el portal del representante, con validaciones, control de acceso JWT e interfaces en Next.js.",
                   "Implemented modules for students, guardians and enrollment, reports and the guardian portal, with validation, JWT access control and Next.js interfaces."),
            ],
        ),
        dict(
            org="Abimatik Medical Instruments",
            role=tr("Desarrollador de software · Sistema de informes técnicos",
                    "Software developer · Technical reporting system"),
            period=tr("ago. – sep. 2026", "Aug – Sep 2026"),
            points=[
                tr("Desarrollé una aplicación que convierte una captura estructurada en informes PDF, hojas Excel y correos de entrega (React, TypeScript, PHP 8.3, MySQL).",
                   "Built an application that turns structured input into PDF reports, Excel sheets and delivery emails (React, TypeScript, PHP 8.3, MySQL)."),
                tr("Implementé captura sin conexión, sincronización, correcciones versionadas y registros de auditoría de solo anexado (IndexedDB).",
                   "Implemented offline capture, synchronization, versioned corrections and append-only audit records (IndexedDB)."),
                tr("Automaticé la entrega y las pruebas con cuatro flujos de GitHub Actions.",
                   "Automated delivery and testing with four GitHub Actions workflows."),
            ],
        ),
        dict(
            org=tr("Agencia de Regulación y Control de Electricidad (ARCONEL)",
                   "Electricity Regulation and Control Agency (ARCONEL)"),
            role=tr("Practicante de Tecnologías de la Información · Dirección de TIC",
                    "Information Technology intern · ICT Directorate"),
            period=tr("jun. – ago. 2026", "Jun – Aug 2026"),
            points=[
                tr("Recuperé y validé un entorno institucional de procesamiento de datos y reportes sobre AlmaLinux, integrando Apache, Python, ODBC y SQL Server.",
                   "Recovered and validated an institutional data processing and reporting environment on AlmaLinux, integrating Apache, Python, ODBC and SQL Server."),
                tr("Implementé agendamiento médico interno con Microsoft Bookings, Forms y Power Automate, con validaciones y notificaciones.",
                   "Implemented internal medical scheduling with Microsoft Bookings, Forms and Power Automate, including validation and notifications."),
            ],
        ),
    ]


def projects():
    repo = tr("Repositorio", "Repository")
    return [
        dict(
            span="wide",
            status=tr("En desarrollo", "In development"),
            title=tr("Monitor de calidad de datos de contratación pública",
                     "Public procurement data quality monitor"),
            text=tr("Conservación inmutable de evidencia con SHA-256, acceso HTTP a las fuentes y persistencia en PostgreSQL, con migraciones versionadas y pruebas automatizadas.",
                    "Immutable evidence preservation with SHA-256, HTTP access to the sources and PostgreSQL persistence, with versioned migrations and automated tests."),
            proof=tr("fuente HTTP → evidencia SHA-256 → PostgreSQL", "HTTP source → SHA-256 evidence → PostgreSQL"),
            note=tr("La ingesta integral está pendiente.", "End-to-end ingestion is still pending."),
            stack="Python · PostgreSQL · SHA-256 · pytest",
            link=("https://github.com/Vladimirjon/ec-public-procurement-quality-monitor", repo),
        ),
        dict(
            span="narrow",
            status=tr("Implementado y validado", "Implemented and validated"),
            title=tr("Identidad distribuida y alta disponibilidad",
                     "Distributed identity and high availability"),
            text=tr("OpenLDAP replicado, Kerberos, PKI/TLS, HAProxy y Keepalived sobre tres máquinas virtuales Linux. Validé escenarios de conmutación por fallo.",
                    "Replicated OpenLDAP, Kerberos, PKI/TLS, HAProxy and Keepalived across three Linux virtual machines. Validated failover scenarios."),
            proof=None,
            note=None,
            stack="Linux · OpenLDAP · Kerberos · HAProxy · Keepalived",
            link=("https://github.com/Vladimirjon/PasquelJ-MiniIdM", repo),
        ),
        dict(
            span="narrow",
            status=tr("Investigación aplicada · 2025", "Applied research · 2025"),
            title=tr("Visión por computadora para el juego Amazons",
                     "Computer vision for the game of Amazons"),
            text=tr("Reconstrucción automática de tableros y movimientos a partir de imágenes, con YOLOv8 y OpenCV. Colaboración en equipo.",
                    "Automatic reconstruction of boards and moves from images, using YOLOv8 and OpenCV. Team collaboration."),
            proof=tr("99,50 % mAP50 en la evaluación del proyecto", "99.50% mAP50 on the project evaluation"),
            note=None,
            stack="Python · YOLOv8 · OpenCV",
            link=("https://github.com/Vladimirjon/Captura_automatica_de_posiciones_con_AI_Vision", repo),
        ),
        dict(
            span="wide",
            status=tr("Proyecto de sistemas", "Systems project"),
            title="PasquelJ-MiniHTTPd",
            text=tr("Servidor HTTP de un solo proceso construido sobre E/S TCP no bloqueante y multiplexación de eventos.",
                    "Single-process HTTP server built on non-blocking TCP I/O and event multiplexing."),
            proof=None,
            note=None,
            stack=tr("C · TCP no bloqueante · multiplexación de eventos", "C · non-blocking TCP · event multiplexing"),
            link=("https://github.com/Vladimirjon/PasquelJ-MiniHTTPd", repo),
        ),
    ]


def principles():
    return [
        (tr("Conservar la evidencia", "Preserve the evidence"),
         tr("Los datos originales se guardan con SHA-256 antes de interpretarlos.",
            "Original data is stored with SHA-256 before it is interpreted.")),
        (tr("Corregir sin borrar", "Correct without erasing"),
         tr("Correcciones versionadas y auditoría de solo anexado.",
            "Versioned corrections and append-only audit records.")),
        (tr("Probar y automatizar", "Test and automate"),
         tr("Pruebas automatizadas y flujos de entrega en GitHub Actions.",
            "Automated tests and delivery pipelines on GitHub Actions.")),
    ]


def skills():
    return [
        (tr("Datos y analítica", "Data and analytics"),
         ["Python", "SQL", "PostgreSQL", "MySQL", "SQL Server", tr("Modelado relacional", "Relational modeling"),
          "Power BI", "Power Query", "DAX"]),
        (tr("Desarrollo", "Development"),
         ["TypeScript", "JavaScript", "React", "Next.js", "NestJS", "PHP", "API REST", "GitHub Actions"]),
        (tr("Infraestructura y automatización", "Infrastructure and automation"),
         ["Linux", "Docker", "Git", "n8n", "Power Automate", "OpenLDAP", "Kerberos"]),
    ]


def credentials():
    return [
        "Cambridge English C1",
        tr("n8n Professional Certificate (2026)", "n8n Professional Certificate (2026)"),
        "Power BI, Santander Open Academy (2026)",
        "Scrum Fundamentals Certified (2025)",
    ]


# ---------------------------------------------------------------- plantillas

def render_hero(base):
    rows = "".join(
        f'<li><p>{text}</p><span class="meta">{e(meta)}</span></li>' for text, meta in results()
    )
    return f"""
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap hero-grid">
        <div class="hero-copy">
          <p class="hero-id">Johann Pasquel <span aria-hidden="true">/</span> {tr("Desarrollador de software y soluciones de datos", "Software and data solutions developer")}</p>
          <h1 id="hero-title">{tr("Datos útiles.<br><em>Procesos confiables.</em>", "Useful data.<br><em>Reliable processes.</em>")}</h1>
          <p class="hero-lead">{tr("Backend, bases de datos y automatización, con atención a la integridad y la trazabilidad. Hoy profundizo en ingeniería de datos.",
                                   "Backend, databases and automation, with a focus on integrity and traceability. Currently deepening my data engineering practice.")}</p>
          <div class="actions">
            <a class="button primary" href="#projects">{tr("Ver proyectos", "View projects")}</a>
            <a class="button" href="{base}assets/Pasquel_Johann_CV.pdf" download>{tr("Descargar CV", "Download CV")}{ICON["down"]}</a>
          </div>
        </div>
        <aside class="ledger" aria-labelledby="ledger-title">
          <h2 id="ledger-title" class="ledger-title">{tr("Resultados recientes", "Recent results")}</h2>
          <ul>{rows}</ul>
        </aside>
      </div>
    </section>"""


def render_profile(base):
    items = "".join(
        f"<div><dt>{e(t)}</dt><dd>{e(d)}</dd></div>" for t, d in principles()
    )
    return f"""
    <section class="section profile" id="profile" aria-labelledby="profile-title">
      <div class="wrap profile-grid">
        <figure class="portrait">
          <img src="{base}assets/img/profile.jpg" width="498" height="440" alt="{tr("Retrato de Johann Pasquel", "Portrait of Johann Pasquel")}" loading="lazy">
        </figure>
        <div class="profile-copy">
          <h2 id="profile-title">{tr("Perfil", "Profile")}</h2>
          <p class="statement">{tr("Desarrollo software para que los datos sean útiles y los procesos, confiables. Integro frontend, APIs, bases de datos y automatización, con especial atención a la integridad y la trazabilidad.",
                                  "I build software so that data is useful and processes are reliable. I integrate frontend, APIs, databases and automation, with particular attention to integrity and traceability.")}</p>
          <dl class="principles">{items}</dl>
        </div>
      </div>
    </section>"""


def render_experience():
    rows = []
    for job in experience():
        points = "".join(f"<li>{e(p)}</li>" for p in job["points"])
        rows.append(f"""
        <article class="job">
          <p class="job-period">{e(job["period"])}</p>
          <div class="job-body">
            <h3>{e(job["org"])}</h3>
            <p class="job-role">{e(job["role"])}</p>
            <ul>{points}</ul>
          </div>
        </article>""")
    return f"""
    <section class="section" id="experience" aria-labelledby="experience-title">
      <div class="wrap split">
        <h2 id="experience-title">{tr("Experiencia", "Experience")}</h2>
        <div class="jobs">{"".join(rows)}</div>
      </div>
    </section>"""


def render_projects():
    cards = []
    for p in projects():
        proof = f'<p class="proof">{ICON["to"].join(e(x.strip()) for x in p["proof"].split("→"))}</p>' if p["proof"] else ""
        note = f'<p class="note">{e(p["note"])}</p>' if p["note"] else ""
        url, label = p["link"]
        cards.append(f"""
        <article class="project {p["span"]}">
          <p class="status">{e(p["status"])}</p>
          <h3>{e(p["title"])}</h3>
          <p>{e(p["text"])}</p>
          {proof}{note}
          <div class="project-foot">
            <span class="stack">{e(p["stack"])}</span>
            <a class="link" href="{url}" target="_blank" rel="noopener">{e(label)}{ICON["arrow"]}<span class="sr-only"> {tr("(se abre en una pestaña nueva)", "(opens in a new tab)")}</span></a>
          </div>
        </article>""")
    research = tr(
        "<strong>Prótesis mioeléctrica · 2026.</strong> Participé en el desarrollo de un prototipo en el Laboratorio de IA y Visión por Computadora “Alan Turing”.",
        "<strong>Myoelectric prosthesis · 2026.</strong> Contributed to the development of a prototype at the “Alan Turing” AI and Computer Vision Laboratory.",
    )
    return f"""
    <section class="section" id="projects" aria-labelledby="projects-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="projects-title">{tr("Proyectos seleccionados", "Selected projects")}</h2>
          <p>{tr("Cada uno indica su estado real y enlaza al código.", "Each one states its real status and links to the code.")}</p>
        </div>
        <div class="project-grid">{"".join(cards)}</div>
        <p class="research">{research}</p>
      </div>
    </section>"""


def render_skills():
    cols = "".join(
        f'<div><dt>{e(title)}</dt><dd>{e(", ".join(items))}</dd></div>' for title, items in skills()
    )
    return f"""
    <section class="section" id="skills" aria-labelledby="skills-title">
      <div class="wrap">
        <h2 id="skills-title">{tr("Competencias", "Skills")}</h2>
        <dl class="skills">{cols}</dl>
      </div>
    </section>"""


def render_education():
    certs = "".join(f"<li>{e(c)}</li>" for c in credentials())
    return f"""
    <section class="section" id="education" aria-labelledby="education-title">
      <div class="wrap split">
        <h2 id="education-title">{tr("Formación y credenciales", "Education and credentials")}</h2>
        <div class="edu">
          <div>
            <h3>Escuela Politécnica Nacional (EPN)</h3>
            <p>{tr("Ingeniería en Ciencias de la Computación, en curso", "B.Eng. in Computer Science, in progress")}</p>
            <p class="meta">2022 – {tr("actualidad", "present")}</p>
          </div>
          <div>
            <h3>IEEEXtreme 19.0</h3>
            <p>{tr("Tercer lugar en Ecuador, equipo Kiubit.", "Third place in Ecuador, team Kiubit.")}</p>
          </div>
          <div>
            <h3>{tr("Certificaciones", "Certifications")}</h3>
            <ul class="plain">{certs}</ul>
          </div>
        </div>
      </div>
    </section>"""


def render_contact():
    return f"""
    <section class="section contact" id="contact" aria-labelledby="contact-title">
      <div class="wrap">
        <h2 id="contact-title">{tr("Contacto", "Contact")}</h2>
        <p class="contact-lead">{tr("Abierto a oportunidades en ingeniería de datos y desarrollo backend.", "Open to opportunities in data engineering and backend development.")}</p>
        <p class="email-row">
          <a class="email" href="mailto:{EMAIL}">{EMAIL}</a>
          <button class="button" type="button" id="copy-email" data-copied="{tr("Correo copiado", "Email copied")}" data-failed="{tr("No se pudo copiar. Selecciona el correo manualmente.", "Could not copy. Select the email manually.")}">{tr("Copiar correo", "Copy email")}{ICON["copy"]}</button>
        </p>
        <ul class="links">
          <li><a class="link" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn{ICON["arrow"]}<span class="sr-only"> {tr("(se abre en una pestaña nueva)", "(opens in a new tab)")}</span></a></li>
          <li><a class="link" href="{GITHUB}" target="_blank" rel="noopener">GitHub{ICON["arrow"]}<span class="sr-only"> {tr("(se abre en una pestaña nueva)", "(opens in a new tab)")}</span></a></li>
        </ul>
        <p class="toast" id="toast" role="status" aria-live="polite"></p>
      </div>
    </section>"""


def render_page(lang):
    global LANG
    LANG = lang
    base = "" if lang == "es" else "../"
    url = SITE if lang == "es" else SITE + "en/"
    other_href = "en/" if lang == "es" else "../"
    title = tr("Johann Pasquel · Desarrollador de software y soluciones de datos",
               "Johann Pasquel · Software and data solutions developer")
    description = tr(
        "Portafolio de Johann Pasquel, Quito. Backend, bases de datos y automatización con integridad y trazabilidad. Experiencia en sistemas académicos, informes técnicos y datos institucionales.",
        "Portfolio of Johann Pasquel, Quito. Backend, databases and automation with integrity and traceability. Experience in academic systems, technical reporting and institutional data.",
    )
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Johann Pasquel",
        "jobTitle": tr("Desarrollador de software y soluciones de datos", "Software and data solutions developer"),
        "url": url,
        "email": f"mailto:{EMAIL}",
        "image": SITE + "assets/img/profile.jpg",
        "address": {"@type": "PostalAddress", "addressLocality": "Quito", "addressCountry": "EC"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Escuela Politécnica Nacional"},
        "sameAs": [LINKEDIN, GITHUB],
        "knowsLanguage": ["es", "en"],
    }
    nav = [
        ("#experience", tr("Experiencia", "Experience")),
        ("#projects", tr("Proyectos", "Projects")),
        ("#skills", tr("Competencias", "Skills")),
        ("#contact", tr("Contacto", "Contact")),
    ]
    nav_html = "".join(f'<a href="{h}">{e(t)}</a>' for h, t in nav)
    es_attr = ' aria-current="true"' if lang == "es" else ""
    en_attr = ' aria-current="true"' if lang == "en" else ""
    es_href = "#top" if lang == "es" else "../"
    en_href = "en/" if lang == "es" else "#top"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#f5f6f8">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="es" href="{SITE}">
  <link rel="alternate" hreflang="en" href="{SITE}en/">
  <link rel="alternate" hreflang="x-default" href="{SITE}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}assets/img/og.png">
  <meta property="og:locale" content="{tr("es_EC", "en_US")}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preload" href="{base}assets/fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{base}assets/css/styles.css">
  <script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
<body id="top">
  <a class="skip" href="#main">{tr("Ir al contenido", "Skip to content")}</a>
  <header class="site-header">
    <div class="wrap bar">
      <a class="brand" href="#top">Johann Pasquel</a>
      <nav aria-label="{tr("Principal", "Main")}">{nav_html}</nav>
      <div class="bar-tools">
        <div class="lang" role="group" aria-label="{tr("Idioma", "Language")}">
          <a href="{es_href}" hreflang="es" lang="es"{es_attr}>ES</a>
          <a href="{en_href}" hreflang="en" lang="en"{en_attr}>EN</a>
        </div>
        <a class="button small" href="{base}assets/Pasquel_Johann_CV.pdf" download>CV</a>
      </div>
    </div>
  </header>
  <main id="main">{render_hero(base)}{render_profile(base)}{render_experience()}{render_projects()}{render_skills()}{render_education()}{render_contact()}
  </main>
  <footer class="site-footer">
    <div class="wrap foot">
      <span>© 2026 Johann Pasquel · Quito, Ecuador</span>
      <a href="#top">{tr("Volver arriba", "Back to top")}</a>
    </div>
  </footer>
  <script src="{base}assets/js/main.js" defer></script>
</body>
</html>
"""


def main():
    (ROOT / "index.html").write_text(render_page("es"), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(render_page("en"), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f'  <url><loc>{SITE}</loc><xhtml:link rel="alternate" hreflang="en" href="{SITE}en/"/></url>\n'
        f'  <url><loc>{SITE}en/</loc><xhtml:link rel="alternate" hreflang="es" href="{SITE}"/></url>\n'
        "</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
    print("OK: index.html, en/index.html, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
