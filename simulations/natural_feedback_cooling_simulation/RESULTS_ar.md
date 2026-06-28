# نتائج محاكاة التغذية الراجعة الطبيعية للتبريد

[English](RESULTS.md) | [日本語](RESULTS_ja.md) | [العربية](RESULTS_ar.md)

تلخص هذه الصفحة نتائج نموذج مفاهيمي يقارن بين قيمة التعويض المحاسبي وسيناريوهات أرصدة التبريد القائمة على التبريد الفيزيائي المقاس، واحتفاظ الماء، والتبخر-النتح، وتعافي الدبال، وتجدد الغابات، وخفض ضغط الكوارث، والمنافع الاقتصادية المحلية.

تستخدم الرسوم تسميات باللغة الإنجليزية، لكن أسفل كل شكل توجد شروح بالإنجليزية واليابانية والعربية.

---

## النتيجة الرئيسية

يعطي سيناريو **التغذية الراجعة الطبيعية المتكاملة** أعلى قيمة لأرصدة التبريد لأنه يجمع بين التبريد الحضري، وتحويل النفايات العضوية إلى دبال، وتجدد الغابات، واستعادة رطوبة التربة، واستعادة التبخر-النتح، وثقة MRV، والمشاركة المحلية.

أما سيناريو **التعويض المحاسبي وحده** فقد تزيد قيمته الدفترية، لكنه في هذا النموذج المفاهيمي لا ينتج تبريدًا فيزيائيًا أو احتفاظًا بالماء أو استعادة للتبخر-النتح أو خفضًا لضغط الكوارث.

---

## ملخص السنة الأخيرة

| السيناريو | قيمة رصيد التبريد | التبريد الفيزيائي | احتفاظ الماء | التبخر-النتح | خفض ضغط الكوارث | المنافع المحلية |
|---|---:|---:|---:|---:|---:|---:|
| Integrated Natural Feedback | 57.30 | 57.73 | 92.61 | 89.97 | 66.60 | 71.06 |
| Forest Regeneration | 15.68 | 28.58 | 58.79 | 64.24 | 39.26 | 46.83 |
| Organic Waste to Humus | 11.67 | 24.07 | 56.43 | 50.97 | 27.51 | 45.22 |
| Urban Mist Cooling | 6.51 | 24.94 | 28.98 | 21.58 | 19.44 | 28.14 |
| Accounting Offset Only | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 4.10 |

---

## الأشكال

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

## ملف البيانات

- [CSV لملخص السنة الأخيرة](outputs/natural_feedback_cooling_final_year_summary.csv)

عند تشغيل سكربت Python محليًا، يتم أيضًا إنشاء CSV كامل للسلسلة الزمنية.

---

## تنبيه

هذا نموذج مفاهيمي حتمي، وليس توقعًا للطقس أو المياه أو المحاصيل أو الكوارث أو نصيحة استثمارية. يجب استبدال جميع الافتراضات ببيانات محلية مقاسة وMRV مستقل قبل استخدامه في السياسات أو الدعم أو التأمين أو الاستثمار.
