"""
Natural Feedback Cooling Simulation

Conceptual deterministic model for comparing carbon-credit-style accounting
with Cooling Credit implementation scenarios based on physical cooling,
water retention, evapotranspiration, humus regeneration, forest recovery,
EEZ ocean cooling, oxygenation, fishery recovery, coastal desert-edge
regeneration, underground settlement efficiency, and local economic co-benefits.

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
    ocean_circulation: float
    ocean_cooling: float
    ocean_oxygenation: float
    phytoplankton_fishery: float
    coral_tourism: float
    desert_desalination: float
    desert_mist: float
    desert_humus: float
    desert_vegetation: float
    desert_energy: float
    underground_efficiency: float
    ecological_safety: float
    desert_safety: float
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
        ocean_circulation=0.00,
        ocean_cooling=0.00,
        ocean_oxygenation=0.00,
        phytoplankton_fishery=0.00,
        coral_tourism=0.00,
        desert_desalination=0.00,
        desert_mist=0.00,
        desert_humus=0.00,
        desert_vegetation=0.00,
        desert_energy=0.00,
        underground_efficiency=0.00,
        ecological_safety=1.00,
        desert_safety=1.00,
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
        ocean_circulation=0.03,
        ocean_cooling=0.02,
        ocean_oxygenation=0.03,
        phytoplankton_fishery=0.02,
        coral_tourism=0.05,
        desert_desalination=0.05,
        desert_mist=0.12,
        desert_humus=0.03,
        desert_vegetation=0.04,
        desert_energy=0.05,
        underground_efficiency=0.03,
        ecological_safety=1.00,
        desert_safety=0.95,
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
        ocean_circulation=0.02,
        ocean_cooling=0.02,
        ocean_oxygenation=0.02,
        phytoplankton_fishery=0.02,
        coral_tourism=0.02,
        desert_desalination=0.04,
        desert_mist=0.05,
        desert_humus=0.25,
        desert_vegetation=0.10,
        desert_energy=0.03,
        underground_efficiency=0.02,
        ecological_safety=1.00,
        desert_safety=0.95,
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
        ocean_circulation=0.05,
        ocean_cooling=0.04,
        ocean_oxygenation=0.05,
        phytoplankton_fishery=0.04,
        coral_tourism=0.08,
        desert_desalination=0.02,
        desert_mist=0.03,
        desert_humus=0.10,
        desert_vegetation=0.18,
        desert_energy=0.03,
        underground_efficiency=0.02,
        ecological_safety=1.00,
        desert_safety=0.95,
        mrv_confidence=0.68,
        local_participation=0.70,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="EEZ Ocean Cooling",
        implementation_strength=0.65,
        urban_mist=0.05,
        humus_recovery=0.05,
        forest_recovery=0.05,
        water_cycle_recovery=0.55,
        ocean_circulation=0.85,
        ocean_cooling=0.80,
        ocean_oxygenation=0.90,
        phytoplankton_fishery=0.75,
        coral_tourism=0.65,
        desert_desalination=0.05,
        desert_mist=0.06,
        desert_humus=0.03,
        desert_vegetation=0.05,
        desert_energy=0.08,
        underground_efficiency=0.04,
        ecological_safety=0.82,
        desert_safety=0.95,
        mrv_confidence=0.78,
        local_participation=0.72,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="Coastal Desert Edge Regeneration",
        implementation_strength=0.68,
        urban_mist=0.20,
        humus_recovery=0.35,
        forest_recovery=0.12,
        water_cycle_recovery=0.60,
        ocean_circulation=0.02,
        ocean_cooling=0.02,
        ocean_oxygenation=0.03,
        phytoplankton_fishery=0.02,
        coral_tourism=0.05,
        desert_desalination=0.85,
        desert_mist=0.75,
        desert_humus=0.80,
        desert_vegetation=0.70,
        desert_energy=0.85,
        underground_efficiency=0.75,
        ecological_safety=1.00,
        desert_safety=0.82,
        mrv_confidence=0.76,
        local_participation=0.74,
        credit_revenue_growth=0.05,
    ),
    Scenario(
        name="Integrated Natural Feedback",
        implementation_strength=0.92,
        urban_mist=0.55,
        humus_recovery=0.85,
        forest_recovery=0.85,
        water_cycle_recovery=0.90,
        ocean_circulation=0.65,
        ocean_cooling=0.60,
        ocean_oxygenation=0.65,
        phytoplankton_fishery=0.55,
        coral_tourism=0.40,
        desert_desalination=0.65,
        desert_mist=0.55,
        desert_humus=0.75,
        desert_vegetation=0.70,
        desert_energy=0.70,
        underground_efficiency=0.60,
        ecological_safety=0.88,
        desert_safety=0.86,
        mrv_confidence=0.85,
        local_participation=0.87,
        credit_revenue_growth=0.06,
    ),
]


def saturating_growth(year: np.ndarray, strength: float, speed: float = 0.13, delay: float = 2.0) -> np.ndarray:
    """Smooth adoption / ecological recovery curve from 0 to strength."""
    shifted = np.maximum(year - delay, 0)
    return strength * (1.0 - np.exp(-speed * shifted))


def simulate_scenario(scenario: Scenario) -> pd.DataFrame:
    y = YEARS.astype(float)

    adoption = saturating_growth(y, scenario.implementation_strength, speed=0.18, delay=0.0)
    urban = saturating_growth(y, scenario.urban_mist, speed=0.28, delay=0.5)
    humus = saturating_growth(y, scenario.humus_recovery, speed=0.16, delay=1.0)
    forest = saturating_growth(y, scenario.forest_recovery, speed=0.10, delay=3.0)
    water_cycle = saturating_growth(y, scenario.water_cycle_recovery, speed=0.12, delay=2.0)
    ocean_circulation = saturating_growth(y, scenario.ocean_circulation, speed=0.16, delay=1.5)
    ocean_cooling = saturating_growth(y, scenario.ocean_cooling, speed=0.18, delay=1.0)
    ocean_oxygenation = saturating_growth(y, scenario.ocean_oxygenation, speed=0.18, delay=1.0)
    phytoplankton_fishery = saturating_growth(y, scenario.phytoplankton_fishery, speed=0.12, delay=3.0)
    coral_tourism = saturating_growth(y, scenario.coral_tourism, speed=0.10, delay=4.0)
    desert_desalination = saturating_growth(y, scenario.desert_desalination, speed=0.16, delay=0.5)
    desert_mist = saturating_growth(y, scenario.desert_mist, speed=0.22, delay=0.5)
    desert_humus = saturating_growth(y, scenario.desert_humus, speed=0.14, delay=1.5)
    desert_vegetation = saturating_growth(y, scenario.desert_vegetation, speed=0.10, delay=3.0)
    desert_energy = saturating_growth(y, scenario.desert_energy, speed=0.20, delay=0.5)
    underground_efficiency = saturating_growth(y, scenario.underground_efficiency, speed=0.18, delay=1.0)

    accounting_revenue_index = 100.0 * ((1.0 + scenario.credit_revenue_growth) ** y)
    waste_to_humus_conversion_rate = np.clip(0.08 + 0.75 * humus * adoption, 0, 0.90)

    soil_microbial_recovery_index = np.clip(100 * (0.15 + 0.55 * humus + 0.20 * forest + 0.10 * water_cycle + 0.10 * desert_humus), 0, 100)
    water_retention_index = np.clip(100 * (0.17 * urban + 0.34 * humus + 0.20 * forest + 0.27 * water_cycle + 0.06 * ocean_circulation + 0.20 * desert_humus + 0.15 * desert_desalination + 0.10 * desert_vegetation), 0, 100)
    evapotranspiration_recovery_index = np.clip(100 * (0.08 * urban + 0.30 * humus + 0.30 * forest + 0.34 * water_cycle + 0.14 * desert_vegetation + 0.10 * desert_humus), 0, 100)
    urban_heat_island_reduction_index = np.clip(100 * (0.60 * urban + 0.15 * humus + 0.10 * forest + 0.20 * water_cycle + 0.08 * desert_mist), 0, 100)

    ocean_surface_cooling_index = np.clip(100 * (0.45 * ocean_cooling + 0.25 * ocean_circulation + 0.20 * ocean_oxygenation + 0.10 * water_cycle) * scenario.mrv_confidence * scenario.ecological_safety, 0, 100)
    dissolved_oxygen_recovery_index = np.clip(100 * (0.60 * ocean_oxygenation + 0.25 * ocean_circulation + 0.15 * water_cycle) * scenario.mrv_confidence * scenario.ecological_safety, 0, 100)
    marine_food_web_recovery_index = np.clip(100 * (0.40 * phytoplankton_fishery + 0.20 * ocean_oxygenation + 0.20 * ocean_circulation + 0.10 * coral_tourism + 0.10 * scenario.ecological_safety) * scenario.mrv_confidence, 0, 100)
    fishery_tourism_cobenefit_index = np.clip(100 * (0.30 * phytoplankton_fishery + 0.20 * coral_tourism + 0.20 * ocean_oxygenation + 0.15 * ocean_cooling + 0.15 * scenario.local_participation) * scenario.ecological_safety, 0, 100)

    desert_surface_cooling_index = np.clip(100 * (0.25 * desert_mist + 0.20 * desert_desalination + 0.20 * desert_vegetation + 0.15 * desert_humus + 0.10 * water_cycle + 0.10 * underground_efficiency) * scenario.mrv_confidence * scenario.desert_safety, 0, 100)
    desert_water_supply_index = np.clip(100 * (0.45 * desert_desalination + 0.20 * desert_mist + 0.20 * desert_humus + 0.15 * water_cycle) * scenario.mrv_confidence * scenario.desert_safety, 0, 100)
    humus_soil_settlement_index = np.clip(100 * (0.40 * desert_humus + 0.20 * humus + 0.20 * desert_vegetation + 0.10 * desert_desalination + 0.10 * scenario.desert_safety) * scenario.mrv_confidence, 0, 100)
    desert_vegetation_recovery_index = np.clip(100 * (0.35 * desert_vegetation + 0.25 * desert_humus + 0.20 * desert_desalination + 0.10 * desert_mist + 0.10 * water_cycle) * scenario.mrv_confidence * scenario.desert_safety, 0, 100)
    desert_energy_settlement_index = np.clip(100 * (0.35 * desert_energy + 0.30 * underground_efficiency + 0.15 * desert_desalination + 0.10 * desert_mist + 0.10 * scenario.local_participation) * scenario.mrv_confidence, 0, 100)

    physical_cooling_index = np.clip(100 * (0.18 * urban + 0.12 * humus + 0.12 * forest + 0.20 * water_cycle + 0.18 * (ocean_surface_cooling_index / 100.0) + 0.20 * (desert_surface_cooling_index / 100.0)) * scenario.mrv_confidence, 0, 100)
    disaster_pressure_reduction_index = np.clip(100 * (0.14 * urban_heat_island_reduction_index / 100.0 + 0.21 * water_retention_index / 100.0 + 0.17 * evapotranspiration_recovery_index / 100.0 + 0.16 * forest + 0.15 * ocean_surface_cooling_index / 100.0 + 0.17 * desert_water_supply_index / 100.0) * scenario.mrv_confidence, 0, 100)

    local_economic_cobenefit_index = np.clip(100 * (0.13 * waste_to_humus_conversion_rate + 0.13 * humus + 0.13 * forest + 0.10 * urban + 0.14 * fishery_tourism_cobenefit_index / 100.0 + 0.14 * desert_energy_settlement_index / 100.0 + 0.11 * desert_vegetation_recovery_index / 100.0 + 0.22 * scenario.local_participation), 0, 100)
    natural_cooling_function_recovery_factor = np.clip(0.30 + 0.16 * humus + 0.16 * forest + 0.22 * water_cycle + 0.16 * ocean_circulation + 0.16 * desert_vegetation + 0.12 * desert_humus + 0.10 * scenario.local_participation, 0, 1.80)
    local_cobenefit_factor = np.clip(0.50 + local_economic_cobenefit_index / 100.0, 0.5, 1.6)

    cooling_credit_value = physical_cooling_index * scenario.mrv_confidence * natural_cooling_function_recovery_factor * local_cobenefit_factor * scenario.ecological_safety * scenario.desert_safety
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
            "ocean_surface_cooling_index": ocean_surface_cooling_index,
            "dissolved_oxygen_recovery_index": dissolved_oxygen_recovery_index,
            "marine_food_web_recovery_index": marine_food_web_recovery_index,
            "fishery_tourism_cobenefit_index": fishery_tourism_cobenefit_index,
            "desert_surface_cooling_index": desert_surface_cooling_index,
            "desert_water_supply_index": desert_water_supply_index,
            "humus_soil_settlement_index": humus_soil_settlement_index,
            "desert_vegetation_recovery_index": desert_vegetation_recovery_index,
            "desert_energy_settlement_index": desert_energy_settlement_index,
            "physical_cooling_index": physical_cooling_index,
            "disaster_pressure_reduction_index": disaster_pressure_reduction_index,
            "local_economic_cobenefit_index": local_economic_cobenefit_index,
            "natural_cooling_function_recovery_factor": natural_cooling_function_recovery_factor,
            "local_cobenefit_factor": local_cobenefit_factor,
            "ecological_safety_factor": scenario.ecological_safety,
            "desert_safety_factor": scenario.desert_safety,
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
        "cooling_credit_value": ("Cooling Credit Value: Physical Cooling + Natural Feedback + Co-benefits", "Composite value index", "cooling_credit_value.png"),
        "physical_cooling_index": ("Physical Cooling Index", "Index (0-100)", "physical_cooling_index.png"),
        "water_retention_index": ("Water Retention Recovery Index", "Index (0-100)", "water_retention_index.png"),
        "evapotranspiration_recovery_index": ("Evapotranspiration Recovery Index", "Index (0-100)", "evapotranspiration_recovery_index.png"),
        "ocean_surface_cooling_index": ("Ocean Surface Cooling Index", "Index (0-100)", "ocean_surface_cooling_index.png"),
        "dissolved_oxygen_recovery_index": ("Dissolved Oxygen Recovery Index", "Index (0-100)", "dissolved_oxygen_recovery_index.png"),
        "marine_food_web_recovery_index": ("Marine Food Web Recovery Index", "Index (0-100)", "marine_food_web_recovery_index.png"),
        "fishery_tourism_cobenefit_index": ("Fishery and Tourism Co-benefit Index", "Index (0-100)", "fishery_tourism_cobenefit_index.png"),
        "desert_surface_cooling_index": ("Desert Surface Cooling Index", "Index (0-100)", "desert_surface_cooling_index.png"),
        "desert_water_supply_index": ("Desert Water Supply and Retention Index", "Index (0-100)", "desert_water_supply_index.png"),
        "humus_soil_settlement_index": ("Humus and Soil Settlement Index", "Index (0-100)", "humus_soil_settlement_index.png"),
        "desert_vegetation_recovery_index": ("Desert Vegetation Recovery Index", "Index (0-100)", "desert_vegetation_recovery_index.png"),
        "desert_energy_settlement_index": ("Desert Energy and Underground Settlement Index", "Index (0-100)", "desert_energy_settlement_index.png"),
        "disaster_pressure_reduction_index": ("Disaster Pressure Reduction Index", "Index (0-100)", "disaster_pressure_reduction_index.png"),
        "local_economic_cobenefit_index": ("Local Economic Co-benefit Index", "Index (0-100)", "local_economic_cobenefit_index.png"),
    }

    for metric, (title, ylabel, filename) in plots.items():
        plot_metric(df, metric, title, ylabel, filename)

    final_year = df[df["year"] == YEARS[-1]].copy()
    final_year = final_year.sort_values("cooling_credit_value", ascending=False)
    final_year.to_csv(OUTPUT_DIR / "natural_feedback_cooling_final_year_summary.csv", index=False)

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
                "ocean_surface_cooling_index",
                "dissolved_oxygen_recovery_index",
                "marine_food_web_recovery_index",
                "fishery_tourism_cobenefit_index",
                "desert_surface_cooling_index",
                "desert_water_supply_index",
                "humus_soil_settlement_index",
                "desert_vegetation_recovery_index",
                "desert_energy_settlement_index",
                "disaster_pressure_reduction_index",
                "local_economic_cobenefit_index",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()
