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

## 2. Install Python And Spec-Kit On macOS

macOS usually ships with system Python, but you should install your own development Python instead of relying on the system copy.

### Option A: Install Python With Homebrew

Install Homebrew if you do not already have it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python:

```bash
brew install python@3.11
python3.11 --version
python3.11 -m pip --version
```

If `python3.11` works but `python` does not, use `python3.11` in commands or add an alias:

```bash
echo 'alias python=python3.11' >> ~/.zshrc
echo 'alias pip="python3.11 -m pip"' >> ~/.zshrc
source ~/.zshrc
```

### Option B: Install Python From python.org

1. Download Python 3.11+ from <https://www.python.org/downloads/macos/>.
2. Run the macOS installer.
3. Open a new terminal.
4. Verify:

```bash
python3 --version
python3 -m pip --version
```

### Create The Virtual Environment On macOS

From the project folder:

```bash
cd ~/Documents/SpecDrivenDevelopment
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the app:

```bash
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

Run tests:

```bash
pytest
```

### Install Spec-Kit On macOS

Spec-Kit supports Linux/macOS with Bash scripts by default. Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen the terminal, then verify:

```bash
uv --version
```

Install Spec-Kit from the official GitHub repository:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
specify version
specify self check
```

Initialize Spec-Kit in a macOS project:

```bash
cd ~/Documents/SpecDrivenDevelopment
specify init . --script sh --integration copilot
```

If you prefer one-time usage without installing the `specify` command permanently:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init . --script sh --integration copilot
```

The official docs note that Bash scripts are the default on Linux/macOS, while PowerShell scripts are the default on Windows.

## 3. Install VS Code Extensions

Recommended extensions:

- Python by Microsoft.
- GitHub Copilot.
- GitHub Copilot Chat.

Open this project:

```powershell
cd C:\Users\MSUSERSL123\Documents\SpecDrivenDevelopment
code .
```

## 4. Create The Python Virtual Environment

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

## 5. Install Spec-Kit

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

## 6. What Spec-Kit Added

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

## 7. Recommended Spec-Kit Workflow

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

## 8. After `/speckit.specify`, What Happens Next?

`/speckit.specify` does not implement code. It creates or updates a feature specification, usually in a folder like:

```text
specs/002-product-reviews/spec.md
specs/003-wishlist-feature/spec.md
```

After running `/speckit.specify`, check these things:

```powershell
git status
dir specs
```

Open the new `spec.md` and confirm:

- The user stories are correct.
- The acceptance scenarios are correct.
- The requirements are specific.
- The out-of-scope items are clear.
- The status is ready to continue or only marked draft because clarification is still needed.

If you created more than one feature, do not implement both at once while learning. Pick one feature, finish it, test it, commit it, then move to the next feature.

Current example:

```text
Feature 1: specs/002-product-reviews/
Feature 2: specs/003-wishlist-feature/
```

Recommended order:

```text
Finish product reviews first, then wishlist.
```

## 9. How To Make Sure Plan, Tasks, Implement, And Tests Are Done

Use this checklist for every feature.

### Step 1: Specify

Creates the feature specification.

```text
/speckit.specify Add product reviews to the ecommerce app...
```

Done when:

- `specs/<feature-name>/spec.md` exists.
- User stories and acceptance criteria are readable.
- You understand exactly what the feature should do.

### Step 2: Clarify

Resolves ambiguity before design and planning.

```text
/speckit.clarify Focus on required fields, edge cases, validation, and out-of-scope behavior.
```

Done when:

- Questions are answered.
- The spec no longer has unclear assumptions.
- Edge cases are captured.

### Step 3: Checklist

Checks specification quality.

```text
/speckit.checklist
```

Done when:

- A checklist exists under `specs/<feature-name>/checklists/`.
- Important checklist items are passed or deliberately resolved.

### Step 4: Plan

Creates the technical design and implementation plan.

```text
/speckit.plan Use Flask, SQLAlchemy, SQLite, Jinja2, Bootstrap 5, and pytest...
```

Done when:

- `specs/<feature-name>/plan.md` exists.
- It describes model changes.
- It describes route changes.
- It describes template/UI changes.
- It describes tests.
- It has a sensible implementation order.

### Step 5: Tasks

Breaks the plan into ordered work items.

```text
/speckit.tasks
```

