# محاكاة تكلفة ومنفعة التبريد الحضري

## الغرض والأهمية

يقارن تكاليف الصحة وطاقة التبريد وكوارث الحر بين عدم التدخل ومشروع تبريد لمدة 20 سنة. وتظهر الكلفة الأولية والخسارة المتجنبة المتأخرة في تقييم واحد.

## الافتراضات والمؤشرات

القيم الافتراضية: السنوات والخصم ونمو الضرر وفئات الخسارة ورأس المال والتشغيل والتحقق ونسب الخفض ومؤشرات الحرارة وسعر وكمية الرصيد.

يسجل CSV مؤشرات سنوية مادية ومالية ومخصومة وتراكمية. القيم النقدية بوحدات توضيحية.

## التشغيل

```bash
pip install -r requirements.txt
python urban_cooling_cost_benefit_sim.py
```

ينشأ `outputs/` تلقائيًا والنموذج حتمي.

## المخرجات والتفسير

`urban_cooling_cost_benefit_results.csv`, `cumulative_cost_comparison.png`, `annual_avoided_costs.png`, `net_benefit_and_payback.png`, `cooling_indicators.png`, `roi_sensitivity.png`.

تقرأ الفئات السنوية قبل التراكمية. سنة الاسترداد هي أول سنة يصبح فيها التدفق التراكمي غير سالب؛ يستخدم NPV الخصم المحدد، ويقسم ROI المنفعة الصافية غير المخصومة على CAPEX الأولي. الحساسية تغير متغيرًا واحدًا وليست توزيعًا احتماليًا.

## القيود

هذا نموذج مفاهيمي لدعم القرار، وليس توقعًا دقيقًا. يجب استبدال الافتراضات ببيانات محلية مقاسة قبل استخدامه في قرارات السياسة أو الاستثمار. لا يغطي كل التفاعلات والتوزيع والضرائب والتمويل وعدم اليقين والتهجير والذيل المتطرف. يمنع العد المزدوج وتطلب مراجعة هندسية واكتوارية ومالية وقانونية.

## نتائج الحالة الأساسية

| المؤشر | النتيجة |
|---|---:|
| فترة التقييم | 20 سنة |
| الاسترداد | السنة 11 |
| المنافع | الصحة وطاقة التبريد وأضرار الحر وإيراد الرصيد |
| القيود | رأس المال والتشغيل وMRV |
| التفسير | نموذج بلدي تتراكم فيه الخسائر المتجنبة متوسط الأجل |

يبين الرسم التراكمي عبء الاستثمار المبكر، ثم تراكم تجنب الصحة والكهرباء وأضرار الحر حتى الاسترداد قرب السنة 11.

## الرسوم الناتجة

### Cumulative Cost Comparison

![Cumulative Cost Comparison](outputs/cumulative_cost_comparison.png)

### Annual Avoided Costs

![Annual Avoided Costs](outputs/annual_avoided_costs.png)

### Net Benefit and Payback

![Net Benefit and Payback](outputs/net_benefit_and_payback.png)

### Cooling Indicators

![Cooling Indicators](outputs/cooling_indicators.png)

### ROI Sensitivity

![ROI Sensitivity](outputs/roi_sensitivity.png)

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
