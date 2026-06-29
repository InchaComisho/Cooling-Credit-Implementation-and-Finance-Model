"""
Tourism Resource Recovery Simulation

Conceptual deterministic model for Cooling Credit tourism-resource recovery.
It compares conventional tourism development with regenerative tourism based on
natural cooling, water-cycle recovery, ecosystem recovery, landscape value,
visitor comfort, Cooling Credit value, and local reinvestment.

This is not a forecast. Replace assumptions with local measured data before use.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUTPUT_DIR = Path("outputs")
YEARS = np.arange(0, 16)


@dataclass(frozen=True)
class TourismScenario:
    name: str
    infrastructure_development: float
    water_cycle_recovery: float
    greening_evapotranspiration: float
    marine_lake_recovery: float
    landscape_restoration: float
    biodiversity_recovery: float
    mist_heat_reduction: float
    local_reinvestment: float
    mrv_confidence: float
    overtourism_pressure: float


SCENARIOS: List[TourismScenario] = [
    TourismScenario("Degraded Destination", 0.10, 0.05, 0.05, 0.05, 0.08, 0.05, 0.00, 0.05, 0.35, 0.20),
    TourismScenario("Conventional Tourism Development", 0.85, 0.10, 0.12, 0.08, 0.25, 0.08, 0.08, 0.18, 0.45, 0.80),
    TourismScenario("Cooling Tourism Recovery", 0.45, 0.75, 0.70, 0.65, 0.70, 0.60, 0.55, 0.60, 0.75, 0.35),
    TourismScenario("Integrated Regenerative Destination", 0.60, 0.85, 0.85, 0.80, 0.85, 0.78, 0.65, 0.82, 0.82, 0.30),
]


def growth(year: np.ndarray, strength: float, speed: float, delay: float = 0.0) -> np.ndarray:
    shifted = np.maximum(year - delay, 0)
    return strength * (1.0 - np.exp(-speed * shifted))


def simulate(s: TourismScenario) -> pd.DataFrame:
    y = YEARS.astype(float)
    infra = growth(y, s.infrastructure_development, 0.22, 0.5)
    water = growth(y, s.water_cycle_recovery, 0.16, 1.0)
    green = growth(y, s.greening_evapotranspiration, 0.14, 1.0)
    marine_lake = growth(y, s.marine_lake_recovery, 0.12, 1.5)
    landscape = growth(y, s.landscape_restoration, 0.18, 0.5)
    biodiversity = growth(y, s.biodiversity_recovery, 0.11, 2.0)
    mist = growth(y, s.mist_heat_reduction, 0.28, 0.3)
    reinvestment = growth(y, s.local_reinvestment, 0.16, 1.0)
    overtourism = growth(y, s.overtourism_pressure, 0.22, 0.5)

    natural_cooling_asset_index = np.clip(100 * (0.25 * water + 0.25 * green + 0.15 * marine_lake + 0.20 * mist + 0.15 * biodiversity) * s.mrv_confidence, 0, 100)
    water_landscape_ecosystem_index = np.clip(100 * (0.25 * water + 0.20 * marine_lake + 0.20 * landscape + 0.20 * biodiversity + 0.15 * green) * s.mrv_confidence, 0, 100)
    destination_comfort_index = np.clip(100 * (0.30 * natural_cooling_asset_index / 100 + 0.25 * landscape + 0.15 * infra + 0.15 * water + 0.15 * mist) * (1 - 0.35 * overtourism), 0, 100)
    visitor_stay_income_index = np.clip(100 * (0.30 * destination_comfort_index / 100 + 0.25 * landscape + 0.20 * infra + 0.15 * reinvestment + 0.10 * biodiversity) * (1 - 0.25 * overtourism), 0, 100)
    disaster_pressure_reduction_index = np.clip(100 * (0.30 * water + 0.25 * green + 0.20 * marine_lake + 0.15 * natural_cooling_asset_index / 100 + 0.10 * biodiversity) * s.mrv_confidence, 0, 100)
    overtourism_risk_index = np.clip(100 * (0.65 * overtourism + 0.25 * infra - 0.25 * reinvestment - 0.15 * biodiversity), 0, 100)

    local_economic_cobenefit_index = np.clip(100 * (0.30 * visitor_stay_income_index / 100 + 0.20 * reinvestment + 0.20 * landscape + 0.15 * biodiversity + 0.15 * destination_comfort_index / 100), 0, 100)
    tourism_cooling_credit_value = (
        natural_cooling_asset_index
        * s.mrv_confidence
        * (0.5 + water_landscape_ecosystem_index / 100)
        * (0.5 + local_economic_cobenefit_index / 100)
        * (1 - 0.25 * overtourism_risk_index / 100)
    )

    return pd.DataFrame(
        {
            "year": YEARS,
            "scenario": s.name,
            "natural_cooling_asset_index": natural_cooling_asset_index,
            "water_landscape_ecosystem_index": water_landscape_ecosystem_index,
            "destination_comfort_index": destination_comfort_index,
            "visitor_stay_income_index": visitor_stay_income_index,
            "disaster_pressure_reduction_index": disaster_pressure_reduction_index,
            "local_economic_cobenefit_index": local_economic_cobenefit_index,
            "overtourism_risk_index": overtourism_risk_index,
            "tourism_cooling_credit_value": tourism_cooling_credit_value,
        }
    )


def plot_metric(df: pd.DataFrame, metric: str, title: str, ylabel: str, filename: str) -> None:
    plt.figure(figsize=(10, 6))
    for name, group in df.groupby("scenario"):
        plt.plot(group["year"], group[metric], marker="o", label=name)
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=160)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.concat([simulate(s) for s in SCENARIOS], ignore_index=True)
    df.to_csv(OUTPUT_DIR / "tourism_resource_recovery_timeseries.csv", index=False)

    plots: Dict[str, tuple[str, str, str]] = {
        "tourism_cooling_credit_value": ("Tourism Cooling Credit Value", "Composite value index", "tourism_cooling_credit_value.png"),
        "destination_comfort_index": ("Destination Comfort Index", "Index (0-100)", "destination_comfort_index.png"),
        "natural_cooling_asset_index": ("Natural Cooling Asset Index", "Index (0-100)", "natural_cooling_asset_index.png"),
        "water_landscape_ecosystem_index": ("Water, Landscape, and Ecosystem Index", "Index (0-100)", "water_landscape_ecosystem_index.png"),
        "visitor_stay_income_index": ("Visitor Stay and Income Index", "Index (0-100)", "visitor_stay_income_index.png"),
        "overtourism_risk_index": ("Overtourism Risk Index", "Index (0-100)", "overtourism_risk_index.png"),
    }
    for metric, (title, ylabel, filename) in plots.items():
        plot_metric(df, metric, title, ylabel, filename)

    final = df[df["year"] == YEARS[-1]].sort_values("tourism_cooling_credit_value", ascending=False)
    final.to_csv(OUTPUT_DIR / "tourism_resource_recovery_final_summary.csv", index=False)
    print(final[["scenario", "tourism_cooling_credit_value", "destination_comfort_index", "natural_cooling_asset_index", "visitor_stay_income_index", "overtourism_risk_index"]].to_string(index=False))


if __name__ == "__main__":
    main()
