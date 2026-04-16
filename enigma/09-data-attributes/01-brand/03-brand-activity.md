# Brand Activity

> https://documentation.enigma.com/reference/attributes/brand-activity

## Overview

The Brand Activity attribute "identifies businesses that engage in activities with a high compliance risk."

## Key Details

**Coverage:** Approximately 130K brands classified as high-risk, including online-only businesses without physical addresses.

**Data Sources:** Derived from business names, websites, and public web descriptions using heuristics across Enigma's data sources (card transactions, legal entity registrations).

**Methodology:** Enigma searches for keywords in industry descriptions, names, and website URLs. For example, cannabis classification looks for terms like "cannabis," "marijuana," "dispensary," "CBD," and "THC."

## High-Risk Categories

- Cannabis (retail, growers, software)
- Tobacco and Vaping
- Firearms, Weapons and Ammunition
- Adult Entertainment and Dating
- Gambling and Sports Betting
- Payments and Money Transfer
- Multi-level Marketing
- Pawn Shops, Check Cashing and Payday Loans
- Cryptocurrencies and Digital Assets
- Investments and Financing
- Legal Finance (collections, bail bonds)
- Gift Cards
- Health and Lifestyle
- Prescription Drugs

## Data Fields

| Field | Label | Type |
|-------|-------|------|
| activityType | Activity Type | String |
| firstObservedDate | First Observed Date | String |
| id | ID | UUID |
| lastObservedDate | Last Observed Date | String |

**Tier:** Plus (all fields)
