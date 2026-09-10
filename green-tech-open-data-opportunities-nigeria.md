# Green-Tech & Climate Products Nigeria Can Build on Open Data
## A market, data, product, funding and carbon-finance research study

*Prepared: 10 September 2026. Prepared by Pjoc. Companion to the EV Ride-Hailing feasibility study in this repository.*

---

## How to read this report

- **Verified fact** = supported by a cited source, linked inline. Sources were checked in September 2026.
- **Estimate / assessment** = the author's synthesis and scoring, clearly the author's judgement, not audited fact.
- Nigerian policy, tariffs, FX and funding windows move fast. Every dataset link, API and funding programme named here was live when checked but **must be re-verified before you spend money**. Treat this as a live-updated scan, not a permanent reference.
- Currency: US dollars, with naira (₦) where a Nigerian figure is native. Assumed rate **₦1,530 = $1 (Sept 2026)** — itself a moving risk.
- "EO" = Earth observation (satellite). "MRV" = Measurement, Reporting & Verification. "DRE" = distributed renewable energy. "C&I" = commercial & industrial. "EF" = emission factor. "B2G" = business-to-government. "tCO₂e" = tonnes of carbon-dioxide equivalent.
- Abbreviations for Nigerian bodies are expanded on first use and collected in Appendix A.

---

# 1. Executive summary

**The thesis.** Nigeria has a large, fast-worsening set of environmental and climate problems — gas flaring and methane, flooding, an electricity crisis now compounded by post-subsidy diesel costs, deforestation, desertification across the north, urban air pollution, plastic and waste mismanagement, and coastal/Niger-Delta degradation. In parallel, an unusually rich body of **free, open, legally reusable data** already covers Nigeria: European (Copernicus/Sentinel), American (NASA, USGS, NOAA), multilateral (World Bank, FAO, UNEP), pan-African (Digital Earth Africa, AFRICapacity), and increasingly Nigerian (GRID3, the Oil Spill Monitor, the Gas Flare Tracker, energydata.info). The **gap is not data — it is the translation layer**: Nigerian agencies, lenders, insurers, exporters and SMEs cannot turn this data into decisions, compliance evidence or fundable projects. That gap is a software opportunity.

**What this study did.** It scanned ~30 sectors, inventoried ~45 open-data sources for Nigeria coverage/licence/API status, converted the strongest into **26 concrete product concepts**, scored 16 of them across 15 criteria, and pressure-tested each against green-funding eligibility and carbon-market rules.

**Headline findings.**

1. **The three best "build-first" opportunities** — highest combined score on open-data readiness, market need, buildability, revenue, funding and carbon potential — are:
   - **① FlareWatch NG** — a gas-flaring & methane intelligence + MRV platform for regulators, oil & gas operators, banks and carbon developers. Best green-funding and market-gap story; methane is the single hottest climate-finance theme globally and nobody sells a Nigeria-specific product.
   - **② SolarLedger NG** — a distributed-energy feasibility + **diesel-displacement MRV** platform for SMEs/C&I sites and the banks and developers financing their solar. Fastest path to revenue; largest buyer base; cleanest additionality story for carbon in Nigeria.
   - **③ FloodShield NG** — asset-level flood-risk analytics and early-warning for state emergency agencies, insurers and lenders. Largest adaptation-finance pool; enormous, recurring, well-documented need.
2. **Open data is genuinely sufficient for an MVP** in at least 12 of the 26 concepts. Where it is not sufficient alone, the missing piece is almost always **operator/field data** (metered kWh, farm polygons, stove-use logs) that the platform itself collects once customers are on board — a defensible moat, not a blocker.
3. **"Avoided emissions" ≠ "carbon credits."** Roughly half the concepts can produce credible *impact reports*; only ~6 have a realistic path to *verified, tradable credits*, and all of those need physical/operational data on top of open data, plus a registered methodology and third-party verification.
4. **Funding is real but conditional.** Nigeria's annual climate-finance shortfall is put at **>$15 billion** by the National Council on Climate Change ([Authority, Sept 2025](https://authorityngr.com/2025/09/23/nigerias-climate-finance-shortfall-exceeds-15-billion-annually-dg-nccc/)). Grants, concessional debt and results-based finance exist (GCF, GEF, AfDB, World Bank DARES, GEAPP, All On, Catalyst Fund, Lacuna Fund's successors, InsuResilience). None will fund a slide deck: they require a defined intervention, a measurable KPI, a baseline, a reporting standard, and usually a pilot with real numbers.

**The single recommendation (Section 10):** build **SolarLedger NG** first — it reaches paying customers fastest, needs the least capital, uses the most reliable free data, and its diesel-displacement MRV engine is the same asset that later unlocks carbon finance and doubles as the core of FlareWatch. Start experimenting **today** with the Global Solar Atlas API, NASA POWER, Google Open Buildings, and VIIRS Black Marble night-lights — all free, no procurement.

---

# 2. The open-data landscape for Nigeria

This section is the raw-material inventory. Products in Section 4 reference these by ID (e.g. **D-03**).

## 2.1 How to read the licence column

| Tier | Meaning | Commercial MVP? |
|---|---|---|
| **A — fully open** | Free, public, explicit reuse licence (CC BY 4.0, CC0, public domain, ODbL, Copernicus "free, full and open"). Commercial use allowed with attribution. | Yes, unrestricted. |
| **B — open, limits** | Free but rate-limited, key-gated, or "non-commercial without permission", or heavy compute needed to use it. | Yes, with engineering or a licence conversation. |
| **C — paid / restricted** | Licence fee, or redistribution forbidden, or Nigerian agency sells it. | Only as a paid input or replace with a Tier-A substitute. |

## 2.2 Master data table — Earth observation & climate

