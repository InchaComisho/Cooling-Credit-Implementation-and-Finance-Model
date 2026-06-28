# 自然冷却フィードバック・シミュレーション結果

[English](RESULTS.md) | [日本語](RESULTS_ja.md) | [العربية](RESULTS_ar.md)

このページは、帳簿上の相殺価値と、測定された物理的冷却・保水・蒸散・腐葉土化・山林再生・災害圧力低減・地域経済共便益に基づくクーリングクレジット・シナリオを比較する概念シミュレーション結果である。

グラフ本体のラベルは英語だが、各図の下に英語・日本語・アラビア語の説明を付けている。

---

## 主要結果

**統合自然フィードバック**シナリオが最も高いクーリングクレジット価値を示した。これは、都市冷却、有機ごみ腐葉土化、山林再生、土壌保水、蒸散回復、MRV信頼度、地域参加が相互に強化されるためである。

**帳簿上の相殺のみ**のシナリオでは、会計上の価値は増加し得るが、この概念モデル上では、物理的冷却、保水、蒸散回復、災害圧力低減は発生しない。

---

## 最終年サマリー

| シナリオ | クーリングクレジット価値 | 物理冷却 | 保水 | 蒸散・蒸発散 | 災害圧力低減 | 地域共便益 |
|---|---:|---:|---:|---:|---:|---:|
| Integrated Natural Feedback | 57.30 | 57.73 | 92.61 | 89.97 | 66.60 | 71.06 |
| Forest Regeneration | 15.68 | 28.58 | 58.79 | 64.24 | 39.26 | 46.83 |
| Organic Waste to Humus | 11.67 | 24.07 | 56.43 | 50.97 | 27.51 | 45.22 |
| Urban Mist Cooling | 6.51 | 24.94 | 28.98 | 21.58 | 19.44 | 28.14 |
| Accounting Offset Only | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.10 |

---

## 図

### Accounting Offset Value: Ledger Growth Without Guaranteed Cooling

![Accounting Offset Value](outputs/accounting_offset_value.svg)

- **EN:** This figure shows how ledger-style offset value can rise even when the accounting-only scenario does not generate measured cooling, water retention, evapotranspiration, or disaster-pressure reduction.
- **JA:** この図は、帳簿上の相殺価値が増えても、会計だけのシナリオでは測定された冷却・保水・蒸散・災害圧力低減が発生しないことを示す。
- **AR:** يوضح هذا الشكل أن قيمة التعويض المحاسبية قد ترتفع حتى عندما لا ينتج سيناريو المحاسبة وحده تبريدًا مقاسًا أو احتفاظًا بالماء أو تبخرًا-نتحًا أو خفضًا لضغط الكوارث.

---

### Cooling Credit Value: Physical Cooling + Natural Feedback

![Cooling Credit Value](outputs/cooling_credit_value.svg)

- **EN:** This figure compares Cooling Credit value across scenarios. The integrated natural feedback scenario rises highest because cooling, water retention, evapotranspiration, forest recovery, humus recovery, MRV, and local co-benefits reinforce one another.
- **JA:** この図は、各シナリオのクーリングクレジット価値を比較する。統合自然フィードバックは、冷却・保水・蒸散・山林回復・腐葉土化・MRV・地域共便益が相互に強化されるため最も高くなる。
- **AR:** يقارن هذا الشكل قيمة أرصدة التبريد بين السيناريوهات. يرتفع سيناريو التغذية الراجعة الطبيعية المتكاملة أكثر لأن التبريد واحتفاظ الماء والتبخر-النتح وتعافي الغابات والدبال وMRV والمنافع المحلية يعزز بعضها بعضًا.

---

### Final-Year Physical Outcomes by Scenario

![Final-Year Physical Outcomes](outputs/final_year_physical_outcomes.svg)

- **EN:** This figure compares final-year physical and social outcomes. Cooling Credit is strongest when the project changes real environmental functions, not only financial accounting.
- **JA:** この図は、最終年の物理的・社会的成果を比較する。クーリングクレジットは、金融会計だけでなく、現実の環境機能を変えるほど強くなる。
- **AR:** يقارن هذا الشكل النتائج الفيزيائية والاجتماعية في السنة الأخيرة. تكون أرصدة التبريد أقوى عندما يغيّر المشروع وظائف البيئة الحقيقية، لا الحسابات المالية فقط.

---

## データファイル

- [最終年サマリーCSV](outputs/natural_feedback_cooling_final_year_summary.csv)

Pythonスクリプトをローカル実行すると、完全な時系列CSVも生成される。

---

## 注意

これは概念的な決定論モデルであり、気象予測、水文予測、作物予測、災害予測、投資助言ではない。政策、補助金、保険、投資に使う場合は、地域の実測データと独立MRVで前提値を置き換える必要がある。