Done when:

- `specs/<feature-name>/tasks.md` exists.
- Tasks are small enough to implement.
- Tasks are grouped by phase.
- Tasks include tests and verification.

### Step 6: Analyze

Checks whether spec, plan, and tasks agree with each other.

```text
/speckit.analyze
```

Done when:

- No major contradictions remain.
- Every important requirement has a task.
- Every task maps back to the feature.

### Step 7: Implement

Writes the actual code.

```text
/speckit.implement
```

Done when:

- Application code changed.
- Templates changed if UI was required.
- Tests were added or updated.
- The feature can be used in the running app.

### Step 8: Test

Verifies the implementation.

```powershell
pytest
python run.py
```

Done when:

- Tests pass.
- The app starts.
- You manually verify the feature in the browser.
- You commit the completed feature.

```powershell
git status
git add .
git commit -m "Add product reviews"
git push
```

## 10. Constitution -> Specify -> Plan -> Tasks -> Implement -> Test

Think of the workflow like this:

```text
Constitution = project rules
Specify      = what users need
Clarify      = remove confusion
Checklist    = validate requirement quality
Plan         = how the app will be changed
Tasks        = ordered engineering checklist
Analyze      = consistency check before coding
Implement    = write the code
Test         = prove it works
```

### Constitution

Use once at the start, then update only when your project principles change.

Example:

```text
/speckit.constitution This is a Flask ecommerce learning project. Use Python 3.11, Flask, SQLAlchemy, SQLite, Jinja2, Bootstrap 5, and pytest. Requirements live in local markdown files. Features must be small, testable, and easy to explain.
```

### Specify

Describe the feature from the user perspective.

Example:

```text
/speckit.specify Add wishlist support. Shoppers can add products to a session-based wishlist, view wishlist items, remove items, and move items to cart. Authentication is not required.
```

### Plan

Describe the technical implementation.

Example:

```text
/speckit.plan Use Flask sessions for wishlist storage. Add wishlist helper functions, routes, Jinja2 templates, Bootstrap buttons, and pytest coverage. Do not add a database table for wishlist in v1.
```

### Tasks

Ask Spec-Kit to create the implementation checklist.

```text
/speckit.tasks
```

### Implement

Ask the coding agent to execute the tasks.

```text
/speckit.implement
```

### Test

Run automated and manual checks.

```powershell
pytest
python run.py
```

## 11. Current Feature Example: Product Reviews

You already ran:

```text
/speckit.specify Add product reviews to the ecommerce app. Shoppers can add a review to a product detail page with reviewer name, rating from 1 to 5, and comment. Product detail pages show all reviews and average rating. Authentication is not required. Reviews should be stored in SQLite. Reviews cannot be edited or deleted in this version.
```

Next commands:

```text
/speckit.clarify Focus on required fields, comment length, rating validation, empty review states, and whether one user can submit multiple reviews.
```

```text
/speckit.checklist
```

```text
/speckit.plan Use the existing Flask app factory, SQLAlchemy models, SQLite database, Jinja2 templates, Bootstrap 5, and pytest. Add a Review model with product_id, reviewer_name, rating, comment, and created_at. Add a POST route to create reviews from product detail pages. Display average rating and reviews on product detail. Add tests for validation and display.
```

```text
/speckit.tasks
```

```text
/speckit.analyze
```

```text
/speckit.implement
```

Then verify:

```powershell
pytest
python run.py
```

Expected files for this feature:

```text
specs/002-product-reviews/spec.md
specs/002-product-reviews/checklists/requirements.md
specs/002-product-reviews/plan.md
specs/002-product-reviews/tasks.md
```

## 12. Current Feature Example: Wishlist

You already ran:

```text
/speckit.specify Add a wishlist feature. Shoppers can add products to a wishlist from catalog and product detail pages. The wishlist is stored in the session for v1. Shoppers can view wishlist items, remove items, and move an item from wishlist to cart. Authentication is not required.
```

Next commands:

```text
/speckit.clarify Focus on duplicate wishlist entries, empty wishlist behavior, moving wishlist items to cart, and session-only persistence.
```

```text
/speckit.checklist
```

```text
/speckit.plan Use the existing Flask session approach, similar to the cart. Add wishlist helper functions, routes for add/remove/view/move-to-cart, Bootstrap template updates, and pytest coverage for wishlist behavior. Do not create a database table for wishlist v1.
```

