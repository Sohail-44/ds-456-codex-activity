# Macalester DS 456 - Projects in Data Science - Codex Activity
Dooly and Sohail


*Originally created by Shilad Sen (with help from Codex), 2025/11/25. Updated by Bret Jackson 2026/11/08*

In this activity you will:

- Use Codex as a collaborator on a real spatial dataset.
- Practice being *critical* of Codex’s suggestions (not just accepting them).
- Progress from exploration to a reviewed analysis plan, implement it with Codex, and verify one important result.

# 0. Get the project

- Fork the [Codex Activity](https://github.com/bretjackson/ds-456-codex-activity) on GitHub.
- Clone **your fork** (not the original) to your computer.

# 1. Choose your tools and set up Codex

You may work in **Python (VS Code)** or **R (VS Code or RStudio)**.

## 1.1 Highly Recommended: VS Code + Codex (Python or R)

- Install [VS Code](https://code.visualstudio.com/).
- Install the [Codex VS Code extension](https://developers.openai.com/codex/ide/).
- If you are using R, also install the [VS Code R extension](https://marketplace.visualstudio.com/items?itemName=reditorsupport.r).
- Open your cloned repo folder in VS Code.
- In the Codex sidebar:
  - Click “Use API Key” and use the key Shilad gave you.  
    **DO NOT PUT THIS KEY ANYWHERE IN YOUR GITHUB REPO.**
  - Open Codex settings → “Open `config.toml`” and set it to:
    ```toml
    model = "gpt-6.1-sol"
    model_reasoning_effort = "medium"
    web_search = "live"

    [sandbox_workspace_write]
    network_access = true
    ```
  - Restart VS Code after editing `config.toml`.

## 1.2 Optional: RStudio + Codex in a separate terminal

If you strongly prefer RStudio:

- Use **RStudio** for your R scripts / Rmd files.
- Using a terminal, install the Codex CLI: `npm i -g @openai/codex`
- In a terminal, run `codex` once so it creates a config file at `~/.codex/config.toml`.
- Open `~/.codex/config.toml` in any text editor you like (VS Code, TextEdit, Notepad, `nano`, etc.) and paste the same settings shown in 1.1.
- In a separate terminal window (**from the repo root**), run Codex and use it to:
  - Draft and refactor R code.
  - Ask questions about errors.
- You are still responsible for keeping all code and writeups in this repo so they can be graded.

# 2. Create your assignment skeleton

You will **not** edit this `README.md` directly. Instead:

- Copy `README.md` to `Codex_Activity.md`.
- Add your name(s) at the top of `Codex_Activity.md`.
- For every prompt marked **Task:** below, you will write your answers in `Codex_Activity.md`.
- Your actual analysis code should live in code files, for example:
  - R: `analysis/codex_activity.qmd` or `analysis/codex_activity.R`
  - Python: `analysis/codex_activity.ipynb` or `analysis/codex_activity.py`

You may reference your code files from `Codex_Activity.md` (e.g., “see Figure 1 in `analysis/codex_activity.Rmd`”).

Keep using the same Codex conversation as you move from exploration to mapping and analysis, including when you return for the second class session. If you start a new conversation, provide your research question (if chosen), relevant file paths, and a short summary of what you have discovered.

# 3. Early dataset interactions

- Pick a spatial dataset from [Open Data Minneapolis](https://opendata.minneapolismn.gov).  
  One fun option (used in the instructor example) is  
  [Motorized Foot & eBike Trips in 2025](https://opendata.minneapolismn.gov/datasets/d9a1f322528447ff9c1bc86e5d0895c5_0/explore).
- Give Codex the URL for the dataset and ask it to help you get started understanding the data.  
  Keep your request intentionally vague (e.g., “Help me explore this dataset”).

**Task 3.1 (in `Codex_Activity.md`):**  
In 2–3 short bullets, describe what you notice about this early interaction. Consider:

- What did Codex assume or gloss over?
- Did it make any mistakes or questionable choices?
- How clear or explainable was the code it produced?

Retain useful code and observations from this interaction so you can build on them in the next sections.
* There are places where it is going too far into the weeds
* It is only looking at one day from the dataset while we could be exploring a lot more 


# 4. More directed exploration

- If you are partner coding, *switch partners*.
- Download the dataset you would like to analyze and move it under `data/`.
- Ask Codex to help you analyze the **basic information** about the dataset:
  - basic summaries (rows, columns, variable types),
  - simple visualizations,
  - any surprising patterns.
- Then ask Codex for specific improvements (e.g., “Use `dplyr` instead of base R”, “Add labels and titles”, “Handle missing values more carefully”).
- Save useful exploration code in your analysis file and keep notes about relevant variables and assumptions. You will reuse this work for mapping and your research question.

**Task 4.1 (in `Codex_Activity.md`):**
Respond in 2–3 short bullets, considering:

- What did Codex do well?
- What would you have done differently if you wrote the code yourself?
- Looking at the code Codex wrote, what could be improved (style, clarity, correctness, efficiency)?

# 5. Mapping the data

- If you are partner coding, *switch partners*.
- Discuss with your partner how you could geocode / map the data.
- Once you have an idea for how to do it, ask Codex to help you map your data. Pay attention to what happens at first:
  - Does it correctly identify what is needed to make a map?
  - Does it confuse attributes (like IDs) with coordinates?

- For the scooter/e‑bike example, the goal is to join trips to a street or trail network such as the  
  [PW Street Centerline dataset](https://opendata.minneapolismn.gov/datasets/pw-street-centerline/about) and then map trip counts by segment.
- Identify a calculation, join, coordinate interpretation, or mapped value you could verify later. In Section 7.3, you will be asked to do some verification.

**Task 5.1 (in `Codex_Activity.md`):**
Respond in 2–3 short bullets, considering:

- Describe what was easier and harder about doing this with Codex.
- Where did Codex help, and where did it get in the way?
- What would you do differently next time you had to map a new dataset with AI assistance?

# 6. Identifying a research question with Codex

- If you are partner coding, *switch partners*.
- You will now work with Codex to identify and refine a research question (RQ) about your dataset.
- Choose a question you can answer with the downloaded data and a small extension of your existing exploration or mapping code. A descriptive question is sufficient; aim for an analysis you can implement in about 20 minutes.

## 6.1 Brainstorm candidate questions

- Seed the brainstorming session with some themes or ideas of research questions that interest you.
- Ask Codex to propose several possible research questions.
- Collaborate with Codex to prioritize the questions along the decision dimensions you think are most appropriate.

**Task 6.1 (in `Codex_Activity.md`):**

- List at least two candidate research questions that Codex suggested.
- For each, briefly note what seems interesting and what might be problematic (data, scope, ethics, feasibility).

## 6.2 Refine and choose your question

- Pick one question (it may be a slight modification of a Codex suggestion).
- Ask Codex to critique and refine that question. For example:
  - “Here is my tentative research question: […]. Critique its clarity and feasibility. Propose 1–2 improved versions.”
- Decide on a **final RQ** you will try to answer. This choice is yours, not Codex’s.

**Task 6.2 (in `Codex_Activity.md`):**

- Write down your final research question in one clear sentence.
- In 2–3 sentences, explain why you chose it (and why you rejected other candidates).

# 7. Answering your question: plan, implement, and verify

Build on your exploration and map to answer **one research question**. Review a plan with Codex, implement it, and verify one important result or transformation.

## 7.1 Design and review a plan

**Plan mode** lets Codex inspect context, ask clarifying questions, and propose an approach before implementation. It can investigate existing files; it should not implement your analysis while planning. See the [OpenAI guidance on Plan mode](https://learn.chatgpt.com/docs/learn/best-practices).

1. Wait until Codex finishes its current response.
2. In the **Codex chat input inside VS Code**, enter `/plan`, select the command, and press Enter. Check that Plan mode is active. If using Codex CLI alongside RStudio, enter the command in the Codex conversation in your terminal.
3. Submit your planning request and answer any clarifying questions.
4. Review and revise the proposed plan before leaving Plan mode.

Review the plan yourself:

- Does it answer your chosen question using available data?
- Are the units, filters, grouping, and treatment of missing values appropriate?
- Does it reuse relevant exploration or mapping work?
- Is the proposed verification feasible and capable of detecting a meaningful error?

Ask Codex to clarify or revise anything you cannot justify. If you do not understand the type of analysis or choices it is suggesting, stop! Discuss them with your partner and clarify with Codex.

**Task 7.1 (in `Codex_Activity.md`):**

- Record your final plan in 3–5 bullets.
- Explain one decision you made while reviewing it. A justified decision to retain a proposed approach counts; you do not need to change the plan just to make a change. However, don't just blindly accept what it suggests. Stop and discuss each decision with your partner!

## 7.2 Implement and inspect

Use the `/plan` toggle to leave Plan mode and confirm it is off **before** requesting implementation, or Press the "Implement this plan" option if it appears.

- You can request the whole small plan or start with a meaningful first step and continue after inspecting it.
- Keep the work in the R or Python analysis file.
- Inspect the changed code and outputs. Does the analysis answer your question? Are the results interpretable and relevant?
- Ask targeted follow-up questions and revise as needed. 

**Task 7.2 (in `Codex_Activity.md`):**

- Briefly state your result and link to the supporting figure, table, or code.
- Describe one implementation choice or issue you examined and what you decided about it.

## 7.3 Verify one important result and reflect

Perform **one documented check** of a consequential claim, calculation, or transformation from your exploration, mapping, or final analysis. 

Choose a check suited to your dataset. Here are some possibilities you could consider:

| Check | Evidence you could provide |
|---|---|
| Recalculate a summary | Manually compute a count, mean, or percentage for a small identified subset and compare it with the code's result for that subset. |
| Check a join used in mapping | Inspect several known matches against the source records and account for unmatched or duplicated records. |
| Check mapped locations | Compare several identifiable features with an authoritative reference and record specific matches or discrepancies. |
| Check a derived variable | Use documented units and a few source records to calculate expected values independently and compare them with the derived values. |

Successful execution, a plausible-looking map, or Codex saying “this is correct” does not satisfy this requirement. Codex may help write checking code, but **you must explain the basis of the check and inspect its evidence**. Establish an expected result or reference independently of the output you are checking.

**Task 7.3 (in `Codex_Activity.md`):**

Record:

- **What I checked and why it matters.**
- **How I checked it**, including the independently established expectation or reference.
- **What I observed**, with actual values, identified records, or another concrete comparison.
- **What I changed or concluded**, including the result of rechecking any correction.


# 8. What to hand in

By the end of the activity, your repo should include at least:

- `Codex_Activity.md` with answers to all **Task** prompts (3.1, 4.1, 5.1, 6.1, 6.2, 7.1, 7.2, 7.3), including your reviewed plan, research-question result, and verification evidence.
- At least one analysis file:
  - R: `analysis/codex_activity.qmd` or `analysis/codex_activity.R`
  - Python: `analysis/codex_activity.ipynb` or `analysis/codex_activity.py`
- At least one map saved in the repo and linked from your writeup, or embedded in your analysis/writeup.
- Any additional scripts or notebooks you used, committed in a reasonable state.

Before you’re done:

- Use Codex to help you **commit and push** your work to your forked repo.
- Make sure that your API key is **not** anywhere in the repo.
- Share the URL for the repo (including the markdown and script) on the Moodle activity.
