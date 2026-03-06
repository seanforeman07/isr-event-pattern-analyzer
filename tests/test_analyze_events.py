from pathlib import Path

from src.analyze_events import cluster_hotspots, load_events, score_priority_areas


def test_pipeline_runs_on_sample_data() -> None:
    root = Path(__file__).resolve().parents[1]
    df = load_events(root / "data" / "events_sample.csv")
    clustered = cluster_hotspots(df)
    ranking = score_priority_areas(clustered)

    assert "cluster_id" in clustered.columns
    assert "priority_score" in ranking.columns or ranking.empty
