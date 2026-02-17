# Python Programming (B.Tech CSE - Sem 2)

Repository for course materials for **Python Programming**:
- Unit-wise lecture slides and notes (LaTeX + compiled PDFs)
- Lab experiments (Python scripts + per-exercise explanation PDFs)

GitHub: `https://github.com/tali7c/Python-Programming`

## Structure

### Lectures
Each lecture folder follows:
```
Unit-01/
  Lecture-01/
    latex/          # slides.tex, notes.tex + LaTeX aux files
    demo/           # hands-on scripts used in lecture
    data/           # datasets (if any)
    images/         # generated figures (if any)
    slides.pdf
    notes.pdf
Unit-02/
  Lecture-01/
    ...
```

### Experiments
Each experiment folder follows:
```
Experiments/
  Experiment-01/
    scripts/        # Python programs for each exercise
    explanations/   # compiled PDFs for each exercise (one PDF per exercise)
      latex/        # LaTeX sources + LaTeX aux files (one .tex per exercise)
    latex/          # experiment-level LaTeX sources (e.g., exercise sheet)
    exercises.pdf   # problem statements only (no solutions)
```

## Build (Compile PDFs)
Requirements:
- A LaTeX distribution with `pdflatex` (TeX Live / MiKTeX)
- Windows PowerShell

From the repo root:
```powershell
.\build.ps1
```

If script execution is blocked by PowerShell execution policy, use:
```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\build.ps1
```

Notes:
- PDFs are generated in the parent folder of each `latex/` directory.
- LaTeX auxiliary files (`.aux`, `.log`, `.toc`, ...) are moved into the
  corresponding `latex/` directory to keep folders clean.
