# محاكاة تكاليف ومنافع التبريد الحضري

[English](README.md) | [日本語](README_ja.md) | [العربية](README_ar.md)

## الغرض والأهمية

تقارن بين التكاليف الطبية وطاقة التبريد وكوارث الحرارة في حالة عدم اتخاذ أي إجراء، مقابل 20 عاماً من تدخل التبريد وتكاليفه وإيرادات الأرصدة. تجعل التكلفة المقدمة والخسارة المُجنَّبة المتأخرة مرئيتين في تقييم واحد متسق.

## الافتراضات والمؤشرات

القيم الافتراضية: السنوات، والخصم ونمو الأضرار، وثلاث فئات خسارة أولية، وCAPEX/OPEX/MRV، ومعدلات التخفيض، وتغيرات WBGT ودرجة حرارة السطح، وسعر الرصيد ووحداته ونموه.

يُرسل CSV المؤشرات السنوية الفيزيائية والتكلفة والإيراد والقيمة المخصومة والتراكمية. القيم النقدية بوحدات عملة توضيحية.

## التشغيل

```bash
pip install -r requirements.txt
python urban_cooling_cost_benefit_sim.py
```

يُنشئ السكربت `outputs/` تلقائياً وهو حتمي.

## ملفات الإخراج والتفسير

`urban_cooling_cost_benefit_results.csv`، `cumulative_cost_comparison.png`، `annual_avoided_costs.png`، `net_benefit_and_payback.png`، `cooling_indicators.png`، `roi_sensitivity.png`.

اقرأ مخططات الفئات السنوية قبل المخططات التراكمية. الاسترداد هو أول سنة يصبح فيها صافي التدفق النقدي التراكمي إيجابياً. مخططات الحساسية ليست توزيعات احتمالية.

## القيود

هذا نموذج مفاهيمي لدعم القرار وليس توقعاً. جميع الافتراضات شفافة ويجب استبدالها ببيانات محلية مقاسة قبل قرارات السياسة أو الاستثمار. تجنب الازدواج في فئات المنافع واحصل على مراجعة هندسية وإكتوارية ومالية وقانونية.

## نتائج الحالة الأساسية

| المؤشر | النتيجة |
|---|---:|
| فترة التقييم | 20 سنة |
| الاسترداد | السنة 11 |
| المنافع الرئيسية | تجنب التكاليف الطبية وطاقة التبريد وخسائر الحرارة؛ إيرادات الأرصدة |
| القيود الرئيسية | CAPEX، OPEX، MRV |
| التفسير | نموذج بلدي تتراكم فيه الخسائر المتجنبة على المدى المتوسط |

## مخططات الإخراج

### مقارنة التكاليف التراكمية

![Cumulative Cost Comparison](outputs/cumulative_cost_comparison.png)

### التكاليف السنوية المتجنبة

![Annual Avoided Costs](outputs/annual_avoided_costs.png)

### صافي المنفعة وفترة الاسترداد

![Net Benefit and Payback](outputs/net_benefit_and_payback.png)

### مؤشرات التبريد

![Cooling Indicators](outputs/cooling_indicators.png)

### حساسية ROI

![ROI Sensitivity](outputs/roi_sensitivity.png)

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
