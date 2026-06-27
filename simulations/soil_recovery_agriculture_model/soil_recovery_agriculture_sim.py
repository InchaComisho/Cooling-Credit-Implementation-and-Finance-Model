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
farm_area_ha=100
baseline_yield_per_ha=4.0
crop_price_per_ton=350
baseline_yield_decline_rate=0.01
drought_loss_probability=0.22
baseline_drought_loss_rate=0.30
soil_recovery_capex=900_000
annual_organic_matter_cost=120_000
annual_mrv_cost=40_000
soil_moisture_improvement_rate=0.025
yield_stability_improvement_rate=0.015
drought_loss_reduction_rate=0.35
fertilizer_cost_reduction_rate=0.18
water_cost_reduction_rate=0.12
baseline_fertilizer_cost=180_000
baseline_water_cost=120_000
cooling_credit_revenue_initial=80_000
credit_revenue_growth_rate=0.02

y=np.arange(1,years+1)
potential_baseline=baseline_yield_per_ha*(1-baseline_yield_decline_rate)**(y-1)
baseline_drought_loss=potential_baseline*drought_loss_probability*baseline_drought_loss_rate
baseline_yield=potential_baseline-baseline_drought_loss
# Recovery limits yield improvement to a gradual stability gain rather than indefinite compounding.
stability_gain=np.minimum(y*yield_stability_improvement_rate,0.30)
restored_potential=baseline_yield_per_ha*(1+stability_gain)
restored_drought_loss=restored_potential*drought_loss_probability*baseline_drought_loss_rate*(1-drought_loss_reduction_rate)
restored_yield=restored_potential-restored_drought_loss
baseline_revenue=baseline_yield*farm_area_ha*crop_price_per_ton
restored_revenue=restored_yield*farm_area_ha*crop_price_per_ton
fert_saving=np.full(years,baseline_fertilizer_cost*fertilizer_cost_reduction_rate)
water_saving=np.full(years,baseline_water_cost*water_cost_reduction_rate)
credit=cooling_credit_revenue_initial*(1+credit_revenue_growth_rate)**(y-1)
net=(restored_revenue-baseline_revenue)+fert_saving+water_saving+credit-annual_organic_matter_cost-annual_mrv_cost
cash=net.copy();cash[0]-=soil_recovery_capex
cumulative=np.cumsum(cash); discount=(1+discount_rate)**y
npv=float(np.sum(net/discount)-soil_recovery_capex);roi=float(cash.sum()/soil_recovery_capex);payback=payback_year(cumulative)
moisture_index=100*(1+soil_moisture_improvement_rate)**y
df=pd.DataFrame({"year":y,"baseline_yield_t_per_ha":baseline_yield,"restored_yield_t_per_ha":restored_yield,"baseline_expected_drought_loss_t_per_ha":baseline_drought_loss,"restored_expected_drought_loss_t_per_ha":restored_drought_loss,"soil_moisture_index":moisture_index,"baseline_farm_revenue":baseline_revenue,"restored_farm_revenue":restored_revenue,"fertilizer_cost_saving":fert_saving,"water_cost_saving":water_saving,"cooling_credit_revenue":credit,"annual_net_benefit":net,"project_cash_flow_after_capex":cash,"cumulative_cash_flow":cumulative,"discounted_annual_net_benefit":net/discount,"project_npv":npv,"project_roi":roi,"payback_year":payback})
df.to_csv(OUT/"soil_recovery_agriculture_results.csv",index=False)
plt.figure(figsize=(9,5));plt.plot(y,baseline_yield,label="Degraded soil");plt.plot(y,restored_yield,label="Restored soil");plt.xlabel("Year");plt.ylabel("Expected yield (t/ha)");plt.title("Expected Yield Comparison");plt.legend();save("yield_comparison.png")
plt.figure(figsize=(9,5));plt.plot(y,moisture_index,marker="o");plt.xlabel("Year");plt.ylabel("Soil moisture index (year 0=100)");plt.title("Restored-Soil Moisture Index");save("soil_moisture_index.png")
plt.figure(figsize=(9,5));plt.bar(y,cash/1e3,label="Annual cash flow");plt.plot(y,cumulative/1e3,color="black",label="Cumulative");plt.axhline(0,color="gray");plt.xlabel("Year");plt.ylabel("Thousand");plt.title("Agricultural Net Benefit");plt.legend();save("agricultural_net_benefit.png")
plt.figure(figsize=(8,5));plt.bar(["Fertilizer","Water"],[fert_saving[0]/1e3,water_saving[0]/1e3]);plt.ylabel("Annual saving (thousand)");plt.title("Input Cost Savings");save("input_cost_savings.png")
drought_reductions=[0.20,0.35,0.50];vals=[]
for dr in drought_reductions:
    ry=restored_potential-restored_potential*drought_loss_probability*baseline_drought_loss_rate*(1-dr); n=(ry-baseline_yield)*farm_area_ha*crop_price_per_ton+fert_saving+water_saving+credit-annual_organic_matter_cost-annual_mrv_cost;c=n.copy();c[0]-=soil_recovery_capex;vals.append(c.sum()/soil_recovery_capex*100)
plt.figure(figsize=(8,5));plt.bar(["Low 20%","Medium 35%","High 50%"],vals);plt.ylabel("ROI (%)");plt.title("ROI Sensitivity to Drought-Loss Reduction");save("agriculture_roi_sensitivity.png")
print(f"Soil recovery model: NPV={npv:,.0f}, ROI={roi:.1%}, payback year={payback or 'not reached'}")
