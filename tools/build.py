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
PHONE_TEL = "+593996857747"
PHONE_SHOW = "+593 99 685 7747"
LINKEDIN = "https://www.linkedin.com/in/johannpasquel"
GITHUB_USER = "Vladimirjon"
GITHUB = f"https://github.com/{GITHUB_USER}"

LANG = "es"


def tr(es, en):
    return es if LANG == "es" else en


def e(text):
    return escape(text, quote=True)


ICON = {
    "arrow": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11 11 5M6 5h5v5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "down": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 3v8m0 0L4.5 7.5M8 11l3.5-3.5M3 13.5h10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "copy": '<svg class="icon" viewBox="0 0 16 16" aria-hidden="true"><path d="M5.5 5.5h7v8h-7zM3.5 10.5v-8h7" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>',
}


def _glyph(body):
    return f'<svg class="glyph" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{body}</svg>'


GLYPH = {
    "shield": _glyph('<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>'),
    "branch": _glyph('<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>'),
    "check": _glyph('<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>'),
    "database": _glyph('<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>'),
    "code": _glyph('<path d="m18 16 4-4-4-4"/><path d="m6 8-4 4 4 4"/><path d="m14.5 4-5 16"/>'),
    "server": _glyph('<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>'),
    "network": _glyph('<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/><path d="M12 12V8"/>'),
    "eye": _glyph('<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="1"/><path d="M18.944 12.33a1 1 0 0 0 0-.66 7.5 7.5 0 0 0-13.888 0 1 1 0 0 0 0 .66 7.5 7.5 0 0 0 13.888 0"/>'),
    "terminal": _glyph('<polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/>'),
    "mail": _glyph('<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>'),
    "phone": _glyph('<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>'),
    "linkedin": _glyph('<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/>'),
    "github": _glyph('<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>'),
    "file": _glyph('<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>'),
    "cap": _glyph('<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>'),
    "trophy": _glyph('<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>'),
    "award": _glyph('<path d="m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526"/><circle cx="12" cy="8" r="6"/>'),
    "repo": _glyph('<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/>'),
}

FLAG = '<svg class="flag" viewBox="0 0 24 16" aria-hidden="true" focusable="false"><rect width="24" height="8" fill="#ffdd00"/><rect y="8" width="24" height="4" fill="#034ea2"/><rect y="12" width="24" height="4" fill="#ed1c24"/></svg>'


def icon_box(name):
    return f'<span class="icon-box">{GLYPH[name]}</span>'


def new_tab():
    return f'<span class="sr-only"> {tr("(se abre en una pestaña nueva)", "(opens in a new tab)")}</span>'


# ---------------------------------------------------------------- contenido

def built():
    return [
        ("database",
         tr("Cinco tablas, un solo modelo", "Five tables, one model"),
         tr("Consolidé las cinco tablas de calificaciones heredadas en un único modelo relacional y construí los servicios REST para consultar, calcular y registrar notas.",
            "Consolidated five legacy grade tables into a single relational model and built the REST services to query, calculate and record grades."),
         tr("Conservatorio Nacional de Música · MySQL, NestJS", "National Conservatory of Music · MySQL, NestJS")),
        ("file",
         tr("Informes que se generan solos", "Reports that generate themselves"),
         tr("Una captura estructurada produce el informe PDF, la hoja Excel y el correo de entrega. Funciona sin conexión y deja una auditoría de solo anexado.",
            "One structured capture produces the PDF report, the Excel sheet and the delivery email. It works offline and leaves an append-only audit trail."),
         "Abimatik Medical Instruments · React, PHP, MySQL"),
        ("server",
         tr("Entorno de datos otra vez operativo", "A data environment, operational again"),
         tr("Recuperé y validé el entorno institucional de procesamiento y reportes sobre AlmaLinux, integrando Apache, Python, ODBC y SQL Server.",
            "Recovered and validated the institutional processing and reporting environment on AlmaLinux, integrating Apache, Python, ODBC and SQL Server."),
         "ARCONEL · AlmaLinux, SQL Server"),
        ("eye",
         tr("Visión por computadora", "Computer vision"),
         tr("Un modelo YOLOv8 reconstruye tableros y jugadas de Amazons a partir de fotos. Obtuvo 99,50 % de mAP50 en la evaluación del proyecto.",
            "A YOLOv8 model reconstructs Amazons boards and moves from photos. It reached 99.50% mAP50 on the project evaluation."),
         tr("Investigación aplicada · 2025", "Applied research · 2025")),
    ]


