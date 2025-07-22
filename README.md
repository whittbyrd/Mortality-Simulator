# Mortality Simulation

Mortality Simulation is a Python-based Monte Carlo engine that models individual lifetimes using age-specific mortality probabilities. 

## Overview

A lightweight Monte Carlo engine for simulating human lifetimes from an age‐indexed mortality (qx) table. Given a starting age and a table of annual death probabilities, the package repeatedly simulates independent lives, tallies the terminal ages at death, and reports descriptive statistics (expected age at death, probability of dying before a target age, standard deviation, and median age). Results can be written to CSV for downstream analysis.

---

## Features

- **CSV‑driven mortality input**: Simple Age,Qx file format

- **Monte Carlo lifetime simulation**: Year‑by‑year survival checking using age‑specific q_x (probability of death within the next year given survival to current age)

- **Summary statistics out of the box**: Expected age at death, probability of dying before an age threshold, population standard deviation, and median age

- **Compact, pure‑stdlib implementation**: No external dependencies beyond Python’s standard library

- **Export to CSV**: Quick way to capture simulation settings and summary metrics

---

## Included Components

### Mortality Table

- **Purpose**: Handles loading and accessing mortality data from a CSV file.
- **Parameters**: fileName – Path to a CSV with Age,Qx columns
- **Behavior**: Loads a dictionary mapping age -> qx (probability of death within one year)

### Person

- **Purpose**: Represents a single individual’s life, simulated year by year using a mortality table
- **Attributes**: age – Current or terminal age, mortalityTable – Reference to a MortalityTable object, isDead – Tracks if the individual has died

### Simulation

- **Purpose**: Manages the execution of multiple life simulations and computes statistical results.
- **Attributes**: age – Starting age for each simulated life, simulations – Number of lives to simulate, Ages – Dictionary tracking the frequency of terminal ages

---

## Author

Created by Whitt Byrd.
