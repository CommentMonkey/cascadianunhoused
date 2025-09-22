# Cascadian Unhoused

**Cascadian Unhoused** is an open-source project that gathers, normalizes, and shares data on homelessness across the Cascadia bioregion. The goal is to provide a clear, accessible picture of housing insecurity in the Pacific Northwest through transparent data collection and reporting.

## Purpose

Homelessness in Cascadia is both a humanitarian and civic crisis. Public datasets exist, but they are often fragmented, inconsistent, or hard to access. This project aims to:

- Aggregate data from multiple sources (state, county, nonprofit, and municipal).
- Normalize data into a common structure for analysis and visualization.
- Provide open access so communities, policymakers, journalists, and advocates can use the data to inform decisions.
- Encourage collaboration between technologists and service providers.

## Features (in progress)

- Data ingestion pipelines for Oregon and Washington homelessness datasets.
- Storage in a relational database (PostgreSQL).
- REST API powered by Flask for programmatic access. 
- Visualizations and dashboards for trends over time. 
- Documentation to help contributors expand or adapt the project to other regions. 

## Tech Stack

- **Python 3**
- **Flask** (API and web service) 
- **SQLAlchemy** (ORM connoecting Flask and PostgreSQ)
- **PostgreSQL** (data store)

## Contributing

We welcome contributions from developers, data scientists, community members, and anyone passionate about addressing homelessness. Areas to contribute include:

- Adding new data sources.
- Improving ETL (Extract, Transform, Load) pipelines. 
- Building API endpoints.
- Designing user-friendly visualizations. 
- Writing documentation and commentary to make the code more accessible.

