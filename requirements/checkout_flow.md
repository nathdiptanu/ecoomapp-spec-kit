# Checkout Flow Requirements

## Cart
- Cart data can be stored in the browser session for v1.
- Cart summary shows product name, unit price, quantity, line total, and grand total.
- Quantity updates must support setting a quantity to zero to remove an item.

## Checkout
- Checkout requires full name, email, address, and city.
- Buy Now simulates payment success.
- A successful checkout creates one order and one order item per cart line.
- The cart is cleared after successful checkout.

## Acceptance Criteria
- A shopper can complete checkout without entering card data.
- Admin can see the new order after checkout.
- Order detail includes customer details, line items, payment status, and total.
