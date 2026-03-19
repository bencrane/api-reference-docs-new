# Tracking Events

As mailpieces travel through the mail stream, USPS scans their unique barcodes, and Lob processes these mail scans to generate tracking events.

## Certified Tracking Event Details

Letters sent with USPS Certified Mail are fully tracked by USPS, and therefore their tracking events have an additional `details` object with more detailed information about the tracking event. The following table shows the potential values for the fields in the `details` object mapped to the tracking event `name`.

| Name | Event | Description | Action Required |
|---|---|---|---|
| Mailed | `package_accepted` | Package has been accepted into the carrier network for delivery. | `false` |
| In Transit | `package_arrived` | Package has arrived at an intermediate location in the carrier network. | `false` |
| In Transit | `package_departed` | Package has departed from an intermediate location in the carrier network. | `false` |
| In Transit | `package_processing` | Package is processing at an intermediate location in the carrier network. | `false` |
| In Transit | `package_processed` | Package has been processed at an intermediate location. | `false` |
| In Local Area | `package_in_local_area` | Package is at a location near the end destination. | `false` |
| Processed For Delivery | `delivery_scheduled` | Package is scheduled for delivery. | `false` |
| Processed For Delivery | `out_for_delivery` | Package is out for delivery. | `false` |
| Pickup Available | `pickup_available` | Package is available for pickup at carrier location. | `true` |
| Delivered | `delivered` | Package has been delivered. | `false` |
| Re-Routed | `package_forwarded` | Package has been forwarded. | `false` |
| Returned to Sender | `returned_to_sender` | Package is to be returned to sender. | `false` |
| Issue | `address_issue` | Address information is incorrect. Contact carrier to ensure delivery. | `true` |
| Issue | `contact_carrier` | Contact the carrier for more information. | `true` |
| Issue | `delayed` | Delivery of package is delayed. | `false` |
| Issue | `delivery_attempted` | Delivery of package has been attempted. Contact carrier to ensure delivery. | `true` |
| Issue | `delivery_rescheduled` | Delivery of package has been rescheduled. | `false` |
| Issue | `location_inaccessible` | Delivery location inaccessible to carrier. Contact carrier to ensure delivery. | `true` |
| Issue | `notice_left` | Carrier left notice during attempted delivery. Follow carrier instructions on notice. | `true` |
| Issue | `package_damaged` | Package has been damaged. Contact carrier for more details. | `true` |
| Issue | `package_disposed` | Package has been disposed. | `false` |
| Issue | `package_held` | Package held at carrier location. Contact carrier for more details. | `true` |
| Issue | `package_lost` | Package has been lost. Contact carrier for more details. | `true` |
| Issue | `package_unclaimed` | Package is unclaimed. | `true` |
| Issue | `package_undeliverable` | Package is not able to be delivered. | `true` |
| Issue | `reschedule_delivery` | Contact carrier to reschedule delivery. | `true` |
| Issue | `other` | Unrecognized carrier status. | `false` |