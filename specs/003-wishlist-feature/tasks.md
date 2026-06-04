# Tasks: Wishlist Feature

**Feature**: `003-wishlist-feature`

## Phase 1: Session Helpers

- [ ] T001 Add `_wishlist()` helper in `app/routes.py`.
- [ ] T002 Add `_wishlist_items()` helper to load products from session IDs.
- [ ] T003 Add `_wishlist_count()` helper.
- [ ] T004 Update context processor to expose `wishlist_count`.

## Phase 2: Routes

- [ ] T005 Add `GET /wishlist` route.
- [ ] T006 Add `POST /wishlist/add/<product_id>` route.
- [ ] T007 Add `POST /wishlist/remove/<product_id>` route.
- [ ] T008 Add `POST /wishlist/move-to-cart/<product_id>` route.
- [ ] T009 Prevent duplicate wishlist entries.
- [ ] T010 Ensure move-to-cart removes the item from wishlist.

## Phase 3: Templates

- [ ] T011 Add `templates/wishlist.html`.
- [ ] T012 Add wishlist link and count to `templates/base.html`.
- [ ] T013 Add add-to-wishlist action to catalog cards.
- [ ] T014 Add add-to-wishlist action to product detail page.
- [ ] T015 Add empty wishlist state.

## Phase 4: Tests

- [ ] T016 Add test for adding a product to wishlist.
- [ ] T017 Add test for viewing wishlist item.
- [ ] T018 Add test that duplicate adds do not duplicate display rows.
- [ ] T019 Add test for removing a wishlist item.
- [ ] T020 Add test for moving wishlist item to cart.
- [ ] T021 Add test that wishlist routes do not require authentication.

## Phase 5: Verification

- [ ] T022 Run `pytest`.
- [ ] T023 Run `python run.py`.
- [ ] T024 Manually add a product to wishlist from catalog.
- [ ] T025 Manually add a product to wishlist from product detail.
- [ ] T026 Manually move a wishlist item to cart.
