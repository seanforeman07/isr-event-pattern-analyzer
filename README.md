# ISR Event Pattern Analyzer

Python defense analytics project that detects ISR hotspot clusters and ranks priority areas from simulated event logs.

## Mission Question
Which geographic areas should be prioritized for analyst review based on event density, confidence, and threat level?

## Technical Scope
- Ingest ISR-style event data with timestamp and geospatial coordinates.
- Detect hotspots with `DBSCAN` clustering.
- Compute a weighted priority score by cluster.
- Output ranked clusters for triage workflows.

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
- Built an ISR event triage pipeline to convert raw geospatial activity into ranked analyst priorities.
- Combined clustering and weighted threat scoring to support faster, evidence-based review.

## Interview Talking Points
- Why `DBSCAN` was selected for unknown cluster counts and noisy geospatial data.
- Tradeoffs in `eps`/`min_samples` and how those parameters change cluster sensitivity.
- How to extend this baseline with time-window drift detection and map visualization.
