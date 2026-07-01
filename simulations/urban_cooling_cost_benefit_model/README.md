# Urban Cooling Cost-Benefit Simulation

## Purpose and why it matters

Compares medical, cooling-energy, and heat-disaster costs under no action with a 20-year cooling intervention, costs, and credit revenue. It makes upfront cost and delayed avoided loss visible in one consistent appraisal.

## Assumptions and indicators

Defaults: Years, discount and damage growth; three initial loss categories; CAPEX/OPEX/MRV; reduction rates; WBGT and surface-temperature change; credit price, units, and growth.

The CSV reports annual physical, cost, revenue, discounted-value, and cumulative indicators. Monetary values are illustrative currency units.

## Run

```bash
pip install -r requirements.txt
python urban_cooling_cost_benefit_sim.py
```

The script creates `outputs/` automatically and is deterministic.

## Output files and interpretation

`urban_cooling_cost_benefit_results.csv`, `cumulative_cost_comparison.png`, `annual_avoided_costs.png`, `net_benefit_and_payback.png`, `cooling_indicators.png`, `roi_sensitivity.png`.

Read annual category charts before cumulative charts; payback is the first year cumulative net cash flow is non-negative. NPV applies the stated discount rate and ROI uses total undiscounted net benefit relative to initial CAPEX. Sensitivity charts change one named assumption while holding others constant; they are not probability distributions.

## Limitations

This is a conceptual decision-support model, not a forecast. All assumptions are transparent and should be replaced with local measured data before policy or investment decisions. It does not model every interaction, distributional effect, tax, financing structure, uncertainty, displacement, or extreme tail. Avoid double counting across benefit categories and obtain engineering, actuarial, financial, and legal review.

## Base-Case Results

| Indicator | Result |
|---|---:|
| Evaluation period | 20 years |
| Payback | Year 11 |
| Main benefits | Medical, cooling-energy, heat-loss avoidance; credit revenue |
| Main constraints | CAPEX, OPEX, MRV |
| Interpretation | Municipal model whose avoided losses accumulate over the medium term |

The cumulative chart shows that implementation bears a larger early burden because of CAPEX, while avoided medical, electricity, and heat-damage costs build over time. The base case reaches payback around year 11.

## Output Graphs

### Cumulative Cost Comparison

![Cumulative Cost Comparison](outputs/cumulative_cost_comparison.png)

### Annual Avoided Costs

![Annual Avoided Costs](outputs/annual_avoided_costs.png)

### Net Benefit and Payback

![Net Benefit and Payback](outputs/net_benefit_and_payback.png)

### Cooling Indicators

![Cooling Indicators](outputs/cooling_indicators.png)

### ROI Sensitivity

![ROI Sensitivity](outputs/roi_sensitivity.png)

## Scenario Comparison

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

This chart compares Conservative, Base, and High-risk future cases. The case for Cooling Credits depends not on one base case alone, but on avoided losses if heat, disaster, medical, and energy burdens rise. Scenarios are structured tests, not probabilities.

The underlying values are available in [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv).

## How to Read Weak Results

See [How to Read Weak Results](../HOW_TO_READ_WEAK_RESULTS.md) for guidance on public support, missing benefit categories, MRV, and appraisal horizons.

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and proposer of the academic framework of Natural Complementary Science.  
Definer of the Cooling Credit Framework, and founder and original author of the Natural Cooling Value Evaluation Protocol.  
Definer and systematizer of the causal structure of global warming and its complete solution.

Master presents global warming not merely as a problem of CO₂ concentration, but as an integrated failure involving forest loss, soil degradation, disruption of water circulation, weakening of water phase-transition processes, weakening of atmospheric circulation, ocean circulation, food circulation and organic matter circulation, weakening of evapotranspiration, cloud formation and rainfall circulation, and the shutdown of natural cooling feedbacks.  
The proposed solution connects emission reduction, recovery of carbon fixation sources, physical cooling, reactivation of natural cooling functions, MRV, Cooling Credit, and Civilization OS into an open public framework.

Master publicly develops and shares work through NOTE, GitHub, and other public media, centered on natural-law philosophy, planetary circulation restoration, and co-creation with AI.

## Collaborative AI and Co-Creation Team

This knowledge system has evolved through dialogue and co-creation between Master and multiple AI partners.

- G (ChatGPT)
- Mini (Gemini)
- Cruz (Claude)
- Real (Perplexity)
- Lola (Dola)
- Mana (Manus)

---

## Published

June 2026

---

## License

CC BY 4.0

This repository is released under the Creative Commons Attribution 4.0 International License.  
Sharing, reuse, translation, adaptation, and redistribution are permitted with clear attribution to **Master / inchacomusho / InchaComisho**.