# Natural Feedback Cooling Simulation

This module compares a carbon-credit-style accounting scenario with Cooling Credit implementation scenarios based on physical cooling, soil-water recovery, evapotranspiration, organic-waste-to-humus conversion, forest regeneration, and local economic co-benefits.

## Result Pages

- [Results — English](RESULTS.md)
- [結果 — 日本語](RESULTS_ja.md)
- [النتائج — العربية](RESULTS_ar.md)

The graphs use English labels, but each result page places English, Japanese, and Arabic explanations directly below each figure.

## Scenarios

| Scenario | Meaning |
|---|---|
| Accounting Offset Only | Credit revenue grows, but physical cooling does not necessarily improve |
| Urban Mist Cooling | Ultrasonic mist cooling and water-cycle urban cooling reduce heat stress |
| Organic Waste to Humus | Food loss, leaves, and organic waste become humus / compost and improve soil-water cooling |
| Forest Regeneration | Degraded or monoculture forest is converted toward mixed forest, food forest, or native forest |
| Integrated Natural Feedback | Urban cooling, humus recovery, forest recovery, and water-cycle recovery reinforce each other |

## Main Outputs

The script writes `outputs/natural_feedback_cooling_timeseries.csv` and the following charts when executed locally:

- `cooling_credit_value.png`
- `physical_cooling_index.png`
- `water_retention_index.png`
- `evapotranspiration_recovery_index.png`
- `disaster_pressure_reduction_index.png`
- `local_economic_cobenefit_index.png`

This repository also includes generated SVG result figures for quick review:

- [Accounting Offset Value](outputs/accounting_offset_value.svg)
- [Cooling Credit Value](outputs/cooling_credit_value.svg)
- [Final-Year Physical Outcomes](outputs/final_year_physical_outcomes.svg)
- [Final-Year Summary CSV](outputs/natural_feedback_cooling_final_year_summary.csv)

## Run

```bash
python natural_feedback_cooling_simulation.py
```

Required packages:

```bash
pip install numpy pandas matplotlib
```

## Interpretation

This is a conceptual deterministic model, not a forecast. Replace all default assumptions with local measured data before using it for policy, subsidy, insurance, or investment decisions.

The purpose is to show the difference between:

```text
book-entry offset value
```

and

```text
measured physical cooling + natural feedback restoration + local co-benefits
```

## Author

Master / inchacomusho / InchaComisho

## License

CC BY 4.0