def experience():
    return [
        dict(
            org=tr("Conservatorio Nacional de Música", "National Conservatory of Music"),
            role=tr("Desarrollador full-stack · Sistema de gestión académica",
                    "Full-stack developer · Academic management system"),
            period=tr("ago. – oct. 2026", "Aug – Oct 2026"),
            lead=tr("Un único modelo académico donde antes había cinco tablas de calificaciones.",
                    "A single academic model where there used to be five grade tables."),
            points=[
                tr("Participé en la migración y evolución de la plataforma en cuatro repositorios de frontend y backend: sistema anterior (Angular, Express/Sequelize) y nuevo (Next.js, NestJS/TypeORM).",
                   "Worked on the migration and evolution of the platform across four frontend and backend repositories: the legacy system (Angular, Express/Sequelize) and the new one (Next.js, NestJS/TypeORM)."),
                tr("Unifiqué cinco tablas de calificaciones en un modelo académico único y desarrollé servicios REST para consulta, cálculo y registro de notas (MySQL).",
                   "Unified five grade tables into a single academic model and built REST services to query, calculate and record grades (MySQL)."),
                tr("Implementé módulos de estudiantes, representantes y matrículas, reportes y el portal del representante, con validaciones, control de acceso JWT e interfaces en Next.js.",
                   "Implemented modules for students, guardians and enrollment, reports and the guardian portal, with validation, JWT access control and Next.js interfaces."),
            ],
            stack=["Next.js", "NestJS", "TypeORM", "MySQL", "JWT"],
        ),
        dict(
            org="Abimatik Medical Instruments",
            role=tr("Desarrollador de software · Sistema de informes técnicos",
                    "Software developer · Technical reporting system"),
            period=tr("ago. – sep. 2026", "Aug – Sep 2026"),
            lead=tr("De la captura estructurada al informe entregado, sin volver a digitar.",
                    "From structured capture to delivered report, with no re-typing."),
            points=[
                tr("Desarrollé una aplicación que convierte una captura estructurada en informes PDF, hojas Excel y correos de entrega (React, TypeScript, PHP 8.3, MySQL).",
                   "Built an application that turns structured input into PDF reports, Excel sheets and delivery emails (React, TypeScript, PHP 8.3, MySQL)."),
                tr("Implementé captura sin conexión, sincronización, correcciones versionadas y registros de auditoría de solo anexado (IndexedDB).",
                   "Implemented offline capture, synchronization, versioned corrections and append-only audit records (IndexedDB)."),
                tr("Automaticé la entrega y las pruebas con cuatro flujos de GitHub Actions.",
                   "Automated delivery and testing with four GitHub Actions workflows."),
            ],
            stack=["React", "TypeScript", "PHP 8.3", "MySQL", "IndexedDB", "GitHub Actions"],
        ),
        dict(
            org=tr("Agencia de Regulación y Control de Electricidad (ARCONEL)",
                   "Electricity Regulation and Control Agency (ARCONEL)"),
            role=tr("Practicante de Tecnologías de la Información · Dirección de TIC",
                    "Information Technology intern · ICT Directorate"),
            period=tr("jun. – ago. 2026", "Jun – Aug 2026"),
            lead=tr("Un entorno de datos institucional de nuevo operativo y validado.",
                    "An institutional data environment, operational and validated again."),
            points=[
                tr("Recuperé y validé un entorno institucional de procesamiento de datos y reportes sobre AlmaLinux, integrando Apache, Python, ODBC y SQL Server.",
                   "Recovered and validated an institutional data processing and reporting environment on AlmaLinux, integrating Apache, Python, ODBC and SQL Server."),
                tr("Implementé agendamiento médico interno con Microsoft Bookings, Forms y Power Automate, con validaciones y notificaciones.",
                   "Implemented internal medical scheduling with Microsoft Bookings, Forms and Power Automate, including validation and notifications."),
            ],
            stack=["AlmaLinux", "Apache", "Python", "ODBC", "SQL Server", "Power Automate"],
        ),
    ]


