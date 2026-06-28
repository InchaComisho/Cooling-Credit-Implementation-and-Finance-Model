"""
Forest Conversion Business Simulation

Conceptual deterministic model for converting abandoned or monoculture mountain
forests into native-fruit mixed forests, watershed forests, mushroom forests,
wild edible forests, tourism / education forests, and Cooling Credit assets.

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
YEARS = np.arange(0, 21)


@dataclass(frozen=True)
class ForestScenario:
    name: str
    thinning_management: float
    humus_recovery: float
    broadleaf_native_recovery: float
    fruit_wild_edible_zone: float
    mushroom_forest_zone: float
    watershed_protection: float
    biodiversity_corridor: float
    tourism_education_access: float
    owner_participation: float
    mrv_confidence: float
    overharvest_risk: float


SCENARIOS: List[ForestScenario] = [
    ForestScenario("Abandoned Monoculture", 0.05, 0.05, 0.03, 0.00, 0.00, 0.08, 0.05, 0.00, 0.05, 0.35, 0.10),
    ForestScenario("Timber-Only Management", 0.75, 0.15, 0.08, 0.00, 0.03, 0.18, 0.08, 0.08, 0.30, 0.50, 0.45),
    ForestScenario("Native-Fruit Mixed Forest", 0.55, 0.70, 0.75, 0.65, 0.55, 0.70, 0.65, 0.40, 0.62, 0.72, 0.20),
    ForestScenario("Integrated Watershed Food Tourism Forest", 0.65, 0.82, 0.85, 0.75, 0.68, 0.85, 0.80, 0.70, 0.78, 0.80, 0.18),
]


def growth(year: np.ndarray, strength: float, speed: float, delay: float = 0.0) -> np.ndarray:
    shifted = np.maximum(year - delay, 0)
    return strength * (1.0 - np.exp(-speed * shifted))


def simulate(s: ForestScenario) -> pd.DataFrame:
    y = YEARS.astype(float)
    thinning = growth(y, s.thinning_management, 0.16, 0.5)
    humus = growth(y, s.humus_recovery, 0.12, 1.0)
    broadleaf = growth(y, s.broadleaf_native_recovery, 0.10, 2.5)
    fruit = growth(y, s.fruit_wild_edible_zone, 0.13, 2.0)
    mushroom = growth(y, s.mushroom_forest_zone, 0.14, 1.5)
    watershed = growth(y, s.watershed_protection, 0.12, 1.0)
    biodiversity = growth(y, s.biodiversity_corridor, 0.10, 2.0)
    tourism = growth(y, s.tourism_education_access, 0.16, 2.0)
    owner = growth(y, s.owner_participation, 0.14, 0.5)
    overharvest = growth(y, s.overharvest_risk, 0.18, 0.5)

    watershed_retention_index = np.clip(100 * (0.30 * watershed + 0.25 * humus + 0.20 * broadleaf + 0.15 * thinning + 0.10 * biodiversity) * s.mrv_confidence, 0, 100)
    forest_surface_cooling_index = np.clip(100 * (0.25 * broadleaf + 0.25 * watershed + 0.20 * humus + 0.15 * biodiversity + 0.15 * fruit) * s.mrv_confidence, 0, 100)
    biodiversity_recovery_index = np.clip(100 * (0.30 * biodiversity + 0.25 * broadleaf + 0.15 * watershed + 0.15 * mushroom + 0.15 * fruit) * s.mrv_confidence, 0, 100)
    food_tourism_income_index = np.clip(100 * (0.25 * fruit + 0.20 * mushroom + 0.20 * tourism + 0.15 * owner + 0.10 * broadleaf + 0.10 * thinning) * (1 - 0.20 * overharvest), 0, 100)
    wildfire_erosion_risk_reduction_index = np.clip(100 * (0.25 * thinning + 0.25 * watershed + 0.20 * humus + 0.15 * broadleaf + 0.15 * biodiversity) * s.mrv_confidence, 0, 100)
    owner_income_stability_index = np.clip(100 * (0.25 * food_tourism_income_index / 100 + 0.20 * owner + 0.20 * thinning + 0.15 * tourism + 0.10 * mushroom + 0.10 * fruit), 0, 100)

    forest_cooling_credit_value = (
        forest_surface_cooling_index
        * s.mrv_confidence
        * (0.5 + watershed_retention_index / 100)
        * (0.5 + biodiversity_recovery_index / 100)
        * (0.5 + owner_income_stability_index / 100)
        * (1 - 0.30 * overharvest)
    )

    return pd.DataFrame(
        {
            "year": YEARS,
            "scenario": s.name,
            "watershed_retention_index": watershed_retention_index,
            "forest_surface_cooling_index": forest_surface_cooling_index,
            "biodiversity_recovery_index": biodiversity_recovery_index,
            "food_tourism_income_index": food_tourism_income_index,
            "wildfire_erosion_risk_reduction_index": wildfire_erosion_risk_reduction_index,
            "owner_income_stability_index": owner_income_stability_index,
            "overharvest_risk_index": overharvest * 100,
            "forest_cooling_credit_value": forest_cooling_credit_value,
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
    df.to_csv(OUTPUT_DIR / "forest_conversion_timeseries.csv", index=False)

    plots: Dict[str, tuple[str, str, str]] = {
        "forest_cooling_credit_value": ("Forest Cooling Credit Value", "Composite value index", "forest_cooling_credit_value.png"),
        "watershed_retention_index": ("Watershed Retention Index", "Index (0-100)", "watershed_retention_index.png"),
        "forest_surface_cooling_index": ("Forest Surface Cooling Index", "Index (0-100)", "forest_surface_cooling_index.png"),
        "biodiversity_recovery_index": ("Biodiversity Recovery Index", "Index (0-100)", "biodiversity_recovery_index.png"),
        "food_tourism_income_index": ("Food and Tourism Income Index", "Index (0-100)", "food_tourism_income_index.png"),
        "wildfire_erosion_risk_reduction_index": ("Wildfire and Erosion Risk Reduction Index", "Index (0-100)", "wildfire_erosion_risk_reduction_index.png"),
    }
    for metric, (title, ylabel, filename) in plots.items():
        plot_metric(df, metric, title, ylabel, filename)

    final = df[df["year"] == YEARS[-1]].sort_values("forest_cooling_credit_value", ascending=False)
    final.to_csv(OUTPUT_DIR / "forest_conversion_final_summary.csv", index=False)
    print(final[["scenario", "forest_cooling_credit_value", "watershed_retention_index", "forest_surface_cooling_index", "biodiversity_recovery_index", "food_tourism_income_index", "wildfire_erosion_risk_reduction_index"]].to_string(index=False))


if __name__ == "__main__":
    main()
