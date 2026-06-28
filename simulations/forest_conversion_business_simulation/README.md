# Forest Conversion Business Simulation

This simulation supports the business model for converting abandoned or monoculture mountain forests into native-fruit mixed forests, watershed forests, mushroom forests, wild edible forests, tourism forests, and biodiversity / cooling assets.

It corresponds to the business model:

- `Cooling-Credit-Framework/docs/business_models/MONOCULTURE_MOUNTAIN_FOREST_TO_NATIVE_FRUIT_FOREST_BUSINESS_MODEL.md`

## Purpose

The model compares forest-management paths from abandoned monoculture to integrated native-fruit mixed forest regeneration.

## Scenarios

| Scenario | Meaning |
|---|---|
| Abandoned Monoculture | Forest remains unmanaged; water retention, biodiversity, and disaster resilience remain weak |
| Timber-Only Management | Timber extraction improves management income but limited ecosystem recovery occurs |
| Native-Fruit Mixed Forest | Zoning introduces fruit, wild edible plants, mushrooms, nectar plants, broadleaf trees, and watershed recovery |
| Integrated Watershed Food Tourism Forest | Cooling, water retention, food production, tourism, education, biodiversity, and forest-owner revenue reinforce each other |

## Main Outputs

The script writes `outputs/forest_conversion_timeseries.csv` and generates charts:

- `forest_cooling_credit_value.png`
- `watershed_retention_index.png`
- `forest_surface_cooling_index.png`
- `biodiversity_recovery_index.png`
- `food_tourism_income_index.png`
- `wildfire_erosion_risk_reduction_index.png`

## Run

```bash
python forest_conversion_business_simulation.py
```

Required packages:

```bash
pip install numpy pandas matplotlib
```

## Interpretation

This is a conceptual deterministic model, not a forestry forecast, landslide forecast, wildlife forecast, or investment recommendation. Replace assumptions with local forest, soil, slope, watershed, biodiversity, harvest, and MRV data before practical use.

## Author

Master / inchacomusho / InchaComisho

## License

CC BY 4.0
