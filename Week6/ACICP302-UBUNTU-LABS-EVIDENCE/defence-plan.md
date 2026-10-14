# ACICP302ICS — Activity 07 Project Defence Plan

**Learner:** Aminu Ibrahim Jalo
**Registration number:** C11/26/ACIS/17359
**Course:** ACICP302ICS — Network Security & Attacks
**Course source commit:** 2a66f9bcf253eb3fe31c68ad52794cd535421da8

## 1. Objective

Explain the supplied OT simulation, compare direct and guarded paths, present evidence-backed findings, describe limitations, and demonstrate approved recovery.

## 2. Demonstration outline

1. Identify the canonical course source and exact commit.
2. Explain the local simulation architecture: direct path on port 5020, guarded path on port 5021, and dashboard on port 8080.
3. Present the recorded Attack Hold results:
   - Direct path: peak pressure 95.0 bar, with 76/76 readings out of range.
   - Guarded path: peak pressure 31.7 bar, with 0/76 readings out of range; the supplied script reported containment.
4. Present the recorded False Data Injection results:
   - Direct path: peaks of 110.0 °C, 55.0 bar and 200.0 Nm3/h.
   - Guarded path: peaks of 71.7 °C, 35.2 bar and 142.1 Nm3/h; the supplied script reported containment.
5. Explain the Slow Drift limitation: actual reported pressure did not exceed 40 bar on either path, and no new Slow Drift-specific event was confirmed in the displayed guard log.
6. Present the cleanup verification showing no listeners on ports 5020, 5021 and 8080 at 19:43:24 WAT on 14 October 2026.
7. Explain the remaining evidence gaps and the instructor-directed recovery/snapshot status.

## 3. Key technical points

- The code is supplied course source, not my original implementation.
- The tests compare behaviour in specific scenarios; they do not prove comprehensive protection.
- Dashboard status is not sufficient by itself to prove every internal process state is safe.
- A listener check confirms only that the specified ports had no listeners at the recorded time.
- Packet-level conclusions require an actual learner-created capture and matching request/response analysis.

## 4. Evidence to show

- Activity 06 scenario result files.
- Activity 06 final report.
- Activity 07 evidence log and risk register.
- Cleanup verification record.
- Verified topology, register map, packet analysis and screenshots, if available.
- Final report and evidence index.

## 5. Questions to prepare for

**Why compare ports 5020 and 5021?**
They represent the direct and guarded simulation paths used in the supplied lab, allowing comparison of observed process values and guard behaviour.

**Did the guard stop every attack?**
The recorded Attack Hold and False Data Injection tests reported containment on the guarded path. The Slow Drift evidence is less conclusive, and these tests do not establish comprehensive protection.

**What proves recovery?**
The recorded check found no listeners on the documented lab ports. Snapshot restoration and complete safe-state verification must be supported by additional evidence if required.

**What are the main limitations?**
The findings are limited to the supplied simulation, tested inputs and recorded observations. Packet evidence, event correlation and additional approved validation are needed for stronger conclusions.

## 6. Safety

Do not rerun an attack for the defence unless the instructor explicitly approves it. Do not connect to external or real OT systems. Follow the assigned VM isolation and snapshot/recovery instructions.
