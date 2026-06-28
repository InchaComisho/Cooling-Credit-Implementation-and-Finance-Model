# محاكاة التغذية الراجعة الطبيعية للتبريد

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

تقارن هذه الوحدة بين سيناريو التعويض المحاسبي بأسلوب أرصدة الكربون وسيناريوهات تنفيذ أرصدة التبريد المبنية على التبريد الفيزيائي المقاس، واستعادة رطوبة التربة، والتبخر-النتح، وتحويل النفايات العضوية إلى دبال، وتجدد الغابات، وتبريد المحيط داخل EEZ، وتجدد حافة الصحراء الساحلية، والمنافع الاقتصادية المحلية.

## صفحات النتائج

- [Results — English](RESULTS.md)
- [結果 — 日本語](RESULTS_ja.md)
- [النتائج — العربية](RESULTS_ar.md)

تستخدم الرسوم تسميات إنجليزية، لكن كل صفحة نتائج تضع شروحاً بالإنجليزية واليابانية والعربية مباشرة أسفل كل شكل.

## السيناريوهات

| السيناريو | المعنى |
|---|---|
| Accounting Offset Only | تنمو إيرادات الأرصدة لكن التبريد الفيزيائي لا يتحسن بالضرورة |
| Urban Mist Cooling | يقلل التبريد بالرذاذ فوق الصوتي والتبريد الحضري القائم على دورة المياه من الإجهاد الحراري |
| Organic Waste to Humus | يتحول فقد الغذاء والأوراق والنفايات العضوية إلى دبال وسماد لتحسين تبريد رطوبة التربة |
| Forest Regeneration | تتحول الغابات المتدهورة أو أحادية النبات إلى غابات مختلطة أو غابات غذائية أو غابات أصلية |
| EEZ Ocean Cooling | تبريد المحيط بأسلوب OBS/OTU/UMS، وأكسجة، ودوران رأسي، ودعم شبكة الغذاء، واستعادة المصايد، ومنافع المرجان والسياحة |
| Coastal Desert Edge Regeneration | تحلية ساحلية، وتبريد بنظام UMS، واستقرار الدبال والكائنات الدقيقة، ونباتات حافة الصحراء، وطاقة شمسية هرمية ورياح عمودية، وكفاءة السكن تحت الأرض |
| Integrated Natural Feedback | يعزز التبريد الحضري واستعادة الدبال وتجدد الغابات وتبريد المحيط وتجدد حافة الصحراء واستعادة دورة المياه بعضها بعضاً |

## المخرجات الرئيسية

يكتب السكربت `outputs/natural_feedback_cooling_timeseries.csv` والرسوم التالية عند تشغيله محلياً.

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

يتضمن المستودع أيضاً أشكال SVG للنتائج المُنشأة للمراجعة السريعة.

- [Accounting Offset Value](outputs/accounting_offset_value.svg)
- [Cooling Credit Value with Ocean Scenario](outputs/cooling_credit_value_with_ocean.svg)
- [Cooling Credit Value with Desert Scenario](outputs/cooling_credit_value_with_desert.svg)
- [Final-Year Physical Outcomes with Desert Scenario](outputs/final_year_physical_outcomes_with_desert.svg)
- [Ocean Cooling and Fishery Outcomes](outputs/ocean_cooling_fishery_outcomes.svg)
- [Desert Edge Regeneration Outcomes](outputs/desert_edge_regeneration_outcomes.svg)
- [Final-Year Summary CSV with Desert Scenario](outputs/natural_feedback_cooling_final_year_summary_with_desert.csv)

## التشغيل

```bash
python natural_feedback_cooling_simulation.py
```

الحزم المطلوبة:

```bash
pip install numpy pandas matplotlib
```

## التفسير / التنبيه

هذا نموذج مفاهيمي حتمي وليس توقعاً. استبدل جميع الافتراضات الافتراضية ببيانات محلية مقاسة قبل استخدامه في السياسات أو الدعم أو التأمين أو قرارات الاستثمار.

الغرض هو إظهار الفرق بين:

```text
قيمة التعويض المحاسبي
```

و

```text
التبريد الفيزيائي المقاس + استعادة التغذية الراجعة الطبيعية + دوران المحيط + تجدد حافة الصحراء + المنافع المحلية
```

## المؤلف

Master / inchacomusho / InchaComisho

## الترخيص

CC BY 4.0
