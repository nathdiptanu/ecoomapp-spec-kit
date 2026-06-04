# Tasks: Wishlist Feature

**Feature**: `003-wishlist-feature`

## Phase 1: Session Helpers

- [x] T001 Add `_wishlist()` helper in `app/routes.py`.
- [x] T002 Add `_wishlist_items()` helper to load products from session IDs.
- [x] T003 Add `_wishlist_count()` helper.
- [x] T004 Update context processor to expose `wishlist_count`.

## Phase 2: Routes

- [x] T005 Add `GET /wishlist` route.
- [x] T006 Add `POST /wishlist/add/<product_id>` route.
- [x] T007 Add `POST /wishlist/remove/<product_id>` route.
- [x] T008 Add `POST /wishlist/move-to-cart/<product_id>` route.
- [x] T009 Prevent duplicate wishlist entries.
- [x] T010 Ensure move-to-cart removes the item from wishlist.

## Phase 3: Templates

- [x] T011 Add `templates/wishlist.html`.
- [x] T012 Add wishlist link and count to `templates/base.html`.
- [x] T013 Add add-to-wishlist action to catalog cards.
- [x] T014 Add add-to-wishlist action to product detail page.
- [x] T015 Add empty wishlist state.

## Phase 4: Tests

- [x] T016 Add test for adding a product to wishlist.
- [x] T017 Add test for viewing wishlist item.
- [x] T018 Add test that duplicate adds do not duplicate display rows.
- [x] T019 Add test for removing a wishlist item.
- [x] T020 Add test for moving wishlist item to cart.
- [x] T021 Add test that wishlist routes do not require authentication.

## Phase 5: Verification

- [x] T022 Run `pytest`.
- [x] T023 Run `python run.py`.
- [x] T024 Manually add a product to wishlist from catalog.
- [x] T025 Manually add a product to wishlist from product detail.
- [x] T026 Manually move a wishlist item to cart.
