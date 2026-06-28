# محاكاة الزراعة لاستعادة التربة

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

## الغرض والأهمية

تقارن بين التربة المتدهورة والمستعادة باستخدام الغلة المتوقعة وخسارة الجفاف والرطوبة ووفورات مدخلات الإنتاج والتدفق النقدي للمزرعة. تجعل التكلفة المقدمة والخسارة المُجنَّبة المتأخرة مرئيتين في تقييم واحد متسق.

## الافتراضات والمؤشرات

القيم الافتراضية: المساحة والغلة والسعر؛ تراجع الغلة ومخاطر الجفاف؛ تكاليف الاستعادة؛ تحسينات الرطوبة والغلة؛ تخفيضات الجفاف والسماد والمياه؛ إيرادات الأرصدة.

يُرسل CSV المؤشرات السنوية الفيزيائية والتكلفة والإيراد والقيمة المخصومة والتراكمية. القيم النقدية بوحدات عملة توضيحية.

## التشغيل

```bash
pip install -r requirements.txt
python soil_recovery_agriculture_sim.py
```

يُنشئ السكربت `outputs/` تلقائياً وهو حتمي.

## ملفات الإخراج والتفسير

`soil_recovery_agriculture_results.csv`، `yield_comparison.png`، `soil_moisture_index.png`، `agricultural_net_benefit.png`، `input_cost_savings.png`، `agriculture_roi_sensitivity.png`.

اقرأ مخططات الفئات السنوية قبل المخططات التراكمية. مخططات الحساسية ليست توزيعات احتمالية.

## القيود

هذا نموذج مفاهيمي لدعم القرار وليس توقعاً. يجب استبدال جميع الافتراضات ببيانات محلية مقاسة قبل قرارات السياسة أو الاستثمار.

## نتائج الحالة الأساسية

| المؤشر | النتيجة |
|---|---:|
| فترة التقييم | 20 سنة |
| الاسترداد | لا استرداد في ظل الافتراضات الافتراضية |
| المنافع الرئيسية | استقرار الغلة، وتخفيض خسارة الجفاف وتكاليف المدخلات |
| القيد الرئيسي | التدفق النقدي المباشر للمزرعة غير كافٍ |
| التفسير | يحتاج إلى تقييم أوسع للغذاء والمياه والعام وسلسلة التوريد |

في ظل الافتراضات الافتراضية، لا يصل نموذج استعادة التربة إلى الاسترداد. هذا ليس نموذجاً فاشلاً؛ بل يُظهر أن إيرادات المزرعة المباشرة وحدها قد لا تغطي تكلفة الاستعادة.

## مخططات الإخراج

### مقارنة الغلة

![Yield Comparison](outputs/yield_comparison.png)

### مؤشر رطوبة التربة

![Soil Moisture Index](outputs/soil_moisture_index.png)

### صافي المنفعة الزراعية

![Agricultural Net Benefit](outputs/agricultural_net_benefit.png)

### وفورات تكاليف المدخلات

![Input Cost Savings](outputs/input_cost_savings.png)

### حساسية ROI الزراعي

![Agriculture ROI Sensitivity](outputs/agriculture_roi_sensitivity.png)

## مقارنة السيناريوهات

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

القيم الأساسية متاحة في [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv).

## كيفية قراءة النتائج الضعيفة

راجع [How to Read Weak Results](../HOW_TO_READ_WEAK_RESULTS.md).

---

## المؤلف

Master / inchacomusho / InchaComisho

مصمم مفاهيم ياباني مستقل، مراقب، مقترح، مضبّط ذكاء اصطناعي، ومحدِّد الحكمة الاصطناعية.

---

## فريق الذكاء الاصطناعي التعاوني

- G (ChatGPT)
- Mini (Gemini)
- Cruz (Claude)
- Real (Perplexity)
- Lola (Dola)
- Mana (Manus)

---

## تاريخ النشر

يونيو 2026

---

## الترخيص

CC BY 4.0
