# Python Basics → Advanced Learning Repository

This repository is now structured as a full learning path for Python preparation from beginner to advanced.

## Start here
- New to Python: start at `01_Variables` and follow `LEARNING_ROADMAP.md` in order.
- Already know basics: run recap diagnostics in:
  - `checkpoints/foundations_recap_01_02.md`
  - `checkpoints/foundations_recap_03_04.md`
  - `checkpoints/foundations_recap_05_06.md`
- If you pass recap tasks quickly, jump to `07_Strings` and continue.

## Roadmap
See `/home/runner/work/Python-Basics/Python-Basics/LEARNING_ROADMAP.md` for:
- Level outcomes (Foundations, Intermediate, Advanced)
- Ready-to-move-on checklists
- Ordered module path with prerequisites
- Project progression

## Repository structure
Each module follows a consistent layout:

```text
<module>/
  concepts/
  examples/
  practice/
  solutions/
  mini_project/
```

Current modules:
- Foundations: `01_` to `06_`
- Intermediate: `07_` to `15_`
- Advanced: `16_` to `24_`

## How to run examples
From repository root (`/home/runner/work/Python-Basics/Python-Basics`):

```bash
python 01_Variables/examples/example.py
python 09_File_Handling/examples/example.py
python projects/beginner/calculator/calculator.py
```

## Practice workflow
1. Read `concepts/README.md` in the module.
2. Run and modify files under `examples/`.
3. Solve `practice/exercises.md` with difficulty targets.
4. Save final answers under `solutions/`.
5. Complete `mini_project/README.md` task.
6. Update `/home/runner/work/Python-Basics/Python-Basics/PROGRESS_TRACKER.md`.

## Recommended study order
1. Follow module order in `LEARNING_ROADMAP.md`.
2. Complete weekly challenge files under `assessments/weekly_challenges/`.
3. Run revision drill checklist from `assessments/revision_drills.md` every week.
4. Move to the next level only when checklist criteria are met.

## Project progression
- Beginner: calculator, quiz, file organizer
- Intermediate: expense tracker (CLI milestone), contact manager, text analyzer
- Advanced: automation workflow capstone (staged)

## Validation and tests
Run project validation from root:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## Contribution style for adding new modules
When adding a module:
1. Follow numeric naming (e.g., `25_New_Topic`).
2. Include all five required directories.
3. Add module outcome, common mistakes, and debugging tips in `concepts/README.md`.
4. Add at least one runnable example.
5. Add practice tasks with difficulty label and completion criteria.
6. Update `LEARNING_ROADMAP.md` and `PROGRESS_TRACKER.md`.
