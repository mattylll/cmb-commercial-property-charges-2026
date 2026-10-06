# Commercial property charges: regional contributions and county comparisons, H1 2026

Matt Lenzie · Commercial Mortgages Broker · 6 October 2026  
Research ID: CMB-CH-2026-H1-01 · Version 1.0

**The England and Wales total increased by 136 classified commercial-property charges, while two of seven reporting regions declined.** This package makes the arithmetic inspectable and lets readers compare percentage changes with their underlying counts. It uses the H1 fields in the [Commercial Mortgages Broker Jan–Sep 2026 research release](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3); it does not treat that release as a Q3-only dataset.

## What changed across regions?

The observed national count rose from **7,620 to 7,756 (+1.8%)**. Five regions rose and two fell. London & South East added 116 charges and the Midlands added 87. Those increases were partly offset by the North West (−93) and Wales (−33). This is why a small national movement can coexist with substantial regional differences.

| Reporting region | H1 2025 | H1 2026 | Net change | Change |
|---|---:|---:|---:|---:|
| [Midlands](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/midlands) | 1,203 | 1,290 | +87 | +7.2% |
| [London & South East](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/london-and-south-east) | 2,404 | 2,520 | +116 | +4.8% |
| [North East & Yorkshire](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/north-east-and-yorkshire) | 962 | 992 | +30 | +3.1% |
| [South West](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/south-west) | 815 | 840 | +25 | +3.1% |
| [East of England](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/east-of-england) | 705 | 709 | +4 | +0.6% |
| [Wales](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/wales) | 406 | 373 | -33 | -8.1% |
| [North West](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3/north-west) | 1,125 | 1,032 | -93 | -8.3% |

Seven regional rows reconcile exactly to the England and Wales benchmark in both years. These are the publisher's reporting regions, including combined regions, rather than the standard nine English regions. Scotland and Northern Ireland are excluded.

## County comparisons need the denominator

The companion file covers 44 English county reporting areas: 26 increased, 16 decreased and two were unchanged. East Sussex rose from 104 to 164 (+57.7%, +60); Kent rose from 230 to 318 (+38.3%, +88). A higher percentage change does not necessarily mean a larger numerical increase. Surrey fell from 184 to 107 (−41.8%, −77) and Merseyside from 274 to 188 (−31.4%, −86).

Use the source links in each CSV row for the [county reports](https://commercialmortgagesbroker.co.uk/research/commercial-property/2026-q3#breakdown). The reporting areas include bespoke boundaries: Bristol includes South Gloucestershire, while the Gloucestershire cut excludes it. These 44 areas are not a complete UK county series. Never sum the national, regional and county rows together.

## What the measure means

The source is Commercial Mortgages Broker's classification of [Companies House charge records](https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/charges/list). These are **counts of charge instruments**, not pounds lent, mortgage approvals, unique borrowers, loans or lender market shares. Multiple charge instruments can relate to one financing arrangement. A rise does not establish better credit availability or explain why activity changed.

The published method classifies a charge as commercial using property-location information and borrower SIC classifications or a match to commercial-sale evidence. This derivative checks the public aggregate arithmetic; it does not independently reproduce the private raw-record extraction or validate every classification. The charge snapshot is labelled 1 October 2026. The H1 comparison reduces exposure to the source's expressly provisional Q3 window, but historic records can still be revised.

The source release also contains sales and planning figures. They are deliberately outside this package: different coverage, registration lags and definitions make it inappropriate to combine them into a single lending-demand measure.

## Files and reproduction

- `charge-counts.csv`: 52 observations — one national benchmark, seven regions and 44 county areas, with exact report and CSV links.
- `regional-contributions.csv`: seven regions ranked by percentage change, with absolute differences.
- `datawrapper-regions.csv`: the seven-row input for the chart adaptation.
- `source-manifest.json`: URLs and SHA-256 hashes of the 52 publicly downloadable source CSVs used.
- `reproduce.py`: standard-library checks of counts, percentage calculations, national/regional reconciliation and chart derivation.
- `CITATION.cff`: suggested citation.

Run `python3 reproduce.py` from this directory. This verifies the derived tables; it is not independent raw-register reproduction. Public source URLs may change later; the manifest identifies the version used.

## Citation and reuse

Suggested citation: Lenzie, Matt / Commercial Mortgages Broker (2026), *Commercial property charges: regional contributions and county comparisons, H1 2026*, version 1.0, research ID CMB-CH-2026-H1-01.

This is an author-published analysis, not peer-reviewed research. Cite Commercial Mortgages Broker for the classifications and calculations and Companies House for the underlying register. No new licence is asserted over third-party material. Retain the measure definitions, periods and source links when quoting findings.
