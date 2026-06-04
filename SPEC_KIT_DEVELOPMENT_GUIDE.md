# Spec-Kit Development Guide For SpecShop

This guide explains how to install Python, set up this Flask ecommerce project, install Spec-Kit, and use Spec-Kit prompts to develop new features from requirements through implementation.

Official Spec-Kit docs:

- Installation: <https://github.github.com/spec-kit/installation.html>
- Quick start: <https://github.github.com/spec-kit/quickstart.html>
- Repository: <https://github.com/github/spec-kit>

## 1. Install Python On Windows

1. Download Python 3.11.1 from <https://www.python.org/downloads/release/python-3111/>.
2. Run the installer.
3. Select **Add python.exe to PATH**.
4. Select **Customize installation**.
5. Keep `pip` selected.
6. Finish installation.
7. Close and reopen PowerShell or VS Code.

Verify:

```powershell
python --version
pip --version
py -0p
```

Expected:

```text
Python 3.11.1
```

If `python --version` says Python was not found:

1. Open **Windows Settings**.
2. Go to **Apps > Advanced app settings > App execution aliases**.
3. Turn off aliases for `python.exe` and `python3.exe`.
4. Reinstall Python and select **Add python.exe to PATH**.
5. Restart VS Code and terminal.

## 2. Install VS Code Extensions

Recommended extensions:

- Python by Microsoft.
- GitHub Copilot.
- GitHub Copilot Chat.

Open this project:

```powershell
cd C:\Users\MSUSERSL123\Documents\SpecDrivenDevelopment
code .
```

## 3. Create The Python Virtual Environment

From the VS Code terminal:

```powershell
cd C:\Users\MSUSERSL123\Documents\SpecDrivenDevelopment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Run the Flask app:

```powershell
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

Run tests:

```powershell
pytest
```

## 4. Install Spec-Kit

Spec-Kit should be installed from the official GitHub repository. Do not install unrelated similarly named PyPI packages.

Install `uv`:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen PowerShell, then verify:

```powershell
uv --version
```

