from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)
plt.style.use("default")

def save(name):
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=160, bbox_inches="tight")
    plt.close()

def payback_year(cumulative):
    hits = np.flatnonzero(np.asarray(cumulative) >= 0)
    return int(hits[0] + 1) if len(hits) else None

# Transparent illustrative defaults; this model is decision support, not a forecast.
years = 20
discount_rate = 0.03
initial_medical_cost = 2_000_000
initial_cooling_energy_cost = 3_000_000
initial_disaster_related_heat_cost = 1_500_000
annual_damage_growth_rate = 0.035
capex = 12_000_000
annual_opex = 650_000
annual_mrv_cost = 120_000
wbgt_reduction_c = 1.2
surface_temp_reduction_c = 4.0
cooling_energy_reduction_rate = 0.12
heatstroke_reduction_rate = 0.18
disaster_heat_loss_reduction_rate = 0.08
cooling_credit_price = 40
cooling_credit_units_initial = 20_000
credit_growth_rate = 0.02

y = np.arange(1, years + 1)
growth = (1 + annual_damage_growth_rate) ** (y - 1)
medical = initial_medical_cost * growth
energy = initial_cooling_energy_cost * growth
disaster = initial_disaster_related_heat_cost * growth
baseline = medical + energy + disaster
avoid_med = medical * heatstroke_reduction_rate
avoid_energy = energy * cooling_energy_reduction_rate
avoid_disaster = disaster * disaster_heat_loss_reduction_rate
avoided = avoid_med + avoid_energy + avoid_disaster
credit_units = cooling_credit_units_initial * (1 + credit_growth_rate) ** (y - 1)
credit_revenue = credit_units * cooling_credit_price
operating = annual_opex + annual_mrv_cost
# Implementation cost includes residual losses and project costs, net of credit revenue.
implementation_annual = baseline - avoided + operating - credit_revenue
implementation_total = implementation_annual.copy()
implementation_total[0] += capex
annual_net_benefit = avoided + credit_revenue - operating
project_cash_flow = annual_net_benefit.copy()
project_cash_flow[0] -= capex
cumulative_net = np.cumsum(project_cash_flow)
cumulative_no_action = np.cumsum(baseline)
cumulative_implementation = np.cumsum(implementation_total)
discount = (1 + discount_rate) ** y
npv = float(np.sum(annual_net_benefit / discount) - capex)
roi = float(np.sum(project_cash_flow) / capex)
payback = payback_year(cumulative_net)

df = pd.DataFrame({
    "year": y, "baseline_medical_cost": medical, "baseline_cooling_energy_cost": energy,
    "baseline_heat_disaster_cost": disaster, "baseline_annual_cost": baseline,
    "avoided_medical_cost": avoid_med, "avoided_energy_cost": avoid_energy,
    "avoided_heat_disaster_cost": avoid_disaster, "total_avoided_cost": avoided,
    "cooling_credit_units": credit_units, "cooling_credit_revenue": credit_revenue,
    "annual_opex": annual_opex, "annual_mrv_cost": annual_mrv_cost,
    "implementation_annual_net_cost": implementation_annual,
    "annual_project_net_benefit": annual_net_benefit, "project_cash_flow_after_capex": project_cash_flow,
    "cumulative_no_action_cost": cumulative_no_action,
    "cumulative_implementation_net_cost": cumulative_implementation,
    "cumulative_net_benefit": cumulative_net, "discounted_annual_net_benefit": annual_net_benefit / discount,
    "wbgt_reduction_c": wbgt_reduction_c, "surface_temp_reduction_c": surface_temp_reduction_c,
    "cooling_energy_reduction_rate": cooling_energy_reduction_rate,
    "project_npv": npv, "project_roi": roi, "payback_year": payback,
})
df.to_csv(OUT / "urban_cooling_cost_benefit_results.csv", index=False)

