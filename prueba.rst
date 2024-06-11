Sale 1 products::

    >>> Sale = Model.get('sale.sale')
    >>> SaleLine = Model.get('sale.line')
    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_sc1
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    True
    >>> sale.click('quote')

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_sc2
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    False
    >>> sale.click('quote') # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    trytond.model.modelstorage.DomainValidationError: The value for field "Product" in "Sale Line" is not valid according to its domain. -

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_sc2n1
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    False
    >>> sale.click('quote')# doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    trytond.model.modelstorage.DomainValidationError: The value for field "Product" in "Sale Line" is not valid according to its domain. -

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_sc2n2
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    True
    >>> sale.click('quote')

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_all
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    True
    >>> sale.click('quote')

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_none
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    True
    >>> sale.click('quote')

    >>> sale = Sale()
    >>> sale.party = customer
    >>> sale.invoice_method = 'order'
    >>> sale_line = SaleLine()
    >>> sale.lines.append(sale_line)
    >>> sale_line.product = product_all_ns
    >>> sale_line.quantity = 2.0
    >>> sale_line.company_salable
    False
    >>> sale.click('quote')# doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    trytond.model.modelstorage.DomainValidationError: The value for field "Product" in "Sale Line" is not valid according to its domain. -