```text
/speckit.tasks
```

```text
/speckit.analyze
```

```text
/speckit.implement
```

Then verify:

```powershell
pytest
python run.py
```

Expected files for this feature:

```text
specs/003-wishlist-feature/spec.md
specs/003-wishlist-feature/checklists/requirements.md
specs/003-wishlist-feature/plan.md
specs/003-wishlist-feature/tasks.md
```

## 13. What Each Prompt Means

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

## 14. Example Feature: Product Reviews

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

## 15. Example Feature: Wishlist

```text
/speckit.specify Add a wishlist feature. Shoppers can add products to a wishlist from catalog and product detail pages. The wishlist is stored in the session for v1. Shoppers can view wishlist items, remove items, and move an item from wishlist to cart. Authentication is not required.
```

```text
/speckit.plan Use the existing Flask session approach, similar to the cart. Add wishlist helper functions, routes for add/remove/view/move-to-cart, Bootstrap template updates, and pytest coverage for wishlist behavior.
```

## 16. Example Improvement: Catalog Pagination

```text
/speckit.specify Improve the product catalog with pagination. The catalog should show 12 products per page, preserve search and category filters between pages, and display previous/next controls. The UI should remain responsive.
```

```text
/speckit.plan Use Flask query parameters for page number, SQLAlchemy pagination or limit/offset, existing Jinja2 templates, Bootstrap pagination controls, and tests for filtered pagination.
```

## 17. Example Improvement: Admin Authentication

```text
/speckit.specify Add simple admin authentication. Admin pages should require login. A single admin username and password can be configured with environment variables. If environment variables are missing, use safe local development defaults documented in README. Shopper catalog, cart, and checkout remain public.
```

```text
/speckit.plan Use Flask sessions for admin login state. Add login/logout routes, protect all /admin routes, add environment variable configuration, update templates, and add tests that admin pages redirect when logged out.
```

## 18. Sample Feature Prompts For Practice

Use these prompts to practice Spec-Kit feature development. For each idea, start with `/speckit.specify`, then run `/speckit.clarify`, `/speckit.checklist`, `/speckit.plan`, `/speckit.tasks`, `/speckit.analyze`, `/speckit.implement`, and finally `pytest`.

### 1. Product Reviews

```text
/speckit.specify Add product reviews to the ecommerce app. Shoppers can add a review to a product detail page with reviewer name, rating from 1 to 5, and comment. Product detail pages show all reviews and average rating. Authentication is not required. Reviews should be stored in SQLite. Reviews cannot be edited or deleted in this version.
```

```text
/speckit.plan Use Flask, SQLAlchemy, SQLite, Jinja2 templates, Bootstrap 5, and pytest. Add a Review model related to Product, a review submission route, validation, product detail display, and tests.
```

### 2. Wishlist

```text
/speckit.specify Add a wishlist feature. Shoppers can add products to a wishlist from catalog and product detail pages. The wishlist is stored in the session for v1. Shoppers can view wishlist items, remove items, and move an item from wishlist to cart. Authentication is not required.
```

```text
/speckit.plan Use Flask sessions for wishlist storage. Add wishlist helper functions, routes for add, remove, view, and move-to-cart. Update catalog, product detail, navbar, and add pytest coverage.
```

### 3. Catalog Pagination

```text
/speckit.specify Improve the product catalog with pagination. The catalog should show 12 products per page, preserve search and category filters between pages, and display previous and next controls. The UI should remain responsive.
```

```text
/speckit.plan Use SQLAlchemy pagination or limit/offset, Flask query parameters, Bootstrap pagination controls, and tests for normal, filtered, and empty result pages.
```

### 4. Admin Authentication

```text
/speckit.specify Add simple admin authentication. Admin pages should require login. A single admin username and password can be configured with environment variables. Shopper catalog, cart, and checkout remain public.
```

```text
/speckit.plan Use Flask sessions for admin login state. Add login and logout routes, protect all /admin routes, update templates, read credentials from environment variables, and test protected redirects.
```

### 5. Product Sorting

```text
/speckit.specify Add sorting to the product catalog. Shoppers can sort products by name, price low to high, price high to low, and newest first. Sorting should work with search and category filters.
```

