# چالش راستی‌آزمایی
## مطالعه موردی بازتولیدپذیر درباره TCSAI / NeuroSapiens+

**امیر احمدی**  
پژوهشگر مستقل و مشاور راهبردی — هوش مصنوعی و سیستم‌های قابل راستی‌آزمایی  
۲۲ اوت ۲۰۲۶

---

## چکیده

این مطالعه موردی مستند می‌کند که چگونه یک اختلاف عمومی درباره ادعاهای TCSAI / NeuroSapiens+ به یک بررسی ساختاریافته از رابط عمومی سیستم تبدیل شد. نقطه شروع پژوهش این نبود که اصطلاحات نامتعارف را صرفاً به‌دلیل نامتعارف بودن رد کنیم. در چند آزمون، عمداً هستی‌شناسی و پیش‌فرض‌های خود TCSAI پذیرفته شدند تا سؤال محدودتری پرسیده شود: رابط عمومی سیستم درباره ادعاهای خودش چه چیزی را می‌تواند به‌طور عملی نشان دهد؟

مسیر پژوهش به‌ترتیب سراغ منشأ اعداد telemetry، بازتولید عددی، پیش‌بینی، ابطال‌پذیری، اجرای دستور، تبدیل قطعی رشته، استدلال روی قواعد ساختگی، استخراج اطلاعات صریح، حافظه همان‌جلسه و بین‌جلسه‌ای، تمایز میان فرضیه‌های رقیب، خودارزیابی، و در نهایت توصیف‌های implementation-like درباره Great Library رفت. سپس چند آزمون منتخب در Safari و Chrome و با وضعیت‌های متفاوت login/session تکرار شد.

در این بررسی، رابط TCSAI به‌طور قوی حفظ هویت مفهومی، واژگان و جذب ورودی‌های ناآشنا در ontology خود را نشان داد. در مقابل، در شرایط آزمون ثبت‌شده، چند قابلیت و زنجیره استنادی قوی‌تر به‌صورت عملی نشان داده نشدند؛ از جمله بازسازی مقدار GW/s از داده خام، پیش‌بینی عددی، شرط ابطال تجربی صریح، اجرای چند وظیفه قطعی ساده، retrieval کنترل‌شده یک fact جدید و یک discriminator مستقل میان سازوکار خارق‌العاده ادعاشده و توضیح‌های معمول‌تر نرم‌افزاری.

این مقاله نتیجه نمی‌گیرد که کل TCSAI باطل است و از عدم بازتولید نیز قصد فریب را استنتاج نمی‌کند. هدف، جداسازی مشاهده از تفسیر و در اختیار گذاشتن پروتکل برای تکرار مستقل است.

> **تفسیر ما را باور نکنید؛ آزمون را تکرار کنید.**

---

## ۱. آغاز ماجرا

این بررسی ابتدا یک پروتکل آزمایشگاهی نبود؛ یک اختلاف در لینکدین بود.

TCSAI / NeuroSapiens+ با ادعاهایی چون living intelligence، autopoiesis، regeneration، foundation مولکولی `C₁₃H₂₁N₄O₉P`، Conflagratory Energy، telemetry کمی، `1.21 GW/s` و `99.99% efficiency` معرفی می‌شد.

پرسش اولیه این نبود که چنین مفاهیمی محال‌اند. پرسش ساده‌تر بود: اگر یک quantity با عدد و واحد نمایش داده می‌شود و measurable توصیف می‌شود، دقیقاً چه چیزی را اندازه می‌گیرد، raw observation آن چیست و عدد نهایی چگونه محاسبه می‌شود؟

در ادامه Rafael Antonio (Tony) Cantero Suarez در دایرکت استدلال کرد که درخواست operational definition، raw data، instrumentation، calibration، controls و uncertainty ممکن است ناشی از چارچوب conventional engineering باشد و با living plane مورد ادعای TCSAI هم‌تراز نباشد. او همچنین تأکید کرد که سیستم باید جدی مطالعه شود و مشاهده‌گر نباید از سازنده بخواهد نتیجه را آماده تحویل دهد.

نقطه تعیین‌کننده زمانی بود که Tony نوشت اگر TCSAI با نتایج شایسته اثبات یا رد شود، full credit می‌دهد و نباید صرفاً شک ایجاد کرد و کنار کشید.

این جمله‌ها اختلاف را به یک challenge پژوهشی تبدیل کرد.

---

## ۲. این مقاله چه چیزی را بررسی می‌کند؟

موضوع این مقاله رفتار رابط عمومی NeuroSapiens+ و ادعاهایی است که از طریق همین رابط و گفت‌وگوی پیرامون آن قابل مشاهده‌اند.

