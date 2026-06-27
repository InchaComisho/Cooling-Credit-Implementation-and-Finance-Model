from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# WARNING: This is not a physical climate model. It is a conceptual
# risk-pressure model for comparing local and global implementation scales.
years = 30
baseline_risk_index = 100
annual_climate_risk_growth = 0.035
deployment_scenarios = {
    "Local pilots": {"deployment_scale": 0.05, "surface_cooling_effect": 0.02, "water_cycle_recovery": 0.01, "soil_moisture_recovery": 0.01, "dryland_cooling_effect": 0.005},
    "National programs": {"deployment_scale": 0.20, "surface_cooling_effect": 0.08, "water_cycle_recovery": 0.05, "soil_moisture_recovery": 0.05, "dryland_cooling_effect": 0.03},
    "Continental dryland networks": {"deployment_scale": 0.45, "surface_cooling_effect": 0.18, "water_cycle_recovery": 0.12, "soil_moisture_recovery": 0.10, "dryland_cooling_effect": 0.12},
    "Global coordinated implementation": {"deployment_scale": 0.75, "surface_cooling_effect": 0.30, "water_cycle_recovery": 0.22, "soil_moisture_recovery": 0.20, "dryland_cooling_effect": 0.20},
}
out=Path(__file__).resolve().parent/"outputs";out.mkdir(exist_ok=True)
y=np.arange(0,years+1)
no_action=baseline_risk_index*(1+annual_climate_risk_growth)**y
rows=[];curves={}
components=[]
for name,s in deployment_scenarios.items():
    weighted={"surface cooling":0.30*s["surface_cooling_effect"],"water-cycle recovery":0.30*s["water_cycle_recovery"],"soil-moisture recovery":0.20*s["soil_moisture_recovery"],"dryland cooling":0.20*s["dryland_cooling_effect"]}
    mitigation_factor=s["deployment_scale"]*sum(weighted.values())
    risk_growth_after_mitigation=annual_climate_risk_growth*(1-mitigation_factor)
    risk=baseline_risk_index*(1+risk_growth_after_mitigation)**y
    curves[name]=risk
    for year,n,sr in zip(y,no_action,risk):
        rows.append({"year":year,"scenario":name,"deployment_scale":s["deployment_scale"],"mitigation_factor":mitigation_factor,"risk_growth_after_mitigation":risk_growth_after_mitigation,"no_action_risk_index":n,"scenario_risk_index":sr,"avoided_risk":n-sr})
    components.append({"scenario":name,**{k:s["deployment_scale"]*v for k,v in weighted.items()},"mitigation_factor":mitigation_factor})
pd.DataFrame(rows).to_csv(out/"global_stabilization_results.csv",index=False)

def save(name):
    plt.grid(True,alpha=.3);plt.tight_layout();plt.savefig(out/name,dpi=160,bbox_inches="tight");plt.close()
plt.figure(figsize=(10,6));plt.plot(y,no_action,label="No action",linewidth=3,color="black")
for name,risk in curves.items():plt.plot(y,risk,label=name)
plt.xlabel("Year");plt.ylabel("Conceptual risk-pressure index");plt.title("Risk-Pressure Index by Deployment Scale");plt.legend();save("risk_index_comparison.png")
plt.figure(figsize=(10,6))
for name,risk in curves.items():plt.plot(y,no_action-risk,label=name)
plt.xlabel("Year");plt.ylabel("Avoided risk-pressure index points");plt.title("Conceptual Avoided Risk by Scenario");plt.legend();save("avoided_risk_by_scenario.png")
cdf=pd.DataFrame(components).set_index("scenario")
cdf[["surface cooling","water-cycle recovery","soil-moisture recovery","dryland cooling"]].plot(kind="bar",stacked=True,figsize=(11,6))
plt.ylabel("Contribution to mitigation factor");plt.title("Deployment Effect Components");plt.xticks(rotation=15,ha="right");save("deployment_effect_components.png")
plt.figure(figsize=(10,6));plt.plot(y,curves["Local pilots"],label="Local pilots",linewidth=2);plt.plot(y,curves["Global coordinated implementation"],label="Global coordinated implementation",linewidth=2);plt.fill_between(y,curves["Global coordinated implementation"],curves["Local pilots"],alpha=.25,label="Local-global gap");plt.xlabel("Year");plt.ylabel("Conceptual risk-pressure index");plt.title("Local Pilots vs Global Coordinated Implementation");plt.legend();save("global_vs_local_gap.png")
print("This is not a physical climate model.")
print("It is a conceptual risk-pressure model for comparing local and global implementation scales.")
for name,risk in curves.items():print(f"{name}: year-{years} index={risk[-1]:.2f}, avoided={no_action[-1]-risk[-1]:.2f}")
