# Nigeria Green-Tech & Open-Data Opportunity Study

Which green, climate-tech, sustainability and environmental **software products can be built in
Nigeria on free / open / publicly accessible data** — and which one to build first if the long-term
goal is attracting green / climate funding.

**Prepared by Pjoc** · September 2026 · Companion to the [Green Initiative EV Ride-Hailing feasibility study](https://github.com/pjocng).

> ⚠️ Dataset links, APIs, funding programmes and policy references were checked in September 2026 and
> were live at the time. Nigerian policy, tariffs, FX and funding windows move fast — **re-verify every
> source before spending money.** Scores are the author's assessment, not audited fact. Not investment advice.

---

## Read it

| Format | Link |
|---|---|
| **Interactive web page** | **https://pjocng.github.io/nigeria-green-tech-opportunities/** — sticky table of contents, scrollspy, collapsible sections, section filter, click-to-sort tables, dark/light, print-to-PDF. Self-contained, works offline. |
| Markdown source | [`green-tech-open-data-opportunities-nigeria.md`](green-tech-open-data-opportunities-nigeria.md) (~22,600 words, fully source-linked) |

## What's inside

1. **Open-data inventory** — ~45 datasets / APIs / platforms with Nigeria coverage, resolution, update
   frequency, API + download availability, cost, and a licence tier (A fully-open / B open-with-limits /
   C paid), each with the official link and an "MVP-sufficient?" call.
2. **Sector scan** — ~32 sectors mapped to problem severity, data readiness, who pays.
3. **26 product concepts** — 16 fully profiled (problem, users, mechanism, features, open data,
   proprietary data later, revenue, government + private customers, dev complexity, MVP effort, data
   reliability, regulatory considerations, competition, and the market gap each fills).
4. **Green-funding landscape** — 20+ funders / programmes (GCF, GEF, Adaptation Fund, World Bank DARES
   & ACReSAL, AfDB SEFA, GEAPP, All On, Catalyst Fund, InsuResilience, GGFR / IMEO, Lacuna successors…)
   with tickets and current status, plus a 10-point checklist of what any funder requires first.
5. **Environmental-impact measurement** — every metric → calculation method → feeding dataset.
6. **Carbon-credit potential** — concept-by-concept: additionality, baseline, whether open data can
   support MRV, candidate methodologies, and the extra physical data needed. Only 6 concepts have a
   real credit pathway — all as MRV provider, not project owner.
7. **Scoring** — 15 criteria, 1–10, for 16 concepts, ranked; plus a weighted "build-first" view.
8. **Recommendations** — Top 10; Top 5 easiest / commercial / B2G / climate-funding / carbon-MRV;
   Top 3 overall, each with a full deep dive (architecture, data schema, MVP vs advanced features,
   AI/ML and GIS opportunities, impact methodology, pricing, go-to-market, partners, agencies and
   companies to approach, risks, a 12-month roadmap, and MVP effort).
9. **Market gaps** — the 10 "data exists but nobody built the layer" patterns, mapped to concepts.
10. **Final recommendation** — build **SolarLedger NG** first (distributed-energy decisions +
    diesel-displacement MRV), with the Open Data → Processing → Platform → Customer → Impact → Revenue
    → Green Funding value chain and a 10-dataset "start experimenting today for $0" list.

## Rebuild the page

```
pip install markdown
python build.py
```

Regenerates `index.html` from the Markdown source. No other dependencies.

---

*Sources for factual claims (Nigerian government & regulators, World Bank, AfDB, GCF, ESA/Copernicus,
NASA, WRI, reputable industry press) are linked inline in the study.*
