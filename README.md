# ISR Event Pattern Analyzer

Defense-focused analytics project that ingests ISR-style event logs, identifies hotspot regions and anomalous activity, and produces analyst-ready outputs.

## Stack
- Python 3.11+
- pandas
- scikit-learn
- streamlit (optional dashboard)

## Project Structure
- `data/events_sample.csv`: simulated ISR events
- `src/analyze_events.py`: hotspot + anomaly analysis pipeline
- `tests/test_analyze_events.py`: starter tests

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/analyze_events.py
```

## Resume Angle
- Built geospatial-temporal anomaly detection for ISR event triage.
- Produced priority area rankings to support analyst decision-making.