Install Spec-Kit persistently:

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify version
specify self check
```

Initialize Spec-Kit in this repository:

```powershell
cd C:\Users\MSUSERSL123\Documents\SpecDrivenDevelopment
specify init . --script ps --integration copilot
```

If the directory is not empty, Spec-Kit warns that template files may be merged. That is expected when initializing inside an existing project. Commit your code before running it when possible.

## 5. What Spec-Kit Added

Spec-Kit adds project workflow files:

```text
.specify/
.github/prompts/
.github/agents/
.vscode/
```

Important files:

- `.specify/memory/constitution.md`: project rules and principles.
- `.specify/templates/spec-template.md`: default specification template.
- `.specify/templates/plan-template.md`: default plan template.
- `.specify/templates/tasks-template.md`: default task template.
- `.github/prompts/`: slash prompt definitions for GitHub Copilot.
- `.github/agents/`: agent definitions for GitHub Copilot.

## 6. Recommended Spec-Kit Workflow

For quick experiments:

```text
/speckit.specify -> /speckit.plan -> /speckit.tasks -> /speckit.implement
```

For serious feature development:

```text
/speckit.constitution -> /speckit.specify -> /speckit.clarify -> /speckit.checklist -> /speckit.plan -> /speckit.tasks -> /speckit.analyze -> /speckit.implement
```

Use Git between features:

```powershell
git status
git add .
git commit -m "Save current work"
```

## 7. What Each Prompt Means

### `/speckit.constitution`

Defines the rules of the project. Use it once at the beginning and update it when your engineering principles change.

Use it for:

- Tech boundaries.
- Testing expectations.
- Security principles.
- Code style.
- What is in scope or out of scope.
- How decisions should be made.

Example:

```text
/speckit.constitution This is a Flask ecommerce learning project. Use Python 3.11, Flask, SQLAlchemy, SQLite, Jinja2, Bootstrap 5, and pytest. Keep requirements in local markdown files. Avoid real payment processing in v1. Every feature should include tests for the main workflow. Prefer simple readable code over complex abstractions.
```

### `/speckit.specify`

Creates the product specification. Focus on what the user needs and why. Avoid deep technical implementation details here.

Good specification prompts include:

- User goal.
- User roles.
- Core workflow.
- Acceptance criteria.
- Out-of-scope items.

Example:

```text
/speckit.specify Add product reviews. Shoppers can submit a reviewer name, rating from 1 to 5, and comment from the product detail page. Product pages display reviews and average rating. Authentication is not required. Reviews can be created but not edited or deleted in this version.
```

### `/speckit.clarify`

Finds unclear requirements before planning. Use this when a feature could be interpreted in more than one way.

Example:

```text
/speckit.clarify Focus on review validation, rating rules, anonymous users, and whether reviews can be edited or deleted.
```

### `/speckit.checklist`

Validates the quality of the specification. It helps catch missing acceptance criteria, vague wording, or contradictions before design work begins.

Example:

```text
/speckit.checklist
```

### `/speckit.plan`

Creates the technical implementation plan. This is where you mention stack and architecture.

Use it for:

- Framework choices.
- Database changes.
- Route/API changes.
- UI approach.
- Testing approach.
- Migration or seed data concerns.

Example:

```text
/speckit.plan Use Flask, SQLAlchemy, SQLite, Jinja2 templates, Bootstrap 5, and pytest. Add a Review model related to Product. Add a POST route for review creation. Update the product detail page to show average rating and review list. Add tests for creating and displaying reviews.
```

### `/speckit.tasks`

Breaks the plan into implementation tasks. The output should be actionable and ordered.

Example:

```text
/speckit.tasks
```

Expected task types:

- Add model.
- Update seed or database setup.
- Add route.
- Update template.
- Add validation.
- Add tests.
- Run verification.

### `/speckit.analyze`

Checks consistency between the specification, plan, and tasks. Use it before implementation so mismatches are fixed early.

Example:

```text
/speckit.analyze
```

### `/speckit.implement`

Executes the tasks and writes code. Use it after the spec, plan, and tasks are clear.

Example:

```text
/speckit.implement
```

After implementation, run:

```powershell
pytest
python run.py
```

## 8. Example Feature: Product Reviews

### Step 1: Specify

```text
/speckit.specify Add product reviews to the ecommerce app. Shoppers can add a review to a product detail page with reviewer name, rating from 1 to 5, and comment. Product detail pages show all reviews and average rating. Authentication is not required. Reviews should be stored in SQLite. Reviews cannot be edited or deleted in this version.
```

### Step 2: Clarify

```text
/speckit.clarify Focus on required fields, comment length, rating validation, empty review states, and whether one user can submit multiple reviews.
```

Recommended answers:

```text
Reviewer name and rating are required. Comment is optional with a 500 character limit. Rating must be 1 through 5. Show "No reviews yet" when empty. Multiple reviews from the same name are allowed for this learning version.
```

### Step 3: Plan

```text
/speckit.plan Use the existing Flask app factory, SQLAlchemy models, SQLite database, Jinja2 templates, Bootstrap 5, and pytest. Add a Review model with product_id, reviewer_name, rating, comment, and created_at. Add a POST route to create reviews from product detail pages. Display average rating and reviews on product detail. Add tests for validation and display.
```

### Step 4: Tasks

```text
/speckit.tasks
```

### Step 5: Analyze

```text
/speckit.analyze
```

### Step 6: Implement

```text
/speckit.implement
```

### Step 7: Test

```powershell
pytest
python run.py
```

## 9. Example Feature: Wishlist

```text
/speckit.specify Add a wishlist feature. Shoppers can add products to a wishlist from catalog and product detail pages. The wishlist is stored in the session for v1. Shoppers can view wishlist items, remove items, and move an item from wishlist to cart. Authentication is not required.
```

```text
/speckit.plan Use the existing Flask session approach, similar to the cart. Add wishlist helper functions, routes for add/remove/view/move-to-cart, Bootstrap template updates, and pytest coverage for wishlist behavior.
```

## 10. Example Improvement: Catalog Pagination

```text
/speckit.specify Improve the product catalog with pagination. The catalog should show 12 products per page, preserve search and category filters between pages, and display previous/next controls. The UI should remain responsive.
```

```text
/speckit.plan Use Flask query parameters for page number, SQLAlchemy pagination or limit/offset, existing Jinja2 templates, Bootstrap pagination controls, and tests for filtered pagination.
```

## 11. Example Improvement: Admin Authentication

```text
/speckit.specify Add simple admin authentication. Admin pages should require login. A single admin username and password can be configured with environment variables. If environment variables are missing, use safe local development defaults documented in README. Shopper catalog, cart, and checkout remain public.
```

```text
/speckit.plan Use Flask sessions for admin login state. Add login/logout routes, protect all /admin routes, add environment variable configuration, update templates, and add tests that admin pages redirect when logged out.
```

## 12. Best Practices

- Start every feature with a clear user problem.
- Keep `/speckit.specify` mostly product-focused.
- Put technical stack details in `/speckit.plan`.
- Use `/speckit.clarify` whenever requirements are fuzzy.
- Use `/speckit.analyze` before coding.
- Commit before and after each feature.
- Run tests after implementation.
- Keep real payment integration out of learning versions unless you intentionally create a payment feature.

## 13. Git And GitHub Commands

Add the GitHub remote:

```powershell
git remote add origin https://github.com/nathdiptanu/ecoomapp-spec-kit.git
```

Commit:

```powershell
git add .
git commit -m "Initialize Spec-Kit ecommerce app"
```

Push:

```powershell
git push -u origin master
```

For later changes:

```powershell
git status
git add .
git commit -m "Add feature name"
git push
```
