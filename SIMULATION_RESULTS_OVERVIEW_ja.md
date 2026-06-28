# クーリングクレジット・シミュレーション結果一覧

[English](SIMULATION_RESULTS_OVERVIEW.md) | [日本語](SIMULATION_RESULTS_OVERVIEW_ja.md) | [العربية](SIMULATION_RESULTS_OVERVIEW_ar.md)

このページは、`Cooling-Credit-Implementation-and-Finance-Model` に含まれる主要シミュレーション結果を、事業モデルと対応づけて1枚で読めるように整理した概要ページである。

詳細な数式・前提・CSV・スクリプトは各シミュレーションページに分け、ここでは「どの図が何を示すのか」「どの事業モデルと対応するのか」を中心に示す。

---

## 1. まず読むべき結論

クーリングクレジットのシミュレーション群は、次の違いを見える化する。

```text
帳簿上の相殺
= お金や証書は動くが、物理的な冷却を直接示さない

クーリングクレジット
= 実測された冷却・保水・蒸散・海洋回復・砂漠外輪再生・地域共便益を評価する
```

総合的には、都市・土壌・森林・海洋・砂漠を別々に評価するだけでなく、それらがつながった **Integrated Natural Feedback / 統合自然フィードバック** が最も強い値を示す。

---

## 2. 全体結果：どのシナリオが総合的に強いか

![Cooling Credit Value with Desert Edge Scenario](simulations/natural_feedback_cooling_simulation/outputs/cooling_credit_value_with_desert.svg)

この図は、都市・土壌・森林・海洋・砂漠を含めた総合的なクーリングクレジット価値を比較する。

読み方は次の通りである。

- **Integrated Natural Feedback** は、都市冷却、腐葉土化、森林再生、海洋循環、砂漠外輪再生、水循環が同時に働くため、総合値が最も高い。
- **Coastal Desert Edge Regeneration** は、砂漠特化の指標では強いが、地球全体の複合フィードバックでは統合シナリオに劣る。
- **EEZ Ocean Cooling** は、海洋特化指標では強いが、陸域・都市・森林・土壌までは単独で回復しない。
- **Accounting Offset Only** は、帳簿上の価値は増えても、物理冷却が発生しないため、クーリングクレジット価値はゼロに近い。

---

## 3. 海洋モデル：EEZ・漁業・酸素・観光

![Ocean Cooling and Marine Co-benefit Outcomes](simulations/natural_feedback_cooling_simulation/outputs/ocean_cooling_fishery_outcomes.svg)

この図は、海洋に特化した成果を示す。

主に見るべき指標は次である。

- 海面冷却
- 溶存酸素回復
- 海洋食物網回復
- 漁業・観光共便益

対応する事業モデルは、**EEZ Fishery Recovery Cooling Credit Business Model / 排他的経済水域・漁場回復モデル** である。

OBS / OTU / UMS によって、海面の熱、酸素、鉛直循環、植物プランクトン基盤、漁業・観光資源を評価する。

---

## 4. 砂漠モデル：沿岸・外輪からの再生

![Desert Edge Regeneration Outcomes](simulations/natural_feedback_cooling_simulation/outputs/desert_edge_regeneration_outcomes.svg)

この図は、砂漠に特化した成果を示す。

主に見るべき指標は次である。

- 沿岸淡水化による水供給
- UMS / 超音波ミスト冷却
- 腐葉土・微生物定着
- 外輪植生回復
- 地上エネルギー・地下居住効率

対応する事業モデルは、**Desert Circular Pyramid City Business Model / 砂漠循環ピラミッド都市モデル** である。

重要なのは、砂漠中央へいきなり入るのではなく、沿岸や外輪の比較的湿度があり、昼夜の気温差が小さい領域から段階的に再生する点である。

---

## 5. 観光資源回復モデル

観光資源回復シミュレーションは、観光地を単なるホテル・道路・広告ではなく、**涼しさ、水、緑、景観、生態系、滞在快適性** として評価する。

対応するシミュレーションは次である。

- [Tourism Resource Recovery Simulation](simulations/tourism_resource_recovery_simulation/README.md)

