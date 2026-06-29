# 森林転換事業シミュレーション

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

このシミュレーションは、放置された山林や単一植林を、在来果樹混交林・水源涵養林・キノコ林・山菜林・観光林・生物多様性・冷却資産へ転換する事業モデルを支援する。

対応する事業モデル：

- `Cooling-Credit-Framework/docs/business_models/MONOCULTURE_MOUNTAIN_FOREST_TO_NATIVE_FRUIT_FOREST_BUSINESS_MODEL.md`

## 目的

このモデルは、放置された単一植林から統合型の在来果樹混交林再生まで、森林管理の経路を比較する。

## 比較シナリオ

| シナリオ | 内容 |
|---|---|
| Abandoned Monoculture | 管理されないまま放置。保水・生物多様性・防災力は弱いまま |
| Timber-Only Management | 木材採取が管理収益を改善するが、生態系回復は限定的 |
| Native-Fruit Mixed Forest | ゾーニングによって果樹・山菜・キノコ・蜜源植物・広葉樹・水源回復を導入 |
| Integrated Watershed Food Tourism Forest | 冷却・保水・食料生産・観光・教育・生物多様性・森林所有者収益が互いに強化し合う |

## 主な出力

スクリプトは `outputs/forest_conversion_timeseries.csv` とグラフを生成する。

- `forest_cooling_credit_value.png`
- `watershed_retention_index.png`
- `forest_surface_cooling_index.png`
- `biodiversity_recovery_index.png`
- `food_tourism_income_index.png`
- `wildfire_erosion_risk_reduction_index.png`

## 実行方法

```bash
python forest_conversion_business_simulation.py
```

必要なパッケージ：

```bash
pip install numpy pandas matplotlib
```

## 解釈 / 注意

これは概念的な決定論モデルであり、林業予測・土砂崩れ予測・野生動物予測・投資推奨ではない。実用前に、地域の森林・土壌・斜面・水源・生物多様性・収穫・MRVデータで仮定を置き換えること。

## Author / 著者

Master / inchacomusho / InchaComisho

## License / ライセンス

CC BY 4.0