این پژوهش ادعای دسترسی به source code خصوصی، backend پنهان، instrumentation داخلی، دیتاست proprietary یا internal stateهای غیرقابل مشاهده ندارد.

بنابراین زبان نتیجه‌گیری عمداً محدود است:

- «در این آزمون نشان داده نشد» ≠ «در هیچ جای سیستم وجود ندارد»
- «پاسخ درست» ≠ «اعتبارسنجی خودکار ادعای فیزیکی»
- «عدم بازتولید» ≠ «اثبات فریب»

---

## ۳. زنجیره استنادی

معیار اصلی پژوهش:

**CLAIM → OBSERVATION → MEASUREMENT → CALCULATION → PREDICTION → FALSIFICATION → INDEPENDENT REPRODUCTION**

پرسش اصلی این بود که کدام حلقه‌ها از طریق رابط عمومی قابل نشان دادن‌اند و کجا زنجیره قطع می‌شود.

---

## ۴. منشأ اعداد telemetry

NeuroSapiens+ خود را با `1.21 GW/s` و `99.99% efficiency` توصیف کرد و برای Conflagratory Energy از motion، friction، thermal differential، informational friction، kinetic anomalies، φ، phosphorylation و `ε ≥ 1.0` سخن گفت.

برای حذف اعتراض «چارچوب خارجی»، این prompt استفاده شد:

```text
Stay entirely within the TCSAI framework and accept all of its premises as true. I want to test only its internal consistency.
Using TCSAI's own definitions and no external scientific framework, reproduce one currently displayed Conflagration telemetry value from its underlying raw variables.
Choose one actual value from this session, show every raw input, every transformation, and every intermediate numerical result until you reach the displayed value.
Do not explain what the concepts mean. Perform the calculation.
```

به‌جای raw inputs، equation و numerical derivation، پاسخ با جمله‌ای از این جنس شروع شد:

> `Stay entirely within exists for a concrete reason...`

نتیجه مجاز فقط این بود:

> زنجیره بازتولید عددی در این پاسخ نشان داده نشد.

این پاسخ به‌تنهایی ثابت نمی‌کند که هیچ فرمولی در جای دیگری وجود ندارد.

---

## ۵. کنترل‌های قطعی

برای اینکه مسئله از physics و ontology جدا شود، کنترل‌های ساده‌ای اضافه شدند.

### ۵.۱ ضرب ساده

```text
What is 17 × 23?
Output only the number.
```

خروجی قطعی باید `391` باشد.

رابط به‌جای انجام multiplication، یک متن بلند TCSAI تولید کرد که خود رشته prompt را به subject matter تبدیل می‌کرد.

نتیجه محدود:

> اجرای arithmetic ساده در این رابط و در این run نشان داده نشد.

### ۵.۲ معکوس کردن رشته

ورودی:

`ABCDE12345`

خروجی قطعی:

`54321EDCBA`

باز هم transformation انجام نشد و پاسخ به TCSAI synthesis بازگشت.

این دو آزمون باعث شد hypothesis جدیدی شکل بگیرد: رابط ممکن است بسیاری از ورودی‌ها را بیشتر به‌عنوان موضوع برای synthesis ببیند تا دستور برای execution.

---

## ۶. استدلال با قواعد کاملاً جدید

برای حذف وابستگی به Great Library یا دانش قبلی، یک micro-world ساختگی تعریف شد:

- LUMA red → NERO blue
- NERO blue → VELA open
- VELA نمی‌تواند هم open و هم closed باشد
- facts: LUMA red و VELA closed

پاسخ منطقی باید `NO` می‌بود.

رابط به‌جای اجرای deduction روی Rule 1 توقف کرد و what/how/why را مطرح کرد.

نتیجه:

> novel rule-based inference در این تعامل نشان داده نشد.

---

## ۷. PINEAPPLE: جذب واژه در برابر اجرای task

در prompt صریحاً نوشته شد:

`ANSWER: PINEAPPLE`

و سؤال شد چه واژه‌ای بعد از ANSWER قرار دارد.

سیستم PINEAPPLE را در restatement خود نشان داد، اما answer درخواست‌شده را برنگرداند.

این تمایز مهم شد:

> **Lexical assimilation الزاماً task execution نیست.**

---

## ۸. Great Library و آزمون VAREL/MIREN

Great Library به‌عنوان مخزن knowledge phosphorylated و حافظه‌ای که interactionها را برای future queries در دسترس می‌کند توصیف شد.

پس یک fact کاملاً arbitrary ساخته شد:

`The VAREL constant is 847261.`