def projects():
    repo = tr("Repositorio", "Repository")
    return [
        dict(
            kind="featured",
            icon="database",
            status=tr("En desarrollo", "In development"),
            state="open",
            title=tr("Monitor de calidad de datos de contratación pública",
                     "Public procurement data quality monitor"),
            text=tr("Base para conservar y evaluar los datos de contratación pública de Ecuador. Cada fuente se consulta por HTTP, se guarda como evidencia inmutable con huella SHA-256 y se persiste en PostgreSQL, con migraciones versionadas y pruebas automatizadas.",
                    "A foundation for preserving and assessing Ecuadorian public procurement data. Each source is fetched over HTTP, stored as immutable evidence with a SHA-256 fingerprint and persisted in PostgreSQL, with versioned migrations and automated tests."),
            pipeline=[
                (tr("Fuente HTTP", "HTTP source"), "done"),
                (tr("Evidencia SHA-256", "SHA-256 evidence"), "done"),
                ("PostgreSQL", "done"),
                (tr("Ingesta integral", "End-to-end ingestion"), "pending"),
            ],
            note=tr("La ingesta integral es el siguiente paso.", "End-to-end ingestion is the next step."),
            stack=["Python", "PostgreSQL", "SHA-256", "pytest"],
            link=("https://github.com/Vladimirjon/ec-public-procurement-quality-monitor", repo),
        ),
        dict(
            kind="plain",
            icon="network",
            status=tr("Implementado y validado", "Implemented and validated"),
            state="done",
            title=tr("Identidad distribuida y alta disponibilidad",
                     "Distributed identity and high availability"),
            text=tr("Arquitectura de identidad sobre tres máquinas virtuales Linux: OpenLDAP replicado, Kerberos para la autenticación, PKI/TLS y balanceo con HAProxy y Keepalived. Validé escenarios de conmutación por fallo.",
                    "Identity architecture across three Linux virtual machines: replicated OpenLDAP, Kerberos authentication, PKI/TLS and load balancing with HAProxy and Keepalived. Validated failover scenarios."),
            stack=["Linux", "OpenLDAP", "Kerberos", "HAProxy", "Keepalived"],
            link=("https://github.com/Vladimirjon/PasquelJ-MiniIdM", repo),
        ),
        dict(
            kind="metric",
            icon="eye",
            status=tr("Investigación aplicada · 2025", "Applied research · 2025"),
            state="done",
            title=tr("Visión por computadora para el juego Amazons",
                     "Computer vision for the game of Amazons"),
            text=tr("Pipeline que reconstruye partidas físicas de Amazons a partir de imágenes: detección de objetos con YOLOv8 y OpenCV, combinada con las reglas del juego. Trabajo en equipo.",
                    "Pipeline that reconstructs physical Amazons games from images: object detection with YOLOv8 and OpenCV, combined with the rules of the game. Team project."),
            metric=(tr("99,50 %", "99.50%"), tr("mAP50 en la evaluación del proyecto", "mAP50 on the project evaluation")),
            stack=["Python", "YOLOv8", "OpenCV"],
            link=("https://github.com/Vladimirjon/Captura_automatica_de_posiciones_con_AI_Vision", repo),
        ),
        dict(
            kind="plain",
            icon="terminal",
            status=tr("Proyecto de sistemas", "Systems project"),
            state="done",
            title="PasquelJ-MiniHTTPd",
            text=tr("Servidor HTTP en C de un solo proceso. Usa E/S TCP no bloqueante y multiplexación de eventos para atender varias conexiones a la vez sin un hilo por cada una.",
                    "Single-process HTTP server in C. It uses non-blocking TCP I/O and event multiplexing to serve several connections at once without a thread per connection."),
            stack=["C", tr("TCP no bloqueante", "Non-blocking TCP"), tr("Multiplexación de eventos", "Event multiplexing")],
            link=("https://github.com/Vladimirjon/PasquelJ-MiniHTTPd", repo),
        ),
    ]


