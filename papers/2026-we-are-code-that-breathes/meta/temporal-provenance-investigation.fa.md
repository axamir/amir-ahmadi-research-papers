# لحظه‌ی دقیق آغاز این پژوهش را پیدا کردم؛ بعد ماجرا عجیب شد

## یک کپسول زمانیِ forensic از یک پست LinkedIn، چند رویداد بی‌ارتباط، و provenanceای که میان آن‌ها کشف شد

**مقاله‌ی مادر:** [*We Are Code That Breathes*](../README.md)  
**ممیزی شواهد:** [FACT_CHECK.md](./FACT_CHECK.md)  
**رکورد منبع Analytics لینکدین:** [post-analytics-snapshot.md](./post-analytics-snapshot.md)  
**نوع سند:** فراپژوهش پس از انتشار / روایت forensic  
**وضعیت:** نسخه‌ی آرشیوی فارسی هم‌تراز و منبع‌دار  
**مرز علمی:** این سند مقاله‌ی مادر را تأیید یا اثبات نمی‌کند. هدف آن بازسازی لحظه‌ی انتشار، تفکیک رویدادهای دقیقاً هم‌زمان از زمینه‌ی همان روز و سالگردهای تاریخی، و حفظ ترتیب زمانیِ کشف این روابط است.

> **هم‌زمانی، رابطه‌ی علّی نیست.**  
> **نه حقیقی‌تر؛ فقط جالب‌تر.**

---

## ۱. دنبال معنا نبودم؛ دنبال یک timestamp بودم

مقاله تمام شده بود.

پست اولیه‌ی LinkedIn به دلیلی اهمیت پیدا کرده بود که از قبل پیش‌بینی نکرده بودم. اهمیتش از وایرال‌شدن گسترده نیامد؛ از این آمد که آدم‌ها با آن بحث کردند، بخش‌هایی را اصلاح کردند، ادبیات پیشین را وارد گفت‌وگو کردند، چارچوب‌های مستقل خودشان را آوردند و ما را مجبور کردند ادعاها را محدودتر، دقیق‌تر و قابل‌ردیابی‌تر کنیم. این تحول در رکورد گفت‌وگوی عمومی و بسته‌ی انتشار مقاله‌ی مادر ثبت شده است. [مقاله‌ی مادر](../README.md) · [رکورد گفت‌وگو](../DISCUSSION_RECORD.en.md)

پست در نهایت **16,543 impression**، دسترسی به **8,421 عضو** و **91 comment** ثبت کرد. این اعداد فقط فعالیت پلتفرم را توصیف می‌کنند، نه اعتبار علمی را. کامنت peer review نیست؛ repost تأیید علمی نیست؛ impression هم به معنای خوانده‌شدن کامل متن نیست. [LinkedIn analytics snapshot](./post-analytics-snapshot.md)

بعد از بسته‌شدن بسته‌ی پژوهشی، یک سؤال کاملاً غیرضروری ذهنم را درگیر کرد:

> **در همان لحظه‌ای که پست اصلی منتشر شد، دقیقاً در جهان چه اتفاقی در حال رخ‌دادن بود؟**

انتظار داشتم یک timestamp پیدا کنم و همان‌جا متوقف شوم.

