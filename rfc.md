Perfecto 🚀. Te propongo un **System Prompt estilo RFC** para **ProperT**, con lenguaje claro, formal y de alto nivel (como si fuera la visión de producto/arquitectura).

---

# RFC: ProperTea – Intelligent Real Estate Valuation & Opportunity Detection

## Purpose

ProperTea is a platform designed to **model, monitor, and explain housing prices across time and space**. Its goal is to provide a transparent, data-driven view of real estate markets and detect anomalies (e.g., underpriced or overpriced properties) that can guide decision-making for buyers, sellers, and investors.

## Problem Statement

Housing prices are influenced by multiple factors: intrinsic property features (bedrooms, bathrooms, surface, age), contextual factors (neighborhood, amenities, urban growth), and temporal dynamics (market cycles, inflation, seasonality). Today, this information is fragmented and hard to interpret. Stakeholders lack tools that:

1. Estimate the **fair market value** of a property given its characteristics and context.
2. Track **price evolution over time and across regions**.
3. Detect **outliers** (properties listed well below or above expected value).
4. Provide **actionable insights** for decision-making.

## High-Level Concept

ProperTea composes three layers of intelligence:

1. **Valuation Engine**

   * Learns price distributions using historical and current market data.
   * Incorporates spatial (location, neighborhood) and temporal (time trends, seasonality) dimensions.
   * Produces a baseline *Fair Price Estimate* for each property.

2. **Market Dynamics Module**

   * Tracks how prices evolve per neighborhood, city, or segment.
   * Generates indicators such as *median price per m²*, *growth rates*, and *volatility*.
   * Identifies structural shifts (e.g., gentrification, downturns, speculative bubbles).

3. **Opportunity Detector**

   * Compares published prices against model estimates.
   * Flags properties as:

     * **Underpriced (opportunity)** – potential good deals for buyers/investors.
     * **Overpriced (alert)** – potential negotiation signals or overpriced listings.
   * Provides transparency scores to build trust with users.

## Core Principles

* **Composability**: Each module (Valuation, Market Dynamics, Detection) is independent yet interoperable.
* **Explainability**: Outputs are not black boxes; users understand *why* a property is valued as such.
* **Scalability**: Designed to handle multiple geographies, time ranges, and property types.
* **Fairness & Transparency**: Prevent reinforcing market biases; ensure signals are clear and actionable.

## Vision

ProperTea aspires to become the **intelligent companion for real estate decisions**, empowering stakeholders to:

* Detect undervalued opportunities in real time.
* Understand neighborhood-level price evolution.
* Price properties accurately and transparently.
* Navigate housing markets with data, not guesswork.

---

👉 Este RFC lo puedes usar como **System Prompt base** para alinear a todos los involucrados (técnicos, producto, inversionistas).

¿Quieres que lo lleve un paso más allá y te prepare un **roadmap técnico** (qué datasets, qué modelos, qué métricas de evaluación) o prefieres que quede solo como documento de visión?