def principles():
    return [
        ("shield", tr("Conservar la evidencia", "Preserve the evidence"),
         tr("Los datos originales se guardan con SHA-256 antes de interpretarlos.",
            "Original data is stored with SHA-256 before it is interpreted.")),
        ("branch", tr("Corregir sin borrar", "Correct without erasing"),
         tr("Correcciones versionadas y auditoría de solo anexado.",
            "Versioned corrections and append-only audit records.")),
        ("check", tr("Probar y automatizar", "Test and automate"),
         tr("Pruebas automatizadas y flujos de entrega en GitHub Actions.",
            "Automated tests and delivery pipelines on GitHub Actions.")),
    ]


def skills():
    return [
        ("database", tr("Datos y analítica", "Data and analytics"),
         ["Python", "SQL", "PostgreSQL", "MySQL", "SQL Server", tr("Modelado relacional", "Relational modeling"),
          "Power BI", "Power Query", "DAX"]),
        ("code", tr("Desarrollo", "Development"),
         ["TypeScript", "JavaScript", "React", "Next.js", "NestJS", "PHP", "API REST", "GitHub Actions"]),
        ("server", tr("Infraestructura y automatización", "Infrastructure and automation"),
         ["Linux", "Docker", "Git", "n8n", "Power Automate", "OpenLDAP", "Kerberos"]),
    ]


def credentials():
    return [
        "Cambridge English C1",
        "n8n Professional Certificate (2026)",
        "Power BI, Santander Open Academy (2026)",
        "Scrum Fundamentals Certified (2025)",
    ]


def chips(items, cls="chips"):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


RINGS = '<svg class="rings{extra}" viewBox="0 0 1000 1000" aria-hidden="true" focusable="false"><circle cx="500" cy="500" r="80"/><circle cx="500" cy="500" r="170"/><circle cx="500" cy="500" r="260"/><circle cx="500" cy="500" r="350"/><circle cx="500" cy="500" r="440"/></svg>'


# ---------------------------------------------------------------- plantillas

def render_hero(base):
    rows = "".join(
        f'<li class="s">{GLYPH[g]}<div><h3>{e(t)}</h3><p>{e(d)}</p><span class="meta">{e(m)}</span></div></li>'
        for g, t, d, m in built()
    )
    return f"""
    <section class="hero" aria-labelledby="hero-title">
      {RINGS.format(extra="")}
      <div class="dotgrid" data-dotgrid aria-hidden="true"></div>
      <div class="wrap hero-grid">
        <div class="hero-copy">
          <p class="status-pill"><span class="dot pulse" aria-hidden="true"></span>{tr("Abierto a nuevas oportunidades · Datos y backend", "Open to new opportunities · Data and backend")}</p>
          <h1 id="hero-title">{tr('Sistemas de datos que se pueden <mark>auditar</mark>.', 'Data systems you can <mark>audit</mark>.')}</h1>
          <p class="hero-lead">{tr("Backend, bases de datos y automatización con integridad y trazabilidad: evidencia conservada, correcciones versionadas y pruebas automatizadas.",
                                   "Backend, databases and automation built for integrity and traceability: preserved evidence, versioned corrections and automated tests.")}</p>
          <div class="actions">
            <a class="button primary" href="#projects">{tr("Ver proyectos", "View projects")}</a>
            <a class="button" href="{base}assets/Pasquel_Johann_CV.pdf" download>{tr("Descargar CV", "Download CV")}{ICON["down"]}</a>
          </div>
        </div>
        <aside class="ledger" aria-labelledby="ledger-title">
          <header class="ledger-head">
            <h2 id="ledger-title">{tr("Lo que he construido", "What I've built")}</h2>
            <span class="meta">2025 – 2026</span>
          </header>
          <ul>{rows}</ul>
        </aside>
      </div>
    </section>"""