| ID | Dataset / platform | Provider | Contents | Nigeria coverage | Resolution | Update | API | Download | Cost | Licence tier | Source | MVP-sufficient? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | **Sentinel-2 L2A** (optical) | ESA / EU Copernicus | 13-band optical imagery; land cover, agriculture, water, urban, deforestation | Full, every ~5 days | 10–20 m | 5-day revisit | Yes — Copernicus Data Space (STAC, OData, openEO, Sentinel Hub free tier) | Yes | Free | A ("free, full and open") | [dataspace.copernicus.eu](https://dataspace.copernicus.eu/) | Yes |
| D-02 | **Sentinel-1** (C-band SAR) | ESA / Copernicus | Radar backscatter; flood mapping through cloud, ground motion, oil-slick detection | Full | 5–20 m | 6–12 day | Yes — same as D-01; `sar_coherence` process added Feb 2026 | Yes | Free | A | [Copernicus](https://dataspace.copernicus.eu/news/2026-2-18-new-openeo-release) | Yes |
| D-03 | **Sentinel-5P TROPOMI** | ESA / Copernicus | Atmospheric columns: NO₂, CH₄, SO₂, CO, HCHO, aerosol index | Full, daily | ~5.5 × 3.5 km | Daily | Yes — Copernicus, also on Google Earth Engine, NASA GES DISC | Yes | Free | A | [Copernicus](https://dataspace.copernicus.eu/) | Yes for hotspot/trend work; not for facility attribution |
| D-04 | **Landsat 8/9** | USGS / NASA | Optical + thermal; 50-yr archive, land-surface temperature | Full | 30 m (100 m thermal) | 8-day (two sats) | Yes — USGS M2M, on GEE, AWS | Yes | Free | A (public domain) | [usgs.gov](https://www.usgs.gov/landsat-missions) | Yes |
| D-05 | **MODIS / VIIRS land** | NASA | NDVI, land-surface temp, active fire, aerosol optical depth | Full, daily | 250 m–1 km | Daily | Yes — LAADS, AppEEARS, GEE | Yes | Free | A | [nasa.gov](https://ladsweb.modaps.eosdis.nasa.gov/) | Yes |
| D-06 | **NASA FIRMS** (active fire) | NASA | Near-real-time thermal anomalies / fire detections | Full | 375 m / 1 km | <3 h latency | Yes — REST API, free key | Yes (CSV, WMS) | Free | A | [firms.modaps.eosdis.nasa.gov](https://firms.modaps.eosdis.nasa.gov/) | Yes |
| D-07 | **VIIRS Nightfire (VNF) & Black Marble (VNP46)** | NOAA / NASA / Colorado School of Mines | Nightly detection of combustion sources (gas flares) with temperature, radiant heat, estimated gas volume; separately, calibrated night-lights (electrification, outages) | Full, nightly | 750 m | Nightly | Partial — bulk files; Black Marble via NASA API | Yes | Free | A | [eogdata.mines.edu](https://eogdata.mines.edu/products/vnf/) | Yes — this is the core flare-detection feed |
| D-08 | **ERA5 / ERA5-Land** reanalysis | ECMWF / Copernicus C3S | Hourly weather since 1940: temp, wind, precip, radiation, soil moisture | Full | 9–31 km | Daily (5-day lag) | Yes — Copernicus Climate Data Store (CDS) API | Yes | Free | A (Copernicus licence) | [cds.climate.copernicus.eu](https://cds.climate.copernicus.eu/) | Yes |
| D-09 | **CHIRPS** rainfall | UCSB Climate Hazards Center | Daily/pentad/monthly rainfall, bias-corrected, tuned for Africa, 1981–present | Full | ~5.5 km | ~3-week lag (prelim faster) | Via GEE, direct FTP | Yes | Free | A (public domain) | [chc.ucsb.edu/data/chirps](https://www.chc.ucsb.edu/data/chirps) | Yes — best free rainfall for Nigeria |
| D-10 | **GPM IMERG** precipitation | NASA / JAXA | Half-hourly / daily precipitation, near-global | Full | ~10 km | ~4 h (early run) | Yes — GES DISC, GEE | Yes | Free | A | [gpm.nasa.gov](https://gpm.nasa.gov/data/imerg) | Yes |
| D-11 | **NASA POWER** | NASA Langley | Solar irradiance (GHI/DNI/DIF), temperature, wind, humidity, since 1984 | Full (point/grid) | ~0.5° met, 1° solar (plus higher-res derived) | Daily | Yes — REST API, no key, generous limits | Yes | Free | A | [power.larc.nasa.gov](https://power.larc.nasa.gov/api/pages/) | Yes for feasibility; pair with D-12 for bankable yield |
| D-12 | **Global Solar Atlas / Global Wind Atlas** | World Bank / Solargis / DTU | Long-term solar irradiation, PV output potential; wind resource | Full | 250 m (solar), 250 m–1 km (wind) | Static (multi-year climatology) | Yes — GSA API + bulk GIS layers | Yes | Free | A (CC BY 4.0) | [globalsolaratlas.info](https://globalsolaratlas.info/) | Yes |
| D-13 | **Copernicus GloFAS** (Global Flood Awareness System) | Copernicus Emergency Management Service | River-discharge forecasts up to 30 days, reforecasts, flood hazard maps | Full — Niger & Benue basins well modelled | ~5 km river network | Daily forecast | Yes — CDS API | Yes | Free | A | [global-flood.emergency.copernicus.eu](https://global-flood.emergency.copernicus.eu/) | Yes for basin-scale; not street-level |
| D-14 | **Copernicus EMS Rapid Mapping** | Copernicus EMS | On-demand satellite flood-extent maps during declared emergencies (Nigeria activated repeatedly 2022–2024) | Event-based | 10 m–5 m | On activation | Portal + GeoJSON | Yes | Free | A | [emergency.copernicus.eu](https://emergency.copernicus.eu/) | Yes as historical training/validation data |
| D-15 | **JRC Global Surface Water** | EU Joint Research Centre | Water occurrence, seasonality, change 1984–2021 | Full | 30 m | Annual epochs | Via GEE, direct | Yes | Free | A | [global-surface-water.appspot.com](https://global-surface-water.appspot.com/) | Yes |
| D-16 | **Digital Earth Africa** | DE Africa (AWS-hosted) | Analysis-ready: cropland extent & crop type, Water Observations from Space (WOfS), 700k+ waterbodies with surface-area change, coastline change, fractional cover, GeoMAD | Full (continental) | 10–30 m | Rolling; annual products | Yes — ODC, STAC, WMS/WFS, free Sandbox (JupyterHub) | Yes (AWS Open Data) | Free | A (CC BY 4.0) | [digitalearthafrica.org](https://www.digitalearthafrica.org/) · [docs](https://docs.digitalearthafrica.org/) | Yes — a major shortcut for Nigerian land/water products |
| D-17 | **ESA WorldCover** | ESA | Global land cover, 11 classes, 2020 & 2021 | Full | 10 m | Two epochs | Via Terrascope, GEE | Yes | Free | A (CC BY 4.0) | [esa-worldcover.org](https://esa-worldcover.org/) | Yes |
| D-18 | **Dynamic World** | Google / WRI | Near-real-time land-cover probabilities | Full | 10 m | Per Sentinel-2 pass | GEE only | Via GEE | Free | A (CC BY 4.0) | [dynamicworld.app](https://dynamicworld.app/) | Yes (needs GEE) |
| D-19 | **Copernicus DEM (GLO-30) / FABDEM** | ESA / Airbus; FABDEM by U. Bristol | Elevation; FABDEM removes buildings/trees (better for flood) | Full | 30 m | Static | Direct, AWS, OpenTopography | Yes | Free (FABDEM: free non-commercial, licence for commercial) | A / B | [copernicus-dem](https://spacedata.copernicus.eu/collections/copernicus-digital-elevation-model) · [FABDEM](https://data.bris.ac.uk/data/dataset/25wfy0f9ukoge2gs7a5mqpq2j7) | Yes (check FABDEM commercial terms) |
| D-20 | **WorldPop** | U. Southampton | Gridded population, age/sex structure, births, poverty | Full, strong for Nigeria | 100 m | Annual | Yes — REST API | Yes | Free | A (CC BY 4.0) | [worldpop.org](https://www.worldpop.org/) | Yes |
| D-21 | **Google Open Buildings v3** | Google Research | Building footprints + confidence + Plus Codes; also "Open Buildings 2.5D Temporal" (height/presence over time) | Full Nigeria (~50m+ buildings) | Footprint-level | Periodic releases | Via Earth Engine, direct CSV/GeoParquet | Yes | Free | A (CC BY 4.0 / ODbL dual) | [sites.research.google/open-buildings](https://sites.research.google/gr/open-buildings/) | Yes |
| D-22 | **Microsoft / Overture buildings & places** | Microsoft, Overture Maps Foundation | Building footprints (Nigeria incl.), POI "places" | Full | Footprint-level | Overture ~monthly | GeoParquet on Azure/AWS | Yes | Free | A (ODbL / CDLA) | [overturemaps.org](https://overturemaps.org/) | Yes |
| D-23 | **OpenStreetMap** (+ HOT) | OSM community / HOTOSM | Roads, buildings, land use, rivers, power lines, amenities | Variable; good in Lagos/Abuja, thin rurally | Vector | Continuous | Overpass API, extracts (Geofabrik) | Yes | Free | A (ODbL — share-alike) | [openstreetmap.org](https://www.openstreetmap.org/) · [export.hotosm.org](https://export.hotosm.org/) | Yes (mind ODbL share-alike) |
| D-24 | **Global Forest Watch** — tree-cover loss (Hansen/UMD), Integrated Deforestation Alerts (GLAD-L, GLAD-S2, RADD, DIST-ALERT), carbon flux | WRI / UMD / Wageningen / NASA | Annual tree-cover loss 2001–2024; weekly/near-real-time disturbance alerts (some through cloud via radar); above-ground biomass; emissions/removals | Full; Cross River, Ondo, Taraba, Ogun hotspots | 10–30 m | Alerts weekly; annual loss (2025 data early 2026, then monthly) | Yes — GFW Data API (JSON/GeoJSON, query by admin or custom polygon) | Yes | Free | A (CC BY 4.0) | [globalforestwatch.org](https://www.globalforestwatch.org/) · [API](https://www.globalforestwatch.org/help/developers/) | Yes |
| D-25 | **Global Mangrove Watch** | Aberystwyth U. / UNEP / TNC | Mangrove extent & change 1996–present | Niger Delta fully covered | 25 m | ~Annual | Via portal, STAC | Yes | Free | A (CC BY 4.0) | [globalmangrovewatch.org](https://www.globalmangrovewatch.org/) | Yes |
| D-26 | **ESA CCI Biomass / Spawn AGB** | ESA / NASA | Above-ground woody biomass carbon | Full | 100–300 m | Annual epochs | Direct, GEE | Yes | Free | A | [climate.esa.int/biomass](https://climate.esa.int/en/projects/biomass/) | Yes for screening; not survey-grade |
| D-27 | **Climate TRACE** | Climate TRACE coalition | Asset-level GHG emissions (power plants, oil & gas fields, refineries, cement, steel, road segments, landfills, agriculture, shipping) incl. ownership, confidence | Full — every sector, individual Nigerian assets | Asset / 0.1° grid | Annual 2015–2024 + recent monthly; v5.6.0 April 2026 | Yes — API (beta) + full bulk download | Yes | Free | A (CC BY 4.0) | [climatetrace.org/data](https://climatetrace.org/data) | Yes |
| D-28 | **EDGAR** | EU JRC | Global anthropogenic emissions by sector & gas, gridded | Full | 0.1° | Annual (2-yr lag) | Bulk files | Yes | Free | A | [edgar.jrc.ec.europa.eu](https://edgar.jrc.ec.europa.eu/) | Yes |
| D-29 | **Carbon Mapper portal (Tanager-1 + aircraft)** | Carbon Mapper / Planet / NASA JPL | Point-source methane & CO₂ plumes with location, flux rate, imagery | Growing; global oil/gas, waste; Africa detections since early 2025 | ~30 m plume, point-source | Rolling as observed | Yes — data.carbonmapper.org portal + API | Yes | Free | A | [carbonmapper.org](https://carbonmapper.org/articles/new-tanager-1-methane-data) · [data.carbonmapper.org](https://data.carbonmapper.org/) | Yes for confirmed super-emitters; coverage still sparse |
| D-30 | **UNEP IMEO — MARS (Methane Alert & Response System)** | UN Environment Programme | Satellite-detected large methane plumes, operator notifications, growing public data layer | Global incl. Nigeria | Point-source | Continuous | Data portal (methanedata.unep.org) | Partial | Free | A/B | [methanedata.unep.org](https://methanedata.unep.org/) | Complementary evidence layer |
| D-31 | **Aqueduct 4.0** water risk | WRI | Baseline water stress, drought & riverine-flood risk, projections | Full (sub-basin) | Hydro-basin | Periodic | Yes — API + GIS | Yes | Free | A (CC BY 4.0) | [wri.org/aqueduct](https://www.wri.org/aqueduct) | Yes |
| D-32 | **HydroSHEDS / HydroRIVERS / HydroBASINS** | WWF | River network, catchments, lakes | Full | 3–15 arc-sec | Static | Direct | Yes | Free | A (attribution, non-commercial redistribution limits — check) | [hydrosheds.org](https://www.hydrosheds.org/) | Yes |
| D-33 | **ACAG / van Donkelaar surface PM2.5** | Washington U. in St. Louis | Satellite-derived annual (and monthly) ground-level PM2.5, 1998–2022+ | Full | ~1 km | Annual | Direct download | Yes | Free | A (CC BY 4.0) | [sites.wustl.edu/acag](https://sites.wustl.edu/acag/datasets/surface-pm2-5/) | Yes — best free PM2.5 surface for health burden |
| D-34 | **Copernicus CAMS** (atmosphere) | ECMWF / Copernicus | Global air-quality reanalysis & 5-day forecast: PM2.5, PM10, O₃, NO₂, dust | Full | ~9–40 km | Daily | Yes — ADS API | Yes | Free | A | [atmosphere.copernicus.eu](https://atmosphere.copernicus.eu/) | Yes (coarse; combine with sensors) |

## 2.3 Master data table — sectoral, statistical & Nigerian sources

| ID | Dataset / platform | Provider | Contents | Nigeria coverage | Update | API / Download | Cost | Licence tier | Source | MVP-sufficient? |
|---|---|---|---|---|---|---|---|---|---|---|
| D-40 | **World Bank Open Data / WDI / Climate Change Knowledge Portal (CCKP)** | World Bank | Macro, energy, emissions, poverty; country climate profiles & CMIP6 projections | National + some subnational | Annual; CCKP periodic | Yes — API + bulk | Free | A (CC BY 4.0) | [data.worldbank.org](https://data.worldbank.org/) · [climateknowledgeportal.worldbank.org](https://climateknowledgeportal.worldbank.org/) | Yes |
| D-41 | **energydata.info** | ESMAP / World Bank | Nigeria mini-grid sites, DisCo service areas, transmission network, health-facility electrification, load profiles | Nigeria-specific datasets | Varies | Yes — CKAN API + download | Free | A (mostly CC BY 4.0) | [energydata.info](https://energydata.info/) | Yes |
| D-42 | **Ember electricity data** | Ember | Nigeria generation mix, capacity, emissions intensity — yearly + monthly | National | Monthly/yearly | Yes — API + CSV | Free | A (CC BY 4.0) | [ember-energy.org](https://ember-energy.org/data/) | Yes |
| D-43 | **IRENA statistics** | IRENA | Renewable capacity, generation, costs, jobs | National | Annual | Download + API | Free | A | [irena.org/Data](https://www.irena.org/Data) | Yes |
| D-44 | **Global Energy Monitor trackers** | Global Energy Monitor | Power-plant, gas-pipeline/LNG, solar/wind trackers with locations, status, capacity | Nigeria assets included | ~Biannual | Download; some API | Free | A (CC BY 4.0) | [globalenergymonitor.org](https://globalenergymonitor.org/) | Yes |
| D-45 | **World Bank Global Gas Flaring Reduction (GGFR) / VIIRS flaring estimates** | World Bank / Payne Institute | Annual flare volumes by country and by individual flare site (satellite-derived) | Nigeria — top-10 global flarer, site list | Annual | Report + supplementary data | Free | A | [worldbank.org/GGFR](https://www.worldbank.org/en/programs/gasflaringreduction) | Yes |
| D-46 | **Nigerian Gas Flare Tracker** | Federal Ministry of Environment / NOSDRA + partners | Flare sites, flared volume, CO₂, economic value, company attribution (satellite + regulator data) | Nigeria only — Niger Delta | Periodic | Public web dashboard; scrape/manual export (no formal open API) | Free | B (no explicit licence) | [gasflaretracker.ng](https://gasflaretracker.ng/) · [nosdra.gasflaretracker.ng](https://nosdra.gasflaretracker.ng/) | Yes as a seed layer; verify terms |
| D-47 | **Nigerian Oil Spill Monitor** | NOSDRA + Stakeholder Democracy Network (SDN) | Every reported spill since 2006: date, operator, location, cause (corrosion/sabotage/operational), estimated volume, JIV status | Nigeria only — Niger Delta | Ongoing (reporting lag) | Public map; CSV export | Free | A (effectively open) | [oilspillmonitor.ng](https://oilspillmonitor.ng/) | Yes |
| D-48 | **NUPRC data** (Nigerian Upstream Petroleum Regulatory Commission) | NUPRC | Production, gas utilisation & flaring volumes, flare penalties; "NGFCP" flare-commercialisation site data | Nigeria | Quarterly-ish | Reports/PDF; some dashboards | Free | B | [nuprc.gov.ng](https://www.nuprc.gov.ng/) | Partial — needs parsing |
| D-49 | **GRID3 Nigeria** | Govt of Nigeria (was CIESIN/WorldPop/UNFPA) | 980 datasets / 12 sectors: settlement extents & points (~100 m), gridded population to ward level, health/education/markets, boundaries | Nigeria only, national | Periodic | Yes — data.grid3.org portal + HDX + open.africa | Free | A (mostly CC BY 4.0; some restricted) | [grid3.org/geospatial-data-nigeria](https://grid3.org/geospatial-data-nigeria) · [data.grid3.org](https://data.grid3.org/) | Yes |
| D-50 | **Humanitarian Data Exchange (HDX)** | UN OCHA | Nigeria admin boundaries (COD), population, displacement, flood, conflict, food security | Nigeria only, national | Varies | Yes — CKAN API | Free | A (mostly) | [data.humdata.org](https://data.humdata.org/group/nga) | Yes |
| D-51 | **FAO — FAOSTAT, Hand-in-Hand, WaPOR, ASIS** | FAO | Crop production & agri emissions; WaPOR = evapotranspiration / water productivity / biomass, 100–300 m, 10-daily, Africa focus | Full | FAOSTAT annual; WaPOR 10-daily | Yes — FAOSTAT API, WaPOR API | Free | A (CC BY 4.0) | [fao.org/faostat](https://www.fao.org/faostat/) · [wapor.apps.fao.org](https://wapor.apps.fao.org/) | Yes — WaPOR is strong for irrigation/yield |
| D-52 | **iSDAsoil / SoilGrids** | iSDA (Africa) / ISRIC | Soil properties (pH, N, organic C, texture) — iSDA at 30 m for Africa, SoilGrids 250 m global | Full | Static epochs | iSDA API; SoilGrids WCS/REST | Free | A (CC BY 4.0) | [isda-africa.com/isdasoil](https://www.isda-africa.com/isdasoil/) · [soilgrids.org](https://soilgrids.org/) | Yes for advisory; not plot-precise |
| D-53 | **What a Waste 2.0** | World Bank | Waste generation, composition, collection, disposal by country & many cities | National + Lagos/others | Static (2018 base) | Download | Free | A (CC BY 4.0) | [datacatalog.worldbank.org/…what-a-waste](https://datacatalog.worldbank.org/search/dataset/0039597) | Baseline only — dated; needs local top-up |
| D-54 | **River plastic emission models (Meijer et al. / The Ocean Cleanup)** | The Ocean Cleanup | Modelled plastic mass entering ocean per river/outlet | Nigerian rivers incl. Lagos lagoon system | Static model, periodically revised | Download / portal | Free | A (CC BY) | [theoceancleanup.com/sources](https://theoceancleanup.com/sources/) | Baseline / prioritisation only |
| D-55 | **Global Plastic Watch** | Minderoo Foundation / Earthrise | Satellite-detected plastic-waste aggregation sites | Partial — expanding in Africa | Periodic | Portal + data | Free | A | [globalplasticwatch.org](https://globalplasticwatch.org/) | Screening layer |
| D-56 | **GBIF** | GBIF | Species occurrence records | Nigeria records (uneven) | Continuous | Yes — API | Free | A (CC0/CC BY per dataset) | [gbif.org](https://www.gbif.org/) | Yes for biodiversity baselines |
| D-57 | **Protected Planet (WDPA/WD-OECM)** | UNEP-WCMC / IUCN | Protected & conserved area boundaries | Nigeria parks, reserves | Monthly | Yes — API | Free | **B — no commercial use without written permission** | [protectedplanet.net](https://www.protectedplanet.net/) | Yes for non-commercial; licence talk for commercial |
| D-58 | **ND-GAIN Country Index** | U. Notre Dame | Climate vulnerability + readiness scores, 1995–present | National, ranked | Annual | Download | Free | B (free, non-commercial, attribution) | [gain.nd.edu](https://gain.nd.edu/our-work/country-index/) | Context/marketing, not core |
| D-59 | **INFORM Risk Index** | EU JRC / IASC | Hazard, vulnerability, coping-capacity risk — national + INFORM Subnational Nigeria | National + LGA (subnational model) | Annual | Download + API | Free | A | [drmkc.jrc.ec.europa.eu/inform-index](https://drmkc.jrc.ec.europa.eu/inform-index) | Yes |
| D-60 | **NiMet** (Nigerian Meteorological Agency) | NiMet | Station observations, daily forecasts, Seasonal Climate Prediction (annual SCP) | Nigeria | Daily / annual SCP | **Mostly not open** — data sold; SCP released as report | Paid / restricted | C | [nimet.gov.ng](https://nimet.gov.ng/) | No — substitute ERA5/CHIRPS/IMERG; cite SCP qualitatively |
| D-61 | **NIHSA** (Nigeria Hydrological Services Agency) | NIHSA | Annual Flood Outlook (AFO): high/moderate-risk LGAs & communities; river-level bulletins | Nigeria, LGA-level list | Annual (AFO ~April/May) + season bulletins | **PDF / press only** — not machine-readable, no API | Free (as documents) | C (format) | [nihsa.gov.ng](https://nihsa.gov.ng/) | Digitise manually; combine with D-13 |
| D-62 | **National Bureau of Statistics (NBS)** | NBS | GDP, CPI, labour, living standards, some sector surveys | National + state | Varies | Reports; some datasets; [Nigeria data portal / nigerianstat.gov.ng] | Free | B | [nigerianstat.gov.ng](https://www.nigerianstat.gov.ng/) | Partial |
| D-63 | **Nigeria Energy Transition Plan (ETP) & NDC** | Federal Govt / Energy Transition Office / SEforALL | Sector decarbonisation pathways, investment needs, model outputs; updated NDC 3.0 | National | Periodic | Documents + some model data | Free | B | [energytransition.gov.ng](https://www.energytransition.gov.ng/) | Context + assumptions source |
| D-64 | **IEA Emission Factors 2025** | IEA | Grid & fuel CO₂/CH₄ emission factors incl. Nigeria grid intensity 1990–2024 | National | Annual | **Paid database** | C | [iea.org/…emissions-factors-2025](https://www.iea.org/data-and-statistics/data-product/emissions-factors-2025) | No — use free substitutes (Climate TRACE / Ember / EDGAR / IGES CDM grid EF) |
| D-65 | **IGES List of Grid Emission Factors** | Institute for Global Environmental Strategies (Japan) | CDM/Article 6-style grid emission factors by country incl. Nigeria | National | Periodic | Free spreadsheet | Free | A | [iges.or.jp/en/pub/list-grid-emission-factor](https://www.iges.or.jp/en/pub/list-grid-emission-factor/en) | Yes — use this for the Nigeria grid EF |
| D-66 | **Lagos / Nigeria GTFS transit feeds** | LAMATA / Digital Transport for Africa / WRI | Formal BRT routes + digitised informal (danfo) network as GTFS (coverage partial, ageing) | Lagos mainly; some Abuja/Kano efforts | Sporadic | GitHub / DT4A repos | Free | A/B | [digitaltransport4africa.org](https://digitaltransport4africa.org/) · [data-transport.org](https://data-transport.org/) | Partial — expect to refresh/extend the feed yourself |

**Compute platforms that host most of the above for free:** Google Earth Engine (free non-commercial; paid commercial tiers), Microsoft Planetary Computer (free, Hub by request), AWS Open Data Registry / Digital Earth Africa Sandbox (free), Sentinel Hub (free tier), openEO on Copernicus Data Space (free monthly quota).

## 2.4 What the inventory tells you

- **EO and global climate data for Nigeria is abundant, Tier-A, and API-accessible.** Anything built on Sentinel, Landsat, NASA, Copernicus C3S/CAMS/EMS, Digital Earth Africa, GFW, Climate TRACE, WorldPop or Google Open Buildings can be commercialised now.
- **The weak spots are Nigerian in-situ data:** meteorology (NiMet sells it), hydrology (NIHSA publishes PDFs), air-quality ground truth (a handful of research sensors), electricity operations (fragmented across NERC/NISO/DisCos), and anything requiring a national cadastre or land registry (doesn't exist openly). Every viable product below is designed so the open layer carries the MVP and the Nigerian-specific gap is filled by (a) manual digitisation of published reports, (b) partnerships, or (c) user/operator data captured in-product.
- **Two Nigerian open assets are unusually good and under-exploited:** **GRID3** (D-49) and the **Oil Spill Monitor** (D-47). Both are national, granular, and effectively open.

---

# 3. Sector scan — where the problem, the data and the willingness-to-pay line up

| Sector | Nigerian problem (severity) | Open-data readiness | Who would pay | Best product concept(s) |
|---|---|---|---|---|
| Renewable energy / solar | 4.5 GW average grid supply for 230m people; solar underbuilt | High (D-11, D-12, D-41, D-44) | Developers, EPCs, DFIs, states | **P3 SolarSite**, P20 GridWatch |
| Electricity / energy efficiency | Post-subsidy diesel ~₦1,300+/l crushing businesses; ~$14bn/yr spent on self-generation | High | SMEs, C&I, banks, ESCOs | **P4 SolarLedger / WattWise** |
| Electric vehicles / transport | Fuel cost shock; nascent EV policy | Medium | Fleets, lenders, states | (covered by repo's EV project) + P13 |
| Public transport | Lagos: millions of informal trips, no emissions data | Medium (D-66, D-23) | LAMATA, states, e-bus funders | **P13 MoveNG** |
| Carbon accounting / ESG | ISSB adoption mandatory from 2027–2030; CBAM hitting exporters | Medium (D-27, D-65, D-28) | Listed firms, exporters, banks | **P5 CarbonLedger + CBAM** |
| Carbon credits / markets | Carbon Market Activation Policy stalled but registry live; MRV skills gap | Medium | Project developers, buyers, NCCC | P19 NaijaCarbon, feeds P1/P6/P18 |
| Climate-smart agriculture | Rain-fed, low-yield; erratic seasons; 2024/2025 flood crop losses | High (D-09, D-11, D-16, D-51, D-52) | Aggregators, banks, insurers, states | **P8 FarmClimate**, P9 IndexShield |
| Forestry / deforestation | ~3.5%/yr forest loss (among world's highest); EUDR threat to cocoa | High (D-24, D-25, D-26, D-16) | Cocoa/rubber exporters, states, REDD+ | **P6 TerraProof / EUDR** |
| Waste & recycling / circular economy | <20% collection; Lagos ~13,000 t/day; EPR rules underenforced | Medium (D-53, D-55) + field | Recyclers, FMCGs (EPR), estates, LGAs | **P10 LoopNG** |
| Plastic pollution | Nigerian rivers among top ocean-plastic sources | Medium (D-54, D-55, D-01) | FMCGs, plastic-credit developers | P11 PlastiTrace (⊂ P10) |
| Water supply / quality | ~70m without safe water; NRW >40% | Medium (D-15, D-16, D-31) | Water boards, UNICEF, bottlers | P21 AquaNG |
| Flood monitoring / prediction | 2024: 9m+ affected, 31 of 36 states; 2026 AFO: 1,249 comms, 266 LGAs high-risk | High (D-13, D-01, D-09, D-19, D-20) | SEMAs, NEMA, insurers, banks, telcos | **P2 FloodShield** |
| Climate-risk / disaster mgmt | Fragmented, PDF-based, no asset layer | High | Agencies, DFIs, infra owners, insurers | **P2 FloodShield**, P22 SahelGuard |
| Weather / meteorology | NiMet data closed; forecasts under-distributed | Medium (D-08, D-09, D-10 substitute) | Agri, aviation, events, energy, media | ⊂ P8, P9 |
| Air pollution / air quality | Lagos PM2.5 to 200+ µg/m³; ~4× WHO; sparse monitoring | Medium (D-03, D-33, D-34) + sensors | State MoEs, health, employers, public | **P7 AirView** |
| Sustainable construction / green buildings | Energy-guzzling glass towers; no performance data; EDGE uptake low | Medium (D-04, D-21, D-22) | Developers, banks (green mortgages), IFC | P17 EcoRate |
| Real estate / efficiency | Diesel-dependent estates; buyers lack data | Medium | REDAN, estates, valuers, lenders | P17 EcoRate (⊂ P4) |
| Oil & gas emissions / methane | Nigeria a top-10 flarer; 2025 ≈ 204 bcf flared, ~17 Mt CO₂; methane grossly under-measured | High (D-03, D-07, D-27, D-29, D-30, D-45, D-46) | NUPRC, NOSDRA, NCCC, IOCs, independents, banks, developers | **P1 FlareWatch** |
| Maritime / coastal | Erosion, subsidence and surge from Lagos to Bayelsa; ports exposed | High (D-16 coastlines, D-19, D-25) | NIMASA, ports, coastal states, infra | P15 CoastNG |
| Fisheries | Overfishing, IUU, mangrove loss cutting nursery habitat | Medium (D-25, Global Fishing Watch) | Fisheries dept, coastal communities, donors | ⊂ P15 |
| Land-use monitoring | No routine national land-cover-change service | High (D-16, D-17, D-18, D-24) | Lands ministries, REDD+, planners | ⊂ P6, P22 |
| Biodiversity / conservation | Parks under-resourced; wildlife decline | Medium (D-24, D-56, D-57) | NPS, NCF, NGOs, ecotourism | P23 WildWatch |
| Urban planning / smart cities | Rapid sprawl, heat, no green-space metrics | High (D-04, D-21, D-20, D-17) | Lagos/Kano/Kaduna planners, World Bank | P16 CoolCity |
| Logistics / supply-chain emissions | Exporters need Scope 3; no local factors | Medium (D-23, D-27) | Exporters, 3PLs, FMCGs | P24 FreightCarbon (⊂ P5) |
| Sustainable manufacturing | Energy + CBAM pressure on cement/fertiliser/aluminium | Medium | MAN members, exporters | ⊂ P5 |
| Food waste / food systems | ~40% post-harvest loss; cold-chain gap | Low-medium | Processors, cold-chain, donors | ⊂ P8 |
| Green finance | Banks must screen climate risk (CBN principles); green-bond pipeline thin | Medium (D-27, D-31, D-13) | Banks, PFAs, DMO, NGX | P26 BankRisk |
| Climate insurance | <1% penetration; parametric pilots starting (Lagos 2025) | High (D-09, D-13, D-08) | Insurers, reinsurers, NAIC, states | P9 IndexShield |
| Environmental compliance | NESREA/NUPRC enforcement weak; permits paper-based | Medium + field | Regulators, industry | ⊂ P1, P14 |
| Public-sector environmental monitoring | Agencies lack dashboards over their own mandate | High | NESREA, NOSDRA, NEMA, states | cross-cutting |
| Environmental health | Air/water/heat disease burden unquantified locally | Medium (D-33, D-04, D-20) | Health ministries, donors, researchers | ⊂ P7, P16 |

---

# 4. Product concepts

Each concept uses this template. **Effort** is for a lean 2–4 person team; "MVP" means a paying-pilot-ready v1, not a demo.

## 4.1 Fully profiled concepts (scored in Section 7)

### P1 — FlareWatch NG · gas-flaring & methane intelligence + MRV

- **Sector:** oil & gas emissions, methane, environmental compliance, carbon markets.
- **Problem:** Nigeria flared ~204 billion scf of gas in 2025 (~17 Mt CO₂, ~$1.1bn wasted) and continues despite a 92%+ utilisation headline ([Guardian](https://guardian.ng/energy/feasibility-of-achieving-nigerias-zero-gas-flaring-target/), [Vanguard, Jul 2026](https://www.vanguardngr.com/2026/07/gas-flaring-nigeria-loses-5-5bn-as-methane-waste-hits-30m-daily/)). Methane from venting/leaks is barely measured. Regulators, operators, financiers and carbon developers have **no single, independent, continuously updated view** of which sites flare/leak how much, trending which way, worth how much in gas and credits.
- **Target users:** NUPRC and NOSDRA (regulation/penalties), NCCC (national inventory, Article 6), Ministry of Environment; IOCs and independents (Seplat, Oando, Renaissance Africa Energy, Aiteo, NNPC E&P) for internal MRV and OGMP 2.0 reporting; banks and DFIs financing gas-to-power / flare-capture (due diligence); carbon-project developers; litigation NGOs, journalists, host-community groups.
- **How it works:** ingest VIIRS Nightfire nightly (D-07), Sentinel-5P CH₄/NO₂ (D-03), Carbon Mapper & IMEO plume alerts (D-29, D-30), Climate TRACE oil-&-gas assets (D-27), World Bank/Payne flaring volumes (D-45), the Nigerian Gas Flare Tracker (D-46) and NUPRC reports (D-48). Fuse to a **site register**: each flare/facility gets a monthly time series of detected flaring (volume, radiant heat, temperature), estimated methane, CO₂e, gas energy value, and penalty exposure under Nigeria's flare-payment regime. Layer ownership, trends, and "what-if" flare-down scenarios.
- **Core features:** interactive site map + register; monthly/quarterly emissions & $-value reports per operator/asset/state; anomaly alerts (new flare, step-change, plume); OGMP 2.0 / national-inventory export; carbon-project screening (baseline flare volume, additionality flags, indicative credit volume); API.
- **Open data required:** D-03, D-07, D-27, D-29, D-30, D-45, D-46, D-48; basemaps D-21/D-23.
- **Proprietary data required later:** metered flare-gas volumes and gas composition from operators (for verified MRV); drone/OGI survey data; continuous monitors. These convert "estimated" into "verification-grade".
- **Revenue:** tiered SaaS (regulator/enterprise/analyst seats); commissioned deep-dive reports; **MRV-as-a-service** for flare-reduction carbon projects (issuance-linked fee); data API; expert-witness/ESG-assurance support.
- **Nigerian customers — government:** NUPRC, NOSDRA, NCCC, FMEnv, NEITI, state oil-producing-area commissions. **Private:** the ~10–15 serious upstream operators, gas-processing firms, banks (Access, Zenith, UBA, Stanbic) and DFIs with oil-&-gas exposure, carbon developers, law firms.
- **Development complexity:** medium-high (satellite ingest + fusion + attribution logic). **MVP effort:** ~4–6 months / ~$120–200k for v1 built on VIIRS Nightfire + Gas Flare Tracker + Climate TRACE + S5P monthly composites (defer raw plume retrieval).
- **Data reliability:** VIIRS Nightfire flare detection is well-validated globally and the basis of World Bank flaring stats; TROPOMI is directional for area methane, not facility-exact; plume products are high-confidence but sparse. Net: strong for trends and prioritisation, "indicative" for absolute site methane until operator data is added.
- **Regulatory considerations:** you are publishing numbers that create legal/financial exposure for named companies — defensible methodology, uncertainty disclosure, right-of-reply process, and careful "estimated vs verified" separation are mandatory (mirror the repo's emissions-engine governance principles).
- **Competition:** global — Kayrros, GHGSat, Ember, Carbon Mapper, TransitionZero — none Nigeria-focused or selling to Nigerian regulators/operators as the primary market. Nigeria/Africa — the NOSDRA–SDN methane-tracker prototype (phase 1 only, seeking phase-2 funding: [Vanguard](https://www.vanguardngr.com/2024/09/nosdra-sdn-to-track-methane-in-ogoniland-using-satellites/)); the Gas Flare Tracker (static-ish, CO₂-only, no methane, no analytics). **Real whitespace.**
- **The gap it fills:** an independent, continuously updated, analytics-and-MRV layer over data that already exists but sits in five silos — exactly the "fragmented data / manual reporting / no public monitoring layer" gap in Section 9.

### P2 — FloodShield NG · asset-level flood-risk analytics & early warning

- **Sector:** flood monitoring, climate risk, disaster management, climate insurance, green finance.
- **Problem:** 2024 floods affected 9m+ people across 31 of 36 states; the Alau Dam failure put ~50% of Maiduguri underwater, displacing ~389,000 ([OCHA](https://www.unocha.org/publications/report/nigeria/nigeria-floods-situation-report-no-1-25-september-2024), [ReliefWeb](https://reliefweb.int/report/nigeria/nigeria-joint-post-flood-situation-report-borno-state-31-december-2024)). NIHSA's 2026 Annual Flood Outlook flags 1,249 communities across 266 LGAs as high-risk ([Nigeria Housing Market](https://www.nigeriahousingmarket.com/news/nigeria-2026-flood-outlook-33-states-risk)). The outlook is a PDF; there is no asset-level, continuously updated risk layer that a lender, insurer, factory or SEMA can query.
- **Target users:** State Emergency Management Agencies (SEMAs), NEMA, NIHSA (as a delivery partner), state urban/works ministries; insurers & reinsurers pricing parametric cover (Lagos went live with a parametric flood policy protecting up to 4m people in 2025: [AXA Climate](https://climate.axa/publications/parametric-insurance-flood-nigeria-lagos/), [UNDP IRFF](https://irff.undp.org/press-releases/lagos-state-goes-live-parametric-flood-insurance-policy-protecting-4-million-0)); banks (mortgage, SME, agri-loan collateral risk); logistics, telecoms (tower siting), real-estate developers, humanitarian anticipatory-action programmes.
- **How it works:** combine GloFAS discharge forecasts (D-13), CHIRPS/IMERG rainfall (D-09/D-10), FABDEM terrain + HAND modelling (D-19), historical Sentinel-1 flood extents & Copernicus EMS activations (D-02/D-14), Digital Earth Africa WOfS (D-16), against exposure layers — WorldPop (D-20), Google Open Buildings (D-21), GRID3 infrastructure (D-49), OSM roads (D-23). Output: a per-location flood-hazard score, return-period depth estimates, 1–7-day forecast alerts, and an exposure/loss estimate for a portfolio of assets.
- **Core features:** address/polygon risk lookup + PDF report; portfolio upload & aggregate exposure dashboard; forecast alert service (SMS/email/API) tied to trigger thresholds; parametric-trigger design & monitoring module; historical event replays; embeddable widget for lenders' loan-origination flows.
- **Open data required:** D-09, D-10, D-13, D-14, D-16, D-19, D-20, D-21, D-23, D-49; validation from D-01/D-02.
- **Proprietary data later:** drainage/culvert inventories, dam-operation data, claims history from insurer partners, ground-truth flood marks (crowdsourced), high-res city DEMs from drone surveys.
- **Revenue:** SaaS subscriptions (agencies, lenders); per-report / per-API-call; parametric structuring & monitoring fees (share of premium); anticipatory-action contracts with humanitarian funders; data licensing to reinsurers.
- **Nigerian customers — government:** Lagos, Bayelsa, Kogi, Anambra, Adamawa, Borno, Niger, Delta SEMAs; NEMA; NIHSA; Ecological Fund Office. **Private:** NAICOM-regulated insurers (Leadway, AXA Mansard, AIICO, Royal Exchange), reinsurers (Africa Re, Continental Re), banks, developers, telcos (IHS, ATC), bottlers/manufacturers with riverside plants.
- **Development complexity:** medium-high (hydrology + geospatial pipelines). **MVP effort:** ~5–7 months / ~$150–220k — start with a static national hazard map (FABDEM + historical Sentinel-1 + WOfS) plus GloFAS-driven basin alerts for the Niger–Benue system; add city pluvial modelling later.
- **Data reliability:** GloFAS is skilful for large rivers, weaker for flash/urban and ungauged tributaries; Sentinel-1 historical extents are solid ground truth; the binding uncertainty is exposure valuation. Google Flood Hub already publishes free riverine forecasts for Nigeria — treat forecasting as partly commoditised and compete on **asset-level risk, loss estimation, and integration**, not on the raw forecast.
- **Regulatory considerations:** insurance-adjacent analytics may need NAICOM comfort if you touch pricing; disaster comms must be coordinated with NIHSA/NEMA to avoid conflicting official warnings.
- **Competition:** Google Flood Hub (free forecasts, Nigeria covered — [Google](https://sites.research.google/floods/)); global cat-risk (Fathom, JBA, Munich Re) — expensive, not Nigeria-granular, not sold to Nigerian mid-market; local — essentially none productised. Gap: the affordable, Nigeria-calibrated, asset/portfolio layer for lenders, insurers and states.
- **The gap it fills:** "climate risks poorly visualised", "infrastructure projects need climate-risk assessments", "government data lacks a public monitoring layer".

### P3 — SolarSite NG · distributed-energy siting & project-preparation platform

- **Sector:** renewable energy, electricity access, green finance.
- **Problem:** Nigeria's $750m World-Bank-backed **DARES** programme (via the Rural Electrification Agency) aims to deploy up to 1,500 mini-grids and 1.5m solar home systems and displace 250,000+ diesel gensets, crowding in ~$1.1bn private capital ([ESMAP/World Bank](https://www.esmap.org/), [Industrial Info](https://www.industrialinfo.com/news/article/nigeria-plans-750-million-mini-solar-grid-strategy--355334)). Developers still spend months and thousands of dollars per site on feasibility (resource, demand, competing-grid distance, land, bankability). Site selection and demand estimation are slow, inconsistent and hard to finance.
- **Target users:** mini-grid & SHS developers, C&I solar EPCs, REA, DisCos (for interconnected mini-grids), DFIs and funds (GEAPP, All On, AfDB, InfraCo), state electrification agencies, equipment distributors.
- **How it works:** fuse Global Solar Atlas + NASA POWER (D-11/D-12) for resource; VIIRS Black Marble night-lights (D-07) + HREA-style modelling for current electrification and reliability; Google Open Buildings + WorldPop + GRID3 (D-21/D-20/D-49) for settlement size, structure counts and demand proxies; energydata.info mini-grid & grid layers (D-41) and OSM (D-23) for existing infrastructure and grid distance; land cover (D-17) and protected areas (D-57) for siting constraints. Produce a ranked pipeline of candidate sites with modelled load, indicative system size, LCOE band, and a pre-filled project-prep pack.
- **Core features:** site-ranking map; per-site feasibility one-pager (resource, demand curve, system sizing, capex/opex range, payback, diesel displaced, CO₂e avoided); portfolio/pipeline manager; DFI-ready export; API into developer tools (integrates with, not competes with, operational platforms like Odyssey).
- **Open data required:** D-07, D-11, D-12, D-17, D-20, D-21, D-23, D-41, D-49, D-57.
- **Proprietary data later:** actual metered mini-grid load profiles, willingness-to-pay surveys, ground land-tenure verification, developer cost benchmarks.
- **Revenue:** SaaS (developer/DFI seats); pay-per-feasibility-pack; success fee on financed projects; data licensing to DFIs designing tenders; white-label for REA/state agencies.
- **Nigerian customers — government:** REA, state agencies (e.g. Lagos, Ogun, Cross River, Sokoto), Energy Commission of Nigeria. **Private:** Husk, Nayo, Prado, PowerGen, Rensource-type C&I firms, Sun King / d.light (SHS targeting), Odyssey (partner), banks and funds.
- **Development complexity:** medium. **MVP effort:** ~3–5 months / ~$90–150k — the datasets are tabular/raster and well-documented; the modelling (load estimation, sizing) is established (OnSSET/GEP lineage).
- **Data reliability:** solar resource data is bankable-grade; the weak link is demand estimation without ground surveys — hence the "indicative" framing and the upsell to verified load data.
- **Regulatory considerations:** light. Mini-grid regulation (NERC's mini-grid regs) matters to customers, not to the tool; keep NERC tariff/permit logic current as a feature.
- **Competition:** Odyssey Energy Solutions is the official DARES digital platform for **project management and results-based payments** ([Launch Base Africa](https://launchbaseafrica.com/2025/09/12/odyssey-secures-7-5m-from-bii-to-scale-its-fintech-solution-for-nigerias-off-grid-energy-gap/)) — but that's workflow/finance ops, not open-data-driven **siting and feasibility**. KTH/World Bank Global Electrification Platform did national least-cost modelling (static, academic). Gap: a living, developer-usable siting-and-prep product.
- **The gap it fills:** "open data exists but developers can't turn it into fundable projects"; fragmentation across REA/DisCo/geospatial sources.

### P4 — SolarLedger NG (a.k.a. WattWise) · SME/C&I clean-energy decisions + diesel-displacement MRV

- **Sector:** energy efficiency, distributed renewables, green finance, carbon MRV.
- **Problem:** removal of the petrol subsidy (2023) and FX collapse pushed diesel to ~₦1,300–1,500/l; Nigerian businesses spend an estimated **$14bn+/year** running generators. Thousands of SMEs and mid-caps want to switch to solar-plus-storage but can't size it, can't model the payback credibly, can't get finance, and — once they switch — can't prove the savings or the emissions avoided to a lender, a parent company or a carbon buyer.
- **Target users:** SMEs and mid-market firms (manufacturing, agro-processing, hospitals, schools, hospitality, telecoms sites, cold stores); solar EPCs (as a sales tool); banks and lessors financing solar (BOI, Development Bank of Nigeria, Sterling, leasing companies); C&I developers; corporates tracking Scope 1/2 across Nigerian sites.
- **How it works:** user enters location + uploads 6–12 months of electricity bills and diesel logs (or connects a meter). The platform pulls Global Solar Atlas/NASA POWER (D-11/D-12), the applicable DisCo tariff, grid-supply reliability from night-lights (D-07) and Ember grid data (D-42), and the Nigeria grid emission factor (D-65). It sizes a solar+storage system, models bill savings and payback under FX/fuel scenarios, and — crucially — runs a **diesel/grid-displacement MRV engine** (same architecture as this repo's emissions-engine spec) that produces an auditable "energy & emissions avoided" report each month once the system is running.
- **Core features:** feasibility & payback calculator with scenario sliders; financing-application pack; installer marketplace/quotes; post-install monitoring (manual or meter-integrated); monthly verified savings + tCO₂e-avoided report; portfolio view for lenders and multi-site corporates; carbon-project readiness score.
- **Open data required:** D-07, D-11, D-12, D-42, D-65; tariffs from NERC (D-48-adjacent), building footprint D-21 for roof-area estimate.
- **Proprietary data later:** metered generation/consumption (IoT), installer cost database, verified fuel-price feeds, loan-performance data.
- **Revenue:** freemium calculator → paid SaaS (business tier, installer tier, lender tier); lead-generation fee from installers; MRV/verified-report subscription; carbon-aggregation cut when sites are pooled into a programmatic project.
- **Nigerian customers — government:** BOI, DBN, REA (SHS/C&I windows), state investment promotion agencies, public hospitals/universities going solar. **Private:** MAN members, hospital groups, school groups, QSR chains, tower companies, Sterling/Access/Zenith solar-lending desks, EPCs (Daystar, Rensource, Havenhill, Arnergy customers).
- **Development complexity:** low-medium. **MVP effort:** ~2–4 months / ~$50–110k — a bill-parser + solar model + report generator; the hard part (verification-grade MRV) is incremental and directly reuses the repo's `emissions-engine-spec`.
- **Data reliability:** high — solar resource and tariffs are reliable; savings verification depends on data quality flags (measured > modelled), which the design already enforces.
- **Regulatory considerations:** minimal to launch; carbon-claim rules apply once you issue "avoided" figures publicly — keep the ESG ledger and any future credit ledger separate.
- **Competition:** global calculators (Aurora, HelioScope, PVsyst) — engineering tools, not Nigeria-finance-or-MRV oriented; local — EPCs have in-house spreadsheets; **CarbonCheck** is an early Nigerian SME carbon-footprint startup ([Businessday](https://businessday.ng/opinion/article/esg-a-lifeline-for-the-sustainability-of-nigerias-smes/)) but not energy-modelling/MRV focused; Odyssey is C&I-developer-facing. Gap: the SME-and-their-lender-facing decision + proof layer.
- **The gap it fills:** "Nigerian SMEs can't afford international sustainability software"; "lenders need independent environmental-impact verification"; "reporting is manual".

### P5 — CarbonLedger NG · GHG accounting, ESG reporting & CBAM intelligence

- **Sector:** ESG / corporate sustainability reporting, green finance, sustainable manufacturing, logistics emissions.
- **Problem:** Nigeria's Financial Reporting Council has an amended roadmap making **ISSB/IFRS S1–S2 disclosure mandatory** — voluntary/early from 2027, public-interest entities 2028, SMEs by 2030 ([IAS Plus](https://www.iasplus.com/en/news/2026/01/nigeria-issb), [FRC Nigeria](https://frcnigeria.gov.ng/2026/02/26/frc-unveils-amended-roadmap-and-sustainability-reporting-guideline-to-strengthen-adoption-of-ifrs-sustainability-disclosure-standards-in-nigeria/)). Separately, the EU **CBAM** definitive regime is charging carbon on imports of cement, fertiliser, aluminium, iron & steel, hydrogen — hitting Nigerian exporters (Dangote, Indorama, Notore, aluminium) now. Local firms lack Nigeria-specific emission factors and affordable tooling.
- **Target users:** NGX-listed firms and their subsidiaries, exporters to the EU, banks (CBN Sustainable Banking / climate-risk disclosure), multinationals' Nigerian operations, large SMEs in MNC supply chains, consultants/assurance firms.
- **How it works:** guided data entry (fuel, power, fleet, refrigerants, purchased goods, logistics) → applies IPCC/GHG-Protocol factors plus Nigeria-specific ones (grid EF from D-65, road-transport from D-27, fuels) → produces GHG inventory (Scope 1/2/3), ISSB-aligned disclosure drafts, CBAM embedded-emissions reports per product, and reduction scenarios. Benchmarks against Climate TRACE asset data (D-27) for sanity checks.
- **Core features:** emissions calculator with Nigeria factor library; ISSB/IFRS-S2 & NGX Sustainability report templates; CBAM product-carbon-footprint module + quarterly declaration export; supplier data-collection portal; audit trail for third-party assurance; target-setting & MACC.
- **Open data required:** D-27, D-28, D-42, D-65; FAOSTAT (D-51) for agri supply chains.
- **Proprietary data later:** primary supplier data, metered site data, verified Nigeria-specific LCA factors (a build-and-own asset).
- **Revenue:** SaaS tiers by revenue/complexity; CBAM module premium; assurance-partner referral; consulting; factor-library licensing.
- **Nigerian customers — government:** FRC (standards partner), NGX Regulation, SEC, DMO (green bonds), NEITI. **Private:** the ~150 NGX-listed firms, Dangote Group, BUA, Nigerian Breweries, Nestlé Nigeria, Seplat, MTN/Airtel, banks, Big-4 and local assurance firms.
- **Development complexity:** low-medium (mostly logic + templates + factor DB). **MVP effort:** ~3–5 months / ~$80–140k.
- **Data reliability:** high for Scope 1/2; Scope 3 always weak — manage with data-quality tiers.
- **Regulatory considerations:** must track FRC/ISSB and EU CBAM rule changes; align with the FRC's Sustainability Reporting Guideline (SRG 1) 2026.
- **Competition:** global (Watershed, Persefoni, Greenly, Plan A, Sweep) — priced for OECD, weak on Nigeria factors and CBAM-for-Africa; local — CarbonCheck and consultancies. Gap: Nigeria-localised, CBAM-aware, assurance-ready, affordable.
- **The gap it fills:** "companies need evidence for ESG reports"; "reporting is manual"; "can't afford international software".

### P6 — TerraProof NG · deforestation, EUDR traceability & forest-carbon MRV

- **Sector:** forestry, deforestation monitoring, climate-smart agriculture, carbon markets, land-use.
- **Problem:** the **EU Deforestation Regulation** requires plot-polygon geolocation and deforestation-free proof for cocoa, rubber, palm, wood, coffee, cattle, soy entering the EU. Nigeria is a significant cocoa exporter (Ondo, Cross River, Ekiti, Osun); industry estimates **>half of output may initially fail** and "geolocation and farm-polygon mapping remain the primary compliance bottleneck" ([SCS Global](https://www.scsglobalservices.com/news/nigeria-risks-trade-as-eu-sets-december-2025-deadline-for-deforestation-compliance), [Vanguard](https://www.vanguardngr.com/2025/08/deforestation-nigeria-eu-synergize-on-eudr-compliance-in-cocoa-industry/)). Nigeria also has one of the world's highest deforestation rates and a Cross River REDD+ programme needing MRV.
- **Target users:** cocoa/rubber exporters & licensed buying agents, cooperatives, processors; state forestry commissions and the Federal Department of Forestry; REDD+ programme units; conservation NGOs; agroforestry/ARR carbon developers; banks financing commodity trade; EU importers sourcing from Nigeria.
- **How it works:** collect farm polygons via a field app (or import); screen each against GFW tree-cover loss + integrated alerts + Hansen baseline (D-24), Sentinel-2 time series (D-01), Dynamic World (D-18) and the EU's forest-cover benchmark map for the post-2020 cut-off; generate per-plot risk classification and a consolidated **Due Diligence Statement** pack; for carbon, compute baseline forest area/biomass (D-26) and monitor change for REDD+/ARR/agroforestry.
- **Core features:** field mapping app (offline); plot risk dashboard + alerts; EUDR DDS generator + chain-of-custody ledger; cooperative/ supplier management; REDD+/ARR MRV module (baseline, activity data, leakage flags); buyer-facing verification portal.
- **Open data required:** D-01, D-17, D-18, D-24, D-25, D-26; boundaries D-49/D-50.
- **Proprietary data later:** the farm-polygon database itself (highly defensible), yield/volume records, cooperative membership, ground-verification photos.
- **Revenue:** per-farmer or per-tonne traceability SaaS; DDS-pack fees; MRV-as-a-service for carbon projects (issuance-linked); buyer subscriptions; government licensing for national traceability.
- **Nigerian customers — government:** Federal Ministry of Agriculture & the National Cocoa Management Committee, state cocoa/forestry agencies, Cross River REDD+, NEPC (export promotion). **Private:** exporters (e.g. members of the Cocoa Exporters Association), Olam/ETG-type traders, processors (FTN Cocoa, Cocoa Products Ile-Oluji), rubber firms, chocolate importers.
- **Development complexity:** medium-high (field app + EO change detection + audit ledger). **MVP effort:** ~5–7 months / ~$140–210k; a cocoa-only EUDR MVP in one or two states is a tighter ~4 months.
- **Data reliability:** GFW alerts and Hansen loss are the recognised references (used by the EU and traders); the residual risk is smallholder plot boundary accuracy and the EUDR's shifting timeline.
- **Regulatory considerations:** EUDR text and guidance still evolving (implementation timing has slipped before); align outputs with the EU Information System schema; data-protection for farmer PII.
- **Competition:** global — Satelligence, Nature Alert, Descartes Labs, Meridia, Koltiva, TraceX ([tracextech](https://tracextech.com/eudr-exporters/cocoa-exporters-nigeria/)) — mostly enter via multinationals in Côte d'Ivoire/Ghana; light on-the-ground presence for Nigeria's fragmented exporter base. Gap: a Nigeria-first, cooperative-scale, affordable EUDR + carbon double-use tool.
- **The gap it fills:** "datasets fragmented", "reporting manual", "SMEs can't afford global software", plus a hard regulatory deadline.

### P7 — AirView NG · air-quality nowcasting, forecasting & health intelligence

- **Sector:** air pollution, environmental health, public-sector monitoring, urban planning.
- **Problem:** Lagos PM2.5 readings range from ~6 to **>200 µg/m³** (Banana Island study), routinely multiples of WHO guidance; Nigeria has only a handful of research-grade monitors and no public real-time network ([London Journal of Physics study](https://londonjphysics.org/index.php/ljp/article/view/14431), [UChicago EPIC](https://climate.uchicago.edu/news/lagos-port-harcourt-embrace-innovative-pm2-5-monitoring-with-ai-and-sensor-technology/)). A University of Lagos / EPIC project is deploying just 15 low-cost sensors (2025–26).
- **Target users:** Lagos, Rivers, FCT and other state environment ministries; NESREA; hospitals and health ministries; schools; employers and embassies (duty of care); real-estate; researchers; media; the public (app).
- **How it works:** blend Sentinel-5P NO₂/aerosol (D-03), CAMS PM2.5 forecasts (D-34), ACAG satellite-derived surface PM2.5 climatology (D-33), any available OpenAQ/low-cost sensor feeds, and traffic/road data (D-23) in a land-use-regression / ML model to produce a gridded hourly PM2.5 nowcast + 3-day forecast, calibrated as local sensors come online.
- **Core features:** live AQI map + 72-h forecast; health-risk guidance by group; alerts; historical exposure analytics (for epidemiology, ESG, litigation); "sensor-network-as-a-service" for states; public app with premium tier; API.
- **Open data required:** D-03, D-33, D-34, D-23; OpenAQ.
- **Proprietary data later:** your own/managed low-cost sensor network (the calibration moat), clinic admission data partnerships.
- **Revenue:** B2G dashboards + managed sensor networks; enterprise API/duty-of-care subscriptions; app premium + sponsorship; research data licensing.
- **Nigerian customers — government:** Lagos State Ministry of the Environment & LASEPA, Rivers State, FCT, NESREA, Federal Ministry of Environment, NCDC. **Private:** hospital groups, international schools, oil majors' HSE teams, embassies, property developers.
- **Development complexity:** medium (ML fusion + calibration). **MVP effort:** ~4–6 months / ~$100–160k; a satellite-only city nowcast is faster but less credible without ground calibration.
- **Data reliability:** satellite + CAMS give spatial pattern well but absolute PM2.5 needs ground calibration — the whole model hinges on securing even ~10–20 reference/low-cost points per city.
- **Regulatory considerations:** low; coordinate official AQI messaging with state agencies; sensor siting permissions.
- **Competition:** AirQo (Uganda-based, expanding, already some Lagos coverage), IQAir/PurpleAir (hardware + app, thin Nigeria data), Plume Labs. Gap: a Nigeria-dedicated public+B2G platform with managed local calibration and health framing.
- **The gap it fills:** "open data exists but agencies can't interpret it"; "no public monitoring layer"; "climate/health risk poorly visualised".

### P8 — FarmClimate NG · climate-smart agronomic advisory & de-risking layer

- **Sector:** climate-smart agriculture, weather, food systems, climate insurance.
- **Problem:** ~70% of Nigerian farming is rain-fed and smallholder; season onset is increasingly erratic; 2024–2025 floods and northern dry spells caused major crop losses and food-price spikes. Advisory reach is thin and generic.
- **Target users:** delivered B2B2C via aggregators, cooperatives, agri-SMEs, out-grower schemes, input companies, agri-lenders (NIRSAL), insurers, and state ADPs — not sold direct to farmers.
- **How it works:** CHIRPS + IMERG + ERA5 (D-09/D-10/D-08) for rainfall/onset; NASA POWER (D-11) for GDD/ET; WaPOR (D-51) for water stress and biomass; Sentinel-2 NDVI (D-01) and Digital Earth Africa crop layers (D-16) for in-season crop state; iSDAsoil (D-52) for soil constraints; GEOGLAM/ASIS for anomaly context. Generate location- and crop-specific guidance: planting window, variety, fertiliser timing/rate, pest/disease risk, irrigation need, harvest timing, and a plot "green-up" check.
- **Core features:** SMS/USSD + app advisory; agro-dealer dashboard; lender/insurer risk feed (drought index, NDVI shortfall); MRV hooks for climate-smart practice adoption and fertiliser-optimised N₂O reduction; yield forecast.
- **Open data required:** D-01, D-08, D-09, D-10, D-11, D-16, D-51, D-52.
- **Proprietary data later:** farmer registry + geolocated plots, observed yields, practice adoption logs, agronomist feedback loop.
- **Revenue:** per-farmer SaaS to aggregators/banks/insurers; input-marketing/marketplace commission; bundled-with-credit/insurance fee; carbon (soil/agroforestry) MRV later.
- **Nigerian customers — government:** FMARD, NAERLS, state ADPs, NIRSAL, NAIC, National Agricultural Seeds Council. **Private:** ThriveAgric, Crop2Cash, Babban Gona, AFEX, Releaf, out-grower schemes (Olam, Flour Mills, OLAM, Nestlé), input firms (Notore, Saro), insurers.
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$90–150k for one agro-ecological zone and 2–3 crops.
- **Data reliability:** rainfall/NDVI reliable; yield prediction weak without ground data — position as decision-support + de-risking, not a guarantee.
- **Regulatory considerations:** low; data-protection for farmer data; NCC rules for USSD/SMS.
- **Competition:** crowded — Zenvus, Hello Tractor, ThriveAgric, Crop2Cash ([GSMA](https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_resources/gsma-innovation-fund-start-ups-crop2cash/)), EOS Data Analytics, Pula, aWhere/aClimate, IITA tools. Gap: a pure **open-data climate-risk + agronomy engine** that these players embed rather than build — sell picks-and-shovels, not another farmer app.
- **The gap it fills:** fragmented weather/soil/EO data; no affordable localised agronomic intelligence layer.

### P9 — IndexShield NG · parametric & index-insurance analytics engine

- **Sector:** climate insurance, agriculture, disaster finance.
- **Problem:** insurance penetration <1%; agri and disaster risk is largely uninsured; parametric pilots are starting (Lagos flood 2025; area-yield rice insurance has paid out via Leadway/Pula) but each is bespoke and slow to structure ([InstTech](https://www.instech.co/knowledge-centre/growth-of-parametric-insurance-in-africa-the-parametric-post-issue-28/)).
- **Target users:** insurers, reinsurers, MGAs, brokers, agri-lenders, states, WFP/ARC-type programmes, development funders subsidising premiums.
- **How it works:** a library of hazard indices (rainfall deficit/excess from CHIRPS/IMERG, NDVI shortfall from D-01/D-05, flood extent from D-13/D-02, heat, windstorm) with historical burn-cost analysis, basis-risk diagnostics, trigger design, pricing support, and live monitoring + payout calculation against contract terms.
- **Core features:** index designer + backtester; portfolio pricing & accumulation; contract monitoring & automated payout trigger reports; basis-risk dashboards; regulator/reinsurer reporting packs.
- **Open data required:** D-01, D-02, D-05, D-08, D-09, D-10, D-13.
- **Proprietary data later:** loss/claims history, ground yield data, weather-station cross-validation.
- **Revenue:** analytics SaaS licence; per-policy or per-programme fee; structuring retainers; reinsurance-broking support.
- **Nigerian customers — government:** NAIC, NIRSAL, NAICOM (framework), state governments. **Private:** Leadway, AXA Mansard, AIICO, Royal Exchange, Sovereign Trust, Africa Re, Continental Re, Pula (partner/competitor).
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$100–160k.
- **Data reliability:** good for rainfall/NDVI indices; basis risk is the core product challenge and selling point.
- **Regulatory considerations:** NAICOM parametric/index framework; consumer-protection on basis risk.
- **Competition:** Pula (dominant in African ag index insurance), Global Parametrics, Descartes Underwriting, Raincoat (LatAm), IBISA. Gap: an independent Nigeria-calibrated analytics layer for local insurers who can't build one.
- **The gap it fills:** "investors/lenders need independent verification"; manual, bespoke structuring.

### P10 — LoopNG · waste & recycling marketplace with diversion MRV

- **Sector:** waste management, circular economy, plastic pollution.
- **Problem:** collection rates below 20–40% in most cities; Lagos generates ~13,000 t/day; EPR obligations on producers (NESREA) are poorly tracked; informal waste pickers are unbanked and invisible in data.
- **Target users:** recyclers & aggregators, FMCG producers with EPR obligations, estates and facility managers, LGAs and state waste authorities, plastic-credit buyers, informal collectors.
- **How it works:** app connects households/businesses/collectors to aggregators (pickup requests, geotagged weights, digital payments), while a data layer converts logged tonnages + composition into **landfill-diversion, avoided-methane and recovered-plastic metrics** benchmarked to What a Waste (D-53) and validated against Global Plastic Watch dump-site imagery (D-55) and Sentinel-2 (D-01).
- **Core features:** collection marketplace + wallet; material traceability ledger; EPR compliance reporting for producers; diversion & CO₂e/plastic-credit dashboards; collector ID + credit history.
- **Open data required:** D-01, D-53, D-55; boundaries D-49.
- **Proprietary data later:** transaction weights (the core asset), material prices, facility throughput.
- **Revenue:** transaction commission; EPR compliance & reporting subscriptions from producers; plastic-credit / carbon MRV fees; analytics for LGAs; float/fintech.
- **Nigerian customers — government:** LAWMA and state waste agencies, NESREA, LGAs, Ministry of Environment. **Private:** Nigerian Breweries, Coca-Cola/NBC, Nestlé, Unilever, Dangote, FrieslandCampina (EPR); recyclers (Wecyclers, Scrapays, Chanja Datti, Planet 3R — potential partners/competitors: [Nairametrics](https://nairametrics.com/2025/04/05/unilever-uk-government-and-ey-announce-grant-of-500000-for-five-west-african-startups-including-three-in-nigeria/)).
- **Development complexity:** medium (marketplace + payments + ops). **MVP effort:** ~4–6 months / ~$110–180k; ops-heavy, so capital needs rise with scale.
- **Data reliability:** self-reported weights need audit controls; satellite validation is coarse.
- **Regulatory considerations:** NESREA EPR regs, waste-handler licensing, payments/KYC.
- **Competition:** Wecyclers, Scrapays, Pakam, Chanja Datti, Recyclepoint — several exist. Gap: the **EPR-compliance + verified-diversion data layer** across them, rather than another collection network.
- **The gap it fills:** "reporting manual"; producers "need evidence" for EPR/ESG; fragmented actor data.

### P13 — MoveNG · paratransit planning & transport-emissions platform

- **Sector:** public transportation, sustainable transport, logistics emissions.
- **Problem:** Lagos moves millions daily on ~75,000 informal danfo buses plus BRT; route data is outdated/partial; there is no emissions baseline to justify electrification or BRT expansion, yet funders (GEAPP, World Bank, GIZ) are financing e-buses.
- **Target users:** LAMATA and state transport authorities/ministries, BRT operators, e-bus project developers and their funders, urban planners, freight operators.
- **How it works:** rebuild/extend GTFS for Lagos (and Abuja/Kano) from DT4A/WRI feeds (D-66) + OSM (D-23) + crowdsourced traces; combine with population (D-20), Climate TRACE road transport (D-27) and fuel factors to model ridership, mode share, and fleet emissions; scenario-model BRT/e-bus interventions with CO₂e, fuel and air-quality co-benefits.
- **Core features:** transit data manager + GTFS publishing; demand & emissions model; intervention scenario builder (e-bus, BRT, NMT); MRV module for financed projects; open trip-planner feed for citizens.
- **Open data required:** D-20, D-23, D-27, D-66; D-03/D-33 for co-benefits.
- **Proprietary data later:** AVL/ticketing data from operators, boarding counts, fuel logs.
- **Revenue:** B2G planning SaaS + data services; project business-case & MRV contracts; feed licensing to nav/mobility apps; donor-funded studies.
- **Nigerian customers — government:** LAMATA, Lagos/Ogun/FCT/Kano transport bodies, Federal Ministry of Transportation, NURTW-adjacent cooperatives. **Private:** BRT operators (Primero), e-mobility firms (Oando Clean Energy e-buses, MAX, Metro Africa Xpress), logistics firms.
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$100–150k.
- **Data reliability:** GTFS needs continuous upkeep; emissions modelling is defensible at fleet level, weak per-vehicle without telematics.
- **Regulatory considerations:** low; data-sharing MOUs with authorities.
- **Competition:** WRI/DT4A (open-data enabler, not a product), WhereIsMyTransport (exited 2023), Google (consumer routing only). Gap: a planning-and-MRV product for African paratransit authorities.
- **The gap it fills:** "government data lacks a public layer"; no emissions baseline for transport funding.

### P14 — DeltaGuard NG · Niger Delta environmental monitoring & remediation MRV

- **Sector:** oil & gas, maritime/coastal, biodiversity, environmental compliance, blue carbon.
- **Problem:** thousands of oil-spill incidents (NOSDRA Oil Spill Monitor, D-47), chronic mangrove loss, and the slow UNEP-mandated Ogoniland clean-up (HYPREP). Monitoring is under-resourced and contested; remediation outcomes are rarely independently verified.
- **Target users:** NOSDRA, HYPREP, NUPRC, state environmental agencies; IOCs and their remediation contractors; host-community trusts (PIA-mandated); litigation NGOs and law firms; mangrove-restoration / blue-carbon developers.
- **How it works:** fuse the Oil Spill Monitor record (D-47) with Sentinel-1 slick detection (D-02), Sentinel-2 vegetation/turbidity (D-01), Global Mangrove Watch change (D-25), biomass (D-26) and Digital Earth Africa coastline/water (D-16). Produce incident verification, impact-area estimation, remediation progress tracking, and mangrove-restoration MRV (baseline extent, planting survival, biomass accrual).
- **Core features:** incident dashboard + satellite corroboration; impacted-area & sensitivity mapping; remediation milestone tracker with before/after imagery; blue-carbon MRV module; community-facing transparency portal.
- **Open data required:** D-01, D-02, D-16, D-25, D-26, D-47.
- **Proprietary data later:** field sampling (TPH, soil), drone surveys, planting records, community monitoring reports.
- **Revenue:** monitoring SaaS (regulators, operators); independent verification reports; blue-carbon MRV-as-a-service; expert evidence; donor-funded community monitoring.
- **Nigerian customers — government:** NOSDRA, HYPREP, NUPRC, Bayelsa/Rivers/Delta environment ministries, NDDC, Ministry of Environment. **Private:** Renaissance Africa Energy, Seplat, NNPC, Aiteo, remediation contractors, law firms, blue-carbon developers.
- **Development complexity:** medium-high; **MVP effort:** ~5–7 months / ~$140–200k; an "oil-spill corroboration" MVP alone is ~3–4 months.
- **Data reliability:** Sentinel-1 slick detection has false positives (look-alikes); mangrove change is well-established; spill-volume estimation stays indicative.
- **Regulatory considerations:** politically sensitive; publishing contested numbers requires rigorous methodology and right-of-reply; PIA host-community provisions are an opportunity.
- **Competition:** SkyTruth (global, not productised for Nigeria), SDN's advocacy tools, academic studies. Gap: an operational monitoring + MRV product for the Delta's specific institutions.
- **The gap it fills:** "independent environmental-impact verification"; "public monitoring layer"; fragmented incident data.

### P18 — CleanCook MRV NG · digital MRV for clean-cooking carbon projects

- **Sector:** clean cooking, carbon markets, forestry (fuelwood), environmental health.
- **Problem:** clean cooking is Africa's largest carbon-credit segment but is under an integrity cloud — the ICVCM declined to approve several legacy cookstove methodologies in Feb 2025 and analyses found some projects delivered ~11% of claimed impact ([RMI](https://rmi.org/resources/technical-explainer-clean-and-improved-cookstove-carbon-credits/), [Modern Cooking Africa](https://www.moderncooking.africa/)). Nigeria has huge LPG/improved-stove/ethanol programmes and made its first clean-cooking credit sale, but MRV is "fragmented … weak institutional coordination" ([Business AM](https://businessamlive.com/stakeholders-push-mrv-reform-to-unlock-nigerias-climate-finance-potential/)).
- **Target users:** stove & fuel distributors, carbon-project developers, results-based-finance programmes (World Bank CI-Dev, Clean Cooking Alliance), verifiers, NCCC.
- **How it works:** combine household registry + stove-use sensors (SUMs) + fuel-purchase logs with open context data — DHS/MICS baseline fuel use, GFW fuelwood/forest pressure (D-24), biomass (D-26), population (D-20), and remote checks — into a defensible, ICVCM-aligned digital MRV pipeline with statistically valid sampling, usage decay, stacking adjustments and leakage.
- **Core features:** beneficiary & device registry; sensor/field-survey data capture; kitchen-performance & usage analytics; methodology-compliant emissions calc (fNRB, stacking, drop-off); audit-ready evidence packs; registry integration.
- **Open data required:** D-20, D-24, D-26; DHS/MICS; fNRB datasets (MoFuSS / Bailis).
- **Proprietary data later:** sensor telemetry, survey panels, sales records — the whole verification value is here; open data only provides context and cross-checks.
- **Revenue:** SaaS + issuance-linked MRV fee; RBF verification contracts; methodology-transition advisory.
- **Nigerian customers — government:** NCCC, Federal Ministry of Environment (Nigeria Clean Cooking Policy), Energy Commission, Rural Women Energy programme. **Private:** Atmosfair/DARES-linked distributors, Toyola-type firms, LPG marketers, Envirofit, ethanol players (KOKO), developers (C-Quest, BURN entering Nigeria).
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$100–160k, but needs field partnerships.
- **Data reliability:** the sector's whole problem — your product's pitch is that you fix it with rigorous digital MRV.
- **Regulatory considerations:** ICVCM/CCP alignment, Verra/Gold Standard rules, Nigeria's Article-6 authorisation and (eventual) registry, benefit-sharing.
- **Competition:** BURN's own MRV, Nithio, Carbon Trust tools, Fair Climate Fund; not many independent Nigeria-focused MRV providers. Gap: trusted, local, methodology-current MRV.
- **The gap it fills:** "reporting manual / fragmented"; "independent verification"; a live integrity crisis.

### P22 — SahelGuard NG · dryland restoration & desertification MRV

- **Sector:** land-use, forestry, climate adaptation, agriculture, carbon.
- **Problem:** ~70m people across 19 northern states face desertification; the World Bank **ACReSAL** project has ~923,000 ha under restoration (~97% of target) and reports 9.3m beneficiaries ([FMINO](https://fmino.gov.ng/from-degraded-lands-to-resilient-futures-nigerias-acresal-project-delivers-landmark-mid-term-climate-and-livelihood-gains/)); the National Agency for the Great Green Wall and the new SURAGGWA project need credible, low-cost monitoring of what's actually growing.
- **Target users:** NAGGW, ACReSAL PIU, state environment/afforestation agencies, World Bank/AfDB task teams, pastoralist and land-restoration NGOs, restoration carbon developers.
- **How it works:** CHIRPS rainfall (D-09), MODIS/Sentinel-2 NDVI & land cover (D-05/D-01/D-17), WaPOR biomass/ET (D-51), ESA biomass (D-26), Dynamic World (D-18) and soil (D-52) to monitor vegetation recovery, bare-soil reduction, water-point greening and survival of restoration sites against a baseline — with results-based-finance verification outputs.
- **Core features:** restoration-site registry + polygon monitoring; greening/degradation trend maps; RBF milestone verification; early-warning for drought/land-cover loss; soil-carbon and ARR MRV module; public progress dashboard.
- **Open data required:** D-01, D-05, D-09, D-17, D-18, D-26, D-51, D-52.
- **Proprietary data later:** planting records, species, survival counts, soil sampling, community reports.
- **Revenue:** MRV/verification contracts with programmes and their funders; SaaS for agencies; carbon-MRV service; donor M&E contracts.
- **Nigerian customers — government:** NAGGW, ACReSAL, Ministry of Environment, 19 northern state governments, National Park Service. **Private:** restoration NGOs (SISDO-type), carbon developers, agroforestry firms.
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$90–150k.
- **Data reliability:** NDVI/rainfall trends robust at landscape scale; attributing greening to a specific intervention (vs a good rain year) is the methodological crux — control sites and rainfall normalisation required.
- **Regulatory considerations:** low; procurement-driven; benefit-sharing for any carbon.
- **Competition:** UNCCD/FAO Great Green Wall observatory (programme-level), Land Degradation Neutrality tools, academic groups; no productised Nigeria MRV. Gap: independent, continuous, RBF-grade verification.
- **The gap it fills:** "reporting manual"; funders "need independent verification" of restoration spend.

### P20 — GridWatch NG · electricity-supply transparency & outage analytics

- **Sector:** electricity, energy efficiency, green finance.
- **Problem:** grid data is scattered across NERC, NISO, NBET and 11 DisCos; businesses and investors can't get a clean view of supply hours, outages, generation mix or emissions intensity by location.
- **Target users:** C&I energy buyers, solar developers/financiers, researchers, media, DisCos, regulators, DFIs.
- **How it works:** aggregate Ember national generation/mix (D-42), NISO daily generation, GEM plant tracker (D-44), NERC reports (D-48-adjacent), and **VIIRS Black Marble** night-lights (D-07) to detect blackouts and estimate reliability at feeder/area level; publish indices and an API.
- **Core features:** national + state supply dashboards; outage detection & reliability scoring from night-lights; generation-mix & grid-EF tracker; investor/researcher API; business "reliability report" for a given address.
- **Open data required:** D-07, D-42, D-44; NERC/NISO scraping.
- **Proprietary data later:** crowdsourced outage reports, partner meter data.
- **Revenue:** data subscriptions/API; custom reports; embedded reliability scores for lenders/insurers.
- **Nigerian customers — government:** NERC, NISO, Ministry of Power, states, ECN. **Private:** manufacturers, data centres, solar firms, DFIs, media.
- **Development complexity:** low-medium; **MVP effort:** ~3–4 months / ~$60–110k.
- **Data reliability:** night-lights outage detection is proven (used in academic reliability studies) but cloud/moonlight noise needs handling.
- **Regulatory considerations:** low.
- **Competition:** academic (HREA, Nigeria reliability papers), some dashboards; nothing sustained/commercial. Gap: a maintained product.
- **The gap it fills:** fragmented datasets; no independent monitoring layer.

### P26 — BankRisk NG · climate-risk analytics for lenders & pension funds

- **Sector:** green finance, climate risk, ESG.
- **Problem:** the CBN's Nigeria Sustainable Banking Principles and emerging climate-risk expectations require banks to assess portfolio climate exposure; PFAs (pension funds) face similar pressure. None have the tooling.
- **Target users:** banks' risk & sustainability functions, PFAs, DFIs, NGX, the DMO (sovereign green issuance).
- **How it works:** overlay loan-book / collateral locations on physical-hazard layers (flood D-13/D-19, heat, drought D-31, sea-level) and transition-risk signals (Climate TRACE asset emissions D-27, sector exposure, CBAM) to produce portfolio heat-maps, scenario losses (NGFS-style) and disclosure outputs.
- **Core features:** portfolio upload + geocoding; physical & transition risk scoring; scenario analysis; ISSB/TCFD & CBN disclosure packs; borrower-level climate flags for origination.
- **Open data required:** D-13, D-19, D-27, D-31; D-63 for transition pathways.
- **Proprietary data later:** the bank's own exposure data (client-supplied), local damage functions.
- **Revenue:** enterprise SaaS; per-scenario/reporting fees; advisory.
- **Nigerian customers — government/DFI:** CBN (framework), BOI, DBN, NSIA, DMO. **Private:** tier-1/2 banks, PFAs (Stanbic IBTC Pensions, ARM, Leadway Pensure), Africa Re.
- **Development complexity:** medium; **MVP effort:** ~4–6 months / ~$110–170k.
- **Data reliability:** hazard layers fine; damage functions for Nigerian assets are the weak point.
- **Regulatory considerations:** align to CBN and FRC/ISSB; data confidentiality.
- **Competition:** global (Jupiter, riskthinking.AI, S&P/Sustainable1, Munich Re) — costly, not Nigeria-calibrated. Gap: affordable, local, regulator-aligned.
- **The gap it fills:** "investors/lenders need independent verification"; "infrastructure projects need climate-risk assessments".

## 4.2 Lighter-touch concepts (noted, not separately scored)

- **P11 PlastiTrace** — river-plastic interception MRV and plastic-credit verification (Ocean Cleanup model D-54 + Global Plastic Watch D-55 + Sentinel-2). Best pursued as a module of **P10**. Plastic credits (Verra Plastic Program, PCX) — not carbon.
- **P12 EV/fleet emissions** — already the subject of this repository's EV ride-hailing project; SolarLedger's MRV engine is shared infrastructure.
- **P15 CoastNG** — shoreline-change and coastal-risk monitoring (Digital Earth Africa Coastlines D-16 + DEM D-19 + Global Mangrove Watch D-25) for NIMASA, ports, and coastal states; blue-carbon overlaps P14.
- **P16 CoolCity** — urban heat-island and green-cover analytics (Landsat/Sentinel LST D-04 + Open Buildings D-21 + WorldPop D-20 + land cover D-17) for Lagos/Kano/Kaduna planners and World Bank urban programmes.
- **P17 EcoRate** — building energy-performance rating and green-mortgage screening (D-21/D-22 footprints + heights + LST + climate + tariffs) with IFC EDGE and the Nigeria Green Building Council; overlaps P4.
- **P19 NaijaCarbon** — a project registry / pipeline marketplace with satellite MRV overlays, positioned to plug into Nigeria's national carbon registry once the Carbon Market Activation Policy is ratified; higher policy risk (policy "remains inactive … unratified" — [Green Economy Tracker](https://greeneconomytracker.org/country/nigeria)).
- **P21 AquaNG** — surface-water quantity/quality monitoring (JRC water D-15 + Digital Earth Africa WOfS D-16 + Sentinel-2 turbidity/chl-a D-01 + Aqueduct D-31 + boreholes from GRID3/WASH data D-49) for state water boards, UNICEF and bottlers.
- **P23 WildWatch** — protected-area threat monitoring (GFW D-24 + FIRMS D-06 + GBIF D-56 + WDPA D-57, note D-57's commercial restriction) for the National Park Service and conservation NGOs; nascent biodiversity-credit MRV.
- **P24 FreightCarbon** — logistics/Scope-3 emissions calculator (OSM routing D-23 + GLEC factors + Climate TRACE D-27) for exporters and 3PLs; fold into P5.
- **P25 CBAM-only tool** — a narrow, high-willingness-to-pay wedge for cement/fertiliser/aluminium exporters; the beachhead feature of P5.

---

# 5. Green-funding landscape and what it actually requires

## 5.1 The funders (checked September 2026)

| Funder / programme | Type | Typical ticket | Fit for | Notes / status | Source |
|---|---|---|---|---|---|
| **Green Climate Fund (GCF)** | Grants, concessional debt, equity, guarantees; Readiness (≤$1m), Project Preparation Facility (≤$1.5m), Simplified Approval (≤$25m) | $1m readiness → $250m projects | Adaptation (flood, drylands, agri), mitigation (energy), MRV systems | Nigeria accesses via accredited entities. **Development Bank of Nigeria accredited July 2024**; readiness grant approved Nov 2025. NCCC pushing NSIA/NIRSAL/Ministry of Finance to accredit. | [GCF Nigeria](https://www.greenclimate.fund/countries/nigeria), [DBN](https://www.greenclimate.fund/partners/accredited-entities/dbn-nigeria) |
| **Global Environment Facility (GEF-8)** + **GEF Small Grants Programme** | Grants | SGP: ≤$50k to CBOs/NGOs; full-size: $1–10m | Biodiversity, land degradation, chemicals/waste, climate | SGP Nigeria active (UNDP-run); good for pilots with a community partner. | [GEF](https://www.thegef.org/), [SGP Nigeria](https://sgp.undp.org/) |
| **Adaptation Fund** | Grants | ≤$10m (single-country); small grants | Concrete adaptation — flood EW, drylands, water | **Bank of Industry accredited (2025)** as a Nigerian direct-access entity. | [Aluko & Oyebode](https://www.aluko-oyebode.com/insights/national-climate-change-fund-nigeria-2025/) |
| **World Bank — DARES** (Distributed Access through Renewable Energy Scale-up) | Results-based grants + concessional | $750m programme; RBF per connection/site | Mini-grids, SHS, C&I solar, diesel displacement | Live, via REA; Odyssey is the platform of record. Data/analytics vendors can sell into developers and REA. | [ESMAP](https://www.esmap.org/), [Industrial Info](https://www.industrialinfo.com/news/article/nigeria-plans-750-million-mini-solar-grid-strategy--355334) |
| **World Bank — ACReSAL** | IDA credit + grant | $700m programme | Dryland restoration, watershed, climate-smart ag (19 northern states) | Live; needs MRV/M&E vendors. | [FMINO](https://fmino.gov.ng/from-degraded-lands-to-resilient-futures-nigerias-acresal-project-delivers-landmark-mid-term-climate-and-livelihood-gains/) |
| **AfDB — SEFA, Africa Climate Change Fund (ACCF), ClimDev, Desert to Power, Great Green Wall** | Grants (ACCF €250k–1m), concessional, TA | Small grants to large facilities | Energy access, adaptation, drylands, MRV capacity | Nigeria in Desert to Power and GGW. ACCF small grants suit early platform+pilot. | [AfDB GGW](https://www.afdb.org/en/topics-and-sectors/initiatives-and-partnerships/great-green-wall-initiative) |
| **GEAPP (Global Energy Alliance for People and Planet)** | Grants, catalytic capital | $100k–multi-$m | DRE, battery storage, DisCo digitalisation, e-mobility | Active Nigeria portfolio (BESS, DisCo, demand aggregation). | [energyalliance.org](https://www.energyalliance.org/) |
| **All On** | Impact equity/debt (Shell-funded, Nigeria-only) | $100k–$2m | Off-grid & clean energy, productive use, e-mobility | Nigeria-dedicated; knows the market; good early institutional investor for P3/P4. | [allon.com](https://www.all-on.com/) |
| **Catalyst Fund** | Pre-seed equity + venture-building (climate-adaptation Africa) | ~$200k + support | Climate-adaptation fintech/data (insurance, ag, resilience) | Explicitly backs adaptation data/insurance startups — strong fit for P2/P8/P9. | [TechCabal](https://insights.techcabal.com/africas-climatetech-in-2025-funding-trends-startups-scale/) |
| **InsuResilience Solutions Fund / IDF / UNDP IRFF** | Grants + premium support for climate risk insurance | Product-development grants | Parametric/index insurance analytics & delivery | Funded the Lagos parametric flood policy (2025). Direct fit for P2/P9. | [InsuResilience](https://insuresilience-solutions-fund.org/2025/07/17/idf-insurance-team-delivers-tripartite-programme-parametric-flood-insurance-solution-for-lagos-state-government/) |
| **World Bank GGFR / Global Methane Hub / UNEP IMEO / GMP** | Grants, TA, data partnerships | Varies | Methane & flare measurement, MRV, transparency | The hottest theme in climate philanthropy 2024–26. Direct fit for P1. | [GGFR](https://www.worldbank.org/en/programs/gasflaringreduction) |
| **Lacuna Fund (successor institutions: ACTS, DSFSI Pretoria, AI4D)** | Grants for ML-ready datasets | $50k–$400k | Building open datasets (ag, climate, energy, forests) | Leadership moved to African institutions mid-2025. Good for the *dataset* layer under P6/P8/P22. | [Lacuna Fund](https://lacunafund.org/climate/) |
| **FCDO / GIZ / EU Global Gateway / EU DeSIRA** | Grants, TA, blended | Varies | Energy (GIZ NESP), ag-data (DeSIRA), trade/EUDR support | GIZ Nigerian Energy Support Programme is a long-running channel for P3/P4/P20. EU is funding EUDR readiness (P6). | [GIZ Nigeria](https://www.giz.de/en/worldwide/329.html) |
| **Google.org, Bezos Earth Fund, Patrick J. McGovern Foundation, AIM for Scale** | Philanthropic grants | $100k–$5m | AI-for-climate, MRV, forecasting, air quality | Bezos Earth Fund funds AI grand challenges incl. MRV; Google.org funds flood/air. Fit P1/P2/P7/P18. | — |
| **Nigeria Climate Investment Platform / National Climate Change Fund** | Blended domestic vehicle (announced) | TBD | National climate priorities | FG unveiled a Climate Investment Platform targeting ~$500m ([FMF](https://finance.gov.ng/fg-unveils-climate-investment-platform-to-unlock-500m-in-green-finance/)); NCCF established under the Climate Change Act 2021 — capitalisation still thin. | [climatecouncil.gov.ng](https://climatecouncil.gov.ng/) |
| **VC / DFI equity: E3 Capital, Aruwa, All On, Persistent, Equator, EDFI ElectriFI, BII, Norfund, Proparco, Shortlist/Norrsken** | Equity | $250k–$10m+ | Scale-up capital once revenue exists | Climate took ~38% of African startup funding in 2025 (~$1.1bn) — Nigeria a top-2 destination ([TechCabal](https://insights.techcabal.com/africas-climatetech-in-2025-funding-trends-startups-scale/)). | — |
| **Carbon pre-finance / offtake: Frontier, Milkywire, Cloverly, ACMI-linked buyers, Verra/Gold Standard-registered pipelines** | Advance purchase / results-based | Project-scale | Carbon-generating concepts (P1, P6, P18, P22, P14) | Requires registered methodology + verification pathway before money moves. | — |

## 5.2 What every funder will require before they engage

Funding eligibility is **earned, not assumed**. Across the programmes above, a fundable proposition needs, roughly in order:

1. **A defined intervention, not a platform in the abstract.** "We monitor methane" is not fundable; "we will equip NUPRC and 5 operators with an MRV system that identifies X flare sites covering Y% of national flaring, enabling Z tCO₂e/yr of verified reductions over 3 years" is.
2. **A measurable primary KPI with a baseline.** tCO₂e avoided/reduced, hectares restored & verified, people with reduced flood exposure, MWh of diesel displaced, farmers with verified climate-smart adoption. The baseline must be documented from a credible source (often the open data itself).
3. **A recognised reporting standard.** GHG Protocol / ISO 14064 for corporate; IPCC 2006/2019 for inventories; CDM/Verra/Gold Standard methodologies for credits; the funder's own results framework (GCF has 8 result areas; Adaptation Fund has its own).
4. **A monitoring & evaluation plan** with data sources, frequency, responsible party, and independent verification for anything material.
5. **Additionality / non-displacement logic** — evidence the outcome would not have happened anyway, and that you are not just relabelling existing activity.
6. **Safeguards:** environmental & social risk screening, gender action plan, grievance mechanism, data-protection/PII handling, benefit-sharing where communities are involved.
7. **Co-financing or a route to sustainability** — grant funders increasingly want a commercial tail (subscription revenue, government budget line) so the tool outlives the grant.
8. **A pilot with real numbers.** Almost nothing above funds a pre-pilot idea at scale; they fund *expansion of something that worked small*. Budget to self-fund or micro-grant (GEF SGP, ACCF, Catalyst Fund, Lacuna) the first pilot.
9. **The right applicant vehicle.** Many windows flow only through accredited entities or governments — you partner with DBN, BOI, a state agency, a university or an INGO rather than applying directly.
10. **Certifications where relevant:** ISO 14064/14065 for verification bodies; alignment with ICVCM Core Carbon Principles for credits; SBTi for corporate targets you support.

---

# 6. Measuring environmental impact

Preference throughout this study goes to products whose benefit can be **quantified from data the product already holds**. This section maps each metric to a calculation method and the data that feeds it.

## 6.1 Metric → method → data

| Metric | How it is calculated | Data (open unless noted) | Which concepts |
|---|---|---|---|
| **CO₂e avoided — diesel/grid displacement** | `(baseline_fuel_or_grid_kWh × EF_baseline) − (solar_kWh × ~0) − (residual_grid_kWh × EF_grid)`, per site per month; measured generation > modelled | Metered kWh (operator); EF_grid from IGES/CDM (D-65) or Climate TRACE (D-27); diesel EF from IPCC | P4, P3, P20 |
| **CO₂e reduced — flaring/methane** | `Δflare_volume × (EF_CO₂ combustion + GWP₁₀₀ × slip_CH₄)` and `Δvented_CH₄ × 28–30`; baseline = historical detected flare volume | VIIRS Nightfire volume (D-07), S5P/plumes (D-03/D-29), operator metered volume later | P1, P14 |
| **Fuel consumption avoided (litres)** | diesel: `displaced_kWh ÷ genset_efficiency (≈3–3.5 kWh/l)`; petrol (transport): `displaced_vkm × baseline_l/100km` | Metered kWh; vehicle/genset efficiency defaults; GPS distance | P4, P13, P12 |
| **Renewable electricity generated (MWh)** | metered inverter output; or modelled `PVOUT × kWp × PR` pre-install | Global Solar Atlas PVOUT (D-12), NASA POWER (D-11); inverter data later | P3, P4 |
| **Energy saved (MWh)** | `baseline_consumption − actual_consumption`, weather-normalised (IPMVP Option C) | Utility bills, ERA5 degree-days (D-08) | P4, P17 |
| **Forest area protected / deforestation avoided (ha)** | `baseline_loss_rate × area × project_effect`, with control-area comparison; alerts confirm no loss in protected polygons | GFW loss + integrated alerts (D-24), Sentinel-2 (D-01) | P6, P22, P23 |
| **Trees / biomass carbon (tCO₂)** | `Δ above-ground biomass × 0.47 × 44/12` + below-ground + soil where methodology allows | ESA CCI Biomass (D-26), GFW carbon flux (D-24); plots/allometry later | P6, P22, P14 |
| **Waste diverted from landfill (t) & avoided methane** | `Σ logged_tonnage_by_material`; methane: `diverted_organics × DOC × MCF × F × 16/12 × GWP` (IPCC waste model) | In-app weights; What a Waste composition (D-53) | P10 |
| **Plastic recovered (t)** | `Σ verified_collected_plastic`, cross-checked against river-emission baseline | In-app weights; Ocean Cleanup model (D-54) | P10, P11 |
| **Water conserved / saved (m³)** | `baseline_abstraction − actual`; leakage reduction `Δ NRW × supply volume` | Utility SCADA/partner; WaPOR ET (D-51) for ag | P21, P8 |
| **Flood exposure reduced (people, $)** | `Σ (population/assets in hazard zone) × Δ vulnerability` from EW lead-time, drainage or zoning change | WorldPop (D-20), Open Buildings (D-21), GRID3 (D-49), GloFAS/FABDEM (D-13/D-19) | P2, P26 |
| **Air-quality improvement (µg/m³, DALYs)** | modelled Δ concentration from an intervention → `× exposure-response function × population` | ACAG PM2.5 (D-33), CAMS (D-34), S5P (D-03), WorldPop (D-20) | P7, P13, P16 |
| **EV km travelled / fossil km displaced** | telematics distance × (1 − pre-existing EV share) | GPS (operator) | P12, P13 |
| **Methane detected/reduced (t)** | see flaring row; plus point-source plume flux integration | D-07, D-03, D-29, D-30 | P1, P14, P10 (landfill) |
| **Agricultural emissions reduced (tCO₂e)** | `Δ fertiliser N × EF_N₂O × 273` + `Δ paddy/residue burning`; soil C only with sampling | Practice logs; IPCC EFs; FIRMS burning (D-06) | P8, P22 |

## 6.2 From "estimate" to "auditable report"

Every concept should follow the governance pattern already specified in this repo's `emissions-engine-spec.md`: deterministic, versioned factors, append-only records, **measured > modelled**, conservative defaults, uncertainty deduction on any published figure, and a hard separation between the **impact ledger** (for ESG and funding reports) and any **carbon-credit ledger**.

A platform can graduate to producing **auditable environmental-impact reports** — acceptable to a climate-fund analyst, an ISO 14064-3 verifier, an ESG assurer, or a government reporting line — once it has: (a) documented methodology with version control; (b) traceable input data with quality flags; (c) a defined boundary and baseline; (d) uncertainty quantification; (e) an audit trail; and (f) ideally a third-party review of the methodology itself. Products P1, P4, P6, P18 and P22 are explicitly designed to reach this bar; the others can with added rigour.

---

# 7. Carbon-credit potential

**The distinction that matters:** *calculating avoided emissions* (an accounting exercise the platform can do from data) is **not** the same as *generating a verified, tradable carbon credit* (a legal instrument requiring a registered methodology, demonstrated additionality, a conservative baseline, third-party validation & verification, registry issuance, and — in Nigeria, for internationally transferred credits — government authorisation under Article 6 and a corresponding adjustment).

Nigeria's enabling environment is **partly built**: a Carbon Market Activation Policy was launched at COP28 and a draft NCMAP + Manual of Procedures released for review; a national registry has been developed under ACMI and is described as operational since 2024; but the policy "remains inactive … and unratified", and draft ETS/carbon-tax rules are still pending ([Fastmarkets](https://www.fastmarkets.com/insights/nigeria-finalizes-carbon-market-policy-targets-2-5-bln-in-climate-investment-by-2030/), [Green Economy Tracker](https://greeneconomytracker.org/country/nigeria), [Nairametrics](https://nairametrics.com/2024/09/27/nigerias-carbon-market-activation-policy-expected-to-unlock-2-5-billion-by-2030/)). Plan for credits as a **2027+ revenue tail**, not a launch revenue line.

## 7.1 Concept-by-concept carbon assessment

| Concept | Credits realistically possible? | Crediting activity | Additionality | Baseline | MRV — can open data support it? | Candidate standards / methodologies | Extra (non-open) data required |
|---|---|---|---|---|---|---|---|
| **P1 FlareWatch** | **Yes (strong)** — but the platform is the **MRV provider**, not the project owner | Associated-gas recovery / flare & vent elimination at specific facilities | High in Nigeria: flaring persists despite a legal ban and penalties → reductions are generally beyond compliance-as-practised, though "regulatory surplus" tests apply | Historical detected flare volume per site (VIIRS Nightfire multi-year mean) | **Partly** — satellite gives credible baseline & directional monitoring; issuance-grade needs metered gas volumes + composition | CDM **AM0009**, ACM0009-family; Verra flare/vent methodologies; emerging OGMP-linked approaches | Continuous metered flare-gas volume, gas composition, plant records |
| **P4 SolarLedger** | **Yes (moderate)** — best as **programmatic/grouped** small installations | Diesel & grid electricity displacement by solar+storage at C&I/SME sites | Strong: high-cost solar vs entrenched cheap-to-buy diesel; finance barrier real | Metered pre-install diesel/grid consumption; or conservative deemed baseline | **Yes for the electricity side** — metered generation + published grid EF; diesel needs logs | CDM **AMS-I.A / I.F / I.L**, AMS-III.AV; Gold Standard renewable-energy; I-REC alongside | Metered kWh per site, diesel purchase records |
| **P6 TerraProof** | **Yes** — REDD+, ARR, agroforestry (as MRV provider or in JV) | Avoided deforestation / restoration / agroforestry carbon | Context-dependent; REDD+ additionality heavily scrutinised post-2023 | Historical forest loss rate (GFW/Hansen) vs jurisdictional reference level | **Yes for activity data** (loss/gain, area); biomass needs plots | Verra **VM0048/VM0047**, ART-TREES (jurisdictional), Gold Standard A/R | Ground biomass plots, tenure documents, community agreements |
| **P18 CleanCook MRV** | **Yes (very strong sector, high scrutiny)** | Fuel switching / efficient combustion in households | Generally strong (affordability barrier) but usage & stacking must be proven | Baseline fuel & consumption from surveys (DHS/MICS + project survey) | **Context only** — core MRV needs sensors + surveys; open data cross-checks fNRB & forest pressure | Gold Standard **Metered & Measured**; Verra **VMR0006/VM0050**; ICVCM-approved set (Feb 2025) | Stove-use sensors, kitchen surveys, sales & distribution records |
| **P22 SahelGuard** | **Yes (moderate)** — ARR, sustainable land management, soil carbon | Restoration / avoided degradation / SOC increase | Moderate; rainfall-year confounding must be handled with controls | Pre-project NDVI/biomass/land cover + control sites | **Partly** — vegetation trend yes; soil carbon needs sampling | Verra **VM0042** (agricultural land mgmt), **VM0047**, Gold Standard | Soil sampling, planting/survival records |
| **P14 DeltaGuard** | **Yes (niche)** — mangrove blue carbon | Mangrove restoration / avoided conversion | Strong where restoration is clearly funded & additional | Historic mangrove extent/loss (Global Mangrove Watch) | **Partly** — extent & survival by satellite; soil/root carbon needs cores | Verra **VM0033**, VM0007 (REDD+ wetlands) | Sediment cores, planting records, hydrology |
| **P10 LoopNG** | **Yes (moderate)** — landfill methane avoidance / composting; **plus plastic credits (separate market)** | Diversion of organics from unmanaged dumps; recycling | Moderate; informal-sector displacement risk | IPCC first-order decay on baseline disposal; What a Waste composition | **Weak** — needs audited tonnage; satellite only screens dump sites | CDM **AMS-III.F** (composting), **AMS-III.AJ** (recovery/recycling); Verra Plastic Program (for plastic credits) | Weighbridge/audited tonnage, material fate tracking |
| **P13 MoveNG** | **Marginal** — modal shift & e-bus methodologies are hard, thin | Mode shift to mass transit / electrification | Hard to prove; behavioural | Baseline mode share & fleet emissions | **Weak** — fleet-level only; needs telematics + surveys | CDM AM0031 (BRT), TEEMP; mostly used for finance narrative not credits | Ridership counts, fuel logs, O-D surveys |
| **P2 FloodShield / P9 IndexShield / P7 AirView / P26 BankRisk / P5 CarbonLedger** | **No direct credits** | Adaptation / enabling / reporting activities don't generate credits | — | — | — | These attract **adaptation & results-based finance and ESG revenue**, not carbon credits | — |

## 7.2 Practical implication

Only **P1, P4, P6, P18, P22, P14** have a credible credit pathway, and in every case the platform's realistic role is **MRV infrastructure / digital MRV provider** (fee or issuance-linked revenue) rather than carbon-project owner — which is the lower-risk, higher-margin position anyway, and the one that best matches an open-data software company. The credit tail requires physical data (meters, plots, sensors, cores) layered on the open baseline, plus 12–24 months for methodology selection, validation and first verification.

---

# 8. Scoring framework and ranking

## 8.1 Method

Each concept is scored **1–10** on 15 criteria. For four criteria the scale is inverted so that **10 is always better**:

- **Startup capital** — 10 = can reach MVP on <$75k; 1 = needs >$1m.
- **Competitive intensity** — 10 = open field; 1 = crowded with funded incumbents.
- **Regulatory complexity** — 10 = negligible; 1 = licence-gated / politically hazardous.
- (all others: 10 = strongest)

Criteria: **OD** open-data availability · **NEED** Nigerian market need · **MVP** ease of building the MVP · **CAP** low capital required · **REV** revenue potential · **GOV** government demand · **PVT** private-sector demand · **COMP** low competition · **SCALE** pan-African scalability · **IMP** environmental impact · **QNT** ability to quantify impact · **FUND** green-funding attractiveness · **CARB** carbon-credit potential · **REG** low regulatory complexity · **REL** data reliability.

Weighting is **equal** (total out of 150). A weighted view for a "build-first, revenue-soon, funding-later" founder is given in 8.3.

## 8.2 Scores

| # | Concept | OD | NEED | MVP | CAP | REV | GOV | PVT | COMP | SCALE | IMP | QNT | FUND | CARB | REG | REL | **Total** | **%** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | **FlareWatch NG** | 9 | 9 | 7 | 7 | 7 | 9 | 7 | 7 | 8 | 10 | 9 | 10 | 8 | 6 | 8 | **121** | 81% |
| P3 | **SolarSite NG** | 9 | 9 | 7 | 7 | 7 | 8 | 9 | 5 | 9 | 9 | 8 | 9 | 7 | 8 | 8 | **119** | 79% |
| P4 | **SolarLedger NG** | 8 | 10 | 8 | 8 | 8 | 6 | 9 | 6 | 9 | 8 | 8 | 8 | 7 | 8 | 7 | **118** | 79% |
| P6 | **TerraProof NG** | 9 | 9 | 6 | 7 | 8 | 7 | 9 | 5 | 8 | 8 | 8 | 8 | 8 | 6 | 8 | **114** | 76% |
| P2 | **FloodShield NG** | 9 | 10 | 6 | 7 | 7 | 9 | 8 | 6 | 9 | 8 | 7 | 10 | 2 | 7 | 7 | **112** | 75% |
| P14 | **DeltaGuard NG** | 8 | 9 | 6 | 7 | 7 | 8 | 7 | 7 | 6 | 8 | 7 | 9 | 7 | 6 | 7 | **109** | 73% |
| P18 | **CleanCook MRV NG** | 6 | 9 | 5 | 6 | 8 | 7 | 8 | 5 | 9 | 9 | 7 | 9 | 10 | 5 | 6 | **109** | 73% |
| P22 | **SahelGuard NG** | 8 | 8 | 6 | 7 | 6 | 9 | 4 | 7 | 8 | 8 | 7 | 9 | 7 | 6 | 7 | **107** | 71% |
| P13 | **MoveNG** | 6 | 8 | 6 | 7 | 6 | 9 | 5 | 7 | 8 | 7 | 6 | 9 | 6 | 7 | 6 | **103** | 69% |
| P5 | **CarbonLedger NG** | 7 | 8 | 7 | 8 | 8 | 6 | 9 | 5 | 8 | 5 | 6 | 6 | 3 | 7 | 7 | **100** | 67% |
| P8 | **FarmClimate NG** | 8 | 9 | 6 | 6 | 5 | 7 | 7 | 3 | 8 | 7 | 5 | 8 | 5 | 8 | 6 | **98** | 65% |
| P9 | **IndexShield NG** | 8 | 8 | 6 | 7 | 7 | 6 | 8 | 5 | 9 | 6 | 6 | 8 | 2 | 6 | 6 | **98** | 65% |
| P7 | **AirView NG** | 8 | 8 | 6 | 6 | 5 | 8 | 6 | 6 | 8 | 6 | 6 | 8 | 2 | 8 | 6 | **97** | 65% |
| P26 | **BankRisk NG** | 7 | 7 | 6 | 7 | 8 | 6 | 8 | 6 | 8 | 5 | 6 | 7 | 3 | 6 | 7 | **97** | 65% |
| P10 | **LoopNG** | 5 | 8 | 6 | 6 | 7 | 7 | 8 | 4 | 7 | 7 | 6 | 7 | 6 | 6 | 5 | **95** | 63% |
| P20 | **GridWatch NG** | 7 | 7 | 7 | 8 | 6 | 6 | 7 | 6 | 7 | 5 | 5 | 6 | 3 | 8 | 6 | **94** | 63% |

*Scores are the author's assessment, calibrated to the evidence in Sections 2–7. They are meant to rank, not to be precise.*

## 8.3 Weighted "build-first" view

Re-running with weights that favour a bootstrapped founder — MVP ×2, CAP ×2, REV ×1.5, OD ×1.5, FUND ×1.5, COMP ×1.5, everything else ×1 — reorders the top of the table:

1. **P4 SolarLedger NG** — fast MVP, low capital, immediate revenue, reliable data.
2. **P1 FlareWatch NG** — funding and gap outweigh a slightly harder build.
3. **P3 SolarSite NG** — close to P4; overlapping data and customers.
4. **P5 CarbonLedger NG** — cheap to build, clear buyers, weak on impact/carbon.
5. **P2 FloodShield NG** — funding magnet, but slower B2G revenue and no carbon.

---

# 9. Recommendations

## 9.1 Top 10 green-tech products to build in Nigeria on open data

1. **FlareWatch NG** (P1) — gas-flaring & methane intelligence + MRV.
2. **SolarLedger NG** (P4) — SME/C&I clean-energy decisions + diesel-displacement MRV.
3. **SolarSite NG** (P3) — distributed-energy siting & project preparation.
4. **TerraProof NG** (P6) — deforestation / EUDR traceability + forest-carbon MRV.
5. **FloodShield NG** (P2) — asset-level flood-risk analytics & early warning.
6. **CleanCook MRV NG** (P18) — digital MRV for clean-cooking carbon.
7. **DeltaGuard NG** (P14) — Niger Delta monitoring + remediation / blue-carbon MRV.
8. **SahelGuard NG** (P22) — dryland restoration & desertification MRV.
9. **CarbonLedger NG** (P5) — GHG accounting, ISSB reporting & CBAM intelligence.
10. **MoveNG** (P13) — paratransit planning & transport-emissions platform.

## 9.2 Top 5 easiest to build

1. **SolarLedger NG** (P4) — bill parser + solar model + report generator; MRV reuses this repo's engine spec.
2. **CarbonLedger NG** (P5) — factor library + calculators + report templates; little geospatial work.
3. **GridWatch NG** (P20) — API aggregation + night-lights outage detection.
4. **SolarSite NG** (P3) — well-documented raster/tabular datasets and established siting models.
5. **AirView NG** (P7, dashboard tier) — CAMS + ACAG + S5P tiles; hardest part (ground calibration) deferred.

## 9.3 Top 5 strongest commercial opportunities

1. **SolarLedger NG** (P4) — thousands of SMEs + every solar lender; pain is acute and current.
2. **CarbonLedger NG / CBAM** (P5) — regulatory deadlines (ISSB 2027+, CBAM now) force purchase.
3. **FlareWatch NG** (P1) — small buyer set but very high willingness to pay; MRV fees compound.
4. **TerraProof NG** (P6) — EUDR is a hard trade gate for cocoa exporters.
5. **FloodShield NG** (P2) — insurers and lenders will pay for asset-level risk once parametric markets scale.

## 9.4 Top 5 strongest government / B2G opportunities

1. **FloodShield NG** (P2) — SEMAs, NEMA, NIHSA; recurring annual crisis.
2. **FlareWatch NG** (P1) — NUPRC, NOSDRA, NCCC; enforcement and Article-6 reporting.
3. **SahelGuard NG** (P22) — NAGGW, ACReSAL, 19 northern states; donor-funded M&E budgets.
4. **DeltaGuard NG** (P14) — NOSDRA, HYPREP, NDDC, oil-producing states.
5. **MoveNG** (P13) — LAMATA and state transport authorities financing BRT/e-bus.

## 9.5 Top 5 strongest climate-funding opportunities

1. **FlareWatch NG** (P1) — methane is the top global climate-finance theme; GGFR/IMEO/Global Methane Hub/philanthropy.
2. **FloodShield NG** (P2) — GCF/Adaptation Fund/InsuResilience adaptation pools; largest single bucket.
3. **CleanCook MRV NG** (P18) — results-based finance + carbon pre-finance; integrity crisis = demand for better MRV.
4. **SahelGuard NG** (P22) — ACReSAL/GGW/GCF land-restoration finance needs verification vendors.
5. **SolarLedger NG** (P4) — DARES RBF, GEAPP, All On, AfDB SEFA, GCF energy-access.

## 9.6 Top 5 strongest carbon / MRV opportunities

1. **CleanCook MRV NG** (P18) — largest African credit segment, acute MRV-trust gap.
2. **FlareWatch NG** (P1) — high-volume, high-additionality flare/vent reductions; satellite-supported baseline.
3. **TerraProof NG** (P6) — REDD+/ARR/agroforestry MRV, doubles as EUDR compliance.
4. **DeltaGuard NG** (P14) — mangrove blue carbon in the Niger Delta.
5. **SahelGuard NG** (P22) — dryland ARR and soil-carbon MRV.

## 9.7 Top 3 overall

**① FlareWatch NG · ② SolarLedger NG · ③ FloodShield NG.**

Rationale: FlareWatch tops the unweighted score and owns the best *funding + gap + carbon* story; SolarLedger tops the *build-first* weighting with the fastest revenue and lowest risk and shares its MRV core with FlareWatch; FloodShield is the largest *adaptation-finance and B2G* opportunity against Nigeria's most visible, most recurrent climate harm. Together they span three sectors and three distinct funding pools, so a founder can pick by appetite (funding-ceiling vs speed-to-revenue vs public-mission).

---

# 9A. Deep dive — ① FlareWatch NG

**Product concept.** An independent, continuously updated intelligence and MRV platform that tells you — for every gas flare and oil-&-gas facility in Nigeria — how much is being flared and (increasingly) vented, trending which way, worth how much in wasted gas and in potential carbon credits, and how it compares to what the operator reports. Built on free satellite and public regulator data, sold to regulators, operators, financiers and carbon developers, and designed from day one to become verification-grade MRV infrastructure.

**Proposed product name.** *FlareWatch NG* (platform) with a *MethaneLedger* MRV module. Neutral, descriptive, hard to confuse with an advocacy campaign.

**Problem statement.** Nigeria remains a top-10 global gas flarer. NUPRC data shows ~204 bcf flared in 2025 (~17 Mt CO₂; ~$1.1bn of gas wasted; enough for ~32,000 GWh of power), and Q1-2026 flaring of ~47 bcf ([Guardian](https://guardian.ng/energy/feasibility-of-achieving-nigerias-zero-gas-flaring-target/), [allAfrica/NUPRC](https://allafrica.com/stories/202609100082.html)). Methane from venting and leaks across the same infrastructure is barely measured at all. Five different data sources touch this problem — VIIRS Nightfire, TROPOMI, Carbon Mapper, the World Bank's flaring estimates, Nigeria's own Gas Flare Tracker — and **none is fused into a decision tool**. The NOSDRA–SDN methane-tracker prototype completed phase 1 and is "looking … to mobilise resources … for phase two" ([Vanguard](https://www.vanguardngr.com/2024/09/nosdra-sdn-to-track-methane-in-ogoniland-using-satellites/)). Regulators can't prioritise enforcement, operators can't benchmark, banks can't do due diligence, and carbon developers can't screen sites — for want of software, not data.

**Unique value proposition.** *"Every flare in Nigeria, measured monthly, from public data — with the numbers regulators, lenders and carbon buyers can act on."* The only Nigeria-specific, independent, analytics-plus-MRV layer over methane and flaring.

**Primary customers.**
- **Anchor (B2G):** NUPRC (flare enforcement, NGFCP, national reporting), NOSDRA (methane mandate), NCCC (national inventory, Article-6 pipeline), Federal Ministry of Environment, NEITI.
- **Enterprise (private):** upstream operators — Renaissance Africa Energy, Seplat Energy, NNPC E&P, Oando, Aiteo, First E&P, Conoil — for OGMP 2.0 reporting, internal MRV and benchmarking; gas-processing and midstream firms.
- **Financial:** banks and DFIs with oil-&-gas or gas-to-power exposure (Access, Zenith, UBA, Stanbic IBTC, AfDB, Afreximbank); ESG-rating and assurance firms.
- **Carbon:** flare-reduction / associated-gas project developers and buyers.
- **Accountability:** journalists, host-community trusts, litigation firms, research institutes (NRGI, SDN).

**User journey (regulator analyst).** Logs in → national dashboard: total flaring this month, top-20 sites, biggest month-on-month changes, estimated penalties owed → clicks a Delta site → 5-year flare-volume time series (VIIRS), overlaid TROPOMI methane enhancement, ownership, distance to nearest gas-gathering infrastructure, estimated CO₂e and gas value, operator's self-reported figure vs satellite estimate → generates a "site enforcement brief" PDF → sets an alert for any month where detected flaring rises >20%. Quarterly, exports the national roll-up for the UNFCCC inventory and the Global Methane Pledge tracking.

**Platform architecture.**
- **Ingestion workers** (scheduled): VIIRS Nightfire nightly files (D-07); Sentinel-5P CH₄/NO₂ via Copernicus/GEE (D-03); Carbon Mapper API (D-29); UNEP IMEO MARS (D-30); Climate TRACE oil-&-gas asset bulk + API (D-27); World Bank/Payne flaring dataset (D-45); Gas Flare Tracker scrape (D-46); NUPRC report parser (D-48).
- **Entity-resolution service:** clusters detections into a persistent **facility/flare register** (stable IDs), links ownership, OML/OPL block, and infrastructure context from Global Energy Monitor (D-44) and OSM (D-23).
- **Estimation engine** (deterministic, versioned — per the repo's emissions-engine principles): monthly flared volume, radiant heat, temperature; methane slip; vented-methane indicator from TROPOMI anomalies; CO₂e (versioned GWP set); gas energy and $ value; penalty exposure under the Nigerian flare-payment regime.
- **MethaneLedger MRV module:** ingests operator-supplied metered volumes + gas composition; reconciles against satellite; produces methodology-aligned reduction quantification with uncertainty; append-only records.
- **API + web app** (map, register, time series, alerts, report builder); **exports** (inventory schema, OGMP 2.0, CSV).
- **Governance:** methodology registry, "estimated vs verified" flags, right-of-reply workflow, audit log.

**Required datasets / APIs.** D-03, D-07, D-23, D-27, D-29, D-30, D-44, D-45, D-46, D-48 (all free / Tier A–B). Compute: Google Earth Engine or Copernicus openEO free tier + a modest cloud VM.

**Example data architecture.**
`raw_detections` (source, timestamp, lat/lon, RHI, temp, source-volume) → `facilities` (facility_id, name, operator, block, geom, first_seen) → `detection_facility_link` (detection_id, facility_id, confidence) → `monthly_facility_estimates` (facility_id, month, flare_vol_scf, ch4_t, co2e_t, gas_value_usd, penalty_usd, method_version, uncertainty) → `operator_reports` (operator, month, reported_vol, source_doc) → `mrv_records` (append-only: facility_id, period, measured_vol, composition, reduction_tco2e, data_quality, verifier_status). All estimates carry `method_version` and `input_data_hash` for reproducibility.

**MVP features (months 0–6).** National + state flaring dashboard; facility register (~200–400 Niger Delta sites) with 5-year VIIRS time series; monthly CO₂e + gas-value + penalty estimates; operator benchmarking; change alerts; PDF site briefs; CSV/API. Methane shown as a TROPOMI-derived *enhancement indicator*, clearly labelled non-facility-exact.

**Advanced features (months 6–18).** MethaneLedger MRV module with operator data reconciliation; Carbon Mapper / IMEO plume integration and super-emitter case files; carbon-project screening (baseline, additionality checklist, indicative credit volume, methodology mapping); OGMP 2.0 report generation; predictive flare-out scenario modelling; a public transparency layer (throttled, with right-of-reply).

**AI/ML opportunities.** Detection de-noising and flare-vs-fire classification; gap-filling flare volumes through cloud/no-pass nights; downscaling TROPOMI with NO₂ + wind (D-08) to sharpen hotspot attribution; anomaly detection for new/step-change flares; NLP extraction from NUPRC/operator PDFs; a plume-flux estimator from Sentinel-2/Landsat SWIR for large events.

**GIS / satellite-data opportunities.** The whole product is EO. Additional layers: Sentinel-2 SWIR methane retrieval for big plumes; night-time NO₂ and CO co-location; pairing flare locations with GRID3 settlements (D-49) and health facilities for an environmental-health overlay; mangrove/vegetation stress (D-25) near chronic flares.

**Reporting dashboard.** Three tenant types — **Regulator** (national roll-up, enforcement queue, inventory export), **Operator** (own assets, benchmark vs peers, OGMP export, reduction tracker), **Financier/Developer** (portfolio screening, due-diligence packs, carbon-project pipeline). Every figure links to method version and source detections.

**Environmental-impact calculation methodology.** Baseline = trailing 24–36-month mean detected flare volume per facility (VIIRS), conservatively adjusted. Reduction in a period = `(baseline_vol − observed_vol) × [EF_CO₂,combustion + GWP₁₀₀ × methane_slip_fraction]` for flaring, plus `Δ vented_CH₄ × GWP₁₀₀` where operator or plume data supports it. Apply an uncertainty deduction (start 20–30%, fall as metered data is added). Report **estimated avoided emissions** in the impact ledger; only the MethaneLedger module, with operator metering + third-party verification, feeds a **credit ledger**. Auditable to ISO 14064-3 once methodology is externally reviewed.

**Business model.** SaaS: Regulator licence ($40–120k/yr, often grant-underwritten initially), Operator enterprise ($25–75k/yr), Financier/Analyst ($8–20k/yr seat). Commissioned reports ($5–30k). MethaneLedger MRV: setup + per-verification fee or 3–8% of credit value. API metered. Target: 2–3 anchor contracts + 5–8 enterprise in 18 months → ~$0.6–1.2m ARR.

**Pricing possibilities.** Free public tier (national totals, top-20, quarterly) for credibility and press; paid tiers for site-level history, alerts, exports, API; MRV priced on issuance.

**Go-to-market.** (1) Publish a free quarterly "Nigeria Flaring & Methane Monitor" report — earns media and inbound. (2) Co-develop the methodology with NOSDRA/SDN (extend their prototype rather than compete). (3) Land one operator doing OGMP 2.0 as a lighthouse. (4) Partner with a DFI or NRGI for the due-diligence use case. (5) Convert regulator pilots via a donor-funded deployment (GGFR/IMEO).

**Partnership opportunities.** NOSDRA + Stakeholder Democracy Network (methane prototype); NRGI (governance framing); Payne Institute / Colorado School of Mines (VIIRS Nightfire science); UNEP IMEO; World Bank GGFR; a Nigerian university (UNILAG/UNIPORT) for validation; an accredited entity (DBN) for GCF-adjacent funding.

**Government agencies to approach.** NUPRC, NOSDRA, NCCC, Federal Ministry of Environment, NEITI, Ministry of Petroleum (gas), Nigerian Extractive Industries bodies, oil-producing-state environment ministries.

**Private companies to approach.** Renaissance Africa Energy, Seplat, Oando, Aiteo, First E&P, NNPC E&P, Conoil, gas-processing firms; Access/Zenith/Stanbic sustainability & risk desks; carbon developers active in Nigeria.

**Development organisations to approach.** World Bank GGFR & ESMAP; UNEP IMEO; Global Methane Hub; AfDB; GIZ; Bezos Earth Fund (AI-for-MRV); Clean Air Task Force; Environmental Defense Fund (MethaneSAT/MARS ecosystem).

**Green funding opportunities.** GGFR grants / TA; Global Methane Hub; IMEO data partnerships; Bezos Earth Fund and Google.org AI-for-climate; GCF readiness (via DBN/NCCC) for a national MRV system; AfDB ACCF small grant for the pilot; philanthropic climate-transparency funders. The pitch writes itself against Section 5.2: defined intervention (national flare/methane MRV), primary KPI (tCO₂e of verified reductions enabled; % of national flaring under monitoring), credible baseline (public satellite record), reporting standard (IPCC + OGMP 2.0), sustainability tail (regulator + operator subscriptions).

**Carbon-finance potential.** Strong but as MRV provider: flare-reduction / associated-gas-recovery projects under CDM AM0009 / ACM-family or Verra equivalents; the platform supplies baseline and monitoring, earns fee or issuance share. Requires operator metering + validation; 12–24 months to first issuance. Also positions for Article-6 authorised transfers once Nigeria's registry and NCMAP are ratified.

**Regulatory requirements.** No licence to operate the platform. But: rigorous, published, versioned methodology; explicit uncertainty; a documented right-of-reply before naming operators; data-use terms for the Gas Flare Tracker and NUPRC data; care that "estimated" figures are never presented as official. If offering formal MRV for credits, the verification itself must be done by an accredited third party (ISO 14065) — partner, don't self-verify.

**Major risks.**
- *Political/legal:* naming operators invites pushback or pressure on government clients. Mitigate with method transparency, right-of-reply, DFI/academic cover.
- *Attribution accuracy:* TROPOMI can't pin methane to a single facility; over-claiming destroys credibility. Mitigate with conservative labelling and plume-data corroboration.
- *Buyer concentration:* a dozen serious operators + a few agencies. Mitigate with the financier/developer segment and pan-African expansion (Libya, Algeria, Iraq analogues).
- *Data continuity:* dependence on VIIRS/TROPOMI mission continuity (both funded through the decade; Sentinel-5 follow-on planned) and on the Gas Flare Tracker staying up.
- *Policy drift:* Nigeria's carbon-market and Article-6 timelines keep slipping — don't bank the credit revenue early.
- *Grant dependence:* regulator budgets are thin; without a donor bridge the anchor revenue is slow.

**12-month implementation roadmap.**
- **M0–1:** legal entity; secure GEE/Copernicus access; sign method-collaboration MoU with NOSDRA/SDN or a university; scope facility register for the Niger Delta.
- **M1–3:** build ingestion for VIIRS Nightfire + Gas Flare Tracker + Climate TRACE; entity resolution; first facility register (~250 sites) with historical time series.
- **M3–5:** estimation engine (volume → CO₂e → $ → penalty); web app v1 (map, register, time series, alerts); publish the first free quarterly Monitor.
- **M5–7:** add TROPOMI methane-enhancement layer; operator benchmarking; PDF briefs; API. Start 2 regulator + 2 operator pilots.
- **M7–9:** MethaneLedger MRV module v1 (operator data intake + reconciliation); carbon-project screening; OGMP 2.0 export.
- **M9–12:** convert 1–2 anchor contracts; submit a GGFR/IMEO or Bezos Earth Fund grant with pilot numbers; external methodology review; plan Cameroon/Angola/Libya expansion.

**Estimated MVP development effort.** ~4–6 months, 3–4 people (1 geospatial/data engineer, 1 backend, 1 full-stack, 0.5 domain analyst), ~$120–200k including cloud and a methodology review. The free quarterly report can ship at ~M3 for early credibility.

---

# 9B. Deep dive — ② SolarLedger NG

**Product concept.** A web platform that helps a Nigerian business decide whether to go solar, model the payback honestly under fuel/FX scenarios, get financed, and then — once the system is running — produce an auditable monthly report of the energy saved, diesel displaced and CO₂e avoided. The same engine aggregates many small sites into a portfolio view for the bank or fund that financed them, and into a programmatic carbon project.

**Proposed product name.** *SolarLedger NG* (a.k.a. *WattWise*). "Ledger" signals the MRV/proof angle that differentiates it from yet another solar calculator.

**Problem statement.** Since the 2023 petrol-subsidy removal and the naira devaluation, diesel sits around ₦1,300–1,500/l and Nigerian firms spend an estimated **$14bn+/year** on self-generation. Solar-plus-storage is now often cheaper over its life, and there is real capital to fund it — the **$750m DARES** programme alone targets displacing 250,000+ diesel gensets ([Industrial Info](https://www.industrialinfo.com/news/article/nigeria-plans-750-million-mini-solar-grid-strategy--355334)). Yet an SME owner can't size a system, can't tell an honest payback from an installer's optimistic one, can't easily get a loan (lenders lack a standard way to appraise the saving), and after installation has no independent record of the benefit for a parent company, a lender covenant, an ESG report or a future carbon credit. Existing tools are either engineering software priced for Western EPCs or an installer's sales spreadsheet.

**Unique value proposition.** *"Know your solar payback before you sign — and prove your savings every month after."* The decision tool and the proof tool in one, localised to Nigerian tariffs, fuel prices, FX and the grid emission factor, and priced for SMEs and their lenders.

**Primary customers.**
- **SMEs / mid-caps:** agro-processors, light manufacturing (MAN members), hospitals and clinics, private schools and universities, hotels, cold stores, filling stations, telecom-tower hosts, farms.
- **Solar EPCs / developers:** as a branded sales and proposal tool (Daystar, Rensource, Havenhill, Arnergy's channel, hundreds of smaller installers).
- **Financiers:** Bank of Industry, Development Bank of Nigeria, Sterling, Access, Zenith solar-lending desks; leasing companies; funds (All On, GEAPP, AfDB SEFA, Acumen, EDFI ElectriFI).
- **Corporates:** multinationals tracking Scope 1/2 across Nigerian sites; franchise networks.

**User journey (SME owner).** Enters address and business type → uploads 12 months of NEPA/DisCo bills and a diesel logbook photo → the tool geolocates, pulls solar resource, tariff and grid-reliability data, and returns: recommended system size, indicative price range, monthly and lifetime savings, payback (base / high-fuel / weak-naira scenarios), diesel litres and tCO₂e avoided per year → owner clicks "get quotes" → 2–3 vetted installers respond → owner picks one, and optionally a financing offer pre-filled with the modelled cashflow → after install, owner (or a ₦5k data logger, or the inverter API) submits monthly generation and grid/diesel use → tool issues a **verified savings & emissions statement** each month, shareable with the lender or head office.

**Platform architecture.**
- **Resource & context service:** Global Solar Atlas API + bulk PVOUT layer (D-12); NASA POWER daily (D-11); DisCo tariff table (maintained from NERC orders); grid emission factor (D-65, refreshed against Ember D-42 and Climate TRACE D-27); grid-reliability index from VIIRS Black Marble (D-07); roof-area estimate from Google Open Buildings footprint (D-21).
- **Bill & fuel ingestion:** OCR + parser for DisCo bills and diesel receipts/logs; manual entry fallback; inverter API connectors (Sungrow, Deye, Victron, SMA, Huawei) and a cheap LoRa/GSM meter option.
- **Modelling engine:** load reconstruction from bills; PV+storage sizing; 8760-hour simulation; financial model (capex bands, tenor, rate, FX path, fuel path, degradation); scenario outputs.
- **MRV engine:** deterministic, versioned, append-only (this repo's `emissions-engine-spec.md` applied to stationary energy): `avoided = (baseline_diesel_kWh × EF_diesel + baseline_grid_kWh × EF_grid) − (residual_grid_kWh × EF_grid)`, measured generation preferred, uncertainty deduction on published figures.
- **Marketplace & finance layer:** installer directory + quote routing; lender portal with portfolio dashboard; document generator.
- **API** for EPCs and lenders to embed.

**Required datasets / APIs.** D-07, D-11, D-12, D-21, D-27, D-42, D-65; NERC tariff orders (public PDFs); optional D-41 for context. All free.

**Example data architecture.**
`sites` (site_id, geom, disco, tariff_band, business_type, roof_area_m2) → `resource_cache` (site_id, month, ghi, pvout, temp) → `energy_history` (site_id, month, grid_kwh, grid_naira, diesel_litres, diesel_naira, source, quality_flag) → `system_designs` (site_id, kwp, kwh_batt, capex_low/high, sim_yield) → `finance_scenarios` (design_id, tenor, rate, fx_path, fuel_path, payback_months, npv) → `mrv_monthly` (append-only: site_id, month, gen_kwh, grid_kwh, diesel_litres, energy_saved_kwh, tco2e_avoided, method_version, data_quality) → `portfolios` (lender_id, [site_id], aggregate metrics).

**MVP features (months 0–4).** Address + bill upload → system sizing + payback with 3 scenarios → PDF proposal with diesel litres and tCO₂e avoided → "request quotes" form → simple installer directory. Grid EF and tariffs hard-loaded and versioned.

**Advanced features (months 4–12+).** Inverter-API and meter integration; automated monthly verified statements; lender portfolio dashboard and covenant monitoring; IPMVP-style weather normalisation; carbon-programme aggregation module (group many sites under one Gold Standard / AMS-I.F project); Scope 1/2 multi-site console for corporates; "green asset tag" for resale/refinance.

**AI/ML opportunities.** Load-profile reconstruction from sparse bills; bill/receipt OCR and anomaly detection; payback-risk scoring for lenders (default prediction from site + sector + cashflow); anomaly detection on monthly generation (underperformance, soiling, theft); NLP to keep the tariff/rule library current from regulator publications.

**GIS / satellite-data opportunities.** Roof-area and orientation from Open Buildings 2.5D (D-21); shading from Copernicus DEM (D-19); grid-reliability mapping from night-lights (D-07) to target the worst-served clusters; siting for ground-mount from land cover (D-17); heat-stress context for battery derating from LST (D-04).

**Reporting dashboard.** **SME view:** this month's saving (₦ and kWh), diesel avoided, tCO₂e, payback progress bar, system health. **Installer view:** pipeline, proposal conversion, fleet performance. **Lender view:** portfolio of financed sites, aggregate saving vs projection, arrears risk flags, aggregate tCO₂e for the bank's own green-portfolio reporting. **Corporate view:** all Nigerian sites, Scope 1/2 trend, target tracking.

**Environmental-impact calculation methodology.** Baseline: measured pre-install grid + diesel consumption over ≥6 months (preferred), or a conservative deemed baseline from bills. Monthly avoided emissions as above, with EF_grid from D-65 (Nigeria operating-margin grid factor, ~0.4–0.5 tCO₂/MWh range — verify current value) and EF_diesel from IPCC (~2.68 kgCO₂/l plus upstream). Energy saved reported per IPMVP Option C with ERA5 degree-day normalisation (D-08). Uncertainty deduction 10–20%. Impact ledger vs credit ledger kept separate.

**Business model.** Freemium calculator (lead magnet) → **SME subscription** ₦15–40k/mo for monitoring + verified statements → **Installer tier** ₦150–400k/mo (branded proposals, unlimited runs, leads) → **Lender tier** $6–20k/yr per portfolio + small per-loan fee → **carbon aggregation** 10–20% of credit value on pooled projects → installer lead-gen fees (₦20–60k per closed referral). Path to ~$400–800k ARR in 18–24 months on a few hundred SME seats + 30–60 installers + 3–6 lenders.

**Pricing possibilities.** Keep the single-site payback estimate free forever (growth engine); charge for monitoring, multi-scenario/finance packs, portfolio tools, API, and MRV.

**Go-to-market.** (1) Free calculator seeded through MAN, NACCIMA, hospital and school associations, and solar-Twitter. (2) Sign 10–20 EPCs as the branded proposal tool — they bring the volume. (3) One bank pilot (BOI or DBN or Sterling) to co-design the lender portfolio view. (4) A state or hospital-group solar rollout as a lighthouse. (5) Content: a public "Nigeria Diesel-to-Solar Payback Index" updated monthly with fuel/FX.

**Partnership opportunities.** Solar EPCs (channel); BOI/DBN/Sterling/GEAPP (finance); REA (SHS/C&I windows, DARES data); Odyssey (complementary — they do developer ops, you do site decision + MRV); inverter OEMs; MAN and NACCIMA; a verification body for the carbon tail.

**Government agencies to approach.** Bank of Industry, Development Bank of Nigeria, Rural Electrification Agency, Energy Commission of Nigeria, Nigerian Investment Promotion Commission, state ministries of energy/environment, public hospital and university managements.

**Private companies to approach.** Daystar Power, Rensource, Havenhill Synergy, Arnergy, PowerGen, Sabon Gari-type industrial clusters, hospital groups (Reddington, Lagoon), school groups, QSR chains (Chicken Republic), tower companies (IHS Towers, ATC), cold-chain operators.

**Development organisations to approach.** GEAPP, All On, AfDB SEFA, World Bank/ESMAP DARES team, GIZ NESP, EDFI ElectriFI, Acumen, Shell Foundation, Catalyst Fund, USADF-successor energy windows.

**Green funding opportunities.** DARES results-based finance (via developer/lender partners); GEAPP catalytic grants; All On (Nigeria-only, energy-access equity/debt); AfDB SEFA; GCF energy-access (via DBN accreditation); GIZ NESP TA; carbon pre-finance once the aggregation project is designed. The Section-5.2 checklist: defined intervention (X MWp financed and monitored, Y gensets displaced), KPI (MWh diesel displaced, tCO₂e avoided, $ saved), baseline (metered pre-install), standard (IPMVP + GHG Protocol + AMS-I.F for credits), sustainability tail (subscriptions).

**Carbon-finance potential.** Moderate and real: pool many verified small installations into a **programmatic** CDM AMS-I.F / AMS-I.L or Gold Standard project; the platform is the digital MRV backbone and aggregator, taking a share of issuance. Diesel displacement gives strong additionality in Nigeria. Needs metered kWh per site and diesel records; ~12–18 months to first issuance after reaching a few hundred monitored sites.

**Regulatory requirements.** None to launch. Payments/lead-gen may trigger light fintech/agency considerations. Public "avoided emissions" claims must follow the impact-vs-credit separation. Carbon aggregation needs registry accounts and third-party verification (partner).

**Major risks.**
- *Installer channel conflict:* EPCs may resist an "honest payback" tool. Mitigate by making it their branded tool and lead source.
- *Data quality on baselines:* many SMEs have poor records. Mitigate with conservative deemed baselines and data-quality flags.
- *FX / fuel reversal:* a fuel-price crash weakens the pitch. Mitigate with scenario framing and the ESG/MRV value that persists regardless.
- *Commoditisation:* calculators are easy to copy. Moat is the MRV data, the lender relationships, and the installer network — build those fast.
- *Grid-EF and tariff churn:* Nigeria revises tariffs frequently; keep the rule library versioned and current.

**12-month implementation roadmap.**
- **M0–1:** entity; datasets wired (GSA, NASA POWER, night-lights, grid EF); tariff library v1 from NERC orders.
- **M1–3:** bill parser + load reconstruction + PV/storage sizing + financial model; free single-site calculator live.
- **M3–4:** PDF proposal with impact metrics; installer directory + quote routing; onboard first 5 EPCs.
- **M4–6:** MRV engine v1 (manual monthly input → verified statement); first bank pilot scoping; "Payback Index" content launch.
- **M6–9:** inverter-API + cheap-meter integration; lender portfolio dashboard; 20+ installers, first paying SME cohort.
- **M9–12:** carbon-aggregation module design + verification-partner MoU; corporate multi-site console; grant submission (GEAPP/All On/AfDB) with pilot data; ~$150–300k ARR run-rate target.

**Estimated MVP development effort.** ~2–4 months to the free calculator + PDF proposal (2–3 people: 1 full-stack, 1 data/modelling, 0.5 design), ~$50–110k. MRV engine adds ~1.5–2 months and reuses the existing emissions-engine spec. Marketplace/finance layer another ~2 months.

---

# 9C. Deep dive — ③ FloodShield NG

**Product concept.** An asset-level flood-risk and early-warning platform for Nigeria: given any address, polygon or portfolio of assets, it returns the flood hazard (return-period depths), a 1–7-day forecast alert where relevant, and an estimate of people/assets/value exposed — turning NIHSA's annual PDF outlook and a stack of global models into something a state agency, a bank, an insurer or a factory manager can actually query and act on.

**Proposed product name.** *FloodShield NG* (platform), with a *TriggerDesk* module for parametric-insurance structuring and monitoring.

**Problem statement.** Flooding is Nigeria's most damaging recurrent climate hazard. 2024: **9m+ people affected across 31 of 36 states**; the Alau Dam collapse submerged ~50% of Maiduguri and displaced ~389,000 people; 5m people pushed into acute food insecurity in the north-east ([OCHA](https://www.unocha.org/publications/report/nigeria/nigeria-floods-situation-report-no-1-25-september-2024), [ReliefWeb](https://reliefweb.int/report/nigeria/nigeria-joint-post-flood-situation-report-borno-state-31-december-2024)). NIHSA's 2026 Annual Flood Outlook lists **1,249 communities in 266 LGAs at high risk** ([Nigeria Housing Market](https://www.nigeriahousingmarket.com/news/nigeria-2026-flood-outlook-33-states-risk)). Yet the outlook is a document, not a service; Google Flood Hub gives free riverine forecasts but no asset-level risk or loss estimate; global catastrophe models (Fathom, JBA) are expensive and not tuned to Nigerian exposure. States improvise evacuation, insurers can't price cover, lenders can't see collateral risk, and every infrastructure project re-commissions a one-off study.

**Unique value proposition.** *"From the national flood outlook to your building's risk score — and the loss estimate a lender or insurer will accept."* Nigeria-calibrated, asset-level, affordable, and integrated into the workflows that actually make decisions (loan origination, insurance triggers, evacuation planning).

**Primary customers.**
- **Government (anchor):** State Emergency Management Agencies (Lagos, Bayelsa, Kogi, Anambra, Adamawa, Borno, Niger, Delta, Jigawa), NEMA, NIHSA (delivery partner), state works/urban-planning ministries, the Ecological Fund Office.
- **Insurance:** NAICOM-regulated insurers and MGAs pricing/parametric cover (the Lagos parametric flood policy went live in 2025 protecting up to 4m people — [AXA Climate](https://climate.axa/publications/parametric-insurance-flood-nigeria-lagos/)); reinsurers (Africa Re, Continental Re); brokers.
- **Finance:** banks (mortgage, SME, agri-loan collateral screening), DFIs, microfinance.
- **Corporates / infrastructure:** manufacturers and bottlers with riverside plants, telecom tower cos, logistics, real-estate developers, road/rail project owners.
- **Humanitarian:** anticipatory-action programmes (WFP, Red Cross, Start Network, UN OCHA).

**User journey (bank credit officer).** Uploads a CSV of 4,000 loan collateral addresses → within minutes gets each geocoded and scored (hazard band, modelled 1-in-100 depth, exposure value at risk) → a portfolio heat-map shows ₦X bn of collateral in high-hazard zones, concentrated in 3 LGAs → officer sets a rule flagging new applications above a hazard threshold for extra review → during the rainy season, receives alerts when a GloFAS-driven forecast puts flagged branches/assets in a 3-day risk window → exports a climate-risk annex for the bank's ISSB/CBN disclosure.

**Platform architecture.**
- **Hazard build (offline, periodic):** FABDEM (D-19) + HAND / simplified hydraulic modelling for pluvial and fluvial hazard; calibrated and validated against the historical Sentinel-1 flood-extent archive (D-02), Copernicus EMS activations (D-14) and Digital Earth Africa WOfS (D-16); river context from HydroSHEDS (D-32). Output: national hazard grid with return-period depths.
- **Forecast service (daily):** GloFAS discharge (D-13) for the Niger–Benue system and major tributaries; CHIRPS/IMERG rainfall (D-09/D-10) and ERA5 (D-08) for pluvial triggers; map to affected reaches and alert zones.
- **Exposure service:** WorldPop (D-20), Google Open Buildings + heights (D-21), GRID3 infrastructure and settlement extents (D-49), OSM roads/critical facilities (D-23); simple vulnerability/damage functions (start with global depth-damage curves, localise over time).
- **Risk & loss engine:** intersect hazard × exposure × vulnerability → population at risk, assets at risk, expected annual damage, scenario losses.
- **TriggerDesk:** define parametric triggers (rainfall, discharge, satellite flood-extent), backtest against history, monitor live, generate payout-calculation reports.
- **Delivery:** web app (map, lookup, portfolio upload, dashboards), alert service (SMS/email/webhook), API, embeddable origination widget, PDF reports.

**Required datasets / APIs.** D-02, D-08, D-09, D-10, D-13, D-14, D-16, D-19, D-20, D-21, D-23, D-32, D-49; NIHSA AFO (manually digitised each year). All free / Tier A (FABDEM commercial licence to confirm — Copernicus DEM is a fully-open fallback).

**Example data architecture.**
`hazard_grid` (cell_id, geom, depth_rp10/25/50/100, model_version, confidence) → `assets` (asset_id, owner_id, geom, type, value_ngn, vuln_curve_id) → `asset_hazard` (asset_id, rp, depth, damage_ratio, value_at_risk) → `forecast_events` (event_id, issued_at, horizon, reach_ids, prob, source) → `alerts` (event_id, asset_id/zone_id, severity, sent_at) → `triggers` (contract_id, param, threshold, region) → `trigger_evaluations` (append-only: contract_id, date, observed_value, breach, payout_pct). Historical `flood_observations` (date, geom, source=S1/EMS/WOfS) underpin calibration and are never overwritten.

**MVP features (months 0–6).** National fluvial hazard map (FABDEM + historical Sentinel-1 + WOfS); address/polygon risk lookup + PDF report; portfolio CSV upload → exposure dashboard (population and buildings at risk, indicative value); GloFAS-driven seasonal alerts for the Niger–Benue mainstems; annual digitised NIHSA-AFO overlay.

**Advanced features (months 6–18).** City pluvial (urban flash-flood) modelling for Lagos, Port Harcourt, Kano, Maiduguri; localised depth-damage functions from claims partners; TriggerDesk parametric module; loan-origination API/widget; anticipatory-action decision support (trigger → action → cost) for humanitarian funders; dam-break scenario layers; subsidence (Sentinel-1 InSAR) for coastal Lagos; ISSB/CBN climate-risk report generator.

**AI/ML opportunities.** Rapid flood-extent mapping from Sentinel-1 (segmentation models) for near-real-time situational awareness; downscaling GloFAS to ungauged tributaries with ML on terrain + rainfall; building-level vulnerability inference from Open Buildings morphology + street context; damage estimation from post-event optical imagery; nowcasting urban flash floods from radar rainfall + drainage proxies; NLP to structure NIHSA/NEMA bulletins.

**GIS / satellite-data opportunities.** The product is fundamentally GIS. Distinct plays: a maintained **historical flood-extent archive for Nigeria** (2016–present, Sentinel-1) as a standalone data product; InSAR land-subsidence maps for the coast; drainage-network extraction from DEM + OSM; exposure change detection (new construction in floodplains) from Open Buildings temporal + Dynamic World.

**Reporting dashboard.** **Agency view:** LGA/ward risk ranking, communities and population exposed, live forecast alert board, evacuation-planning layers, post-event impact estimate. **Lender view:** portfolio exposure, concentration, value-at-risk, origination flags, disclosure export. **Insurer view:** accumulation by zone, trigger performance, burn-cost, payout calculations. **Corporate view:** site risk cards, supply-route exposure, business-continuity triggers.

**Environmental-impact calculation methodology.** This is an **adaptation** product — the metric is *risk reduced*, not emissions. Primary KPIs: (a) *people covered by actionable early warning* (population in alert zones receiving ≥24–72h lead time); (b) *reduction in expected annual damage* attributable to an intervention (early warning, drainage works, zoning) computed as `EAD_baseline − EAD_with_measure` from the hazard×exposure×vulnerability stack; (c) *assets/loans stress-tested and re-risked*; (d) for anticipatory action, *losses avoided per $ of pre-arranged finance* from published cost-benefit ratios. Method documented, versioned, validated against observed events — auditable for GCF/Adaptation Fund results frameworks.

**Business model.** **Agency SaaS** $20–80k/yr (often donor-funded initially) + setup. **Lender/insurer SaaS** $15–40k/yr + per-asset or per-API-call. **Reports** $1–8k each (project climate-risk assessments). **TriggerDesk**: structuring fee + % of premium for monitoring. **Anticipatory-action contracts** with humanitarian funders ($30–150k per programme). **Data licensing** (historical flood archive, hazard tiles) to reinsurers and consultancies. Target ~$0.5–1m ARR in 24 months across ~6 agencies, ~6 financial clients, a few programmes.

**Pricing possibilities.** Free public LGA-level risk map (credibility, adoption) + paid asset-level, forecasting, portfolio, API and structuring tiers.

**Go-to-market.** (1) Publish a free national LGA flood-risk map before the rainy season, co-branded with a university or NIHSA — press and agency inbound. (2) Land one lighthouse SEMA (Lagos or Bayelsa) via a donor-funded deployment. (3) Partner with an insurer on the next parametric programme through InsuResilience/UNDP IRFF. (4) One bank pilot for the origination widget. (5) Anticipatory-action pilot with the Red Cross or WFP.

**Partnership opportunities.** NIHSA and NEMA (official data + distribution, avoid conflicting warnings); UNDP IRFF / InsuResilience / IDF (parametric); a Nigerian university hydrology group (calibration, credibility); Google (Flood Hub integration rather than competition); reinsurers (data buyers); telcos (alert delivery).

**Government agencies to approach.** NIHSA, NEMA, state SEMAs, Federal Ministry of Environment (Ecological Fund), state ministries of works and physical planning, the Nigeria Hydrological Services Agency's basin authorities (e.g. Lower Niger, Benue), Lagos State Ministry of the Environment.

**Private companies to approach.** Leadway, AXA Mansard, AIICO, Royal Exchange, Sovereign Trust, Africa Re, Continental Re; Access, Zenith, GTCO, Stanbic IBTC (risk & sustainability); IHS Towers; Nigerian Breweries, Nestlé, Dangote (riverside sites); Julius Berger and other infrastructure contractors.

**Development organisations to approach.** GCF (adaptation, via DBN/NCCC), Adaptation Fund (via BOI), World Bank (Nigeria urban/resilience, ACReSAL for the north), InsuResilience Solutions Fund, UNDP IRFF, GFDRR, Anticipation Hub / Red Cross Climate Centre, Start Network, AfDB ClimDev, Google.org.

**Green funding opportunities.** This is a prime **adaptation-finance** candidate (Section 5.2 fits cleanly): defined intervention (asset-level flood risk + EW for N states and their populations/assets), KPI (people with actionable warning; EAD reduced; $ losses avoided), baseline (historical events + current EAD from the model), reporting standard (GCF/Adaptation Fund results frameworks; Sendai indicators), safeguards and sustainability tail (agency + financial-sector subscriptions). No carbon credits — do not pitch any.

**Carbon-finance potential.** None directly. (Optional narrow tie-in: avoided emissions from flood-damage-and-rebuild cycles, but this is not a recognised crediting pathway — exclude it from funding pitches.)

**Regulatory requirements.** No licence to operate. Coordinate public warnings with NIHSA/NEMA (a formal MoU) so the platform augments rather than contradicts official alerts. Insurance-pricing analytics may need NAICOM familiarity if you move into rating. Data-protection for any personal/asset data uploaded by clients.

**Major risks.**
- *Forecast commoditisation:* Google Flood Hub is free and covers Nigeria. Mitigate by competing on asset-level risk, loss estimation and integration — not the raw forecast — and by integrating Flood Hub as an input.
- *Liability:* a missed or false warning has consequences. Mitigate with clear confidence bands, an official-partner MoU, and terms of use; never be the sole official warning channel.
- *Model credibility in ungauged basins:* GloFAS and global DEMs are weaker for flash/urban floods. Mitigate with local calibration, university validation, and honest uncertainty.
- *B2G sales cycles:* slow, budget-constrained, politically exposed. Mitigate by leading with donor-funded deployments and the faster-moving financial-sector segment.
- *Exposure-data valuation:* the biggest uncertainty in any loss number is asset value. Mitigate with client-supplied values and conservative defaults.
- *Annual manual step:* the NIHSA AFO must be re-digitised yearly — cheap but must not be forgotten.

**12-month implementation roadmap.**
- **M0–1:** entity; compute env; MoU discussions with NIHSA/a university; assemble the Sentinel-1 historical flood archive for Nigeria (2017–present).
- **M1–3:** national fluvial hazard model v1 (FABDEM + HAND, calibrated to S1/EMS/WOfS); address risk lookup + PDF.
- **M3–5:** exposure engine (WorldPop + Open Buildings + GRID3); portfolio upload + dashboard; publish the free LGA risk map.
- **M5–7:** GloFAS forecast service + seasonal alerts for Niger–Benue; onboard first SEMA pilot (donor-funded) and first bank pilot.
- **M7–9:** TriggerDesk v1; localise damage functions with an insurer partner; ISSB/CBN report export.
- **M9–12:** Lagos + Port Harcourt pluvial modelling; anticipatory-action pilot; submit a GCF-readiness or Adaptation Fund concept (via DBN/BOI) with pilot evidence; API + origination widget GA.

**Estimated MVP development effort.** ~5–7 months, 4 people (2 geospatial/hydrology, 1 backend, 1 full-stack/design), ~$150–220k including compute for the historical archive build and hazard modelling. A "risk-lookup + portfolio dashboard, fluvial only" cut can reach a first paying pilot in ~4 months.

---

# 10. Market gaps — where to concentrate

The brief is explicit that the research should favour situations where **the data already exists but nobody has built the layer that makes it usable**. Mapping that test to the findings:

| Gap pattern (from the brief) | Where it bites hardest in Nigeria | Concept that fills it |
|---|---|---|
| Open data exists but agencies/businesses can't interpret it | Methane/flaring (5 data sources, 0 tools); flood outlook (PDF); air quality (satellite data, no public service) | **P1**, **P2**, P7 |
| Datasets fragmented across organisations | Flaring (VIIRS/TROPOMI/GGFR/Gas Flare Tracker/NUPRC); electricity (NERC/NISO/DisCos/Ember); electrification (REA/GRID3/energydata.info) | **P1**, P20, **P3** |
| Environmental reporting still manual | Corporate ESG/ISSB; EPR compliance; restoration-programme M&E; clean-cooking MRV | **P5**, P10, **P22**, **P18** |
| Organisations need dashboards/analytics over their own mandate | NOSDRA (spills/methane), NUPRC (flaring), NEMA/SEMA (floods), NAGGW (restoration), LAMATA (transport) | **P1**, **P2**, P14, P22, P13 |
| Climate risks poorly visualised | Flood exposure for lenders/insurers; heat; coastal erosion; drought | **P2**, P26, P16, P15 |
| Government data lacks a public monitoring layer | Flaring, spills, air quality, electricity reliability, deforestation alerts for Nigeria specifically | **P1**, P14, P7, P20, **P6** |
| Companies need evidence for ESG/sustainability reports | ISSB from 2027; CBAM now; bank sustainable-banking disclosure | **P5**, **P4** |
| Investors/lenders need independent environmental-impact verification | Solar-loan savings; restoration spend; carbon-project claims; green-bond use-of-proceeds | **P4**, **P1**, **P22**, **P18** |
| Infrastructure projects need climate-risk assessments | Every road/bridge/estate/factory in a floodplain; coastal assets | **P2**, P26, P15 |
| Nigerian SMEs can't afford international sustainability software | Carbon accounting, energy management, EUDR compliance | **P4**, **P5**, **P6** |

**Concentration conclusion.** Five concepts sit on *four or more* gap patterns simultaneously — **P1 FlareWatch, P2 FloodShield, P4 SolarLedger, P6 TerraProof, P22 SahelGuard**. These are where an open-data software company has the least competition and the clearest "we built the missing layer" story for both customers and funders. The three deep-dived concepts are drawn from this set (P22 and P6 are the strongest fast-followers).

**What to avoid.** Concepts that mostly re-implement something already widely available for free (a consumer flood-forecast app duplicating Google Flood Hub; a generic farmer-advisory app in a field with 10+ funded players; a carbon calculator with no Nigeria localisation). In each case the viable move is to go one layer deeper — asset-level risk, an embeddable engine, verification-grade MRV — not to rebuild the commodity.

---

# 11. Final recommendation

> **"If I wanted to start building one green-tech product in Nigeria today, using mostly free/open data and with the long-term objective of attracting green funding, which should I build first — and why?"**

## 11.1 Build first: **SolarLedger NG** (P4)

A distributed-energy decision **and** diesel-displacement MRV platform for Nigerian SMEs/C&I sites and the installers, banks and funds around them.

**Why this one first, over the higher-scored FlareWatch:**

1. **Fastest to revenue.** A useful free calculator + paid PDF proposal can ship in ~2–3 months; installers and SMEs pay almost immediately. FlareWatch's anchor customers (regulators) have long, grant-dependent procurement.
2. **Lowest capital and execution risk.** Tabular/raster data, established solar-modelling maths, a small team, ~$50–110k to MVP. No contested public claims about named companies.
3. **Most reliable open data.** Global Solar Atlas and NASA POWER are bankable-grade; tariffs and the grid EF are public; night-lights reliability is well-validated. Less "indicative" hedging than methane or flood-loss numbers.
4. **Biggest, most urgent buyer base.** Post-subsidy diesel pain is universal and current; every solar lender needs a standard appraisal-and-verification method.
5. **It still checks every green-funding box** (DARES RBF, GEAPP, All On, AfDB SEFA, GCF energy-access) and has a **real carbon tail** (programmatic diesel-displacement credits) — so "build first" does not mean "compromise on the funding objective."
6. **The MRV engine is a reusable asset.** The versioned, auditable emissions engine built here is the same core that FlareWatch's MethaneLedger and any future carbon-aggregation product need — so SolarLedger is also the lowest-risk way to build the company's central IP. A founder can sequence: **SolarLedger → add FlareWatch as a second product once the MRV engine, the funder relationships and a verification partner exist.**

**Second choice: FlareWatch NG (P1)** — higher impact ceiling, the single best green-funding and market-gap story (methane is the hottest theme in climate finance and nothing Nigeria-specific exists), and a strong carbon-MRV pathway. Choose this first instead if your team is geospatial-heavy and you have a 6–12-month grant runway to sell to regulators.

**Third choice: FloodShield NG (P2)** — the largest adaptation-finance pool and Nigeria's most visible recurring climate harm, with clear B2G and financial-sector demand. Choose this if your mission priority is public resilience and you can tolerate slower, donor-led revenue. No carbon angle.

## 11.2 The #1 concept as a one-line value chain

```
OPEN DATA                DATA PROCESSING            PLATFORM                 CUSTOMER              ENVIRONMENTAL IMPACT        REVENUE                  GREEN FUNDING
─────────                ───────────────            ────────                 ────────              ───────────────────        ───────                 ─────────────
Global Solar Atlas   →   solar yield model      →   SolarLedger NG:      →   SMEs & mid-caps   →   diesel litres avoided   →  SME subscription      →  DARES results-based
(D-12) PVOUT/GHI          (8760-hr sim)              • payback calculator     (mfg, health,        MWh grid/diesel            (₦15–40k/mo)             finance (via lender
NASA POWER (D-11)     →   bill/diesel parser     →   • financing pack         schools, cold        displaced              →  installer tier          partners)
DisCo tariffs +      →   (OCR + load             →   • installer quotes       chain, telecom)      tCO₂e avoided /            (₦150–400k/mo)       →  GEAPP / All On /
NERC orders              reconstruction)             • monthly VERIFIED   →   Solar EPCs        →   site/month, audited    →  lender portfolio        AfDB SEFA grants
Nigeria grid EF      →   deterministic,         →     savings + emissions     (branded tool)       & versioned               SaaS ($6–20k/yr)     →  GCF energy-access
(D-65, D-42, D-27)        versioned MRV engine        statement           →   Banks & funds     →   → auditable impact     →  carbon-aggregation      (via DBN accreditation)
VIIRS night-lights   →   (measured > modelled,  →   • lender dashboard       (BOI, DBN,           reports for funders,      cut (10–20% of       →  carbon pre-finance
(D-07) reliability        uncertainty deduction)     • carbon aggregator      Sterling, All On)    ESG & carbon MRV          credit value)           (programmatic AMS-I.F)
Open Buildings (D-21) →  roof-area estimate         • API                                                                                          →  Catalyst Fund / GIZ NESP
```

## 11.3 Datasets to start experimenting with **today** — before spending real money

All free, no procurement, usable from a laptop this week:

| Priority | Dataset | Get started | First experiment |
|---|---|---|---|
| 1 | **Global Solar Atlas API + bulk PVOUT layer** (D-12) | [globalsolaratlas.info](https://globalsolaratlas.info/) → "Download data" / API docs | Pull PVOUT and GHI for 20 real business locations (Lagos, Kano, Aba, Port Harcourt); sanity-check against known installed systems. |
| 2 | **NASA POWER API** (D-11) | [power.larc.nasa.gov/api/pages](https://power.larc.nasa.gov/api/pages/) — REST, no key | Daily GHI + temperature time series for the same points; build a simple monthly-yield estimate. |
| 3 | **NERC tariff orders + Nigeria grid EF** (IGES list, D-65; Ember, D-42) | [nerc.gov.ng](https://nerc.gov.ng/) orders; [iges.or.jp grid EF list](https://www.iges.or.jp/en/pub/list-grid-emission-factor/en); [ember-energy.org](https://ember-energy.org/data/) | Assemble a versioned tariff-band + grid-EF table; compute ₦/kWh and kgCO₂/kWh by DisCo. |
| 4 | **VIIRS Black Marble night-lights** (D-07) | NASA Black Marble (VNP46A2) via [LAADS](https://ladsweb.modaps.eosdis.nasa.gov/) or GEE `NOAA/VIIRS/DNB/MONTHLY_V1` | Map monthly radiance for 3 industrial areas over 2 years; look for supply-reliability signal. |
| 5 | **Google Open Buildings v3** (D-21) | [sites.research.google/open-buildings](https://sites.research.google/gr/open-buildings/) — CSV / Earth Engine | Extract footprints + areas for a few industrial estates; estimate usable roof area. |
| 6 | **VIIRS Nightfire (VNF)** (D-07) — for the FlareWatch option | [eogdata.mines.edu/products/vnf](https://eogdata.mines.edu/products/vnf/) | Download a month of Nigeria detections; cluster into flare sites; compare counts to the [Gas Flare Tracker](https://gasflaretracker.ng/). |
| 7 | **Climate TRACE bulk download + API** (D-27) | [climatetrace.org/data](https://climatetrace.org/data) — CC BY 4.0 | Pull Nigeria oil-&-gas and power assets; check coverage and confidence fields. |
| 8 | **Copernicus Data Space** (Sentinel-2 / Sentinel-5P, D-01/D-03) | [dataspace.copernicus.eu](https://dataspace.copernicus.eu/) — free account, openEO free tier | Pull a Sentinel-5P CH₄/NO₂ monthly mean over the Niger Delta; pull Sentinel-2 over a cocoa LGA. |
| 9 | **Digital Earth Africa Sandbox** (D-16) | [digitalearthafrica.org](https://www.digitalearthafrica.org/) → free Sandbox (JupyterHub) | Run the cropland-extent and WOfS notebooks for a Nigerian AOI — instant land/water baselines. |
| 10 | **GloFAS + FABDEM** (D-13/D-19) — for the FloodShield option | [global-flood.emergency.copernicus.eu](https://global-flood.emergency.copernicus.eu/); [FABDEM](https://data.bris.ac.uk/data/dataset/25wfy0f9ukoge2gs7a5mqpq2j7) | Overlay GloFAS 2024 reforecast peaks on FABDEM-derived low-lying zones for the Benue around Makurdi. |

A focused person can, in **2–4 weeks and $0**, validate the SolarLedger yield-and-savings model against real systems, stand up a Nigeria grid-EF/tariff table, and produce a first "diesel-to-solar payback" chart for 20 businesses — enough to show an installer, an SME and a grant officer before writing production code.

---

# Appendix A — Nigerian bodies and abbreviations

| Abbr. | Full name |
|---|---|
| ACReSAL | Agro-Climatic Resilience in Semi-Arid Landscapes (World Bank / FG project) |
| ACMI | Africa Carbon Markets Initiative |
| AFO | Annual Flood Outlook (NIHSA) |
| BOI | Bank of Industry |
| CBN | Central Bank of Nigeria |
| DARES | Distributed Access through Renewable Energy Scale-up (World Bank / REA) |
| DBN | Development Bank of Nigeria |
| DisCo | Electricity Distribution Company (11 of them) |
| ECN | Energy Commission of Nigeria |
| EPR | Extended Producer Responsibility |
| ETP | Nigeria Energy Transition Plan |
| FMARD / FMAFS | Federal Ministry of Agriculture & Rural Development / Food Security |
| FRC | Financial Reporting Council of Nigeria |
| GRID3 | Geo-Referenced Infrastructure & Demographic Data for Development (Nigeria) |
| HYPREP | Hydrocarbon Pollution Remediation Project (Ogoniland) |
| LAMATA | Lagos Metropolitan Area Transport Authority |
| LAWMA | Lagos Waste Management Authority |
| MAN | Manufacturers Association of Nigeria |
| NAGGW | National Agency for the Great Green Wall |
| NAICOM | National Insurance Commission |
| NBS | National Bureau of Statistics |
| NCCC | National Council on Climate Change (Secretariat) |
| NCMAP | Nigeria Carbon Market Activation Policy |
| NEMA | National Emergency Management Agency |
| NERC | Nigerian Electricity Regulatory Commission |
| NESREA | National Environmental Standards & Regulations Enforcement Agency |
| NGFCP | Nigerian Gas Flare Commercialisation Programme |
| NGX | Nigerian Exchange (stock exchange) |
| NIHSA | Nigeria Hydrological Services Agency |
| NiMet | Nigerian Meteorological Agency |
| NIMASA | Nigerian Maritime Administration & Safety Agency |
| NISO | Nigerian Independent System Operator |
| NNPC | Nigerian National Petroleum Company Ltd |
| NOSDRA | National Oil Spill Detection & Response Agency |
| NRGI | Natural Resource Governance Institute |
| NUPRC | Nigerian Upstream Petroleum Regulatory Commission |
| PFA | Pension Fund Administrator |
| PIA | Petroleum Industry Act 2021 |
| REA | Rural Electrification Agency |
| SEMA | State Emergency Management Agency |
| SURAGGWA | Scaling-Up Resilience in Africa's Great Green Wall (project) |

# Appendix B — Method and limitations

- **Coverage:** ~30 sectors scanned; ~45 data sources inventoried; 26 concepts framed; 16 scored. Not exhaustive — plastics, fisheries, cold-chain, hydrogen, e-waste and green-hydrogen/ammonia each merit their own study.
- **Web verification:** dataset, funding-programme and policy facts were checked against primary and reputable-press sources in September 2026 and are cited inline. Some Nigerian-agency portals are intermittently offline; where a source could not be re-confirmed it is flagged (e.g. NiMet, NUPRC data formats).
- **Scores are judgement,** calibrated to the evidence but not empirical. Re-score against your own team's skills, capital and network before committing.
- **Financial figures are illustrative** orders of magnitude for planning, not quotes. FX at ₦1,530 = $1 (Sept 2026) and moving.
- **Not investment advice.** Carbon-market, CBAM, EUDR and Nigerian climate-policy rules are all in flux; obtain specialist legal and methodological advice before structuring anything that depends on them.

---

*Prepared by Pjoc, September 2026. Companion documents: `docs/feasibility-report.md`, `docs/emissions-engine-spec.md`.*





