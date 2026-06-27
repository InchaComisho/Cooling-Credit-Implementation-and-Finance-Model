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

years=20
discount_rate=0.03
annual_extreme_rain_event_probability=0.18
baseline_flood_loss_per_event=20_000_000
annual_risk_growth_rate=0.025
impervious_area_rate=0.72
baseline_infiltration_rate=0.18
improved_infiltration_rate=0.38
rainwater_storage_effect=0.10
green_infrastructure_runoff_reduction=0.16
capex=18_000_000
annual_opex=700_000
annual_mrv_cost=150_000
insurance_risk_reduction_payment=600_000

y=np.arange(1,years+1)
growth=(1+annual_risk_growth_rate)**(y-1)
baseline_eal=annual_extreme_rain_event_probability*baseline_flood_loss_per_event*growth
# Runoff index combines imperviousness and the share not infiltrated.
baseline_runoff_index=impervious_area_rate*(1-baseline_infiltration_rate)
raw_improved=impervious_area_rate*(1-improved_infiltration_rate)
improved_runoff_index=raw_improved*(1-rainwater_storage_effect)*(1-green_infrastructure_runoff_reduction)
runoff_reduction_rate=1-improved_runoff_index/baseline_runoff_index
improved_eal=baseline_eal*(1-runoff_reduction_rate)
avoided=baseline_eal-improved_eal
annual_benefit=avoided+insurance_risk_reduction_payment-annual_opex-annual_mrv_cost
cash=annual_benefit.copy(); cash[0]-=capex
cumulative=np.cumsum(cash)
discount=(1+discount_rate)**y
npv=float(np.sum(annual_benefit/discount)-capex); roi=float(cash.sum()/capex); payback=payback_year(cumulative)
df=pd.DataFrame({"year":y,"baseline_expected_annual_flood_loss":baseline_eal,"improved_expected_annual_flood_loss":improved_eal,"baseline_runoff_index":baseline_runoff_index,"improved_runoff_index":improved_runoff_index,"runoff_reduction_rate":runoff_reduction_rate,"baseline_infiltration_rate":baseline_infiltration_rate,"improved_infiltration_rate":improved_infiltration_rate,"avoided_flood_loss":avoided,"cumulative_avoided_flood_loss":np.cumsum(avoided),"insurance_risk_reduction_payment":insurance_risk_reduction_payment,"annual_project_net_benefit":annual_benefit,"project_cash_flow_after_capex":cash,"cumulative_project_cash_flow":cumulative,"discounted_annual_net_benefit":annual_benefit/discount,"project_npv":npv,"project_roi":roi,"payback_year":payback})
df.to_csv(OUT/"disaster_risk_avoidance_results.csv",index=False)
plt.figure(figsize=(9,5)); plt.plot(y,baseline_eal/1e6,label="Baseline EAL"); plt.plot(y,improved_eal/1e6,label="Improved EAL"); plt.xlabel("Year");plt.ylabel("Expected annual loss (million)");plt.title("Flood Expected Annual Loss");plt.legend();save("flood_expected_annual_loss.png")
plt.figure(figsize=(8,5)); plt.bar(["Baseline runoff","Improved runoff","Baseline infiltration","Improved infiltration"],[baseline_runoff_index,improved_runoff_index,baseline_infiltration_rate,improved_infiltration_rate]);plt.ylabel("Index / rate");plt.title("Runoff and Infiltration Indices");save("runoff_and_infiltration_indices.png")
plt.figure(figsize=(9,5));plt.plot(y,np.cumsum(avoided)/1e6,marker="o");plt.xlabel("Year");plt.ylabel("Cumulative avoided loss (million)");plt.title("Cumulative Avoided Flood Loss");save("cumulative_avoided_flood_loss.png")
plt.figure(figsize=(9,5));plt.bar(y,cash/1e6,label="Annual cash flow");plt.plot(y,cumulative/1e6,color="black",label="Cumulative");plt.axhline(0,color="gray");plt.xlabel("Year");plt.ylabel("Million");plt.title("Disaster Model Payback");plt.legend();save("disaster_model_payback.png")
rates=[0.01,0.025,0.04]; vals=[]
for r in rates:
    e=annual_extreme_rain_event_probability*baseline_flood_loss_per_event*(1+r)**(y-1); a=e*runoff_reduction_rate; b=a+insurance_risk_reduction_payment-annual_opex-annual_mrv_cost;vals.append((np.sum(b/(1+discount_rate)**y)-capex)/1e6)
plt.figure(figsize=(8,5));plt.bar(["Low 1.0%","Medium 2.5%","High 4.0%"],vals);plt.ylabel("NPV (million)");plt.title("Sensitivity to Flood-Risk Growth");save("risk_growth_sensitivity.png")
print(f"Disaster model: runoff reduction={runoff_reduction_rate:.1%}, NPV={npv:,.0f}, ROI={roi:.1%}, payback year={payback or 'not reached'}")