def render_marquee():
    names = []
    for _, _, items in skills():
        for item in items:
            if item not in names:
                names.append(item)
    group = "".join(f"<span>{e(n)}</span>" for n in names)
    return f"""
    <div class="marquee" aria-hidden="true">
      <div class="marquee-track"><div class="marquee-group">{group}</div><div class="marquee-group" data-dup>{group}</div></div>
    </div>"""


def render_approach():
    items = "".join(
        f'<div class="s">{icon_box(i)}<dt>{e(t)}</dt><dd>{e(d)}</dd></div>' for i, t, d in principles()
    )
    return f"""
    <section class="section approach" id="profile" aria-labelledby="profile-title">
      <div class="wrap approach-grid">
        <div>
          <h2 id="profile-title" class="section-title">{tr("Cómo trabajo", "How I work")}</h2>
          <p class="statement">{tr("Desarrollo software para que los datos sean útiles y los procesos, confiables. Integro frontend, APIs, bases de datos y automatización, con especial atención a la integridad y la trazabilidad.",
                                  "I build software so that data is useful and processes are reliable. I integrate frontend, APIs, databases and automation, with particular attention to integrity and traceability.")}</p>
        </div>
        <dl class="principles stagger">{items}</dl>
      </div>
    </section>"""


def render_experience():
    rows = []
    for job in experience():
        points = "".join(f"<li>{e(p)}</li>" for p in job["points"])
        rows.append(f"""
        <article class="job s">
          <p class="job-period">{e(job["period"])}</p>
          <div class="job-body">
            <h3>{e(job["org"])}</h3>
            <p class="job-role">{e(job["role"])}</p>
            <p class="job-lead">{e(job["lead"])}</p>
            <ul class="job-points">{points}</ul>
            {chips(job["stack"])}
          </div>
        </article>""")
    return f"""
    <section class="section" id="experience" aria-labelledby="experience-title">
      <div class="wrap split">
        <h2 id="experience-title" class="section-title">{tr("Experiencia", "Experience")}</h2>
        <div class="jobs stagger">{"".join(rows)}</div>
      </div>
    </section>"""


def render_project(p):
    status = f'<div class="project-top">{icon_box(p["icon"])}<p class="status" data-state="{p["state"]}"><span class="dot" aria-hidden="true"></span>{e(p["status"])}</p></div>'
    extra = ""
    if p["kind"] == "featured":
        steps = "".join(
            f'<li data-step="{state}">{e(label)}'
            + (f'<span class="sr-only"> ({tr("pendiente", "pending")})</span>' if state == "pending" else "")
            + "</li>"
            for label, state in p["pipeline"]
        )
        extra = f'<ol class="pipeline" aria-label="{tr("Flujo del proyecto", "Project flow")}">{steps}</ol><p class="note">{e(p["note"])}</p>'
    elif p["kind"] == "metric":
        value, label = p["metric"]
        extra = f'<p class="metric"><span class="metric-value" data-count="99.5" data-decimals="2" data-sep="{tr(",", ".")}" data-suffix="{tr(" %", "%")}">{e(value)}</span><span class="metric-label">{e(label)}</span></p>'
    url, label = p["link"]
    return f"""
        <article class="project s is-{p["kind"]}">
          {status}
          <h3>{e(p["title"])}</h3>
          <p class="project-text">{e(p["text"])}</p>
          {extra}
          <div class="project-foot">
            {chips(p["stack"])}
            <a class="link" href="{url}" target="_blank" rel="noopener">{e(label)}{ICON["arrow"]}{new_tab()}</a>
          </div>
        </article>"""


