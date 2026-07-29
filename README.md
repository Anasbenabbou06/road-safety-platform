# Road Safety Platform

Analyse de la sécurité routière — Pipeline ETL sur le dataset FARS 2015 (NHTSA)

## Contexte

Stage d'initiation — Alten Delivery Center Maroc, Département Data & AI (Secteur Automobile)

**Stagiaire :** Anas Ben Abbou — ENSMR (ISIP)
**Encadrant :** Hamza El Ouali

## Problématique

Identifier les caractéristiques les plus fréquemment observées dans les accidents mortels enregistrés par le FARS (Fatality Analysis Reporting System) aux États-Unis en 2015.

## Architecture

BigQuery (FARS 2015) → Kaggle/Python (Extraction + Nettoyage) → CSV → PostgreSQL (Stockage) → Power BI (Dashboard)

## Dataset

| Table | Lignes | Colonnes | Description |
|-------|--------|----------|-------------|
| accident | 32 538 | 12 | Un enregistrement par accident mortel |
| vehicle | 49 478 | 16 | Un enregistrement par véhicule impliqué |
| person | 81 620 | 13 | Un enregistrement par personne impliquée |
| factor | 49 546 | 5 | Facteurs contributifs mécaniques par véhicule |

## Outils

- Python 3.x — Pandas, Matplotlib
- PostgreSQL 18 — Stockage relationnel
- Power BI Desktop — Dashboard interactif
- Kaggle Notebooks — Extraction BigQuery + EDA(Exploratory Data Analysis)
- Git / GitHub — Versioning