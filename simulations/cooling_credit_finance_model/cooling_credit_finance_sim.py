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
discount_rate=0.04
initial_project_portfolio_capex=50_000_000
annual_opex_rate=0.045
annual_mrv_cost=500_000
annual_registry_cost=120_000
municipal_outcome_payment_initial=2_000_000
insurance_risk_payment_initial=1_200_000
utility_peak_reduction_payment_initial=800_000
real_estate_value_capture_initial=900_000
agriculture_tourism_benefit_share_initial=700_000
cooling_credit_units_initial=120_000
cooling_credit_price=35
credit_units_growth_rate=0.025
revenue_growth_rate=0.02
community_return_rate=0.15
reserve_rate=0.10

y=np.arange(1,years+1); growth=(1+revenue_growth_rate)**(y-1)
municipal=municipal_outcome_payment_initial*growth
insurance=insurance_risk_payment_initial*growth
utility=utility_peak_reduction_payment_initial*growth
real_estate=real_estate_value_capture_initial*growth
agri_tourism=agriculture_tourism_benefit_share_initial*growth
units=cooling_credit_units_initial*(1+credit_units_growth_rate)**(y-1)
credit=units*cooling_credit_price
gross=municipal+insurance+utility+real_estate+agri_tourism+credit
opex=np.full(years,initial_project_portfolio_capex*annual_opex_rate)
fixed=np.full(years,annual_mrv_cost+annual_registry_cost)
pre_alloc=gross-opex-fixed
# Reserve and community returns apply only to positive cash available after core costs.
reserve=np.maximum(pre_alloc,0)*reserve_rate
community=np.maximum(pre_alloc-reserve,0)*community_return_rate
distributable=pre_alloc-reserve-community
investor_cash=distributable.copy();investor_cash[0]-=initial_project_portfolio_capex
cumulative=np.cumsum(investor_cash);discount=(1+discount_rate)**y
npv=float(np.sum(distributable/discount)-initial_project_portfolio_capex);roi=float(investor_cash.sum()/initial_project_portfolio_capex);payback=payback_year(cumulative)
df=pd.DataFrame({"year":y,"municipal_outcome_payment":municipal,"insurance_risk_payment":insurance,"utility_peak_reduction_payment":utility,"real_estate_value_capture":real_estate,"agriculture_tourism_benefit_share":agri_tourism,"cooling_credit_units":units,"cooling_credit_revenue":credit,"gross_revenue":gross,"annual_operating_cost":opex,"annual_mrv_cost":annual_mrv_cost,"annual_registry_cost":annual_registry_cost,"reserve_allocation":reserve,"community_return":community,"investor_distributable_cash_flow":distributable,"investor_cash_flow_after_capex":investor_cash,"cumulative_investor_cash_flow":cumulative,"discounted_investor_distributable_cash_flow":distributable/discount,"investor_npv":npv,"investor_roi":roi,"payback_year":payback})
df.to_csv(OUT/"cooling_credit_finance_results.csv",index=False)
plt.figure(figsize=(10,5));plt.stackplot(y,municipal/1e6,insurance/1e6,utility/1e6,real_estate/1e6,agri_tourism/1e6,credit/1e6,labels=["Municipal","Insurance","Utility","Real estate","Agriculture/tourism","Credits"]);plt.xlabel("Year");plt.ylabel("Revenue (million)");plt.title("Cooling Project Revenue Stack");plt.legend(ncol=3,loc="upper left");save("revenue_stack.png")
plt.figure(figsize=(9,5));plt.stackplot(y,opex/1e6,fixed/1e6,reserve/1e6,community/1e6,np.maximum(distributable,0)/1e6,labels=["OPEX","MRV + registry","Reserve","Community","Investor"]);plt.xlabel("Year");plt.ylabel("Allocation (million)");plt.title("Cash-Flow Waterfall by Year");plt.legend(loc="upper left");save("cash_flow_waterfall.png")
plt.figure(figsize=(9,5));plt.plot(y,cumulative/1e6,marker="o");plt.axhline(0,color="gray");plt.xlabel("Year");plt.ylabel("Cumulative investor cash flow (million)");plt.title("Investor Cumulative Cash Flow");save("investor_cumulative_cash_flow.png")
plt.figure(figsize=(8,5));plt.bar(["NPV (million)","ROI (%)","Payback year"],[npv/1e6,roi*100,payback or 0]);plt.title("Investor NPV, ROI, and Payback");save("npv_roi_payback.png")
prices=[20,35,50,70];npvs=[]
for p in prices:
    g=municipal+insurance+utility+real_estate+agri_tourism+units*p; pre=g-opex-fixed;r=np.maximum(pre,0)*reserve_rate;c=np.maximum(pre-r,0)*community_return_rate;d=pre-r-c;npvs.append((np.sum(d/discount)-initial_project_portfolio_capex)/1e6)
plt.figure(figsize=(8,5));plt.plot(prices,npvs,marker="o");plt.xlabel("Cooling Credit price");plt.ylabel("Investor NPV (million)");plt.title("Credit Price Sensitivity");save("credit_price_sensitivity.png")
print(f"Finance model: NPV={npv:,.0f}, ROI={roi:.1%}, payback year={payback or 'not reached'}")