```text
/speckit.plan Add a sort query parameter to the catalog route, map allowed sort values to SQLAlchemy order clauses, preserve filters in the UI, and test each sorting mode.
```

### 6. Product Stock Warnings

```text
/speckit.specify Add stock warnings to product cards and product detail pages. Products with stock less than 5 should show "Only a few left". Products with zero stock should show "Out of stock" and cannot be added to cart.
```

```text
/speckit.plan Use the existing Product.stock field. Update add-to-cart validation, catalog cards, product detail template, cart behavior, and tests for low-stock and out-of-stock products.
```

### 7. Coupon Codes

```text
/speckit.specify Add simple coupon codes at checkout. Shoppers can enter a coupon code in the cart or checkout page. Supported demo coupons are SAVE10 for 10 percent off and FREESHIP for a shipping discount display. Coupon discounts should be shown in the order summary. Real payment integration is not required.
```

```text
/speckit.plan Store coupon choice in the session, add validation for allowed coupon codes, update cart and checkout totals, persist discount information on orders if needed, and add tests.
```

### 8. Order Search In Admin

```text
/speckit.specify Add admin order search. Admin users can search orders by customer name, email, or order id. The order list should show matching results and preserve the search term in the input.
```

```text
/speckit.plan Update the admin orders route with optional q parameter, query Order fields safely, update the admin orders template, and add tests for name, email, order id, and no-result searches.
```

### 9. Product Image Upload URL Validation

```text
/speckit.specify Improve admin product management by validating image URLs. When creating or editing a product, image_url must be a valid http or https URL. Invalid image URLs should show a clear validation message and should not save changes.
```

```text
/speckit.plan Add server-side URL validation in product create and edit routes, preserve form values on validation errors, update templates for error messages, and add tests.
```

### 10. Category Management

```text
/speckit.specify Add admin category management. Admin users can create, edit, and delete categories. Categories with products cannot be deleted until products are moved or deleted. Product create and edit forms should use the updated category list.
```

```text
/speckit.plan Add admin category routes and templates, enforce delete protection for categories with products, update navigation if needed, and add tests for create, edit, protected delete, and successful delete.
```

### 11. Recently Viewed Products

```text
/speckit.specify Add recently viewed products. When a shopper opens product detail pages, the app stores the last five viewed products in the session. The catalog page and product detail page should show a compact recently viewed section.
```

```text
/speckit.plan Use Flask session storage for recent product ids, avoid duplicates, keep only the five most recent items, update templates, and test ordering and duplicate behavior.
```

### 12. Order Confirmation Email Preview

```text
/speckit.specify Add an order confirmation email preview. After checkout, the success page should show a preview of the email that would be sent, including customer name, order id, line items, total, and payment status. Actual email sending is not required.
```

```text
/speckit.plan Build an email-preview partial/template using existing Order and OrderItem data. Render it on the order success page and admin order detail page. Add tests that confirmation content appears after checkout.
```

### 13. Product Recommendations

```text
/speckit.specify Add simple product recommendations. Product detail pages should show up to four recommended products from the same category, excluding the current product. If fewer than four exist, show what is available.
```

```text
/speckit.plan Update the product detail route to query same-category products, update the template with recommendation cards, and add tests for exclusion of the current product and limited result count.
```

### 14. Checkout Form Validation

```text
/speckit.specify Improve checkout validation. Customer name, email, address, and city are required. Email must look valid. The checkout page should show field-level validation messages and preserve entered values after validation errors.
```

```text
/speckit.plan Add server-side validation in the checkout route, pass errors and form data back to the template, update checkout UI with Bootstrap validation styling, and add tests for invalid and valid checkout.
```

## 19. Best Practices

- Start every feature with a clear user problem.
- Keep `/speckit.specify` mostly product-focused.
- Put technical stack details in `/speckit.plan`.
- Use `/speckit.clarify` whenever requirements are fuzzy.
- Use `/speckit.analyze` before coding.
- Commit before and after each feature.
- Run tests after implementation.
- Keep real payment integration out of learning versions unless you intentionally create a payment feature.
- Do not assume `/speckit.specify` implemented code. It only prepares requirements.
- Do not implement two new features at once while learning. Finish one feature, test it, commit it, then start the next.

## 20. Git And GitHub Commands

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