plt.figure(figsize=(9, 5)); plt.plot(y, cumulative_no_action/1e6, label="No-action cumulative cost"); plt.plot(y, cumulative_implementation/1e6, label="Implementation net cost"); plt.xlabel("Year"); plt.ylabel("Cumulative cost (million)"); plt.title("Urban Cooling: Cumulative Cost Comparison"); plt.legend(); save("cumulative_cost_comparison.png")
plt.figure(figsize=(9, 5)); plt.stackplot(y, avoid_med/1e6, avoid_energy/1e6, avoid_disaster/1e6, labels=["Medical", "Cooling energy", "Heat-disaster"]); plt.xlabel("Year"); plt.ylabel("Avoided cost (million/year)"); plt.title("Annual Avoided Costs by Category"); plt.legend(loc="upper left"); save("annual_avoided_costs.png")
fig, ax = plt.subplots(figsize=(9, 5)); ax.bar(y, project_cash_flow/1e6, label="Annual cash flow"); ax.plot(y, cumulative_net/1e6, color="black", marker="o", label="Cumulative"); ax.axhline(0,color="gray"); ax.set(xlabel="Year", ylabel="Net benefit (million)", title="Net Benefit and Payback"); ax.legend(); save("net_benefit_and_payback.png")
plt.figure(figsize=(8, 5)); vals=[wbgt_reduction_c,surface_temp_reduction_c,cooling_energy_reduction_rate*100]; plt.bar(["WBGT reduction (°C)","Surface reduction (°C)","Energy reduction (%)"],vals); plt.ylabel("Improvement"); plt.title("Cooling Improvement Indicators"); save("cooling_indicators.png")
rates=[0.015,0.035,0.055]; rois=[]
for r in rates:
    g=(1+r)**(y-1); av=(initial_medical_cost*g*heatstroke_reduction_rate + initial_cooling_energy_cost*g*cooling_energy_reduction_rate + initial_disaster_related_heat_cost*g*disaster_heat_loss_reduction_rate)
    cf=av+credit_revenue-operating; rois.append((cf.sum()-capex)/capex*100)
plt.figure(figsize=(8,5)); plt.bar(["Low 1.5%","Medium 3.5%","High 5.5%"],rois); plt.ylabel("ROI (%)"); plt.title("ROI Sensitivity to Annual Damage Growth"); save("roi_sensitivity.png")
# Scenario comparison changes only the specified assumptions; all other defaults remain fixed.
scenarios = {
    "Conservative": {"annual_damage_growth_rate": 0.02, "cooling_energy_reduction_rate": 0.08, "heatstroke_reduction_rate": 0.12},
    "Base": {"annual_damage_growth_rate": 0.035, "cooling_energy_reduction_rate": 0.12, "heatstroke_reduction_rate": 0.18},
    "High-risk future": {"annual_damage_growth_rate": 0.055, "cooling_energy_reduction_rate": 0.16, "heatstroke_reduction_rate": 0.24},
}
scenario_rows = []
for name, s in scenarios.items():
    sg = (1 + s["annual_damage_growth_rate"]) ** (y - 1)
    sav = (
        initial_medical_cost * sg * s["heatstroke_reduction_rate"]
        + initial_cooling_energy_cost * sg * s["cooling_energy_reduction_rate"]
        + initial_disaster_related_heat_cost * sg * disaster_heat_loss_reduction_rate
    )
    sb = sav + credit_revenue - operating
    scash = sb.copy(); scash[0] -= capex
    scenario_rows.append({"scenario": name, "npv": np.sum(sb / discount) - capex, "roi": scash.sum() / capex, "payback_year": payback_year(np.cumsum(scash))})
scenario_df = pd.DataFrame(scenario_rows)
scenario_df.to_csv(OUT / "scenario_comparison.csv", index=False)
plot_values = scenario_df["payback_year"].fillna(years + 1)
plt.figure(figsize=(8, 5)); bars = plt.bar(scenario_df["scenario"], plot_values)
for bar, value in zip(bars, scenario_df["payback_year"]):
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3, "No payback" if pd.isna(value) else f"Year {int(value)}", ha="center")
plt.ylim(0, years + 3); plt.ylabel("Payback year"); plt.title("Urban Cooling Scenario Payback Comparison"); save("scenario_payback_comparison.png")

print(f"Urban cooling model: NPV={npv:,.0f}, ROI={roi:.1%}, payback year={payback or 'not reached'}")
