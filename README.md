# Pollen Data Sources and Documentation

## Main Data Source

The historical pollen data used in this project was sourced from the official archive of the **Stiftung Deutscher Polleninformationsdienst (PID)**:

[Pollenflug-Rückblick – pollenstiftung.de](https://www.pollenstiftung.de/pollen-im-fokus/pollenflug-rueckblick.html)

This site provides yearly retrospective summaries of pollen activity across Germany in barchart, including total pollen counts for common allergenic species such as Hazel, Alder, Birch, Grass, and more which were extracted manually.

---

## Other Reviewed Sources (Not Used Due to Limitations)

While searching for reliable historical pollen data, the following websites were reviewed but not selected due to various limitations:

| Website | Description |
|---------|-------------|
| [Deutscher Wetterdienst (DWD)](https://www.dwd.de/DE/leistungen/pollen/pollenstatistik.html) | Monthly statistics available, but not easy to extract or download for large-scale analysis. |
| [Allergy.de Pollen Calendar](https://www.allergy.de/pollenflugkalender) | Does not provide historical data or downloadable datasets. |
| [PollenScience.eu](https://pollenscience.eu/historie) | Contains historical charts but takes a long time to load and lacks clear export options. |
| [PollenCount.eu – Brandenburg](https://pollencount.eu/brandenburg-de#chart) | Offers county-based data, but only for a single year (limited historical coverage). |
| [Elsa project - https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Felsa-project.de%2Fwp-content%2Fuploads%2F2024%2F03%2FELSA-20-Pollen-Stack_all-pollen-counts-Britzius-et-al.-2024-Sirocko-et-al.-2021-Sirocko-et-al.-in-prep-1.xlsx&wdOrigin=BROWSELINK | Too much metadata to understand the dataset.|

These sources were helpful for context validation, but the primary dataset in this project is derived exclusively from **pollenstiftung.de** due to its structured yearly overview.

---

## Data Compilation Process

1. **Manual Extraction** from web-based reports and PDFs.
2. **Standardization** of pollen names, units (`pollen/m³`), and date formats.
3. **Cross-Comparison** across multiple years to ensure consistency in species tracking.
4. **Data Cleaning** for missing values and inconsistent terminology.
5. **Master Dataset Creation** in CSV format for analysis and modeling.

---

## Metadata Description

| Field Name      | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `Date`          | Year of pollen measurement                                     |
| `Plant_code`   | Name of the pollen source (e.g., Hazel, Birch)                  |
| `Pollen_count` | Total number of pollen in that year measured in pollen/m^3      |
| `Season`   |Season when the pollen is usually seen the most                      |
| `Index_value`        | Severity value that is given according to number of pollen|
| `Plant_family`        | Plant family for that pollen                             |

---
*Index value:
0 - Low
1 - Medium
2- High
3- Critical

*If you want me to help prepare a formatted PDF or add any more details, just ask!*
