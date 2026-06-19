# OneFlow Ads — brief: MAXXuj design, vytvoř 5 nových reklam

> **Pro Claude (Filipova instance).** Tohle je kompletní zadání. Přečti celé, pak pracuj.
> Výstup = **5 nových PNG reklam** v této složce. Lepší design než reference, **stejná designová DNA**. Všechno **česky**.

---

## 0) MODEL — POVINNÉ

**Veškerý návrh a finální syntézu dělej na modelu Fable 5 (`claude-fable-5`).**
Fable je apex model pro design a syntézu — tenhle úkol je přesně pro něj. Pokud běžíš na jiném modelu, přepni session na Fable 5 (nebo design-synthesis routuj na Fable). Mechanickou práci (render, výpis souborů) můžeš nechat na nižším modelu, ale **kompozici, typografii, copy a finální rozhodnutí dělá Fable**.

---

## 1) Cíl

5 statických reklam, formát **1080×1350 px (4:5)**, render @2× → **2160×2700**.
- **BEZ CTA.** Žádné tlačítko, žádná URL, žádný telefon, žádné „zaregistruj se".
- Na reklamě je **jen sdělení + logo OneFlow**. Nic víc.
- Každá z 5 variant = **jiný úhel / layout**, ale **stejná designová DNA** (viz §4).
- Posuň design **výš než reference** (viz §5 MAXX).

---

## 2) Produkt + publikum (komu to prodáváme)

**OneFlow = „Obchodní AI Brain".** Z 5 signálů (fit, intent, dostupnost, recency, confidence) sestaví každé ráno **pořadník vztahů** — koho oslovit, v jakém pořadí — a u každého **vysvětlí proč** (ne jen číslo). Člověk rozhoduje; **nic neodejde automaticky**.

**Publikum = platící zákazníci OneFlow z high-value segmentu:**
fondy (PE/VC), rodinné kanceláře (family offices), správci aktiv, privátní banky, senior privátní bankéři. Konkrétní avatar = **partner / managing director / head of IR / senior relationship manager**.

**Jejich bolest (na tu cílíme):**
- Hodina partnera je **nejdražší kapitál ve firmě** — a krvácí na špatné vztahy / špatné schůzky.
- Ohromný deal flow / seznam kontaktů, **skoro nula signálu** — který vztah reálně uzavře?
- **Jeden vztah** (mandát, alokace v řádu milionů) **vychladl**, protože se nedostal na řadu.
- CRM (DealCloud/Affinity/Salesforce) = **hřbitov dat**, kterému nikdo nevěří.
- **Nikdy** nepustí bota, aby psal jejich LP/klientům — diskrétnost a reputace jsou všechno.
- Nevěří **black-box skóre** — chtějí vidět **proč** (tezi, ne číslo).

> Dvě nejsilnější devízy OneFlow pro tenhle segment: **(a) vysvětlitelnost (proč, ne černá skříňka)** a **(b) člověk rozhoduje — nic neodejde samo.** Tyhle dvě věci řeší jejich největší námitky. Stav na nich proof.

---

## 3) Reference (složka `reference/`)

- `oneflow-funds-ad-v1.png` — **baseline render**, který máš překonat (stejná DNA, lepší provedení).
- `ad-funds.html` — **zdrojový kód** baseline: přesné barvy, fonty, váhy a **inline logo SVG OneFlow** (bílé). Logo si vytáhni odsud — žádný externí soubor nepotřebuješ.

---

## 4) Brand systém — drž PŘESNĚ (vzorkováno z živého oneflow.cz / offer.oneflow.cz)

```css
--bg:#0A0A0C;  --bg-2:#0C0C0E;  --bg-3:#080809;   /* plochá near-black, jemný vertikální gradient */
--ink:#EBEBEB;        /* světlý zisk / odpověď / headline */
--ink-2:#A8A6A3;      /* tělo proofu */
--dim:#6A6A6C;        /* tmavá „před" / bolest */
--muted:#56565A;      /* labely, eyebrow */
--line:rgba(255,255,255,0.11);  /* hairline předěly */
```
- **Font: Inter Tight** (Google Fonts), váhy **400 / 500 / 600 / 700**, latin-ext (česká diakritika).
- **Monochrom. ŽÁDNÉ syté barvy.** Žádný modrý/fialový gradient, žádný glassmorphism, žádné neony. Jen near-black + světle šedá + hairline.
- Highlight pill = inverze: světlé pozadí `--ink`, tmavý text `#0A0A0C`, `border-radius:10px` (viz `.hl` v reference).

---

## 5) Designové prvky — ZACHOVEJ (to je ta „stejná DNA")

1. **Avatar callout chip** (kicker) nahoře v obsahu — pojmenuje seniorního kupce, ne juniora.
2. **Pain → gain „mirror"**: tmavá bolest (`--dim`) nahoře → **světlý velký zisk** (`--ink`) pod ní.
3. **Jeden inverted-highlight pill** v gain řádku. ⛔ **POUZE na obsahové slovo** (podstatné jméno / sloveso, které nese hodnotu). **NIKDY na spojku ani vztažné/tázací zájmeno** — `který`, `jehož`, `jaký`, `kdo`, `co`, `už` apod. (Tohle je tvrdé pravidlo — highlight na spojce vypadá rozbitě.)
4. **3-buňkový proof band** dole s hairline předěly: **score ring** (kruh se skóre) + 2 staty. Pro tenhle segment ideálně: `skóre z 5 signálů` · `proč u každého doporučení` · `0 odejde bez vašeho svolení`.
5. **Editorial left-align**, velkorysé mezery, **velká čitelná typografie** (headline dominuje).
6. **Score ring** = podpisový vizuální prvek produktu (kruhový gauge). Drž ho.

