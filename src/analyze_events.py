from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.cluster import DBSCAN


def load_events(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df


def cluster_hotspots(df: pd.DataFrame, eps: float = 0.15, min_samples: int = 2) -> pd.DataFrame:
    clustered = df.copy()
    coords = clustered[["lat", "lon"]]
    model = DBSCAN(eps=eps, min_samples=min_samples)
    clustered["cluster_id"] = model.fit_predict(coords)
    return clustered


def score_priority_areas(df: pd.DataFrame) -> pd.DataFrame:
    filtered = df[df["cluster_id"] >= 0]
    if filtered.empty:
        return pd.DataFrame(columns=["cluster_id", "event_count", "avg_confidence", "avg_threat", "priority_score"])

    summary = (
        filtered.groupby("cluster_id", as_index=False)
        .agg(
            event_count=("event_id", "count"),
            avg_confidence=("confidence", "mean"),
            avg_threat=("threat_score", "mean"),
        )
    )
    summary["priority_score"] = (
        summary["event_count"] * 0.4
        + summary["avg_confidence"] * 100 * 0.3
        + summary["avg_threat"] * 0.3
    )
    return summary.sort_values("priority_score", ascending=False)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    events_path = root / "data" / "events_sample.csv"
    df = load_events(events_path)
    clustered = cluster_hotspots(df)
    ranking = score_priority_areas(clustered)

    print("=== Top Priority Areas ===")
    if ranking.empty:
        print("No clusters detected with current parameters.")
    else:
        print(ranking.to_string(index=False))


if __name__ == "__main__":
    main()
