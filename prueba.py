# Sale 1 products::
# 
# 
Sale = Model.get('sale.sale')
SaleLine = Model.get('sale.line')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_sc1
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, True)
sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_sc2
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, False)
with assertRaises(trytond.model.modelstorage.DomainValidationError):
    sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_sc2n1
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, False)
with assertRaises(trytond.model.modelstorage.DomainValidationError):
    sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_sc2n2
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, True)
sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_all
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, True)
sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_none
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, True)
sale.click('quote')
sale = Sale()
sale.party = customer
sale.invoice_method = 'order'
sale_line = SaleLine()
sale.lines.append(sale_line)
sale_line.product = product_all_ns
sale_line.quantity = 2.0
assertEqual(sale_line.company_salable, False)
with assertRaises(trytond.model.modelstorage.DomainValidationError):
    sale.click('quote')