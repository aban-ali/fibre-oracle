# Carbon Fiber Defect Detection & Explainable Inspection System

A production-oriented Computer Vision + LLM system for automated defect detection in composite materials with structured engineering explanation.

This project is designed as a research-grade systems prototype demonstrating:

- Vision-based defect localization
- Structured severity estimation
- Synthetic data generation for controlled experimentation
- Explainable reasoning via LLM grounding
- Async backend architecture with reproducible infrastructure

---

## Motivation

Composite materials such as carbon fiber laminates are widely used in aerospace, automotive, and structural systems. Defect inspection typically requires:

- Manual visual inspection
- Specialized NDT equipment
- Expert interpretation
- Manual reporting

This project explores how modern AI systems can:

1. Detect visible defects from images
2. Quantify defect severity
3. Produce structured, grounded engineering explanations
4. Maintain reproducible and version-controlled data pipelines

The goal is not just model accuracy, but **systems-level reliability and explainability**.

---

## Research Objectives

- Study defect detection in composite materials under controlled synthetic conditions
- Investigate hybrid CV + rule-grounded LLM reasoning
- Design reproducible ML infrastructure with explicit schema versioning
- Explore explainable decision-support systems for material inspection

---

## System Architecture

Client  
→ FastAPI (API Layer)  
→ Redis (Task Queue + Caching)  
→ Celery Worker (CV + LLM Processing)  
→ PostgreSQL (Persistent Storage)  
→ Alembic (Schema Versioning)

Key principles:

- One DB session per request
- Engine-level connection pooling
- Explicit schema migrations
- Background task isolation
- Deterministic synthetic data generation

---

## Tech Stack

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy 2.0 (async)
- PostgreSQL
- Redis
- Celery

### Database & Migrations
- Alembic
- psycopg (sync driver for migrations)
- asyncpg (async driver for runtime)

### Computer Vision
- PyTorch
- OpenCV
- Custom synthetic defect generator

### Infrastructure
- Docker
- Docker Compose
- uv (modern dependency management)

---

## Core Components

### 1. Synthetic Data Generator
Generates controllable carbon fiber–like textures with injected defects:

- Cracks
- Voids / porosity
- Delamination-like regions
- Controlled severity scaling
- Domain randomization (lighting, blur, noise)

Each generated image includes structured metadata for reproducibility.

---

### 2. Defect Detection Pipeline
- Image ingestion
- Preprocessing
- Defect detection (classical + lightweight DL)
- Severity estimation
- Structured defect representation

---

### 3. Explainable LLM Layer
The LLM does not operate on raw images.

Instead, it receives:

- Defect type
- Severity score
- Area estimate
- Material context

It produces:

- Engineering risk explanation
- Structural impact summary
- Recommended action

This avoids hallucination by grounding reasoning in structured outputs.

---

### 4. Database Schema Management

Schema evolution is version-controlled using Alembic.

Migrations are explicit and reproducible.

The `alembic_version` table tracks applied revisions, ensuring:

- Deterministic schema evolution
- Safe production upgrades
- Reproducibility across environments

---

## Project Structure

```
backend/
├── app/
│ ├── api/
│ ├── core/
│ ├── domain/
│ ├── infrastructure/
│ ├── workers/
│ └── main.py
├── alembic/
│ ├── env.py
│ └── versions/
├── pyproject.toml
├── Dockerfile
```

---

## Running the System

### Build

```
docker compose build
```

### Start services

```
docker compose up
```


### Apply database migrations

```
docker compose run backend alembic upgrade head
```

---

## Research-Relevant Contributions

This project demonstrates:

- Integration of CV and LLM systems
- Async backend design for ML pipelines
- Schema versioning discipline
- Reproducible data generation
- Explainability-focused architecture

It is positioned as a systems-oriented AI project rather than a notebook-based model experiment.

---

## Potential Extensions

- Multi-class defect detection
- NDT image integration (ultrasound / thermography)
- Bayesian severity estimation
- Uncertainty calibration
- Active learning over synthetic data
- Deployment benchmarking under constrained GPU

---

## Intended Audience

This project is suitable for:

- AI/ML research internships
- Applied computer vision labs
- Systems-oriented AI programs
- Aerospace / materials research groups

It emphasizes engineering discipline alongside ML experimentation.

---

## License

MIT