# محاكاة أعمال تحويل الغابات

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

تدعم هذه المحاكاة نموذج أعمال تحويل الغابات الجبلية المهملة أو أحادية النبات إلى غابات فاكهة أصلية مختلطة، وغابات أحواض مائية، وغابات فطر، وغابات نباتات برية صالحة للأكل، وغابات سياحة، وأصول تنوع حيوي وتبريد.

تتوافق مع نموذج الأعمال:

- `Cooling-Credit-Framework/docs/business_models/MONOCULTURE_MOUNTAIN_FOREST_TO_NATIVE_FRUIT_FOREST_BUSINESS_MODEL.md`

## الغرض

يقارن النموذج مسارات إدارة الغابات من أحادية النبات المهملة إلى إعادة تجديد الغابات المختلطة متعددة الفاكهة الأصلية المتكاملة.

## السيناريوهات

| السيناريو | المعنى |
|---|---|
| Abandoned Monoculture | تبقى الغابة دون إدارة؛ يبقى احتفاظ الماء والتنوع الحيوي والمرونة من الكوارث ضعيفة |
| Timber-Only Management | يحسّن استخراج الأخشاب دخل الإدارة لكن يحدث تعافٍ محدود للنظام البيئي |
| Native-Fruit Mixed Forest | يُدخل التقسيم المناطقي الفاكهة والنباتات البرية الصالحة للأكل والفطر ونباتات الرحيق والأشجار العريضة الأوراق واستعادة الأحواض المائية |
| Integrated Watershed Food Tourism Forest | يعزز التبريد واحتفاظ الماء وإنتاج الغذاء والسياحة والتعليم والتنوع الحيوي وإيرادات مالك الغابة بعضها بعضاً |

## المخرجات الرئيسية

يكتب السكربت `outputs/forest_conversion_timeseries.csv` ويُنشئ الرسوم:

- `forest_cooling_credit_value.png`
- `watershed_retention_index.png`
- `forest_surface_cooling_index.png`
- `biodiversity_recovery_index.png`
- `food_tourism_income_index.png`
- `wildfire_erosion_risk_reduction_index.png`

## التشغيل

```bash
python forest_conversion_business_simulation.py
```

الحزم المطلوبة:

```bash
pip install numpy pandas matplotlib
```

## التفسير / التنبيه

هذا نموذج مفاهيمي حتمي وليس توقعاً للغابات أو الانزلاقات أو الحياة البرية أو توصية استثمارية. استبدل الافتراضات ببيانات محلية للغابات والتربة والمنحدرات والأحواض المائية والتنوع الحيوي والحصاد وMRV قبل الاستخدام العملي.

## المؤلف

Master / inchacomusho / InchaComisho

## الترخيص

CC BY 4.0
