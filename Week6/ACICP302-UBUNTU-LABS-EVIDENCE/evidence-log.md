# ACICP302ICS Evidence Log

**Learner/Team:** Aminu Ibrahim Jalo
**Registration number(s):** C11/26/ACIS/17359
**Activity:** Activity 07 — Recovery, Evidence and Project Defence
**Date and WAT time:** 14 October 2026; see individual evidence timestamps
**Assigned Ubuntu VM / snapshot:** icdfa-VMware-Virtual-Platform; snapshot status to be confirmed
**Canonical source path:** `labs/ot-security/student-lab-source/`
**Course source commit:** `2a66f9bcf253eb3fe31c68ad52794cd535421da8`
**Authorized loopback scope:** 127.0.0.1; ports 5020, 5021 and 8080

| Time | Starting state | Exact authorized action / supplied script | Observation/result | Evidence reference | Analysis/conclusion | Stop/recovery action |
|---|---|---|---|---|---|---|
| Previous Activity 06 test | Local simulation running | Attack Hold, direct path 5020 | 76 writes; peak pressure 95.0 bar; 76/76 out-of-range readings | `../A06-evidence/A06-04-scenario1-results.txt` | Direct path allowed unsafe simulated pressure values | Lab processes subsequently stopped; see `recovery-record.txt` |
| Previous Activity 06 test | Local simulation running | Attack Hold, guarded path 5021 | 76 writes; peak pressure 31.7 bar; 0/76 out-of-range readings; script reported containment | `../A06-evidence/A06-04-scenario1-results.txt` | Guarded result was within the configured pressure range in this test | Lab processes subsequently stopped |
| Previous Activity 06 test | Local simulation running | False Data Injection, direct path 5020 | Peaks: 110.0 °C, 55.0 bar and 200.0 Nm3/h; 6/6 unsafe readings for each measurement | `../A06-evidence/A06-05-scenario2-results.txt` | Direct path reported unsafe simulated values | Lab processes subsequently stopped |
| Previous Activity 06 test | Local simulation running | False Data Injection, guarded path 5021 | Peaks: 71.7 °C, 35.2 bar and 142.1 Nm3/h; 0/6 unsafe readings for each measurement; script reported containment | `../A06-evidence/A06-05-scenario2-results.txt` | Guarded readings remained within configured limits in this test | Lab processes subsequently stopped |
| Previous Activity 06 test | Local simulation running | Slow Drift, direct and guarded paths | Reported actual pressure: direct 39.5–40.0 bar; guarded 37.9–39.3 bar | `../A06-evidence/A06-06-scenario3-results.txt` | Neither reported range exceeded 40 bar; do not claim a confirmed Slow Drift-specific guard log entry | Lab processes subsequently stopped |
| 2026-10-14 19:43 WAT | Lab processes expected to be stopped | Checked TCP listeners on ports 5020, 5021 and 8080 using `sudo ss -ltnp` | No listeners found on the three ports | `recovery-record.txt` | Confirms no listeners on these ports at the recorded time; does not prove snapshot restoration or every internal state | Snapshot and safe-state verification still need confirmation |

## Safety declaration

This log summarizes results recorded from the authorized local training simulation. The course-provided source is attributed and is not represented as learner-authored code. The listener check is recorded above. The instructor-directed snapshot/recovery action and full safe-state verification must be confirmed before signing this declaration.

**Learner/Team signature(s):** Pending final verification
**Date:** 14 October 2026