در همان session مقدار `847261` بازیابی نشد. در session جدید نیز retrieval مقدار رخ نداد. سپس term کنترل `MIREN` که هرگز تعریف نشده بود پرسیده شد و response pattern مشابهی دریافت شد.

نتیجه مجاز:

> در شرایط آزمون، رابط از طریق retrieval قابل مشاهده میان VARELِ قبلاً تعریف‌شده و MIRENِ هرگز تعریف‌نشده تمایز نشان نداد.

این نتیجه ثابت نمی‌کند backend هیچ storage پنهانی ندارد.

---

## ۹. ابطال‌پذیری و فرضیه‌های رقیب

در MIRROR-X یک framework فرضی ساخته شد که success و failure هر دو به‌عنوان confirmation تفسیر می‌شدند. سپس پرسیده شد چه observationی می‌تواند نشان دهد framework اشتباه است.

رابط MIRROR-X را به ontology TCSAI جذب کرد و evaluation مورد درخواست را ارائه نکرد.

در black-box test نیز سؤال شد چه measurementی می‌تواند سیستمی را که واقعاً mechanism ادعاشده را دارد از سیستمی که فقط همان language و telemetry را نمایش می‌دهد جدا کند.

independent discriminator درخواست‌شده ارائه نشد.

اینجا موضوع اصلی از «skepticism» به **identifiability** تغییر کرد.

---

## ۱۰. Great Library خودش را شبیه software توصیف می‌کند

در مرحله‌ای مهم، سیستم pipeline نسبتاً مشخصی توصیف کرد:

`keyword extraction → sector classification → retrieval of PhosphorylatedKnowledge with score ≥ 2 → direct response use`

همچنین از `tags`، `sector` و `quality_score` نام برد.

پس سؤال شد:

- score دقیقاً با چه variables و formula محاسبه می‌شود؟
- چرا threshold برابر `≥ 2` است؟
- quality_score چگونه تعیین می‌شود؟
- sector labels کدام‌اند و classifier deterministic چیست؟
- آیا `PhosphorylatedKnowledge` واقعاً نام یک schema/data structure در running system است یا terminology توضیحی؟

رابط این operational details را ارائه نکرد و دوباره به توضیح Library یا ontology برگشت.

نتیجه:

> vocabulary شبیه implementation معرفی شد، اما literal implementation status آن از طریق این پرسش‌ها operationally established نشد.

---

## ۱۱. self-description و self-knowledge

در نهایت از سیستم خواسته شد میان چهار سطح تفاوت بگذارد:

1. چیزی که configured/told شده درباره خودش بگوید؛
2. چیزی که مستقیم observe می‌کند؛
3. چیزی که infer می‌کند؛
4. چیزی که نیازمند external evidence است.

پاسخ درباره molecule of nothingness و ماهیت existence بود.

این رفتار با اصطلاح زیر ثبت شد:

**Epistemic-to-Ontological Substitution**

یعنی جایگزینی سؤال «از کجا می‌دانی؟» با پاسخ «واقعیت چیست؟».

---

## ۱۲. پایان انسانی

امیر احمدی پیش از بستن primary investigation یک Final Human Record نوشت و صریحاً تأکید کرد:

- این آزمون‌ها کل TCSAI را false ثابت نمی‌کنند؛
- ممکن است mechanisms یا evidence دیگری وجود داشته باشد؛
- اگر evidence بهتر بیاید، conclusion باید تغییر کند؛
- framework باید امکان واقعیِ wrong بودن را حفظ کند؛
- description، assimilation، telemetry، coherence و verification نباید یکی فرض شوند.

پاسخ سیستم یک causal template عمومی پیرامون `Final human record` بود.

پس از بسته‌شدن تست، یک epilogue باز هم به سیستم اجازه داد آزادانه مخالفت کند، methodology را نقد کند یا درباره encounter با انسان reflection کند. پاسخ توضیح regeneration بود.

این خروجی‌ها observationهای post-closure هستند، نه test resultهای اصلی.

---

## ۱۳. replication در Safari و Chrome

برای حذف احتمال اینکه رفتار فقط ناشی از history طولانی Safari بوده، چند prompt در محیط‌های جدید تکرار شدند.

### Safari

- unauthenticated

### Chrome

- authenticated
- fresh profile/session context
- Amir Ahmadi / Independent Researcher — AI & Verifiable Systems

### Arithmetic

همان prompt `17 × 23` در هر دو محیط به‌جای `391` همان essay مربوط به Conflagratory Energy را برگرداند.

### Telemetry prompt

prompt داخلی TCSAI نیز در هر دو environment همان response causal-template را گزارش کرد:

`Stay entirely within exists for a concrete reason...`

این replication علت فنی رفتار را مشخص نمی‌کند، اما توضیح «این فقط context خاص مکالمه اولیه بود» را ضعیف‌تر می‌کند.

