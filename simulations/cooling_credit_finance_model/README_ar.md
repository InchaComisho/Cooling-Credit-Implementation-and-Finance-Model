# محاكاة تمويل أرصدة التبريد

## الغرض والأهمية

ينمذج إيرادات SPV وتكاليفه واحتياطيه وعائد المجتمع وتدفق المستثمر على 20 سنة. وتظهر الكلفة الأولية والخسارة المتجنبة المتأخرة في تقييم واحد.

## الافتراضات والمؤشرات

القيم الافتراضية: رأس مال المحفظة ومعدل التشغيل والتحقق والسجل وخمسة إيرادات والكمية والسعر والنمو ونسب المجتمع والاحتياط والخصم.

يسجل CSV مؤشرات سنوية مادية ومالية ومخصومة وتراكمية. القيم النقدية بوحدات توضيحية.

## التشغيل

```bash
pip install -r requirements.txt
python cooling_credit_finance_sim.py
```

ينشأ `outputs/` تلقائيًا والنموذج حتمي.

## المخرجات والتفسير

`cooling_credit_finance_results.csv`, `revenue_stack.png`, `cash_flow_waterfall.png`, `investor_cumulative_cash_flow.png`, `npv_roi_payback.png`, `credit_price_sensitivity.png`.

تقرأ الفئات السنوية قبل التراكمية. سنة الاسترداد هي أول سنة يصبح فيها التدفق التراكمي غير سالب؛ يستخدم NPV الخصم المحدد، ويقسم ROI المنفعة الصافية غير المخصومة على CAPEX الأولي. الحساسية تغير متغيرًا واحدًا وليست توزيعًا احتماليًا.

## القيود

هذا نموذج مفاهيمي لدعم القرار، وليس توقعًا دقيقًا. يجب استبدال الافتراضات ببيانات محلية مقاسة قبل استخدامه في قرارات السياسة أو الاستثمار. لا يغطي كل التفاعلات والتوزيع والضرائب والتمويل وعدم اليقين والتهجير والذيل المتطرف. يمنع العد المزدوج وتطلب مراجعة هندسية واكتوارية ومالية وقانونية.

## نتائج الحالة الأساسية

| المؤشر | النتيجة |
|---|---:|
| فترة التقييم | 20 سنة |
| الاسترداد | السنة 9 |
| المنفعة | إيرادات تعاقدية متنوعة مع الرصيد |
| القيد | مخاطر الطرف والتنفيذ والسعر |
| التفسير | أقوى مرشح لهيكل SPV / صندوق |

يوضح تكديس الإيراد قوة المحفظة مقابل مشروع يعتمد على الرصيد وحده، وتسترد الحالة الأساسية في السنة 9.

## الرسوم الناتجة

### Revenue Stack

![Revenue Stack](outputs/revenue_stack.png)

### Cash Flow Waterfall

![Cash Flow Waterfall](outputs/cash_flow_waterfall.png)

### Investor Cumulative Cash Flow

![Investor Cumulative Cash Flow](outputs/investor_cumulative_cash_flow.png)

### NPV ROI Payback

![NPV ROI Payback](outputs/npv_roi_payback.png)

### Credit Price Sensitivity

![Credit Price Sensitivity](outputs/credit_price_sensitivity.png)

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