主な評価軸は次である。

| 指標 | 意味 |
|---|---|
| Tourism Cooling Credit Value | 観光地の冷却・生態系・地域収益を含む総合価値 |
| Destination Comfort Index | 観光地の滞在快適性 |
| Natural Cooling Asset Index | 水・緑・蒸散・ミストなどの自然冷却資産 |
| Water / Landscape / Ecosystem Index | 水質、景観、生態系回復 |
| Visitor Stay and Income Index | 滞在時間・地域収益 |
| Overtourism Risk Index | 観光過多による負荷 |

---

## 6. 森林転換モデル

森林転換シミュレーションは、放置された単一植林を、果樹、山菜、キノコ、蜜源、在来林、水源涵養林、観光・教育資源へ再配置するモデルである。

対応するシミュレーションは次である。

- [Forest Conversion Business Simulation](simulations/forest_conversion_business_simulation/README.md)

主な評価軸は次である。

| 指標 | 意味 |
|---|---|
| Forest Cooling Credit Value | 森林の冷却・保水・生態系・地域収益を含む総合価値 |
| Watershed Retention Index | 水源涵養・保水力 |
| Forest Surface Cooling Index | 森林表面冷却 |
| Biodiversity Recovery Index | 生物多様性回復 |
| Food and Tourism Income Index | 山菜・果樹・キノコ・観光収益 |
| Wildfire and Erosion Risk Reduction Index | 山火事・土砂災害リスク低減 |

---

## 7. 事業モデル別：どのシミュレーションを見るべきか

| 事業モデル | まず見るシミュレーション |
|---|---|
| EEZ漁場回復 | [Natural Feedback Cooling Simulation](simulations/natural_feedback_cooling_simulation/README.md) の EEZ Ocean Cooling |
| 観光資源回復 | [Tourism Resource Recovery Simulation](simulations/tourism_resource_recovery_simulation/README.md) |
| 砂漠循環ピラミッド都市 | [Natural Feedback Cooling Simulation](simulations/natural_feedback_cooling_simulation/README.md) の Coastal Desert Edge Regeneration |
| 都市緑地・冷却インフラ | [Urban Cooling Cost-Benefit](simulations/urban_cooling_cost_benefit_model/README.md) と Natural Feedback Cooling |
| 単一植林→在来果樹混交林 | [Forest Conversion Business Simulation](simulations/forest_conversion_business_simulation/README.md) |
| センター超音波ミスト冷却ファン | [Urban Cooling Cost-Benefit](simulations/urban_cooling_cost_benefit_model/README.md) と Natural Feedback Cooling |
| フードロス・有機ごみ腐葉土化 | [Soil Recovery Agriculture](simulations/soil_recovery_agriculture_model/README.md) と Natural Feedback Cooling |
| 有機物循環・土壌回復・砂漠緑化 | [Soil Recovery Agriculture](simulations/soil_recovery_agriculture_model/README.md) と Natural Feedback Cooling |

---

## 8. 全体の読み方

この一覧ページでは、次の順に読むと分かりやすい。

```text
1. 総合価値グラフを見る
2. 海洋・砂漠など特化グラフを見る
3. 自分の関心がある事業モデルを選ぶ
4. 対応シミュレーションへ進む
5. CSV・スクリプト・MRV指標を見る
```

重要なのは、各シミュレーションの数値は予測ではなく、**比較のための概念モデル** である点である。

実運用には、地域の実測データ、MRV、第三者検証、生態安全評価、衛生検査、停止条件が必要である。

---

## 関連ページ

- [Business Model Simulation Map](BUSINESS_MODEL_SIMULATION_MAP.md)
- [Simulation Package](simulations/README.md)
- [Natural Feedback Cooling Simulation Results](simulations/natural_feedback_cooling_simulation/RESULTS_ja.md)
- [Cooling Credit Framework Business Models](https://github.com/InchaComisho/Cooling-Credit-Framework/tree/main/docs/business_models)

---

## Author / 著者

マスター / inchacomusho / InchaComisho

## License / ライセンス

CC BY 4.0