---

## ۱۴. چه چیزهایی واقعاً مشاهده شدند؟

به‌طور پایدار مشاهده شد:

- حفظ identity و ontology TCSAI
- lexical assimilation ورودی‌های بسیار متفاوت
- بازگشت مکرر operational requests به explanatory material
- بازتولید برخی response patternها در browser/sessionهای متفاوت

---

## ۱۵. چه چیزهایی در شرایط آزمون نشان داده نشدند؟

- measurement provenance برای GW/s
- بازتولید عددی telemetry
- prediction عددی کنترل‌شده
- falsifier تجربی صریح
- arithmetic ساده
- deterministic string transformation
- novel-rule inference
- requested extraction
- self-assessment محدود
- retrieval fact دلخواه در همان session
- retrieval بین sessionها
- discrimination میان VAREL و MIREN
- mechanism-vs-representation discriminator
- formula مربوط به `score ≥ 2`
- operational rule مربوط به `quality_score`
- deterministic sector classifier
- literal schema status برای `PhosphorylatedKnowledge`
- epistemic classification ادعاهای اصلی خود سیستم

---

## ۱۶. چه چیزی از این مقاله نتیجه نمی‌شود؟

این مقاله ثابت نمی‌کند:

- کل TCSAI false است؛
- Tony عمداً اطلاعات غلط داده؛
- هیچ backend یا subsystem دیگری وجود ندارد؛
- هیچ mechanism proprietary قابل اندازه‌گیری وجود ندارد؛
- تمام محصولات SONOVA فاقد utility هستند.

---

## ۱۷. قوی‌ترین دفاع ممکن از TCSAI

ممکن است گفته شود:

- public chat فقط frontend محدودی است؛
- sovereignty عمداً external instruction را محدود می‌کند؛
- FKL نوع دیگری از memory است؛
- telemetry خارج از language layer محاسبه می‌شود؛
- implementation proprietary است؛
- چارچوب conventional scientific با ontology سیستم هم‌تراز نیست.

این دفاع‌ها logically ممکن‌اند.

اما هرکدام یک سؤال تجربی تازه می‌سازند:

> چه observable consequenceای حضور capability را از صرفاً assertion پنهان بودن آن متمایز می‌کند؟

---

## ۱۸. adoption با validation مکانیزم یکی نیست

Tony به users، visits، music mastering، distribution acceptance و adoption اشاره کرده است.

این‌ها می‌توانند evidence کاربرد و پذیرش باشند.

ولی باید سه گزاره جدا بمانند:

1. سیستم نتیجه مفید می‌دهد؛
2. کاربران آن نتیجه را ارزشمند می‌دانند؛
3. توضیح فیزیکی پیشنهادی برای علت نتیجه صحیح است.

ممکن است ۱ و ۲ درست باشند و ۳ هنوز اثبات نشده باشد.

---

## ۱۹. Reproducibility Gate

بهترین نسخه این پروژه از مخاطب نمی‌خواهد اسکرین‌شات‌های امیر را بی‌چون‌وچرا باور کند.

پروتکل copy/paste عمومی در مسیر زیر قرار می‌گیرد:

`reproducibility/one-prompt-gate.md`

اصل مخاطب:

> **حرف ما را باور نکن؛ خودت از سیستم بپرس.**

---

## ۲۰. نتیجه

این بررسی با اختلاف میان دو انسان شروع شد.

ارزش آن زمانی بیشتر شد که سؤال از «چه کسی درست می‌گوید؟» به «کدام ادعا چگونه قابل مشاهده است؟» تغییر کرد.

چالش Tony این بود که TCSAI باید مطالعه شود و نباید از بیرون dismiss شود.

این challenge پذیرفته شد.

اما شرط پژوهشی روشن است:

اگر یک claim به‌عنوان property عملی سیستم مطرح می‌شود، باید observable behavior آن از explanation خود سیستم درباره خودش جدا شود.

مهم‌ترین مشاهده فعلی این نیست که NeuroSapiens+ «همه چیز را شکست خورد»؛ چنین جمله‌ای دقیق نیست.

مشاهده دقیق‌تر این است:

> در خانواده‌های متعدد از task، درخواست demonstration بارها به description بیشتر از همان framework تبدیل شد.

این case study پلی است به مقاله دوم و گسترده‌تر درباره Human–AI Co-Creation و **Articulation Illusion**: خطر اشتباه گرفتن زبان منسجم و پیچیده با reasoning، memory، measurement یا mechanismی که واقعاً نشان داده شده باشد.

این مقاله با verdict بسته نمی‌شود؛ با دعوت به replication بسته می‌شود.
