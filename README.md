# ISR Event Pattern Analyzer

Developed a Python analytics pipeline that identifies ISR event hotspots and ranks priority areas for analyst review using clustering and threat scoring.

## Mission Question
Which geographic areas should analysts prioritize for review based on event density, confidence levels, and threat indicators?

## Technical Scope
- Ingest ISR-style event data containing timestamps and geospatial coordinates.
- Applied DBSCAN clustering to detect activity hotspots without requiring a predefined cluster count.
- Calculated a weighted priority score using event density, confidence levels, and threat indicators.
- Generated ranked cluster outputs supporting analyst triage workflows.

## Stack
- Python 3.11+
- pandas
- scikit-learn
- pytest

## Repository Structure
- `data/events_sample.csv`: simulated ISR events
- `src/analyze_events.py`: clustering + priority scoring pipeline
- `tests/test_analyze_events.py`: pipeline smoke test
- `requirements.txt`: pinned dependencies

## Run Locally
```bash
cd /Users/seanforeman/Documents/Playground/isr-event-pattern-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/analyze_events.py
python -m pytest -q
```

## Expected Output
Running `python src/analyze_events.py` prints:
- `=== Top Priority Areas ===`
- A ranked table with `cluster_id`, `event_count`, `avg_confidence`, `avg_threat`, and `priority_score`

Running tests prints:
- `1 passed`

## Resume-Ready Impact
- Built an ISR event clustering pipeline converting geospatial activity logs into prioritized analyst review areas.
- Combined density-based clustering and weighted threat scoring to support rapid triage of operational events.
