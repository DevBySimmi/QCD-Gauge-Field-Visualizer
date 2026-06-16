# QCD-Gauge-Field-Visualizer

An advanced visualization of a simplified U(1) Lattice Gauge Theory inspired by Quantum Chromodynamics (QCD).

This project demonstrates how gauge fields evolve on a discrete spacetime lattice and provides an intuitive visual representation of plaquette values, energy evolution, and Wilson loop estimates.

---

## Features

- Animated Gauge Field Evolution
- Plaquette Heatmap Visualization
- Real-Time Energy Tracking
- Wilson Loop Estimation
- Dark Scientific Theme
- Lattice Grid Overlay
- Statistical Analysis Panel
- Matplotlib Animation Support

---

## Preview

The simulation window contains:

### Left Panel
- Lattice Gauge Field Heatmap
- Plaquette Visualization
- Iteration Counter
- Mean Value
- Standard Deviation
- Wilson Loop Estimate
- Energy Measurement

### Right Panel
- Real-Time Energy Evolution Graph

---

## Physics Background

Quantum Chromodynamics (QCD) describes the strong interaction between quarks and gluons.

Because solving QCD analytically is extremely difficult, physicists often discretize spacetime into a lattice and study gauge fields numerically.

This project implements a simplified U(1) lattice gauge model for educational and visualization purposes.

The plaquette value is calculated as:

P = cos(φ₁ − φ₂ − φ₃ + φ₄)

where φ represents gauge field values on neighboring lattice sites.

---

## Technologies Used

- Python
- NumPy
- Matplotlib
- Matplotlib Animation
