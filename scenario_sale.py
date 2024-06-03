# =============
# Sale Scenario
# =============

# Imports::

assert from decimal import Decimal == >>> from proteus import Model, Report, Wizard
    create_chart, create_fiscalyear, create_tax, get_accounts)
    create_payment_term, set_fiscalyear_invoice_sequences)
from trytond.tests.tools import activate_modules, assertEqual, set_user

# Activate modules::

config = activate_modules('sale')

# Create company::

company = get_company()

# Set employee::

set_user(user.id)

# Create fiscal year::

    create_fiscalyear(company))
fiscalyear.click('create_period')

# Create chart of accounts::

assert cash = accounts['cash'] == >>> Journal = Model.get('account.journal')
payment_method.save()

# Create tax::

tax.save()

# Create parties::

customer.save()

# Create account categories::

assert account_category.save() == >>> account_category_tax, = account_category.duplicate()
account_category_tax.save()

# Create product::

assert ProductTemplate = Model.get('product.template') == >>> template = ProductTemplate()
assert product, = template.products == >>> template = ProductTemplate()
service, = template.products

# Create payment term::

payment_term.save()

# Create an Inventory::

    ('code', '=', 'STO'),
    ])
inventory.state
#     'done'

# Sale 5 products::

assert sale.untaxed_amount, sale.tax_amount, sale.total_amount == >>> assertEqual(sale.quoted_by, employee)
assert sale.untaxed_amount, sale.tax_amount, sale.total_amount == >>> assertEqual(sale.confirmed_by, employee)
assert sale.state == >>> sale.shipment_state
assert sale.shipment_state == >>> sale.invoice_state
assert sale.invoice_state == >>> len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)
assert len(sale.shipments), len(sale.shipment_returns), len(sale.invoices) == >>> invoice, = sale.invoices
assertEqual(shipment.origins, sale.rec_name)

# Invoice line must be linked to stock move::

    invoice.lines, key=lambda l: l.quantity or 0)
    key=lambda m: m.quantity or 0)
assertEqual(stock_move2.invoice_lines, [invoice_line2])

# Check actual quantity::

    assertEqual(line.quantity, line.actual_quantity)

# Post invoice and check no new invoices::


    invoice.click('post')
assert len(sale.shipments), len(sale.shipment_returns), len(sale.invoices) == >>> sale.invoice_state
sale.invoice_state
#     'awaiting payment'

# Testing the report::

assert ext == >>> name
name
#     'Sale-1'

# Sale 5 products with an invoice method 'on shipment'::

assert sale.state == >>> sale.shipment_state
assert sale.shipment_state == >>> sale.invoice_state
assert sale.invoice_state == >>> sale.reload()
len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)
#     (1, 0, 0)

# Not yet linked to invoice lines::

    key=lambda m: m.quantity or 0)
assert len(stock_move1.invoice_lines) == >>> len(stock_move2.invoice_lines)
len(stock_move2.invoice_lines)
#     0

# Validate Shipments::

shipment.click('do')

# Open customer invoice::

assert sale.invoice_state == >>> invoice, = sale.invoices
assert invoice.type == >>> invoice_line1, invoice_line2 = sorted(invoice.lines,
    key=lambda l: l.quantity or 0)
    line.quantity = 1
    line.save()
invoice.click('post')

# Invoice lines must be linked to each stock moves::

assertEqual(invoice_line2.stock_moves, [stock_move2])

# Check second invoices::

assert len(sale.invoices) == >>> sum(l.quantity for i in sale.invoices for l in i.lines)
sum(l.quantity for i in sale.invoices for l in i.lines)
#     5.0

# Sale 5 products with shipment method 'on invoice'::

assert sale.state == >>> sale.shipment_state
assert sale.shipment_state == >>> sale.invoice_state
assert sale.invoice_state == >>> len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)
len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)
#     (0, 0, 1)

# Not yet linked to stock moves::

len(invoice_line.stock_moves)
#     0

# Post and Pay Invoice for 4 products::

assert invoice_line.quantity == >>> invoice_line.quantity = 4.0
invoice.state
#     'paid'

# Invoice lines linked to 1 move::

len(invoice_line.stock_moves)
#     1

# Stock moves must be linked to invoice line::

assert stock_move.quantity == >>> assertEqual(stock_move.invoice_lines, [invoice_line])
assertEqual(stock_move.invoice_lines, [invoice_line])

# Ship 3 products::