def render_projects():
    cards = "".join(render_project(p) for p in projects())
    research = tr(
        "<strong>Prótesis mioeléctrica · 2026.</strong> Participé en el desarrollo de un prototipo en el Laboratorio de IA y Visión por Computadora “Alan Turing”.",
        "<strong>Myoelectric prosthesis · 2026.</strong> Contributed to the development of a prototype at the “Alan Turing” AI and Computer Vision Laboratory.",
    )
    return f"""
    <section class="section" id="projects" aria-labelledby="projects-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="projects-title" class="section-title">{tr("Proyectos seleccionados", "Selected projects")}</h2>
          <p>{tr("Cada uno indica su estado real y enlaza al código.", "Each one states its real status and links to the code.")}</p>
        </div>
        <div class="project-grid stagger">{cards}
        <p class="research s">{research}</p>
        </div>
      </div>
    </section>"""


def render_github():
    i18n = {
        "repos": tr("repositorios públicos", "public repositories"),
        "followers": tr("seguidores", "followers"),
        "commits": tr("commits públicos en 90 días", "public commits in 90 days"),
        "updated": tr("Actualizado", "Updated"),
        "noDesc": tr("Sin descripción", "No description"),
        "error": tr("No se pudo cargar la actividad en vivo. Puedes verla directamente en GitHub.", "Live activity could not be loaded. You can see it directly on GitHub."),
        "empty": tr("Sin actividad pública en los últimos 90 días.", "No public activity in the last 90 days."),
        "commit": tr("commit", "commit"),
        "commitsWord": tr("commits", "commits"),
        "less": tr("Menos", "Less"),
        "more": tr("Más", "More"),
        "locale": tr("es", "en"),
        "ago": tr("hace", "ago"),
        "today": tr("hoy", "today"),
        "newTab": tr("(se abre en una pestaña nueva)", "(opens in a new tab)"),
        "d": tr("d", "d"),
        "m": tr("meses", "mo"),
        "y": tr("años", "y"),
    }
    featured = {
        "ec-public-procurement-quality-monitor": tr("Preservación y evaluación de datos de contratación pública de Ecuador.", "Preservation and assessment of Ecuadorian public procurement data."),
        "PasquelJ-MiniIdM": tr("Identidad distribuida: LDAP replicado, Kerberos y HAProxy en tres máquinas virtuales Linux.", "Distributed identity: replicated LDAP, Kerberos and HAProxy on three Linux virtual machines."),
        "Captura_automatica_de_posiciones_con_AI_Vision": tr("Reconstrucción de partidas de Amazons a partir de imágenes con YOLOv8 y OpenCV.", "Reconstruction of Amazons games from images with YOLOv8 and OpenCV."),
        "PasquelJ-MiniHTTPd": tr("Servidor HTTP de un solo proceso con E/S TCP no bloqueante.", "Single-process HTTP server with non-blocking TCP I/O."),
        "JohannPasquel_PersonalWebsite": tr("Este portafolio: sitio estático bilingüe, con contenido y plantillas en Python.", "This portfolio: a bilingual static site with content and templates in Python."),
    }
    i18n["featured"] = featured
    skeleton = "".join('<li class="skeleton-row"><span></span><span></span></li>' for _ in range(4))
    return f"""
    <section class="section" id="github" aria-labelledby="github-title">
      <div class="wrap">
        <div class="section-head">
          <h2 id="github-title" class="section-title">{tr("GitHub en vivo", "GitHub, live")}</h2>
          <p>{tr("Datos de la API pública de GitHub, consultados al abrir esta página.", "Data from the public GitHub API, fetched when this page loads.")}</p>
        </div>
        <div class="gh stagger" id="gh" data-user="{GITHUB_USER}" data-i18n="{e(json.dumps(i18n, ensure_ascii=False))}" aria-busy="true">
          <div class="gh-side s">
            <ul class="gh-stats">
              <li><b data-stat="repos">–</b><span>{i18n["repos"]}</span></li>
              <li><b data-stat="followers">–</b><span>{i18n["followers"]}</span></li>
              <li><b data-stat="commits">–</b><span>{i18n["commits"]}</span></li>
            </ul>
            <div class="gh-heat">
              <div class="heat" role="img" aria-label="{tr("Mapa de calor de commits públicos de los últimos 90 días", "Heatmap of public commits over the last 90 days")}"></div>
              <p class="heat-note">{tr("Últimos 90 días · eventos públicos", "Last 90 days · public events")}</p>
            </div>
          </div>
          <div class="gh-main s">
            <ul class="gh-repos">{skeleton}</ul>
            <p class="gh-error" hidden>{i18n["error"]} <a class="link" href="{GITHUB}" target="_blank" rel="noopener">GitHub{ICON["arrow"]}{new_tab()}</a></p>
          </div>
        </div>
      </div>
    </section>"""


