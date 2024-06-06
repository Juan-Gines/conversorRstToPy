"""
Unittest extraídos del archivo RST
"""

import unittest

class TestScenarioSale(unittest.TestCase):

    def test_example_1(self):
        from decimal import Decimal

    def test_example_2(self):
        from proteus import Model, Report, Wizard

    def test_example_3(self):
        from trytond.modules.account.tests.tools import (
            create_chart, create_fiscalyear, create_tax, get_accounts)

    def test_example_4(self):
        from trytond.modules.account_invoice.tests.tools import (
            create_payment_term, set_fiscalyear_invoice_sequences)

    def test_example_5(self):
        from trytond.modules.company.tests.tools import create_company, get_company

    def test_example_6(self):
        from trytond.tests.tools import activate_modules, assertEqual, set_user

    def test_example_7(self):
        config = activate_modules('sale')

    def test_example_8(self):
        _ = create_company()

    def test_example_9(self):
        company = get_company()

    def test_example_10(self):
        User = Model.get('res.user')

    def test_example_11(self):
        Party = Model.get('party.party')

    def test_example_12(self):
        Employee = Model.get('company.employee')

    def test_example_13(self):
        employee_party = Party(name="Employee")

    def test_example_14(self):
        employee_party.save()

    def test_example_15(self):
        employee = Employee(party=employee_party)

    def test_example_16(self):
        employee.save()

    def test_example_17(self):
        user = User(config.user)

    def test_example_18(self):
        user.employees.append(employee)

    def test_example_19(self):
        user.employee = employee

    def test_example_20(self):
        user.save()

    def test_example_21(self):
        set_user(user.id)

    def test_example_22(self):
        fiscalyear = set_fiscalyear_invoice_sequences(
            create_fiscalyear(company))

    def test_example_23(self):
        fiscalyear.click('create_period')

    def test_example_24(self):
        _ = create_chart(company)

    def test_example_25(self):
        accounts = get_accounts(company)

    def test_example_26(self):
        revenue = accounts['revenue']

    def test_example_27(self):
        expense = accounts['expense']

    def test_example_28(self):
        cash = accounts['cash']

    def test_example_29(self):
        Journal = Model.get('account.journal')

    def test_example_30(self):
        PaymentMethod = Model.get('account.invoice.payment.method')

    def test_example_31(self):
        cash_journal, = Journal.find([('type', '=', 'cash')])

    def test_example_32(self):
        cash_journal.save()

    def test_example_33(self):
        payment_method = PaymentMethod()

    def test_example_34(self):
        payment_method.name = 'Cash'

    def test_example_35(self):
        payment_method.journal = cash_journal

    def test_example_36(self):
        payment_method.credit_account = cash

    def test_example_37(self):
        payment_method.debit_account = cash

    def test_example_38(self):
        payment_method.save()

    def test_example_39(self):
        tax = create_tax(Decimal('.10'))

    def test_example_40(self):
        tax.save()

    def test_example_41(self):
        Party = Model.get('party.party')

    def test_example_42(self):
        supplier = Party(name='Supplier')

    def test_example_43(self):
        supplier.save()

    def test_example_44(self):
        customer = Party(name='Customer')

    def test_example_45(self):
        customer.save()

    def test_example_46(self):
        ProductCategory = Model.get('product.category')

    def test_example_47(self):
        account_category = ProductCategory(name="Account Category")

    def test_example_48(self):
        account_category.accounting = True

    def test_example_49(self):
        account_category.account_expense = expense

    def test_example_50(self):
        account_category.account_revenue = revenue

    def test_example_51(self):
        account_category.save()

    def test_example_52(self):
        account_category_tax, = account_category.duplicate()

    def test_example_53(self):
        account_category_tax.customer_taxes.append(tax)

    def test_example_54(self):
        account_category_tax.save()

    def test_example_55(self):
        ProductUom = Model.get('product.uom')

    def test_example_56(self):
        unit, = ProductUom.find([('name', '=', 'Unit')])

    def test_example_57(self):
        ProductTemplate = Model.get('product.template')

    def test_example_58(self):
        template = ProductTemplate()

    def test_example_59(self):
        template.name = 'product'

    def test_example_60(self):
        template.default_uom = unit

    def test_example_61(self):
        template.type = 'goods'

    def test_example_62(self):
        template.salable = True

    def test_example_63(self):
        template.list_price = Decimal('10')

    def test_example_64(self):
        template.account_category = account_category_tax

    def test_example_65(self):
        template.save()

    def test_example_66(self):
        product, = template.products

    def test_example_67(self):
        template = ProductTemplate()

    def test_example_68(self):
        template.name = 'service'

    def test_example_69(self):
        template.default_uom = unit

    def test_example_70(self):
        template.type = 'service'

    def test_example_71(self):
        template.salable = True

    def test_example_72(self):
        template.list_price = Decimal('30')

    def test_example_73(self):
        template.account_category = account_category

    def test_example_74(self):
        template.save()

    def test_example_75(self):
        service, = template.products

    def test_example_76(self):
        payment_term = create_payment_term()

    def test_example_77(self):
        payment_term.save()

    def test_example_78(self):
        Inventory = Model.get('stock.inventory')

    def test_example_79(self):
        Location = Model.get('stock.location')

    def test_example_80(self):
        storage, = Location.find([
                ('code', '=', 'STO'),
                ])

    def test_example_81(self):
        inventory = Inventory()

    def test_example_82(self):
        inventory.location = storage

    def test_example_83(self):
        inventory_line = inventory.lines.new(product=product)

    def test_example_84(self):
        inventory_line.quantity = 100.0

    def test_example_85(self):
        inventory_line.expected_quantity = 0.0

    def test_example_86(self):
        inventory.click('confirm')

    def test_example_87(self):
        inventory.state

    def test_example_88(self):
        Sale = Model.get('sale.sale')

    def test_example_89(self):
        SaleLine = Model.get('sale.line')

    def test_example_90(self):
        sale = Sale()

    def test_example_91(self):
        sale.party = customer

    def test_example_92(self):
        sale.payment_term = payment_term

    def test_example_93(self):
        sale.invoice_method = 'order'

    def test_example_94(self):
        sale_line = SaleLine()

    def test_example_95(self):
        sale.lines.append(sale_line)

    def test_example_96(self):
        sale_line.product = product

    def test_example_97(self):
        sale_line.quantity = 2.0

    def test_example_98(self):
        sale_line = SaleLine()

    def test_example_99(self):
        sale.lines.append(sale_line)

    def test_example_100(self):
        sale_line.type = 'comment'

    def test_example_101(self):
        sale_line.description = 'Comment'

    def test_example_102(self):
        sale_line = SaleLine()

    def test_example_103(self):
        sale.lines.append(sale_line)

    def test_example_104(self):
        sale_line.product = product

    def test_example_105(self):
        sale_line.quantity = 3.0

    def test_example_106(self):
        sale.click('quote')

    def test_example_107(self):
        sale.untaxed_amount, sale.tax_amount, sale.total_amount

    def test_example_108(self):
        assertEqual(sale.quoted_by, employee)

    def test_example_109(self):
        sale.click('confirm')

    def test_example_110(self):
        sale.untaxed_amount, sale.tax_amount, sale.total_amount

    def test_example_111(self):
        assertEqual(sale.confirmed_by, employee)

    def test_example_112(self):
        sale.state

    def test_example_113(self):
        sale.shipment_state

    def test_example_114(self):
        sale.invoice_state

    def test_example_115(self):
        len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)

    def test_example_116(self):
        invoice, = sale.invoices

    def test_example_117(self):
        assertEqual(invoice.origins, sale.rec_name)

    def test_example_118(self):
        shipment, = sale.shipments

    def test_example_119(self):
        assertEqual(shipment.origins, sale.rec_name)

    def test_example_120(self):
        invoice_line1, invoice_line2 = sorted(
            invoice.lines, key=lambda l: l.quantity or 0)

    def test_example_121(self):
        stock_move1, stock_move2 = sorted(shipment.outgoing_moves,
            key=lambda m: m.quantity or 0)

    def test_example_122(self):
        assertEqual(invoice_line1.stock_moves, [stock_move1])

    def test_example_123(self):
        assertEqual(stock_move1.invoice_lines, [invoice_line1])

    def test_example_124(self):
        assertEqual(invoice_line2.stock_moves, [stock_move2])

    def test_example_125(self):
        assertEqual(stock_move2.invoice_lines, [invoice_line2])

    def test_example_126(self):
        for line in sale.lines:
            assertEqual(line.quantity, line.actual_quantity)

    def test_example_127(self):
        for invoice in sale.invoices:
            invoice.click('post')

    def test_example_128(self):
        sale.reload()

    def test_example_129(self):
        len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)

    def test_example_130(self):
        sale.invoice_state

    def test_example_131(self):
        sale_report = Report('sale.sale')

    def test_example_132(self):
        ext, _, _, name = sale_report.execute([sale], {})

    def test_example_133(self):
        ext

    def test_example_134(self):
        name

    def test_example_135(self):
        Sale = Model.get('sale.sale')

    def test_example_136(self):
        SaleLine = Model.get('sale.line')

    def test_example_137(self):
        sale = Sale()

    def test_example_138(self):
        sale.party = customer

    def test_example_139(self):
        sale.payment_term = payment_term

    def test_example_140(self):
        sale.invoice_method = 'shipment'

    def test_example_141(self):
        sale_line = SaleLine()

    def test_example_142(self):
        sale.lines.append(sale_line)

    def test_example_143(self):
        sale_line.product = product

    def test_example_144(self):
        sale_line.quantity = 2.0

    def test_example_145(self):
        sale_line = SaleLine()

    def test_example_146(self):
        sale.lines.append(sale_line)

    def test_example_147(self):
        sale_line.type = 'comment'

    def test_example_148(self):
        sale_line.description = 'Comment'

    def test_example_149(self):
        sale_line = SaleLine()

    def test_example_150(self):
        sale.lines.append(sale_line)

    def test_example_151(self):
        sale_line.product = product

    def test_example_152(self):
        sale_line.quantity = 3.0

    def test_example_153(self):
        sale.click('quote')

    def test_example_154(self):
        sale.click('confirm')

    def test_example_155(self):
        sale.state

    def test_example_156(self):
        sale.shipment_state

    def test_example_157(self):
        sale.invoice_state

    def test_example_158(self):
        sale.reload()

    def test_example_159(self):
        len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)

    def test_example_160(self):
        shipment, = sale.shipments

    def test_example_161(self):
        stock_move1, stock_move2 = sorted(shipment.outgoing_moves,
            key=lambda m: m.quantity or 0)

    def test_example_162(self):
        len(stock_move1.invoice_lines)

    def test_example_163(self):
        len(stock_move2.invoice_lines)

    def test_example_164(self):
        shipment.click('assign_try')

    def test_example_165(self):
        shipment.click('pick')

    def test_example_166(self):
        shipment.click('pack')

    def test_example_167(self):
        shipment.click('do')

    def test_example_168(self):
        sale.reload()

    def test_example_169(self):
        sale.invoice_state

    def test_example_170(self):
        invoice, = sale.invoices

    def test_example_171(self):
        invoice.type

    def test_example_172(self):
        invoice_line1, invoice_line2 = sorted(invoice.lines,
            key=lambda l: l.quantity or 0)

    def test_example_173(self):
        for line in invoice.lines:
            line.quantity = 1
            line.save()

    def test_example_174(self):
        invoice.click('post')

    def test_example_175(self):
        assertEqual(invoice_line1.stock_moves, [stock_move1])

    def test_example_176(self):
        assertEqual(invoice_line2.stock_moves, [stock_move2])

    def test_example_177(self):
        sale.reload()

    def test_example_178(self):
        len(sale.invoices)

    def test_example_179(self):
        sum(l.quantity for i in sale.invoices for l in i.lines)

    def test_example_180(self):
        sale = Sale()

    def test_example_181(self):
        sale.party = customer

    def test_example_182(self):
        sale.payment_term = payment_term

    def test_example_183(self):
        sale.shipment_method = 'invoice'

    def test_example_184(self):
        sale_line = sale.lines.new()

    def test_example_185(self):
        sale_line.product = product

    def test_example_186(self):
        sale_line.quantity = 5.0

    def test_example_187(self):
        sale.click('quote')

    def test_example_188(self):
        sale.click('confirm')

    def test_example_189(self):
        sale.state

    def test_example_190(self):
        sale.shipment_state

    def test_example_191(self):
        sale.invoice_state

    def test_example_192(self):
        len(sale.shipments), len(sale.shipment_returns), len(sale.invoices)

    def test_example_193(self):
        invoice, = sale.invoices

    def test_example_194(self):
        invoice_line, = invoice.lines

    def test_example_195(self):
        len(invoice_line.stock_moves)

    def test_example_196(self):
        invoice_line, = invoice.lines

    def test_example_197(self):
        invoice_line.quantity

    def test_example_198(self):
        invoice_line.quantity = 4.0

    def test_example_199(self):
        invoice.click('post')

    def test_example_200(self):
        pay = invoice.click('pay')

    def test_example_201(self):
        pay.form.payment_method = payment_method

    def test_example_202(self):
        pay.execute('choice')

    def test_example_203(self):
        invoice.reload()

    def test_example_204(self):
        invoice.state

    def test_example_205(self):
        invoice_line, = invoice.lines

    def test_example_206(self):
        len(invoice_line.stock_moves)

    def test_example_207(self):
        sale.reload()

    def test_example_208(self):
        shipment, = sale.shipments

    def test_example_209(self):
        shipment.reload()

    def test_example_210(self):
        stock_move, = shipment.outgoing_moves

    def test_example_211(self):
        stock_move.quantity

    def test_example_212(self):
        assertEqual(stock_move.invoice_lines, [invoice_line])

    def test_example_213(self):
        stock_inventory_move, = shipment.inventory_moves

    def test_example_214(self):
        stock_inventory_move.quantity

    def test_example_215(self):
        stock_inventory_move.quantity = 3.0

    def test_example_216(self):
        shipment.click('assign_try')

    def test_example_217(self):
        shipment.click('pick')

    def test_example_218(self):
        shipment.click('pack')

    def test_example_219(self):
        shipment.click('do')

    def test_example_220(self):
        shipment.state

    def test_example_221(self):
        sale.reload()

    def test_example_222(self):
        len(sale.shipments)

    def test_example_223(self):
        invoice.reload()

    def test_example_224(self):
        invoice_line, = invoice.lines

    def test_example_225(self):
        len(invoice_line.stock_moves)

    def test_example_226(self):
        return_ = Sale()

    def test_example_227(self):
        return_.party = customer

    def test_example_228(self):
        return_.payment_term = payment_term

    def test_example_229(self):
        return_.invoice_method = 'shipment'

    def test_example_230(self):
        return_line = SaleLine()

    def test_example_231(self):
        return_.lines.append(return_line)

    def test_example_232(self):
        return_line.product = product

    def test_example_233(self):
        return_line.quantity = -4.

    def test_example_234(self):
        return_line = SaleLine()

    def test_example_235(self):
        return_.lines.append(return_line)

    def test_example_236(self):
        return_line.type = 'comment'

    def test_example_237(self):
        return_line.description = 'Comment'

    def test_example_238(self):
        return_.click('quote')

    def test_example_239(self):
        return_.click('confirm')

    def test_example_240(self):
        return_.state

    def test_example_241(self):
        return_.shipment_state

    def test_example_242(self):
        return_.invoice_state

    def test_example_243(self):
        (len(return_.shipments), len(return_.shipment_returns),
            len(return_.invoices))

    def test_example_244(self):
        ship_return, = return_.shipment_returns

    def test_example_245(self):
        move_return, = ship_return.incoming_moves

    def test_example_246(self):
        move_return.product.rec_name

    def test_example_247(self):
        move_return.quantity

    def test_example_248(self):
        move_return.quantity = 3

    def test_example_249(self):
        ship_return.click('receive')

    def test_example_250(self):
        return_.reload()

    def test_example_251(self):
        return_.shipment_state

    def test_example_252(self):
        return_.invoice_state

    def test_example_253(self):
        (len(return_.shipments), len(return_.shipment_returns),
            len(return_.invoices))

    def test_example_254(self):
        credit_note, = return_.invoices

    def test_example_255(self):
        credit_note.type

    def test_example_256(self):
        len(credit_note.lines)

    def test_example_257(self):
        sum(l.quantity for l in credit_note.lines)

    def test_example_258(self):
        credit_note.click('post')

    def test_example_259(self):
        return_.reload()

    def test_example_260(self):
        _, ship_return = return_.shipment_returns

    def test_example_261(self):
        move_return, = ship_return.incoming_moves

    def test_example_262(self):
        move_return.product.rec_name

    def test_example_263(self):
        move_return.quantity

    def test_example_264(self):
        ship_return.click('receive')

    def test_example_265(self):
        return_.reload()

    def test_example_266(self):
        return_.shipment_state

    def test_example_267(self):
        return_.invoice_state

    def test_example_268(self):
        (len(return_.shipments), len(return_.shipment_returns),
            len(return_.invoices))

    def test_example_269(self):
        mix = Sale()

    def test_example_270(self):
        mix.party = customer

    def test_example_271(self):
        mix.payment_term = payment_term

    def test_example_272(self):
        mix.invoice_method = 'order'

    def test_example_273(self):
        mixline = SaleLine()

    def test_example_274(self):
        mix.lines.append(mixline)

    def test_example_275(self):
        mixline.product = product

    def test_example_276(self):
        mixline.quantity = 7.

    def test_example_277(self):
        mixline_comment = SaleLine()

    def test_example_278(self):
        mix.lines.append(mixline_comment)

    def test_example_279(self):
        mixline_comment.type = 'comment'

    def test_example_280(self):
        mixline_comment.description = 'Comment'

    def test_example_281(self):
        mixline2 = SaleLine()

    def test_example_282(self):
        mix.lines.append(mixline2)

    def test_example_283(self):
        mixline2.product = product

    def test_example_284(self):
        mixline2.quantity = -2.

    def test_example_285(self):
        mix.click('quote')

    def test_example_286(self):
        mix.click('confirm')

    def test_example_287(self):
        mix.state

    def test_example_288(self):
        mix.shipment_state

    def test_example_289(self):
        mix.invoice_state

    def test_example_290(self):
        len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)

    def test_example_291(self):
        mix_return, = mix.shipment_returns

    def test_example_292(self):
        mix_shipment, = mix.shipments

    def test_example_293(self):
        mix_return.click('receive')

    def test_example_294(self):
        move_return, = mix_return.incoming_moves

    def test_example_295(self):
        move_return.product.rec_name

    def test_example_296(self):
        move_return.quantity

    def test_example_297(self):
        mix_shipment.click('assign_try')

    def test_example_298(self):
        mix_shipment.click('pick')

    def test_example_299(self):
        mix_shipment.click('pack')

    def test_example_300(self):
        mix_shipment.click('do')

    def test_example_301(self):
        move_shipment, = mix_shipment.outgoing_moves

    def test_example_302(self):
        move_shipment.product.rec_name

    def test_example_303(self):
        move_shipment.quantity

    def test_example_304(self):
        mix.reload()

    def test_example_305(self):
        mix_invoice, = mix.invoices

    def test_example_306(self):
        mix_invoice.type

    def test_example_307(self):
        len(mix_invoice.lines)

    def test_example_308(self):
        sorted(l.quantity for l in mix_invoice.lines)

    def test_example_309(self):
        mix_invoice.click('post')

    def test_example_310(self):
        mix = Sale()

    def test_example_311(self):
        mix.party = customer

    def test_example_312(self):
        mix.payment_term = payment_term

    def test_example_313(self):
        mix.invoice_method = 'shipment'

    def test_example_314(self):
        mixline = SaleLine()

    def test_example_315(self):
        mix.lines.append(mixline)

    def test_example_316(self):
        mixline.product = product

    def test_example_317(self):
        mixline.quantity = 6.

    def test_example_318(self):
        mixline_comment = SaleLine()

    def test_example_319(self):
        mix.lines.append(mixline_comment)

    def test_example_320(self):
        mixline_comment.type = 'comment'

    def test_example_321(self):
        mixline_comment.description = 'Comment'

    def test_example_322(self):
        mixline2 = SaleLine()

    def test_example_323(self):
        mix.lines.append(mixline2)

    def test_example_324(self):
        mixline2.product = product

    def test_example_325(self):
        mixline2.quantity = -3.

    def test_example_326(self):
        mix.click('quote')

    def test_example_327(self):
        mix.click('confirm')

    def test_example_328(self):
        mix.state

    def test_example_329(self):
        mix.shipment_state

    def test_example_330(self):
        mix.invoice_state

    def test_example_331(self):
        len(mix.shipments), len(mix.shipment_returns), len(mix.invoices)

    def test_example_332(self):
        mix_return, = mix.shipment_returns

    def test_example_333(self):
        mix_shipment, = mix.shipments

    def test_example_334(self):
        mix_return.click('receive')

    def test_example_335(self):
        move_return, = mix_return.incoming_moves

    def test_example_336(self):
        move_return.product.rec_name

    def test_example_337(self):
        move_return.quantity

    def test_example_338(self):
        mix_shipment.click('assign_try')

    def test_example_339(self):
        mix_shipment.click('pick')

    def test_example_340(self):
        mix_shipment.click('pack')

    def test_example_341(self):
        move_shipment, = mix_shipment.outgoing_moves

    def test_example_342(self):
        move_shipment.product.rec_name

    def test_example_343(self):
        move_shipment.quantity

    def test_example_344(self):
        service_sale = Sale()

    def test_example_345(self):
        service_sale.party = customer

    def test_example_346(self):
        service_sale.payment_term = payment_term

    def test_example_347(self):
        sale_line = service_sale.lines.new()

    def test_example_348(self):
        sale_line.product = service

    def test_example_349(self):
        sale_line.quantity = 1

    def test_example_350(self):
        service_sale.save()

    def test_example_351(self):
        service_sale.click('quote')

    def test_example_352(self):
        service_sale.click('confirm')

    def test_example_353(self):
        service_sale.state

    def test_example_354(self):
        service_sale.shipment_state

    def test_example_355(self):
        service_sale.invoice_state

    def test_example_356(self):
        service_invoice, = service_sale.invoices

    def test_example_357(self):
        service_invoice.click('post')

    def test_example_358(self):
        pay = service_invoice.click('pay')

    def test_example_359(self):
        pay.form.payment_method = payment_method

    def test_example_360(self):
        pay.execute('choice')

    def test_example_361(self):
        service_invoice.reload()

    def test_example_362(self):
        service_invoice.state

    def test_example_363(self):
        service_sale.reload()

    def test_example_364(self):
        service_sale.invoice_state

    def test_example_365(self):
        service_sale.shipment_state

    def test_example_366(self):
        service_sale.state

    def test_example_367(self):
        sale_to_return = Sale()

    def test_example_368(self):
        sale_to_return.party = customer

    def test_example_369(self):
        sale_to_return.payment_term = payment_term

    def test_example_370(self):
        sale_line = sale_to_return.lines.new()

    def test_example_371(self):
        sale_line.product = service

    def test_example_372(self):
        sale_line.quantity = 1

    def test_example_373(self):
        sale_line = sale_to_return.lines.new()

    def test_example_374(self):
        sale_line.type = 'comment'

    def test_example_375(self):
        sale_line.description = 'Test comment'

    def test_example_376(self):
        sale_to_return.click('quote')

    def test_example_377(self):
        sale_to_return.click('confirm')

    def test_example_378(self):
        sale_to_return.state

    def test_example_379(self):
        return_sale = Wizard('sale.return_sale', [sale_to_return])

    def test_example_380(self):
        return_sale.execute('return_')

    def test_example_381(self):
        returned_sale, = Sale.find([
            ('state', '=', 'draft'),
            ])

    def test_example_382(self):
        assertEqual(returned_sale.origin, sale_to_return)

    def test_example_383(self):
        sorted([x.quantity or 0 for x in returned_sale.lines])

    def test_example_384(self):
        sale = Sale()

    def test_example_385(self):
        sale.party = customer

    def test_example_386(self):
        sale.payment_term = payment_term

    def test_example_387(self):
        sale.invoice_method = 'shipment'

    def test_example_388(self):
        line = sale.lines.new()

    def test_example_389(self):
        line.product = product

    def test_example_390(self):
        line.quantity = 10.0

    def test_example_391(self):
        sale.click('quote')

    def test_example_392(self):
        sale.click('confirm')

    def test_example_393(self):
        shipment, = sale.shipments

    def test_example_394(self):
        for move in shipment.inventory_moves:
            move.quantity = 5.0

    def test_example_395(self):
        shipment.click('assign_try')

    def test_example_396(self):
        shipment.click('pick')

    def test_example_397(self):
        shipment.click('pack')

    def test_example_398(self):
        shipment.click('do')

    def test_example_399(self):
        sale.reload()

    def test_example_400(self):
        invoice, = sale.invoices

    def test_example_401(self):
        invoice_line, = invoice.lines

    def test_example_402(self):
        invoice_line.quantity

    def test_example_403(self):
        stock_move, = invoice_line.stock_moves

    def test_example_404(self):
        stock_move.quantity

    def test_example_405(self):
        stock_move.state

    def test_example_406(self):
        sale = Sale()

    def test_example_407(self):
        sale.party = customer

    def test_example_408(self):
        sale.payment_term = payment_term

    def test_example_409(self):
        sale.shipment_method = 'invoice'

    def test_example_410(self):
        line = sale.lines.new()

    def test_example_411(self):
        line.product = product

    def test_example_412(self):
        line.quantity = 10.0

    def test_example_413(self):
        sale.click('quote')

    def test_example_414(self):
        sale.click('confirm')

    def test_example_415(self):
        invoice, = sale.invoices

    def test_example_416(self):
        invoice_line, = invoice.lines

    def test_example_417(self):
        assertEqual(invoice_line.stock_moves, [])

    def test_example_418(self):
        invoice_line.quantity = 5.0

    def test_example_419(self):
        invoice.click('post')

    def test_example_420(self):
        pay = invoice.click('pay')

    def test_example_421(self):
        pay.form.payment_method = payment_method

    def test_example_422(self):
        pay.execute('choice')

    def test_example_423(self):
        invoice.reload()

    def test_example_424(self):
        invoice.state

    def test_example_425(self):
        sale.reload()

    def test_example_426(self):
        sale.invoice_state

    def test_example_427(self):
        invoice_line.reload()

    def test_example_428(self):
        stock_move, = invoice_line.stock_moves

    def test_example_429(self):
        stock_move.quantity

    def test_example_430(self):
        stock_move.state

    def test_example_431(self):
        sale = Sale()

    def test_example_432(self):
        sale.party = customer

    def test_example_433(self):
        line = sale.lines.new()

    def test_example_434(self):
        line.product = product

    def test_example_435(self):
        line.quantity = 10.0

    def test_example_436(self):
        sale.click('quote')

    def test_example_437(self):
        sale.click('confirm')

    def test_example_438(self):
        invoice, = sale.invoices

    def test_example_439(self):
        invoice_line, = invoice.lines

    def test_example_440(self):
        invoice.lines.remove(invoice_line)

    def test_example_441(self):
        invoice.click('post')

    def test_example_442(self):
        sale.reload()

    def test_example_443(self):
        new_invoice, = sale.invoices

    def test_example_444(self):
        new_invoice.number

    def test_example_445(self):
        len(new_invoice.lines)


if __name__ == "__main__":
    unittest.main()