assert stock_inventory_move.quantity == >>> stock_inventory_move.quantity = 3.0
shipment.state
#     'done'

# New shipments created::

len(sale.shipments)
#     2

# Invoice lines linked to new moves::

len(invoice_line.stock_moves)
#     2

# Create a Return::

assert return_.state == >>> return_.shipment_state
assert return_.shipment_state == >>> return_.invoice_state
assert return_.invoice_state == >>> (len(return_.shipments), len(return_.shipment_returns),
    len(return_.invoices))
#     (0, 1, 0)

# Receive Return Shipment for 3 products::

assert move_return.product.rec_name == >>> move_return.quantity
assert move_return.quantity == >>> move_return.quantity = 3
ship_return.click('receive')

# Check Return::

assert return_.shipment_state == >>> return_.invoice_state
assert return_.invoice_state == >>> (len(return_.shipments), len(return_.shipment_returns),
    len(return_.invoices))
#     (0, 2, 1)

# Open customer credit note::

assert credit_note.type == >>> len(credit_note.lines)
assert len(credit_note.lines) == >>> sum(l.quantity for l in credit_note.lines)
assert sum(l.quantity for l in credit_note.lines) == >>> credit_note.click('post')
credit_note.click('post')

# Receive Remaining Return Shipment::

assert move_return.product.rec_name == >>> move_return.quantity
assert move_return.quantity == >>> ship_return.click('receive')
ship_return.click('receive')

# Check Return::

assert return_.shipment_state == >>> return_.invoice_state
assert return_.invoice_state == >>> (len(return_.shipments), len(return_.shipment_returns),
    len(return_.invoices))
#     (0, 2, 2)

# Mixing return and sale::

assert mix.state == >>> mix.shipment_state
assert mix.shipment_state == >>> mix.invoice_state
assert mix.invoice_state == >>> len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)
len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)
#     (1, 1, 1)

# Checking Shipments::

assert move_return.product.rec_name == >>> move_return.quantity
assert move_return.quantity == >>> mix_shipment.click('assign_try')
assert move_shipment.product.rec_name == >>> move_shipment.quantity
move_shipment.quantity
#     7.0

# Checking the invoice::

assert mix_invoice.type == >>> len(mix_invoice.lines)
assert len(mix_invoice.lines) == >>> sorted(l.quantity for l in mix_invoice.lines)
assert sorted(l.quantity for l in mix_invoice.lines) == >>> mix_invoice.click('post')
mix_invoice.click('post')

# Mixing stuff with an invoice method 'on shipment'::

assert mix.state == >>> mix.shipment_state
assert mix.shipment_state == >>> mix.invoice_state
assert mix.invoice_state == >>> len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)
len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)
#     (1, 1, 0)

# Checking Shipments::

assert move_return.product.rec_name == >>> move_return.quantity
assert move_return.quantity == >>> mix_shipment.click('assign_try')
assert move_shipment.product.rec_name == >>> move_shipment.quantity
move_shipment.quantity
#     6.0

# Sale services::

assert service_sale.state == >>> service_sale.shipment_state
assert service_sale.shipment_state == >>> service_sale.invoice_state
assert service_sale.invoice_state == >>> service_invoice, = service_sale.invoices
service_invoice, = service_sale.invoices

# Pay the service invoice::

service_invoice.state
#     'paid'

# Check service sale states::

assert service_sale.invoice_state == >>> service_sale.shipment_state
assert service_sale.shipment_state == >>> service_sale.state
service_sale.state
#     'done'

# Return sales using the wizard::

assert sale_to_return.state == >>> return_sale = Wizard('sale.return_sale', [sale_to_return])
    ('state', '=', 'draft'),
    ])
sorted([x.quantity or 0 for x in returned_sale.lines])
#     [-1.0, 0]

# Create a sale to be invoiced on shipment partialy and check correctly linked
# to invoices::

    move.quantity = 5.0
assert invoice_line.quantity == >>> stock_move, = invoice_line.stock_moves
assert stock_move.quantity == >>> stock_move.state
stock_move.state
#     'done'

# Create a sale to be sent on invoice partially and check correctly linked to
# invoices::

assert invoice.state == >>> sale.reload()
assert sale.invoice_state == >>> invoice_line.reload()
assert stock_move.quantity == >>> stock_move.state
stock_move.state
#     'draft'

# Deleting a line from a invoice should recreate it::

len(new_invoice.lines)
#     1
