# Implementation Plan: Product Reviews

**Feature**: `002-product-reviews`

**Spec**: `specs/002-product-reviews/spec.md`

## Summary

Add product reviews to the ecommerce app. Shoppers can submit a reviewer name, rating from 1 to 5, and comment from a product detail page. Product detail pages display all reviews and an average rating. Reviews are stored in SQLite and do not require authentication.

## Technical Context

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2 templates
- Bootstrap 5
- pytest

## Data Model

### Review

- `id`: integer primary key
- `product_id`: foreign key to `Product`
- `reviewer_name`: required string
- `rating`: required integer, 1 through 5
- `comment`: optional text, max 500 characters recommended
- `created_at`: timestamp

Relationship:

- `Product` has many `Review` records.
- `Review` belongs to one `Product`.

## Route Design

- `POST /products/<product_id>/reviews`
  - Validates reviewer name and rating.
  - Saves review to SQLite.
  - Redirects back to the product detail page.
  - Shows a flash message for success or validation errors.

Existing route to update:

- `GET /products/<product_id>`
  - Loads reviews for the product.
  - Calculates average rating.
  - Renders review form, average rating, and review list.

## UI Design

Update `templates/product_detail.html`:

- Add average rating near product details.
- Add review submission form.
- Add review list below the product information.
- Show an empty state when no reviews exist.

## Validation Rules

- Reviewer name is required.
- Rating is required.
- Rating must be between 1 and 5.
- Comment is optional.
- Comment should be limited to 500 characters.
- No edit or delete controls in this version.

## Testing Strategy

Add pytest coverage for:

- Product detail page shows empty review state.
- Valid review submission creates a database record.
- Product detail page displays submitted review.
- Average rating is calculated correctly.
- Invalid rating is rejected.
- Missing reviewer name is rejected.

## Implementation Order

1. Add `Review` model.
2. Add relationship from `Product` to `Review`.
3. Update product detail route to load reviews and average rating.
4. Add review creation route.
5. Update product detail template.
6. Add tests.
7. Run `pytest`.
8. Run the app locally and manually verify the workflow.
