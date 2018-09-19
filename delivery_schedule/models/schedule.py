from odoo import api, fields, models


class DeliverySchedule(models.Model):
    """ Schedule for the deliveries on specific days """
    _name = 'delivery.schedule'
    _description = 'Product delivery schedule'

    """ Fields descriptions """
    #1.Schedule Reference is  column with random sequence number
    def _compute_reference(self):
        last_ref = self.env['delivery.schedule '].search([], limit=1, order='id desc')
        reference = "DS001"
        if last_ref : # The variable is null
            reference = last_ref.split("DS", 1)
            reference =int(reference[1])
            reference+= 1
            reference ="DS"+str(reference).zfill(3)
        return reference

    schedule_reference = fields.Char(string='Schedule Reference', compute='_compute_reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default='New')

    #2. Schedule Date stores the product delivery date
    schedule_date = fields.Date(string='Schedule Date', required=True,help="Set sheduled date to deliver a prodcut.")

    #3. Customer Name : it can be access from order

    #4. Sale Order Reference
    order_id = fields.Many2one('sale.order', string='Order Reference', required=True, copy=True, auto_join=True, index=True, )

    #5. Customer Purchase order reference -- it might be get from order reference
    #6. Sale Order Date -- accessible from order reference

    #7. Product - A product may have multiple delivery schedules
    product_id = fields.Many2one('sale.order.line', string='Product', required=True, readonly=True, help="Only products from sales order line.")

    #8.Ordered Quantity -- accessible from order reference
    #9.Delivered Quantity -- accessible from delivered reference

    #10.Scheduled Quantity--  stores the quatity to deliver on a day
    scheduled_uom_qty = fields.Float(string='Scheduled Quantity', digits=dp.get_precision('Product Unit of Measure'), required=True, default=1.0)

    #11.Remaining Quantity -- accessible from delivered reference
    #12.Unit of Measurement -- accessible from product reference
    #13.Delivery Date -- accessible from delivered reference
    #14.Contact Person
    contact_person = fields.Char(string='Contact Person', default='None')
    #15.Location
    Location = fields.Char(string='Location', default='None', required=True)
    #16.Remarks
    Remarks = fields.Text(string='Remarks', default='None')
    #17.Status values are planned, partly delivered, fully delivered, cancelled, rescheduled
    status = fields.Selection([
        ('planned', 'Planned'),
        ('partly_delivered', 'Partly delivered'),
        ('fully_delivered', 'Fully delivered'),
        ('cancelled', 'Cancelled'),
        ('rescheduled', 'Rescheduled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    #18.New Schedule ID in case of rescheduling
    schedule_to = fields.One2many('delivery.schedule', 'id', string='Reschedule To',copy=True)

    #19.No Delivery Reason
    no_delivery_reason = fields.Text(string='No Delivery Reason', default='None')

    #20.Reference to confirmed deliveries
    reference_deliveries = fields.One2many('stock.picking', 'id', string='Confirmed Deliveries',copy=True)
