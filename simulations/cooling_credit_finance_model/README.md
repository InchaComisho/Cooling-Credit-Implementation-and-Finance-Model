# Cooling Credit Finance Simulation

## Purpose and why it matters

Models a 20-year SPV revenue stack, costs, reserves, community return, and investor distributable cash flow. It makes upfront cost and delayed avoided loss visible in one consistent appraisal.

## Assumptions and indicators

Defaults: Portfolio CAPEX; OPEX rate; MRV/registry; five outcome revenues; credit units and price; growth; community and reserve rates; discount rate.

The CSV reports annual physical, cost, revenue, discounted-value, and cumulative indicators. Monetary values are illustrative currency units.

## Run

```bash
pip install -r requirements.txt
python cooling_credit_finance_sim.py
```

The script creates `outputs/` automatically and is deterministic.

## Output files and interpretation

`cooling_credit_finance_results.csv`, `revenue_stack.png`, `cash_flow_waterfall.png`, `investor_cumulative_cash_flow.png`, `npv_roi_payback.png`, `credit_price_sensitivity.png`.

Read annual category charts before cumulative charts; payback is the first year cumulative net cash flow is non-negative. NPV applies the stated discount rate and ROI uses total undiscounted net benefit relative to initial CAPEX. Sensitivity charts change one named assumption while holding others constant; they are not probability distributions.

## Limitations

This is a conceptual decision-support model, not a forecast. All assumptions are transparent and should be replaced with local measured data before policy or investment decisions. It does not model every interaction, distributional effect, tax, financing structure, uncertainty, displacement, or extreme tail. Avoid double counting across benefit categories and obtain engineering, actuarial, financial, and legal review.

## Base-Case Results

| Indicator | Result |
|---|---:|
| Evaluation period | 20 years |
| Payback | Year 9 |
| Main benefit | Diversified contracted revenue plus credit revenue |
| Main constraint | Counterparty, delivery, and credit-price risk |
| Interpretation | Strongest candidate for an SPV/fund structure |

The revenue stack shows why a portfolio is stronger than a credit-only project. Contracted outcome revenues, reserves, community return, and investor distributions remain visible; the base case pays back in year 9.

## Output Graphs

### Revenue Stack

![Revenue Stack](outputs/revenue_stack.png)

### Cash Flow Waterfall

![Cash Flow Waterfall](outputs/cash_flow_waterfall.png)

### Investor Cumulative Cash Flow

![Investor Cumulative Cash Flow](outputs/investor_cumulative_cash_flow.png)

### NPV ROI Payback

![NPV ROI Payback](outputs/npv_roi_payback.png)

### Credit Price Sensitivity

![Credit Price Sensitivity](outputs/credit_price_sensitivity.png)

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