def render_skills():
    cols = "".join(
        f'<div class="s">{icon_box(i)}<dt>{e(title)}</dt><dd>{chips(items)}</dd></div>' for i, title, items in skills()
    )
    return f"""
    <section class="section" id="skills" aria-labelledby="skills-title">
      <div class="wrap">
        <h2 id="skills-title" class="section-title">{tr("Competencias", "Skills")}</h2>
        <dl class="skills stagger">{cols}</dl>
      </div>
    </section>"""


def render_education():
    return f"""
    <section class="section" id="education" aria-labelledby="education-title">
      <div class="wrap split">
        <h2 id="education-title" class="section-title">{tr("Formación y credenciales", "Education and credentials")}</h2>
        <div class="edu stagger">
          <div class="edu-row s">
            {icon_box("cap")}
            <p class="edu-when">2022 – {tr("actualidad", "present")}</p>
            <div>
              <h3>Escuela Politécnica Nacional (EPN)</h3>
              <p>{tr("Ingeniería en Ciencias de la Computación, en curso", "B.Eng. in Computer Science, in progress")}</p>
            </div>
          </div>
          <div class="edu-row s">
            {icon_box("trophy")}
            <p class="edu-when">{tr("Reconocimiento", "Recognition")}</p>
            <div>
              <h3>IEEEXtreme 19.0</h3>
              <p>{tr("Tercer lugar en Ecuador, equipo Kiubit.", "Third place in Ecuador, team Kiubit.")}</p>
            </div>
          </div>
          <div class="edu-row s">
            {icon_box("award")}
            <p class="edu-when">{tr("Certificaciones", "Certifications")}</p>
            <div>{chips(credentials())}</div>
          </div>
        </div>
      </div>
    </section>"""


def tile(href, glyph, label, value, extra="", external=False, value_class=""):
    attrs = ' target="_blank" rel="noopener"' if external else ""
    hint = new_tab() if external else ""
    return f"""<li class="s"><a class="tile" href="{href}"{attrs}>{GLYPH[glyph]}<span class="tile-text"><small>{e(label)}</small><b class="{value_class}">{extra}{e(value)}</b></span>{hint}</a></li>"""


