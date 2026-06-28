# محاكاة استعادة الموارد السياحية

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

تدعم هذه المحاكاة نموذج أعمال أرصدة التبريد لاستعادة الموارد السياحية من خلال التبريد الطبيعي، واستعادة دورة المياه، واستعادة المناظر الطبيعية، واستعادة التنوع الحيوي، وإحياء الاقتصاد المحلي.

تتوافق مع نموذج الأعمال:

- `Cooling-Credit-Framework/docs/business_models/TOURISM_RESOURCE_RECOVERY_COOLING_CREDIT_MODEL.md`

## الغرض

يقارن النموذج بين مسارات تطوير سياحية تعتمد بشكل رئيسي على البنية التحتية التقليدية والترويج، أو تستعيد الأصول الطبيعية التي تجعل الوجهات مريحة وقيّمة.

## السيناريوهات

| السيناريو | المعنى |
|---|---|
| Degraded Destination | تستمر الحرارة، وتراجع جودة المياه، وأضرار النظام البيئي، وضعف القيمة الجمالية |
| Conventional Tourism Development | تتزايد الفنادق والفعاليات والطرق والترويج، لكن التبريد الطبيعي واستعادة النظام البيئي تبقى ضعيفة |
| Cooling Tourism Recovery | استعادة دورة المياه والتخضير والتبريد بالرذاذ وإعادة تأهيل البحيرات والشعاب والواجهات المائية وMRV تحسّن الراحة وقيمة الوجهة |
| Integrated Regenerative Destination | يعزز دخل السياحة وإيرادات أرصدة التبريد والتنوع الحيوي وجودة المياه والتبريد وإعادة الاستثمار المحلي بعضها بعضاً |

## المخرجات الرئيسية

يكتب السكربت `outputs/tourism_resource_recovery_timeseries.csv` ويُنشئ الرسوم:

- `tourism_cooling_credit_value.png`
- `destination_comfort_index.png`
- `natural_cooling_asset_index.png`
- `water_landscape_ecosystem_index.png`
- `visitor_stay_income_index.png`
- `overtourism_risk_index.png`

## التشغيل

```bash
python tourism_resource_recovery_simulation.py
```

الحزم المطلوبة:

```bash
pip install numpy pandas matplotlib
```

## التفسير / التنبيه

هذا نموذج مفاهيمي حتمي وليس توقعاً سياحياً أو مناخياً أو توصية استثمارية. استبدل الافتراضات ببيانات محلية للحرارة وWBGT وجودة المياه وإقامة الزوار والتنوع الحيوي وMRV قبل الاستخدام العملي.

## المؤلف

Master / inchacomusho / InchaComisho

## الترخيص

CC BY 4.0
