# Bilingual Alignment Contract

**English source:** `manuscript-core.md` — Release Candidate v0.3  
**Persian aligned edition:** `manuscript.fa.md`

## Rule

The Persian edition is an aligned research edition, not an independent adaptation. It must preserve the English manuscript's claim strength, evidence class, uncertainty, novelty boundaries, prohibited claims, evaluation status, and section-level argumentative structure.

## Section map

| EN | FA | Status |
|---|---|---|
| Abstract | چکیده | aligned |
| 1. Introduction | ۱. مقدمه | aligned |
| 2. Related Work and Novelty Boundary | ۲. پیشینه و مرز نوآوری | aligned |
| 3. Research Gap | ۳. شکاف پژوهشی | aligned |
| 4. Research Questions | ۴. پرسش‌های پژوهش | aligned |
| 5. Method | ۵. روش | aligned |
| 6. PRCEP v0.1 | ۶. PRCEP v0.1 | aligned |
| 7. Case Transitions | ۷. انتقال‌های موردی | aligned |
| 8. Model Mediation | ۸. میانجی‌گری مدل | aligned |
| 9. Falsification and Evaluation | ۹. ابطال و ارزیابی | aligned |
| 10. Ethics, Attribution, and Evidence Policy | ۱۰. اخلاق، انتساب و سیاست شواهد | aligned |
| 11. Boundary Conditions | ۱۱. شرایط مرزی | aligned |
| 12. Limitations | ۱۲. محدودیت‌ها | aligned |
| 13. Discussion | ۱۳. بحث | aligned |
| 14. Conclusion | ۱۴. نتیجه‌گیری | aligned |

## Terminology locks

- provenance: keep `provenance` where translation could collapse lineage, evidence origin, and derivation into one Persian term; explanatory Persian may accompany it.
- lineage: keep `lineage` when referring to intellectual/source lineage relations.
- claim transition: انتقال ادعا
- persistent: پایدار, with the operational definition preserved.
- independently_convergent_with: do not translate into a relation that implies influence or derivation.
- model mediation: میانجی‌گری مدل
- matched-information control: کنترل هم‌اطلاعات
- auditability: ممیزی‌پذیری / قابلیت ممیزی according to sentence grammar.

## Claim-strength locks

The Persian edition must never upgrade:

- `protocol candidate` → validated protocol;
- `case demonstration` → proof;
- `hypothesis` → established finding;
- `independent convergence` → derivation;
- `public challenge record` → peer review;
- `AI mediation` → AI authorship or independent evidence.

## Synchronization rule

Any future material change to the English release candidate must trigger a bilingual alignment check before publication. The two editions may differ stylistically, but not epistemically.