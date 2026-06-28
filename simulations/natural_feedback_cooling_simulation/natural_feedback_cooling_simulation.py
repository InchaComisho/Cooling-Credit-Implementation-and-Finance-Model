"""
Natural Feedback Cooling Simulation

Conceptual deterministic model for comparing carbon-credit-style accounting
with Cooling Credit implementation scenarios based on physical cooling,
water retention, evapotranspiration, humus regeneration, forest recovery,
and local economic co-benefits.

This is not a forecast. Replace all assumptions with locally measured data
before policy, insurance, subsidy, or investment use.
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
class Scenario:
    name: str
    implementation_strength: float
    urban_mist: float
    humus_recovery: float
    forest_recovery: float
    water_cycle_recovery: float
    mrv_confidence: float
    local_participation: float
    credit_revenue_growth: float


SCENARIOS: List[Scenario] = [
    Scenario(
        name="Accounting Offset Only",
        implementation_strength=0.10,
        urban_mist=0.00,
        humus_recovery=0.00,
        forest_recovery=0.00,
        water_cycle_recovery=0.00,
        mrv_confidence=0.45,
        local_participation=0.10,
        credit_revenue_growth=0.10,
    ),
    Scenario(
        name="Urban Mist Cooling",
        implementation_strength=0.45,
        urban_mist=0.80,
        humus_recovery=0.10,
        forest_recovery=0.05,
        water_cycle_recovery=0.25,
        mrv_confidence=0.75,
        local_participation=0.45,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="Organic Waste to Humus",
        implementation_strength=0.55,
        urban_mist=0.10,
        humus_recovery=0.85,
        forest_recovery=0.20,
        water_cycle_recovery=0.45,
        mrv_confidence=0.70,
        local_participation=0.65,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="Forest Regeneration",
        implementation_strength=0.60,
        urban_mist=0.05,
        humus_recovery=0.45,
        forest_recovery=0.90,
        water_cycle_recovery=0.65,
        mrv_confidence=0.68,
        local_participation=0.70,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="Integrated Natural Feedback",
        implementation_strength=0.85,
        urban_mist=0.55,
        humus_recovery=0.85,
        forest_recovery=0.85,
        water_cycle_recovery=0.90,
        mrv_confidence=0.82,
        local_participation=0.85,
        credit_revenue_growth=0.06,
    ),
]


def saturating_growth(year: np.ndarray, strength: float, speed: float = 0.13, delay: float = 2.0) -> np.ndarray:
    """Smooth adoption / ecological recovery curve from 0 to strength."""
    shifted = np.maximum(year - delay, 0)
    return strength * (1.0 - np.exp(-speed * shifted))


def simulate_scenario(scenario: Scenario) -> pd.DataFrame:
    y = YEARS.astype(float)

    adoption = saturating_growth(y, scenario.implementation_strength, speed=0.18)
    urban = saturating_growth(y, scenario.urban_mist, speed=0.28, delay=0.5)
    humus = saturating_growth(y, scenario.humus_recovery, speed=0.16, delay=1.0)
    forest = saturating_growth(y, scenario.forest_recovery, speed=0.10, delay=3.0)
    water_cycle = saturating_growth(y, scenario.water_cycle_recovery, speed=0.12, delay=2.0)

    # Carbon-credit-style revenue can rise without guaranteeing physical cooling.
    accounting_revenue_index = 100.0 * ((1.0 + scenario.credit_revenue_growth) ** y)

    # Organic waste-to-humus conversion: faster than forest recovery, slower than mist deployment.
    waste_to_humus_conversion_rate = np.clip(0.08 + 0.75 * humus * adoption, 0, 0.90)

    soil_microbial_recovery_index = np.clip(100 * (0.15 + 0.55 * humus + 0.20 * forest + 0.10 * water_cycle), 0, 100)
    water_retention_index = np.clip(100 * (0.20 * urban + 0.45 * humus + 0.25 * forest + 0.35 * water_cycle), 0, 100)
    evapotranspiration_recovery_index = np.clip(100 * (0.10 * urban + 0.35 * humus + 0.35 * forest + 0.40 * water_cycle), 0, 100)
    urban_heat_island_reduction_index = np.clip(100 * (0.60 * urban + 0.15 * humus + 0.10 * forest + 0.20 * water_cycle), 0, 100)

    # Physical cooling is a composite of immediate urban cooling and slower natural feedback recovery.
    physical_cooling_index = np.clip(
        100
        * (
            0.30 * urban
            + 0.20 * humus
            + 0.20 * forest
            + 0.30 * water_cycle
        )
        * scenario.mrv_confidence,
        0,
        100,
    )

    disaster_pressure_reduction_index = np.clip(
        100
        * (
            0.20 * urban_heat_island_reduction_index / 100
            + 0.30 * water_retention_index / 100
            + 0.25 * evapotranspiration_recovery_index / 100
            + 0.25 * forest
        )
        * scenario.mrv_confidence,
        0,
        100,
    )

    local_economic_cobenefit_index = np.clip(
        100
        * (
            0.20 * waste_to_humus_conversion_rate
            + 0.20 * humus
            + 0.20 * forest
            + 0.15 * urban
            + 0.25 * scenario.local_participation
        ),
        0,
        100,
    )

    natural_cooling_function_recovery_factor = np.clip(
        0.30
        + 0.25 * humus
        + 0.25 * forest
        + 0.30 * water_cycle
        + 0.10 * scenario.local_participation,
        0,
        1.50,
    )

    local_cobenefit_factor = np.clip(0.50 + local_economic_cobenefit_index / 100.0, 0.5, 1.5)

    # Conceptual credit value. Area and duration are normalized here.
    cooling_credit_value = (
        physical_cooling_index
        * scenario.mrv_confidence
        * natural_cooling_function_recovery_factor
        * local_cobenefit_factor
    )

    # Accounting-only value highlights market growth independent of physical cooling.
    accounting_offset_value = accounting_revenue_index * scenario.mrv_confidence

    return pd.DataFrame(
        {
            "year": YEARS,
            "scenario": scenario.name,
            "adoption_index": adoption * 100,
            "accounting_revenue_index": accounting_revenue_index,
            "accounting_offset_value": accounting_offset_value,
            "waste_to_humus_conversion_rate": waste_to_humus_conversion_rate * 100,
            "soil_microbial_recovery_index": soil_microbial_recovery_index,
            "water_retention_index": water_retention_index,
            "evapotranspiration_recovery_index": evapotranspiration_recovery_index,
            "urban_heat_island_reduction_index": urban_heat_island_reduction_index,
            "physical_cooling_index": physical_cooling_index,
            "disaster_pressure_reduction_index": disaster_pressure_reduction_index,
            "local_economic_cobenefit_index": local_economic_cobenefit_index,
            "natural_cooling_function_recovery_factor": natural_cooling_function_recovery_factor,
            "local_cobenefit_factor": local_cobenefit_factor,
            "cooling_credit_value": cooling_credit_value,
        }
    )


def plot_metric(df: pd.DataFrame, metric: str, title: str, ylabel: str, filename: str) -> None:
    plt.figure(figsize=(10, 6))
    for scenario_name, group in df.groupby("scenario"):
        plt.plot(group["year"], group[metric], marker="o", label=scenario_name)
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

    frames = [simulate_scenario(s) for s in SCENARIOS]
    df = pd.concat(frames, ignore_index=True)
    df.to_csv(OUTPUT_DIR / "natural_feedback_cooling_timeseries.csv", index=False)

    plots: Dict[str, tuple[str, str, str]] = {
        "cooling_credit_value": (
            "Cooling Credit Value: Physical Cooling + Natural Feedback + Co-benefits",
            "Composite value index",
            "cooling_credit_value.png",
        ),
        "physical_cooling_index": (
            "Physical Cooling Index",
            "Index (0-100)",
            "physical_cooling_index.png",
        ),
        "water_retention_index": (
            "Water Retention Recovery Index",
            "Index (0-100)",
            "water_retention_index.png",
        ),
        "evapotranspiration_recovery_index": (
            "Evapotranspiration Recovery Index",
            "Index (0-100)",
            "evapotranspiration_recovery_index.png",
        ),
        "disaster_pressure_reduction_index": (
            "Disaster Pressure Reduction Index",
            "Index (0-100)",
            "disaster_pressure_reduction_index.png",
        ),
        "local_economic_cobenefit_index": (
            "Local Economic Co-benefit Index",
            "Index (0-100)",
            "local_economic_cobenefit_index.png",
        ),
    }

    for metric, (title, ylabel, filename) in plots.items():
        plot_metric(df, metric, title, ylabel, filename)

    final_year = df[df["year"] == YEARS[-1]].copy()
    final_year = final_year.sort_values("cooling_credit_value", ascending=False)

    print("Natural Feedback Cooling Simulation complete")
    print("Outputs written to:", OUTPUT_DIR.resolve())
    print("\nFinal-year scenario ranking by Cooling Credit Value:")
    print(
        final_year[
            [
                "scenario",
                "cooling_credit_value",
                "physical_cooling_index",
                "water_retention_index",
                "evapotranspiration_recovery_index",
                "disaster_pressure_reduction_index",
                "local_economic_cobenefit_index",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