---

## 6) MAXX — co konkrétně zlepšit oproti baseline

Cíl: **stejná DNA, výrazně lepší řemeslo.** Posuň:
- **Typografická hierarchie** — ostřejší kontrast velikostí, lepší tracking, vyladěné zalomení řádků (žádné ošklivé „vdovy"/dangling slova na konci řádku).
- **Rytmus mezer** — promyšlený vertikální rytmus, optické zarovnání, dýchající whitespace; reklama nesmí působit nacpaně ani prázdně.
- **Hloubka v rámci ploché brandy** — jemné, decentní (např. mikro-kontrast vrstev pozadí, vlasový vnitřní okraj, jemný šum/grain ≤3 %). **Nepřekroč monochrom.**
- **Proof band** — vizuálně silnější, lépe odsazený, čitelné labely (min ~18px ve web měřítku).
- **Emoční delta** — tmavá bolest ↓ vs. světlý zisk ↑ ať je čitelná na první pohled (Feel → Think → Act).
- **Prémiový pocit** pro fond/privátní bankovnictví — disciplína, zdrženlivost, white-glove. Žádný „SaaS startup" feeling.

---

## 7) Copywriting — Hormozi (česky, prémiově)

Drž **Value Equation**: *(Dream Outcome × Perceived Likelihood) ÷ (Time Delay × Effort & Sacrifice)*.
- **Pojmenuj avatara** (chip): senior, jehož čas = nejvzácnější kapitál.
- **Agituj bolest**: zmeškaná „velryba" — mandát/alokace, co vychladla, protože se nedostala na řadu (loss aversion, maximální konkrétnost).
- **Zisk**: každá hodina senior času míří na **ten jeden vztah, co uzavře** — a víš **proč**.
- **Proof = zabij námitku**: vysvětlitelnost (`proč`, ne černá skříňka) + člověk rozhoduje (`0` auto-odeslání) + skóre z 5 signálů.
- **Slovní limit**: krátké, úderné. Headline pár slov. Žádné odstavce. Žádná klišé. **Žádná strojová čeština** — musí znít nativně a prémiově. Vyhni se poetické antitéze „X, ne Y" jako berličce.

**TÓN — horní tier (UHNW / velké fondy / privátní bankovnictví).** Mluv jazykem kapitálu, ne SaaSu: **mandát, alokace, kapitál, vztah, principal, schůzka**. Sázky zvyšuj **zdrženlivostí, ne křikem** — žádná hlučná čísla typu „ušetři 10 hodin", žádné vykřičníky, žádný hype. Tihle kupci reagují na **přesnost, status a diskrétnost**. Stáhni zisk na jedno silné podstatné jméno (např. **mandát**) a to dej do highlight pillu.

---

## 8) 5 variant — úhly (každá Hormozi-maxed, česky)

| # | Úhel | Jádro sdělení |
|---|------|----------------|
| 1 | **Hodina principala / zmeškaný mandát** | „Největší vztah roku vychladl. Přišel na řadu pozdě." → ráno víš, který vztah nese **mandát**, a proč. (= aktuální baseline, ten překonej) |
| 2 | **Záplava dealů, nula signálu** | „CRM plný jmen. Signál nula." → jeden pořadník, který vztah **zavře**. |
| 3 | **Diskrétnost / důvěra** | „K vašemu LP nikdy nenapíše bot." → člověk rozhoduje, **0** odejde bez vás. |
| 4 | **Vysvětlitelnost** | „Skóre bez důvodu nikdo nepodepíše." → **doporučení s důvodem**, ne černá skříňka. |
| 5 | **Status / identita** | „Disciplína, ne hluk." → white-glove origination, ne spray-and-pray. |

> Tabulka je startovní matice. Copy si **napiš lépe** (to je ta práce pro Fable). Drž slovní limit a §7.

---

## 9) Tvrdá pravidla (checklist)

- [ ] **BEZ CTA**, bez URL, bez telefonu, bez ceny.
- [ ] Jen **sdělení + logo OneFlow** (inline SVG z `reference/ad-funds.html`, bílé, nedeformovat).
- [ ] **Česky**, gramaticky správně, plná diakritika.
- [ ] **1080×1350**, render @2× (2160×2700), nic se neořízne, nic nepřetéká.
- [ ] **Highlight pill NIKDY na spojce/zájmenu** (§5 bod 3).
- [ ] Monochrom, žádné syté barvy, brand tokeny ze §4.
- [ ] Velká čitelná typografie, žádný drobný nečitelný text.
- [ ] Každá ze 5 variant **vizuálně odlišná**, ale stejná DNA.

---

## 10) Jak renderovat + odevzdat

1. Vytvoř v této složce 5 HTML: `oneflow-fund-1.html` … `oneflow-fund-5.html` (vycházej z `reference/ad-funds.html`, ať máš font, logo a tokeny).
2. Spusť **`python3 render-all.py`** — vyrenderuje každý `*.html` v kořeni složky do stejnojmenného `.png`.
   - Potřebuješ Playwright: `pip install playwright && playwright install chromium`.
3. **Ověř výsledné pixely** — otevři každý PNG a koukni se (ne jen na kód). Zkontroluj checklist §9.
4. **Done** = 5 PNG (1080×1350) v této složce + u každé jeden řádek, jaký úhel hraje.

> Pravidlo č. 1: nikdy neřekni „hotovo" u vizuálu bez otevření výsledného PNG.
