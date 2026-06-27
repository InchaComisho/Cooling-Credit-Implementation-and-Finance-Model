# Disaster Risk Avoidance Simulation

## Purpose and why it matters

Estimates how infiltration, storage, and green infrastructure change runoff and expected flood loss over 20 years. It makes upfront cost and delayed avoided loss visible in one consistent appraisal.

## Assumptions and indicators

Defaults: Event probability and loss; risk growth; imperviousness; baseline/improved infiltration; storage and green-infrastructure effects; CAPEX/OPEX/MRV; insurer payment.

The CSV reports annual physical, cost, revenue, discounted-value, and cumulative indicators. Monetary values are illustrative currency units.

## Run

```bash
pip install -r requirements.txt
python disaster_risk_avoidance_sim.py
```

The script creates `outputs/` automatically and is deterministic.

## Output files and interpretation

`disaster_risk_avoidance_results.csv`, `flood_expected_annual_loss.png`, `runoff_and_infiltration_indices.png`, `cumulative_avoided_flood_loss.png`, `disaster_model_payback.png`, `risk_growth_sensitivity.png`.

Read annual category charts before cumulative charts; payback is the first year cumulative net cash flow is non-negative. NPV applies the stated discount rate and ROI uses total undiscounted net benefit relative to initial CAPEX. Sensitivity charts change one named assumption while holding others constant; they are not probability distributions.

## Limitations

This is a conceptual decision-support model, not a forecast. All assumptions are transparent and should be replaced with local measured data before policy or investment decisions. It does not model every interaction, distributional effect, tax, financing structure, uncertainty, displacement, or extreme tail. Avoid double counting across benefit categories and obtain engineering, actuarial, financial, and legal review.

## Base-Case Results

| Indicator | Result |
|---|---:|
| Evaluation period | 20 years |
| Payback | Year 12 |
| Main benefit | Expected flood-loss avoidance and insurer payment |
| Main constraint | Sensitivity to event probability and loss severity |
| Interpretation | Suitable for insurer, municipal, and watershed appraisal |

Benefits depend strongly on flood frequency, severity, and attribution to infiltration and storage. The base case pays back in year 12; the scenario chart makes this dependence explicit.

## Output Graphs

### Flood Expected Annual Loss

![Flood Expected Annual Loss](outputs/flood_expected_annual_loss.png)

### Runoff and Infiltration Indices

![Runoff and Infiltration Indices](outputs/runoff_and_infiltration_indices.png)

### Cumulative Avoided Flood Loss

![Cumulative Avoided Flood Loss](outputs/cumulative_avoided_flood_loss.png)

### Disaster Model Payback

![Disaster Model Payback](outputs/disaster_model_payback.png)

### Risk Growth Sensitivity

![Risk Growth Sensitivity](outputs/risk_growth_sensitivity.png)

## Scenario Comparison

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

This chart compares Conservative, Base, and High-risk future cases. The case for Cooling Credits depends not on one base case alone, but on avoided losses if heat, disaster, medical, and energy burdens rise. Scenarios are structured tests, not probabilities.

The underlying values are available in [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv).

## How to Read Weak Results

See [How to Read Weak Results](../HOW_TO_READ_WEAK_RESULTS.md) for guidance on public support, missing benefit categories, MRV, and appraisal horizons.

---

## Author

Master / inchacomusho / InchaComisho

Independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and advocate of the academic framework of Natural Complementary Science.  
Publicly active in natural-law philosophy, planetary circulation restoration, and co-creation with AI.

---

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