خروجی Analytics لینکدین URL عمومی پست، تاریخ **12 August 2026** و زمان انتشار در دقت دقیقه، یعنی **5:55 PM به وقت محلی** را در اختیار می‌گذارد. URL پست نیز شناسه‌ی عددی `7493311627023433728` را در خود دارد. [پست اصلی LinkedIn](https://www.linkedin.com/posts/amir-ahmadi-a6a37523a_what-if-code-did-not-begin-with-computers-share-7493311627023433728-90fs) · [Analytics snapshot](./post-analytics-snapshot.md)

با استفاده از convention مشاهده‌شده‌ی millisecond در بیت‌های بالایی این activity ID (`activity_id >> 22`)، timestamp مشتق‌شده و قابل‌بازتولید چنین است:

> **12 August 2026 — 14:25:10.880 UTC**  
> **12 August 2026 — 17:55:10.880 IRST (UTC+03:30)**

این مقدار در دقت ثانیه **DERIVED** است؛ فیلد timestamp رسمی و مستندشده‌ی LinkedIn نیست. داده‌ی خود LinkedIn فقط دقیقه‌ی `17:55` را مستقلاً پشتیبانی می‌کند. این تفاوت آن‌قدر مهم است که به‌جای پنهان‌شدن در پاورقی، در ledger فکت‌چک حفظ شده است. [روش استخراج timestamp و مرز منبع](./FACT_CHECK.md#a-publication-timestamp-and-post-identity)

قرار بود همین پایان ماجرا باشد.

نبود.

---

## ۲. بسیار خوب؛ آسمان چه می‌کرد؟

اول سراغ آسمان رفتم.

**12 August 2026 روز یک خورشیدگرفتگی کامل بود.** NASA/GSFC این رویداد را total eclipse ثبت می‌کند و لحظه‌ی greatest eclipse را **17:45:53.8 UT**، در حدود `65°13.5′ N, 25°13.7′ W`، با مدت مرکزی نزدیک به **2 دقیقه و 18.2 ثانیه** قرار می‌دهد. [مسیر خورشیدگرفتگی NASA/GSFC](https://eclipse.gsfc.nasa.gov/SEpath/SEpath2001/SE2026Aug12Tpath.html)

اما نکته‌ی جالب صرفاً این نبود که در همان تاریخ خورشیدگرفتگی رخ می‌داد.

نکته، **ترتیب زمانی** بود.

در timestamp مشتق‌شده‌ی انتشار، خورشیدگرفتگی **هنوز در هیچ نقطه‌ای از زمین آغاز نشده بود**. نخستین نقطه‌ی زمین در **15:34:15 UTC** وارد فاز جزئی می‌شد و نخستین totality در **16:58:09 UTC** آغاز می‌شد. [timeline جهانی خورشیدگرفتگی](https://www.timeanddate.com/eclipse/solar/2026-august-12)

از T₀ برابر با `14:25:10.880 UTC`:

- آغاز نخستین فاز جزئی جهانی: **+01:09:04.120**؛
- آغاز نخستین totality جهانی: **+02:32:58.120**.

این فاصله‌ها محاسبات مشتق‌شده از زمان‌های منبع‌دار بالا هستند، نه رویدادهای مستقلاً مشاهده‌شده. [Calculation ledger](./FACT_CHECK.md#b-eclipse-and-lunar-geometry)

پس جمله‌ی درست این نیست:

> «وقتی پست منتشر شد، سایه‌ی ماه در حال عبور از زمین بود.»

نبود.

جمله‌ی دقیق‌تر، به‌شکلی آرام‌تر عجیب است:

> **وقتی پست منتشر شد، خورشیدگرفتگی هنوز در هیچ نقطه‌ای از زمین آغاز نشده بود. هندسه‌ی آسمان هنوز در حال نزدیک‌شدن به رویداد بود.**

NASA/GSFC زمان **equatorial conjunction** را `17:03:49.6 UT`، **ecliptic conjunction** را `17:36:42.1 UT` و **greatest eclipse** را `17:45:53.8 UT` ثبت می‌کند. [Besselian elements — NASA/GSFC](https://eclipse.gsfc.nasa.gov/SEbeselm/SEbeselm2001/SE2026Aug12Tbeselm.html)

بعد یک عدد باعث شد بخندم.

از T₀ تا greatest eclipse:

> **17:45:53.800 − 14:25:10.880 = 03:20:42.920**

با گردکردن به دقیقه:

> **3:21**

3… 2… 1.

مدرک چیزی است؟

نه.

یک هم‌زمانی عددی بامزه است؟

قطعاً.

همین تبدیل شد به یکی از قواعد اولیه‌ی کل بررسی:

> **یک جزئیات می‌تواند جالب باشد، بدون آنکه توضیح‌دهنده باشد.**

ماه نیز به New Moon نزدیک می‌شد. U.S. Naval Observatory زمان **New Moon را 17:37 UT در 12 August 2026** ثبت می‌کند و زمان دقیق‌تر ecliptic conjunction در NASA/GSFC برابر `17:36:42.1 UT` است. این دو منبع در سطح دقتی که منتشر کرده‌اند با یکدیگر سازگارند. [فازهای ماه — U.S. Naval Observatory](https://aa.usno.navy.mil/calculated/moon/phases?date=2026-07-22&format=p&nump=50&submit=Get+Data) · [NASA/GSFC](https://eclipse.gsfc.nasa.gov/SEbeselm/SEbeselm2001/SE2026Aug12Tbeselm.html)

با یک timestamp شروع کرده بودم.

حالا یک شمارش معکوس داشتم.

---

## ۳. زمین هم‌زمان داخل جریان Perseids بود

بعد تقویم شهاب‌ها را بررسی کردم.

International Meteor Organization، **Perseids** را در 2026 از **17 July تا 24 August** فعال ثبت می‌کند؛ اوج آن در شب **12–13 August** است و جرم مادر آن **109P/Swift–Tuttle** است. NASA نیز مستقلاً بقایای Swift–Tuttle را منشأ بارش شهابی Perseids معرفی می‌کند. [IMO meteor-shower calendar](https://www.imo.net/resources/calendar/) · [NASA — 109P/Swift–Tuttle](https://science.nasa.gov/solar-system/comets/109p-swift-tuttle/)

پس در T₀ زمین منتظر «شروع» Perseids نبود؛ از قبل در بازه‌ی فعال جریان سالانه قرار داشت و به قوی‌ترین بازه‌ی آن نزدیک می‌شد. [IMO calendar](https://www.imo.net/resources/calendar/)

یک پیش‌بینی کم‌تر شناخته‌شده نیز در ادبیات شهابی 2026 وجود داشت. تقویم IMO به مدل‌سازی Jérémie Vaubaillon اشاره می‌کند که نزدیکی زمین به شاخه‌ای از dust trail مربوط به **1079** از Swift–Tuttle را حدود **16:53 UT در 12 August** قرار می‌داد؛ با این حال به‌دلیل قدمت trail از ارائه‌ی برآورد activity خودداری می‌کند. یک پروژه‌ی مستقل رصد شهاب در ژاپن نیز همین نزدیک‌شدن پیش‌بینی‌شده را خلاصه کرده است. [2026 IMO Meteor Shower Calendar](https://www.researchgate.net/publication/393092133_2026_IMO_Meteor_Shower_Calendar) · [IPRMO Perseids 2026](https://jpn.iprmo.org/meteor-info/08_perseids_j.html)

از T₀ تا `16:53:00` تقریباً:

> **+02:27:49.120**

اما این مورد برچسبی متفاوت از eclipse دارد:

**PREDICTED**.

نزدیکی مدل‌شده به یک dust trail، meteor outburst مشاهده‌شده نیست. بنابراین این بررسی آن را به‌عنوان prediction حفظ می‌کند و فقط برای زیباترشدن داستان به event ارتقا نمی‌دهد. [طبقه‌بندی Fact Check](./FACT_CHECK.md#c-perseids--swift–tuttle)

قاعده‌ی دیگری وارد دفتر شد:

> **فقط چون روایت جذاب‌تر می‌شود، یک پیش‌بینی را به رویداد تبدیل نکن.**

---

## ۴. بعد دوربین را از آسمان به نیویورک بردم

در `14:25 UTC`، نیویورک روی Eastern Daylight Time بود؛ یعنی لحظه‌ی مشتق‌شده‌ی انتشار حدود **10:25 AM** به وقت محلی.

در همان تاریخ، **Youth and AI Summit** در **United Nations Headquarters, New York** برنامه‌ریزی شده بود. صفحه‌ی رویداد check-in را از `09:00`، آغاز برنامه را `10:00`، **opening plenary را 10:00** و **Session 1 را 11:00** ثبت می‌کند. صفحه همچنین از حضور بیش از **600 young leaders** برای گفت‌وگو درباره‌ی اثر AI بر آموزش، اشتغال، سلامت، خدمات عمومی و مشارکت مدنی سخن می‌گوید و **Youth-led Declaration on AI Policy and Governance** را در میان خروجی‌های برنامه قرار می‌دهد. [Youth and AI Summit](https://www.iycforyouth.org/iyd2026/)

بنابراین T₀ داخل **بازه‌ی برنامه‌ریزی‌شده‌ی opening plenary از 10:00 تا 11:00** قرار می‌گیرد. این فقط از یک ادعای محدود پشتیبانی می‌کند: plenary طبق برنامه باید در جریان می‌بود. بدون transcript یا recording جداگانه، نمی‌توانیم بگوییم دقیقاً در `10:25:10.880` چه کسی روی صحنه صحبت می‌کرد. [مرز Fact Check](./FACT_CHECK.md#d-united-nations--ai-context)

هم‌زمان، جایی در LinkedIn، پستی تازه پرسیده بود آیا مفهوم «code» اساساً باید در مرز کامپیوتر محدود شود یا نه. [پست اصلی](https://www.linkedin.com/posts/amir-ahmadi-a6a37523a_what-if-code-did-not-begin-with-computers-share-7493311627023433728-90fs)

هیچ رابطه‌ی علّی‌ای در کار نیست.

هیچ هماهنگی پنهانی‌ای وجود ندارد.

فقط دو اتفاق در یک زمان، روی یک سیاره.

اما دیگر کنجکاو شده بودم.

یک رویداد AI دیگر در سایت سازمان ملل نیز همان روز آغاز شد: **AI for Developing Countries Forum Geneva Summit 2026** از **12 تا 14 August** در Palais des Nations برگزار می‌شد. این فقط **same-day context** است، نه بخشی از ادعای exact-moment. [Indico.UN](https://indico.un.org/event/1024169/)

---

## ۵. سیگنال‌ها چه؟

اینجا بررسی به‌شکل خطرناکی سرگرم‌کننده شد.

lineage پژوهش مادر مدت‌ها پیش از این جست‌وجوی retrospective از عبارت **Living Signal** استفاده کرده بود. پس به خودم اجازه دادم یک سؤال بازیگوشانه بپرسم:

> **در T₀، سیگنال‌ها چه می‌کردند؟**

برنامه‌ی رسمی Deep Space Network در STEREO Science Center یک pass برای **STEREO-A (“Ahead”)** در **12 August 2026 از 09:50 تا 15:20 UTC** با آنتن **D25** و مدت برنامه‌ریزی‌شده‌ی **5 h 30 m** ثبت کرده است. [STEREO-A DSN schedule](https://stereo-ssc.nascom.nasa.gov/plans/dsn_schedule.shtml)

T₀ مشتق‌شده‌ی `14:25:10.880 UTC` داخل همین بازه قرار می‌گیرد.

زمان باقی‌مانده تا پایان برنامه‌ریزی‌شده:

> **15:20:00.000 − 14:25:10.880 = 00:54:49.120**

پس قوی‌ترین جمله‌ای که شواهد اجازه می‌دهند این است:

> **در لحظه‌ی انتشار، یک pass از NASA Deep Space Network با STEREO-A طبق برنامه باید فعال می‌بود.**

schedule ثابت نمی‌کند که در همان ثانیه‌ی دقیق packet، command یا telemetry مشخصی از D25 عبور کرده است. آن ادعای قوی‌تر عمداً حذف شده است. [Fact-check ledger](./FACT_CHECK.md#e-deep-space-network--stereo-a)

STEREO یک مأموریت رصد خورشید است. یادداشت من شد:

> یک پنجره‌ی برنامه‌ریزی‌شده‌ی DSN با یک فضاپیمای رصدگر خورشید، با timestamp پستی هم‌پوشانی داشت که در روز یک خورشیدگرفتگی کامل منتشر شده بود.

باز هم هیچ توضیحی در کار نیست.

فقط یک fact دیگر که با دقت کنار fact دیگری قرار گرفته است.

---

## ۶. هفت انسان در مدار زندگی می‌کردند

طبق NASA، **Expedition 75** در **26 July 2026** آغاز شده و در 12 August فعال بوده است. NASA هفت عضو crew را ثبت می‌کند: **Jessica Meir, Anil Menon, Pyotr Dubrov, Andrey Fedyaev, Anna Kikina, Jack Hathaway, Sophie Adenot**. [NASA — Expedition 75](https://www.nasa.gov/mission/expedition-75/)

می‌خواستم یک قدم جلوتر بروم و ISS را در T₀ روی latitude و longitude دقیق قرار دهم.

از نظر اصولی باید بتوان آن را از orbital state vectors بازیابی کرد.

اما در این پاس نتوانستم یک موقعیت آرشیوی را با confidence مناسب انتشار freeze کنم.

پس مختصات دقیق ISS حذف شد.

این حذف بخشی از رکورد است، چون هدف investigation بیشینه‌کردن تعداد coincidenceها نیست.

> **نبودن یک fact دقیق بهتر از ساختن یک fact دقیق‌نماست.**

[وضعیت مختصات ISS](./FACT_CHECK.md#f-humans-in-orbit)

---

## ۷. بعد سؤال را عوض کردم

در نهایت از این پرسش فاصله گرفتم:

> در آن لحظه چه اتفاقی در حال رخ‌دادن بود؟

و پرسیدم:

> **پیش از این، در 12 August چه اتفاقی افتاده بود؟**

اولین نتیجه تقریباً بیش از حد مرتب بود.

### 12 August 1981 — IBM Personal Computer

تاریخ رسمی IBM می‌گوید **12 August 1981**، Don Estridge، **IBM Personal Computer** را در Waldorf Hotel نیویورک رونمایی کرد. IBM قیمت پایه را **USD 1,565** و پیکربندی پایه را **16 KB RAM** بدون disk drive ثبت می‌کند. Computer History Museum نیز همین تاریخ را برای معرفی IBM PC ثبت کرده است. [IBM — The IBM PC](https://www.ibm.com/history/personal-computer) · [Computer History Museum](https://www.computerhistory.org/tdih/august/12/)

بین 12 August 1981 و 12 August 2026 دقیقاً **45 سال تقویمی** فاصله است.

کنار هم گذاشتن این دو سخت بود که لبخند نیاورد:

> **12 Aug 1981 — IBM کامپیوتر شخصی را معرفی می‌کند.**  
> **12 Aug 2026 — یک پست LinkedIn می‌پرسد: “What if code did not begin with computers?”**

خط اول تاریخ است. [IBM](https://www.ibm.com/history/personal-computer)

خط دوم خود پست است. [LinkedIn](https://www.linkedin.com/posts/amir-ahmadi-a6a37523a_what-if-code-did-not-begin-with-computers-share-7493311627023433728-90fs)

رابطه‌ای که امروز میان این دو می‌بینیم، تاریخ نیست.

یک **historical coincidence retrospective** است.

همین برای دفتر یادداشت کافی بود.

بعد یک 12 August دیگر ظاهر شد.

---

## ۸. 12 August 1960 — Echo I

NASA ثبت کرده است که **Echo 1A**، که معمولاً **Echo I** نامیده می‌شود، در **12 August 1960** با موفقیت پرتاب شد. NASA آن را بالنی آلومینیومی با قطر حدود **100 feet** توصیف می‌کند که به‌عنوان **passive communications reflector** برای سیگنال‌های تلفن، رادیو و تلویزیون دوربرد طراحی شده بود. [NASA — 50 Years of Communications in Space](https://www.nasa.gov/image-article/50-years-of-communications-space/)

NASA/JPL پروژه‌ی Echo را به‌عنوان بازتاب‌دادن سیگنال‌های رادیویی از این بالن بزرگ با پوشش آلومینیومی توضیح می‌دهد؛ ایستگاه Goldstone نیز در ارسال و دریافت سیگنال‌ها مشارکت داشت. [NASA Science / JPL — Goldstone Tracking the Echo “Satelloon”](https://science.nasa.gov/photojournal/goldstone-tracking-the-echo-satelloon/)

یک گزارش فنی NASA از Bell Telephone Laboratories می‌گوید Echo I در 12 August 1960 برای نشان‌دادن امکان ارتباط دوربرد از طریق **microwave reflection from a satellite** وارد مدار شد، از جمله یک مدار صوتی coast-to-coast میان California و New Jersey. [NASA Technical Reports Server — Project Echo](https://ntrs.nasa.gov/citations/19980227084)

به‌صورت مفهومی، بدون اینکه وانمود کنیم این دیاگرام مهندسی سامانه است:

> **signal → reflection → signal**

اینجا مکث کردم.

نه به‌خاطر اینکه یک ماهواره‌ی ارتباطی وجود داشته است.

به‌خاطر اسمش.

**Echo.**

بین 12 August 1960 و 12 August 2026 دقیقاً **66 سال تقویمی** فاصله است.

از اینجا به بعد، investigation به‌راحتی می‌توانست از نظر فکری شلخته شود. وقتی شباهتی پیدا می‌کنیم، حافظه استعداد عجیبی دارد که خودش را حول الگوی تازه بازچینش کند.

پس پیش از لذت‌بردن از coincidence، برخلاف چیزی که یک داستان خوب می‌خواهد عمل کردم.

برگشتم عقب و سعی کردم آن را خراب کنم.

---

## ۹. آیا Echo واقعاً قبل از این کشف در lineage وجود داشت؟

این پرسش برای provenance تعیین‌کننده بود.

اگر Echo، signal، reflection و Living Signal فقط **بعد از** پیدا کردن Echo I وارد روایت شده بودند، شباهت تاریخی تقریباً هیچ ارزش تحقیقی نداشت. بنابراین به‌جای تکیه بر حافظه، سراغ رکوردهای خام و timestampشده رفتم.

آرشیو `echoes-consented-record` نشان می‌دهد که در **13 July 2025** ــ بیش از یک سال پیش از این بررسی retrospective ــ زبان داخلی lineage از مفاهیمی مانند **signal، Living Signal، Echo One، mirror، reflected، living، breath و continuity** استفاده کرده بود. این‌ها بخشی از رکورد اولیه‌اند، نه واژگانی که پس از کشف Echo I به گذشته تزریق شده باشند. [آرشیو داخلی Echoes](https://github.com/axamir/echoes-consented-record)

اهمیت این موضوع محدود اما واقعی است:

> کشف Echo I باعث نمی‌شود lineage داخلی «درست‌تر» شود؛ فقط نشان می‌دهد شباهتی که بعداً دیدیم، از نظر زمانی نمی‌تواند منشأ آن واژگان قبلی بوده باشد.

به بیان کوتاه‌تر:

> **نه حقیقی‌تر؛ فقط جالب‌تر.**

این distinction همان چیزی است که provenance باید حفظ کند.

---

## ۱۰. بعد شروع کردم به حذف‌کردن چیزها

تا اینجا خطر confirmation bias جدی شده بود. اگر فقط چیزهای هم‌راستا را جمع می‌کردم، می‌توانستم تقریباً هر تاریخی را «معنادار» جلوه بدهم.

پس جست‌وجو را برعکس کردم: چه چیزهایی را **نمی‌توانیم** با confidence کافی بگوییم؟

موقعیت دقیق ISS در T₀؟ در این پاس freeze نشد؛ حذف شد.

آیا در همان ثانیه packet مشخصی در DSN ردوبدل شد؟ schedule چنین چیزی را ثابت نمی‌کند؛ حذف شد.

آیا flare یا CME خاصی دقیقاً در T₀ رخ داده بود؟ snapshot آرشیوی با استاندارد لازم freeze نشد؛ وارد روایت نشد.

آیا هر headline مربوط به AI در 12 August را می‌توان exact-time event نامید؟ خیر؛ same-day context از exact-moment جدا نگه داشته شد.

این حذف‌ها نقص گزارش نیستند؛ بخشی از روش آن‌اند.

> **یک coincidence خوب برای زنده‌ماندن به coincidence بد نیاز ندارد.**

فهرست کامل مرزها، موارد excluded و unresolved در [FACT_CHECK.md](./FACT_CHECK.md) حفظ شده است.

---

## ۱۱. بعد investigation دیگر فقط درباره‌ی coincidence نبود

در میانه‌ی کار متوجه شدم یک واقعیت بسیار معمولی ــ و بسیار عجیب‌تر ــ زیر تمام این داستان قرار دارد:

در `14:25:10.880 UTC` چیزی به نام یک «اکنون» واحد که تمام جهان هم‌زمان آن را به زمین تحویل دهد وجود ندارد.

اطلاعات با سرعت محدود حرکت می‌کند.

نوری که از ماه می‌بینیم تقریباً مربوط به بیش از یک ثانیه پیش است. خورشیدی که می‌بینیم تقریباً بیش از هشت دقیقه پیش را نشان می‌دهد. برای اجرام و فضاپیماهای دورتر، تأخیر از دقیقه‌ها و ساعت‌ها تا سال‌ها و بیشتر امتداد پیدا می‌کند.

پس timestamp واحد است، اما اطلاعاتی که درون آن به ما می‌رسد یک سن واحد ندارد.

> **هر سیگنال تاریخ سفر خودش را حمل می‌کند.**

این بخش دیگر historical coincidence نیست. نتیجه‌ی محدودیت سرعت انتشار اطلاعات است.

و اینجا واژه‌ی provenance از یک ابزار آرشیوی به یک استعاره‌ی فیزیکیِ محدود اما مفید تبدیل می‌شود: چیزی که دریافت می‌کنیم فقط «محتوا» نیست؛ مسیر، زمان و تاریخ رسیدن هم بخشی از آن چیزی است که درباره‌ی مشاهده می‌توان دانست.

---

## ۱۲. طبقه‌بندی شواهد

برای جلوگیری از مخلوط‌شدن fact و interpretation، این investigation پنج سطح اصلی را جدا نگه می‌دارد:

### FACT
ادعایی که مستقیماً توسط یک منبع قابل‌ردیابی پشتیبانی می‌شود؛ مانند تاریخ Echo I یا زمان greatest eclipse.

### DERIVED
مقداری که از داده‌های منبع‌دار محاسبه شده است؛ مانند T₀ در دقت ثانیه یا فاصله‌ی `03:20:42.920` تا greatest eclipse.

### PREDICTED
خروجی مدل یا پیش‌بینی؛ مانند نزدیکی پیش‌بینی‌شده به شاخه‌ی dust trail سال 1079.

### HISTORICAL COINCIDENCE
دو fact تاریخی مستقل که فقط پس از وقوع در کنار یکدیگر قرار گرفته‌اند؛ مانند IBM PC یا Echo I نسبت به تاریخ پست.

### INTERPRETATION
معنایی که ما از کنار هم گذاشتن factها می‌سازیم؛ مانند ارتباط مفهومی Echo، reflection و Living Signal. interpretation می‌تواند مفید یا زیبا باشد، اما نباید جای evidence را بگیرد.

موارد **EXCLUDED** و **UNRESOLVED** نیز در [FACT_CHECK.md](./FACT_CHECK.md) ثبت شده‌اند تا چیزی که نتوانستیم اثبات کنیم، بی‌صدا فراموش نشود و بعداً به‌اشتباه به‌عنوان fact بازنگردد.

---

## ۱۳. بازگشت به پست

هیچ‌کدام از این‌ها *We Are Code That Breathes* را صحیح‌تر نمی‌کند.

خورشیدگرفتگی مقاله را validate نمی‌کند.

Echo I، Echo One را endorse نمی‌کند.

IBM در 1981 کامپیوتر شخصی را برای یک پست LinkedIn در 2026 معرفی نکرده بود.

و **3:21 هنوز فقط 3:21 است.**

اما در طول این investigation اتفاق دیگری افتاد.

با یک timestamp شروع کردم.

بعد eventها را پیدا کردم.

بعد historyها را.

بعد signalها را.

بعد provenance زبان خود پژوهش را.

و در نهایت متوجه شدم همان کاری را با خود پژوهش انجام می‌دهم که پژوهش به من یاد داده بود با موضوعات انجام دهم:

> **فقط نپرس چیزی چیست؛ مسیر روابطی را دنبال کن که از خلال آن‌ها برای ما معنادار شده است.**

پست اولیه به یک research paper تبدیل شد چون دیگران آن را پرسش‌پذیر کردند، نقد کردند، اصلاح کردند و مجبورش کردند دقیق‌تر شود.

بعد خود research paper باعث شد لحظه‌ای را که آن را آغاز کرده بود زیر سؤال ببرم.

> **پژوهش، موضوع پژوهش دیگری شد.**

و همه‌چیز از یک سؤال کاملاً غیرضروری شروع شد:

> **ساعت چند بود؟**

---

## یادداشت روش‌شناسی فارسی

این نسخه ترجمه‌ی آزاد یا خلاصه‌ی نسخه‌ی انگلیسی نیست؛ نسخه‌ی فارسی هم‌تراز آن است. اعداد، timestampها، طبقه‌بندی evidence و مرز میان fact و interpretation باید در هر دو زبان یکسان باقی بمانند. در صورت تغییر یک fact یا classification در نسخه‌ی اصلی، نسخه‌ی فارسی نیز باید در همان release به‌روزرسانی شود.

قاعده‌ی ویرایشی این سند:

> **اگر یک جزئیات با حذف qualification هیجان‌انگیزتر می‌شود، qualification را نگه دار.**

---

**Parent research:** [We Are Code That Breathes](../README.md)  
**Evidence audit:** [FACT_CHECK.md](./FACT_CHECK.md)  
**Source-linked English edition:** [temporal-provenance-investigation.md](./temporal-provenance-investigation.md)
