# محاكاة استعادة التربة والزراعة

## الغرض والأهمية

يقارن التربة المتدهورة والمستعادة عبر الغلة وخسارة الجفاف والرطوبة وتوفير المدخلات والتدفق الزراعي. وتظهر الكلفة الأولية والخسارة المتجنبة المتأخرة في تقييم واحد.

## الافتراضات والمؤشرات

القيم الافتراضية: المساحة والغلة والسعر والتدهور والجفاف وكلفة الاستعادة وتحسن الرطوبة والاستقرار وخفض السماد والماء وإيراد الرصيد.

يسجل CSV مؤشرات سنوية مادية ومالية ومخصومة وتراكمية. القيم النقدية بوحدات توضيحية.

## التشغيل

```bash
pip install -r requirements.txt
python soil_recovery_agriculture_sim.py
```

ينشأ `outputs/` تلقائيًا والنموذج حتمي.

## المخرجات والتفسير

`soil_recovery_agriculture_results.csv`, `yield_comparison.png`, `soil_moisture_index.png`, `agricultural_net_benefit.png`, `input_cost_savings.png`, `agriculture_roi_sensitivity.png`.

تقرأ الفئات السنوية قبل التراكمية. سنة الاسترداد هي أول سنة يصبح فيها التدفق التراكمي غير سالب؛ يستخدم NPV الخصم المحدد، ويقسم ROI المنفعة الصافية غير المخصومة على CAPEX الأولي. الحساسية تغير متغيرًا واحدًا وليست توزيعًا احتماليًا.

## القيود

هذا نموذج مفاهيمي لدعم القرار، وليس توقعًا دقيقًا. يجب استبدال الافتراضات ببيانات محلية مقاسة قبل استخدامه في قرارات السياسة أو الاستثمار. لا يغطي كل التفاعلات والتوزيع والضرائب والتمويل وعدم اليقين والتهجير والذيل المتطرف. يمنع العد المزدوج وتطلب مراجعة هندسية واكتوارية ومالية وقانونية.

## نتائج الحالة الأساسية

| المؤشر | النتيجة |
|---|---:|
| فترة التقييم | 20 سنة |
| الاسترداد | لا استرداد في الافتراضات الأساسية |
| المنافع | استقرار الغلة وخفض الجفاف والمدخلات |
| القيد | التدفق الزراعي المباشر غير كافٍ |
| التفسير | يلزم تقييم الغذاء والماء والدعم وسلسلة الإمداد |

لا تسترد الحالة الأساسية التكلفة. هذه نتيجة مفيدة لا فشلًا: قد يلزم دعم عام وتقييم الأمن الغذائي وتسعير مخاطر المياه ومدفوعات سلسلة الإمداد وأفق أطول.

## الرسوم الناتجة

### Yield Comparison

![Yield Comparison](outputs/yield_comparison.png)

### Soil Moisture Index

![Soil Moisture Index](outputs/soil_moisture_index.png)

### Agricultural Net Benefit

![Agricultural Net Benefit](outputs/agricultural_net_benefit.png)

### Input Cost Savings

![Input Cost Savings](outputs/input_cost_savings.png)

### Agriculture ROI Sensitivity

![Agriculture ROI Sensitivity](outputs/agriculture_roi_sensitivity.png)

## مقارنة السيناريوهات

![Scenario Payback Comparison](outputs/scenario_payback_comparison.png)

يقارن الرسم الحالات المحافظة والأساسية والمستقبل عالي المخاطر. تظهر أهمية الأرصدة عند مقارنة الخسائر المتجنبة إذا ارتفعت أعباء الحر والكوارث والصحة والطاقة؛ وهذه اختبارات وليست احتمالات.

تتوفر القيم الأساسية في [`outputs/scenario_comparison.csv`](outputs/scenario_comparison.csv).

## كيفية قراءة النتائج الضعيفة

See [كيفية قراءة النتائج الضعيفة](../HOW_TO_READ_WEAK_RESULTS_ar.md) for guidance on public support, missing benefit categories, MRV, and appraisal horizons.

---

## المؤلف

Master / inchacomusho / InchaComisho

مفكر ياباني مستقل، ومراقب، وصاحب تصورات ومقترحات، ومُعَيِّر للذكاء الاصطناعي، ومُعرِّف لمفهوم الحكمة الاصطناعية.  
مؤسس ومقترح الإطار العلمي لـ Natural Complementary Science.  
ينشط علنًا في فلسفة القوانين الطبيعية، واستعادة دوران الكوكب، والتشارك الإبداعي مع الذكاء الاصطناعي.

---

## الذكاء الاصطناعي المتعاون وفريق التشارك

لقد تطور هذا النظام المعرفي من خلال الحوار والتشارك بين Master وعدة شركاء من الذكاء الاصطناعي.

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

يُنشر هذا المستودع بموجب ترخيص المشاع الإبداعي الدولي Attribution 4.0.  
يُسمح بالمشاركة وإعادة الاستخدام والترجمة والتعديل وإعادة التوزيع مع الإشارة الواضحة إلى **Master / inchacomusho / InchaComisho**.
