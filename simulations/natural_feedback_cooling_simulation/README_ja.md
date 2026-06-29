# 自然冷却フィードバック・シミュレーション

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

このモジュールは、炭素クレジット方式の帳簿上相殺シナリオと、物理的な冷却・土壌水分回復・蒸散・有機廃棄物の腐葉土化・森林再生・EEZ海洋冷却・沿岸砂漠外輪再生・地域経済共便益に基づくクーリングクレジット実装シナリオを比較する。

## 結果ページ

- [Results — English](RESULTS.md)
- [結果 — 日本語](RESULTS_ja.md)
- [النتائج — العربية](RESULTS_ar.md)

グラフ内のラベルは英語だが、各結果ページの各図の直下に英語・日本語・アラビア語の説明を配置している。

## 比較シナリオ

| シナリオ | 内容 |
|---|---|
| Accounting Offset Only | クレジット収益は増えるが、物理的な冷却は必ずしも改善しない |
| Urban Mist Cooling | 超音波ミスト冷却と水循環型都市冷却が熱ストレスを軽減する |
| Organic Waste to Humus | 食品ロス・落葉・有機廃棄物が腐葉土・堆肥となり、土壌水分冷却を改善する |
| Forest Regeneration | 劣化した単一植林を混交林・食料林・在来林へ転換する |
| EEZ Ocean Cooling | OBS/OTU/UMS型海洋冷却、酸素化、垂直循環、食物網支援、漁業回復、サンゴ・観光共便益 |
| Coastal Desert Edge Regeneration | 沿岸淡水化、UMS冷却、腐葉土・微生物定着、砂漠外輪植生、ピラミッド型太陽光・垂直風力、地下居住効率 |
| Integrated Natural Feedback | 都市冷却・腐葉土・森林回復・海洋冷却・砂漠外輪再生・水循環が互いに強化し合う |

## 主な出力

スクリプトをローカル実行すると `outputs/natural_feedback_cooling_timeseries.csv` と以下のグラフを出力する。

- `cooling_credit_value.png`
- `physical_cooling_index.png`
- `water_retention_index.png`
- `evapotranspiration_recovery_index.png`
- `ocean_surface_cooling_index.png`
- `dissolved_oxygen_recovery_index.png`
- `marine_food_web_recovery_index.png`
- `fishery_tourism_cobenefit_index.png`
- `desert_surface_cooling_index.png`
- `desert_water_supply_index.png`
- `humus_soil_settlement_index.png`
- `desert_vegetation_recovery_index.png`
- `desert_energy_settlement_index.png`
- `disaster_pressure_reduction_index.png`
- `local_economic_cobenefit_index.png`

リポジトリには生成済みSVG結果図も含まれている。

- [Accounting Offset Value](outputs/accounting_offset_value.svg)
- [Cooling Credit Value with Ocean Scenario](outputs/cooling_credit_value_with_ocean.svg)
- [Cooling Credit Value with Desert Scenario](outputs/cooling_credit_value_with_desert.svg)
- [Final-Year Physical Outcomes with Desert Scenario](outputs/final_year_physical_outcomes_with_desert.svg)
- [Ocean Cooling and Fishery Outcomes](outputs/ocean_cooling_fishery_outcomes.svg)
- [Desert Edge Regeneration Outcomes](outputs/desert_edge_regeneration_outcomes.svg)
- [Final-Year Summary CSV with Desert Scenario](outputs/natural_feedback_cooling_final_year_summary_with_desert.csv)

## 実行方法

```bash
python natural_feedback_cooling_simulation.py
```

必要なパッケージ：

```bash
pip install numpy pandas matplotlib
```

## 解釈 / 注意

これは概念的な決定論モデルであり、予測ではない。政策・補助金・保険・投資判断に使う前に、すべてのデフォルト仮定を地域の実測データに置き換えること。

このモデルの目的は、次の二つの違いを示すことにある。

```text
帳簿上の相殺価値
```

と

```text
実測された物理冷却 + 自然フィードバック回復 + 海洋循環 + 砂漠外輪再生 + 地域共便益
```

## Author / 著者

Master / inchacomusho / InchaComisho

## License / ライセンス

CC BY 4.0
