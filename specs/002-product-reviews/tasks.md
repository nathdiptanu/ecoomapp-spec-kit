# Tasks: Product Reviews

**Feature**: `002-product-reviews`

## Phase 1: Model

- [ ] T001 Add `Review` model in `app/models.py`.
- [ ] T002 Add `reviews` relationship on `Product`.
- [ ] T003 Add `average_rating` helper or route-level calculation.

## Phase 2: Routes

- [ ] T004 Update `product_detail` route to load reviews and average rating.
- [ ] T005 Add `POST /products/<product_id>/reviews` route.
- [ ] T006 Validate required reviewer name.
- [ ] T007 Validate rating is an integer from 1 to 5.
- [ ] T008 Validate comment length.
- [ ] T009 Persist valid reviews to SQLite.
- [ ] T010 Redirect back to product detail after review submission.

## Phase 3: Templates

- [ ] T011 Update `templates/product_detail.html` with review form.
- [ ] T012 Display average rating.
- [ ] T013 Display all reviews.
- [ ] T014 Display empty review state.
- [ ] T015 Display validation and success flash messages.

## Phase 4: Tests

- [ ] T016 Add test for empty review state on product detail.
- [ ] T017 Add test for valid review submission.
- [ ] T018 Add test that submitted review appears on product detail.
- [ ] T019 Add test for average rating calculation.
- [ ] T020 Add test for invalid rating rejection.
- [ ] T021 Add test for missing reviewer name rejection.

## Phase 5: Verification

- [ ] T022 Run `pytest`.
- [ ] T023 Run `python run.py`.
- [ ] T024 Manually submit a review from a product detail page.
- [ ] T025 Confirm no edit/delete review controls are visible.