def render_contact(base):
    tiles = "".join([
        tile(f"mailto:{EMAIL}", "mail", tr("Correo", "Email"), EMAIL, value_class="email"),
        tile(f"tel:{PHONE_TEL}", "phone", tr("Teléfono · Ecuador", "Phone · Ecuador"), PHONE_SHOW, extra=FLAG),
        tile(LINKEDIN, "linkedin", "LinkedIn", "in/johannpasquel", external=True),
        tile(GITHUB, "github", "GitHub", f"@{GITHUB_USER}", external=True),
    ])
    return f"""
    <section class="section contact-section" id="contact" aria-labelledby="contact-title">
      <div class="wrap">
        <div class="contact">
          {RINGS.format(extra=" rings-dark")}
          <div class="dotgrid dotgrid-dark" data-dotgrid aria-hidden="true"></div>
          <h2 id="contact-title">{tr("Conversemos sobre tu próximo sistema de datos.", "Let's talk about your next data system.")}</h2>
          <p class="contact-lead">{tr("Ingeniería de datos, backend y automatización. Quito, Ecuador.", "Data engineering, backend and automation. Quito, Ecuador.")}</p>
          <ul class="tiles stagger">{tiles}</ul>
          <div class="actions">
            <button class="button primary" type="button" id="copy-email" data-copied="{tr("Correo copiado", "Email copied")}" data-failed="{tr("No se pudo copiar. Selecciona el correo manualmente.", "Could not copy. Select the email manually.")}">{tr("Copiar correo", "Copy email")}{ICON["copy"]}</button>
            <a class="button" href="{base}assets/Pasquel_Johann_CV.pdf" download>{tr("Descargar CV", "Download CV")}{ICON["down"]}</a>
          </div>
          <p class="toast" id="toast" role="status" aria-live="polite"></p>
        </div>
      </div>
    </section>"""


def render_page(lang):
    global LANG
    LANG = lang
    base = "" if lang == "es" else "../"
    url = SITE if lang == "es" else SITE + "en/"
    title = tr("Johann Pasquel · Desarrollador de software y soluciones de datos",
               "Johann Pasquel · Software and data solutions developer")
    description = tr(
        "Johann Pasquel, Quito. Desarrollo backend, ingeniería de datos y automatización: sistemas con integridad y trazabilidad, de la base de datos al informe entregado.",
        "Johann Pasquel, Quito. Backend development, data engineering and automation: systems built with integrity and traceability, from the database to the delivered report.",
    )
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Johann Pasquel",
        "jobTitle": tr("Desarrollador de software y soluciones de datos", "Software and data solutions developer"),
        "url": url,
        "email": f"mailto:{EMAIL}",
        "telephone": PHONE_TEL,
        "address": {"@type": "PostalAddress", "addressLocality": "Quito", "addressCountry": "EC"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Escuela Politécnica Nacional"},
        "sameAs": [LINKEDIN, GITHUB],
        "knowsLanguage": ["es", "en"],
    }
    nav = [
        ("#experience", tr("Experiencia", "Experience")),
        ("#projects", tr("Proyectos", "Projects")),
        ("#github", "GitHub"),
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
  <meta name="theme-color" content="#fafaf9">
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
  <link rel="preload" href="{base}assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{base}assets/css/styles.css">
  <script>document.documentElement.classList.add('js')</script>
  <script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>
</head>
<body id="top">
  <a class="skip" href="#main">{tr("Ir al contenido", "Skip to content")}</a>
  <div class="progress" aria-hidden="true"></div>
  <header class="site-header">
    <div class="wrap bar">
      <a class="brand" href="#top">Johann Pasquel</a>
      <nav aria-label="{tr("Principal", "Main")}">{nav_html}</nav>
      <div class="bar-tools">
        <div class="lang" role="group" aria-label="{tr("Idioma", "Language")}">
          <a href="{es_href}" hreflang="es" lang="es"{es_attr}>ES</a>
          <a href="{en_href}" hreflang="en" lang="en"{en_attr}>EN</a>
        </div>
        <a class="button small" href="{base}assets/Pasquel_Johann_CV.pdf" download>{tr("Descargar CV", "Download CV")}</a>
      </div>
    </div>
  </header>
  <main id="main">{render_hero(base)}{render_marquee()}{render_approach()}{render_experience()}{render_projects()}{render_github()}{render_skills()}{render_education()}{render_contact(base)}
  </main>
  <footer class="site-footer">
    <div class="wrap foot">
      <span>© 2026 Johann Pasquel · Quito, Ecuador</span>
      <a href="#top">{tr("Volver arriba", "Back to top")}</a>
    </div>
  </footer>
  <script src="{base}assets/js/anime.min.js" defer></script>
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
