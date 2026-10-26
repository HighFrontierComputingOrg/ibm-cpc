# IBM Card-Programmed Electronic Calculator (CPC)

This folder brings together source material and a proposed proof of concept
for exploring the IBM Card-Programmed Electronic Calculator. The emulator is
not implemented yet: the design note describes a possible small behavioral
model, not a working or cycle-accurate simulator.

## Historical references

- [`cpc-overview.pdf`](cpc-overview.pdf) — a 1951 overview of the CPC.
- [`cpc-principles.pdf`](cpc-principles.pdf) — the 1954 *Principles of
  Operation* manual, the main reference for the proposed model.

The manuals describe the historical machine, while the POC design note uses
them to identify which behaviors a small teaching model might represent.

## Emulator proof-of-concept design

[`cpc-emulator-poc.md`](cpc-emulator-poc.md) proposes a minimal Python
behavioral model centered on the separate control panel, decimal calculator,
card reader, and 941 storage unit. It outlines a staged card-processing
workflow, a small multiply-and-print demonstration, execution tracing,
error handling, and a test plan.

The proposal deliberately excludes low-level hardware timing, a graphical
plugboard, complete physical card encoding, and claims of exact historical
equivalence. It is a design document only; the proposed emulator modules and
examples have not been built.

## `msc/` numerical examples

The [`msc/`](msc/) subfolder contains exploratory Python examples for repeated
complex squaring and matrix inversion, with a local guide in
[`msc/readme.md`](msc/readme.md). These are numerical demonstrations, not
components of the CPC emulator.
