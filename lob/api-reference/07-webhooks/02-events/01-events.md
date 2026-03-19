# Events

When various notable things happen within the Lob architecture, Events will be created. To get these events sent to your server automatically when they occur, you can set up Webhooks.

## Postcards

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `postcard.created` | false | A postcard is successfully created (Lob returns a 200 status code). |
| `postcard.rejected` | false | A postcard was not successfully created (Usually happens when one or more postcards fail the creation step during a batch request). |
| `postcard.rendered_pdf` | false | A postcard's PDF proof is successfully rendered. |
| `postcard.rendered_thumbnails` | false | A postcard's thumbnails are successfully rendered. |
| `postcard.deleted` | false | A postcard is successfully canceled. |
| `postcard.mailed` | true | A postcard receives a "Mailed" tracking event. Only enabled for certain Print & Mail Editions. |
| `postcard.in_transit` | true | A postcard receives an "In Transit" tracking event. |
| `postcard.in_local_area` | true | A postcard receives an "In Local Area" tracking event. |
| `postcard.processed_for_delivery` | true | A postcard receives a "Processed for Delivery" tracking event. |
| `postcard.delivered` | false | A postcard receives a "Delivered" tracking event. |
| `postcard.failed` | false | A postcard receives a "Failed" rendering error or tracking event. |
| `postcard.re-routed` | true | A postcard receives a "Re-Routed" tracking event. |
| `postcard.returned_to_sender` | true | A postcard receives a "Returned to Sender" tracking event. |
| `postcard.international_exit` | true | A postcard receives a "International Exit" tracking event. |
| `postcard.viewed` | false | A postcard QR code or URL was scanned or viewed by the recipient. |
| `postcard.informed_delivery.email_sent` | true | An informed delivery email was sent to the recipient. |
| `postcard.informed_delivery.email_opened` | true | An informed delivery email was opened by the recipient. |
| `postcard.informed_delivery.email_clicked_through` | true | The link in an informed delivery email was clicked on. |

## Self Mailers

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `self_mailer.created` | false | A self_mailer is successfully created (Lob returns a 200 status code). |
| `self_mailer.rejected` | false | A self_mailer was not successfully created (Usually happens when one or more self_mailers fail the creation step during a batch request). |
| `self_mailer.rendered_pdf` | false | A self_mailer's PDF proof is successfully rendered. |
| `self_mailer.rendered_thumbnails` | false | A self_mailer's thumbnails are successfully rendered. |
| `self_mailer.deleted` | false | A self_mailer is successfully canceled. |
| `self_mailer.mailed` | true | A self_mailer receives a "Mailed" tracking event. Only enabled for certain Print & Mail Editions. |
| `self_mailer.in_transit` | true | A self_mailer receives an "In Transit" tracking event. |
| `self_mailer.in_local_area` | true | A self_mailer receives an "In Local Area" tracking event. |
| `self_mailer.processed_for_delivery` | true | A self_mailer receives a "Processed for Delivery" tracking event. |
| `self_mailer.delivered` | true | A self_mailer receives a "Delivered" tracking event. |
| `self_mailer.failed` | false | A self_mailer receives a "Failed" rendering error or tracking event. |
| `self_mailer.re-routed` | true | A self_mailer receives a "Re-Routed" tracking event. |
| `self_mailer.returned_to_sender` | true | A self_mailer receives a "Returned to Sender" tracking event. |
| `self_mailer.international_exit` | true | A self_mailer receives an "International Exit" tracking event. |
| `self_mailer.viewed` | false | A self_mailer's QR code or URL was scanned or viewed by the recipient. |
| `self_mailer.informed_delivery.email_sent` | true | An informed delivery email was sent to the recipient. |
| `self_mailer.informed_delivery.email_opened` | true | An informed delivery email was opened by the recipient. |
| `self_mailer.informed_delivery.email_clicked_through` | true | The link in an informed delivery email was clicked on. |

## Letters

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `letter.created` | false | A letter is successfully created (Lob returns a 200 status code). |
| `letter.rejected` | false | A letter was not successfully created (Usually happens when one or more letters fail the creation step during a batch request). |
| `letter.rendered_pdf` | false | A letter's PDF proof is successfully rendered. |
| `letter.rendered_thumbnails` | false | A letter's thumbnails are successfully rendered. |
| `letter.deleted` | false | A letter is successfully canceled. |
| `letter.mailed` | true | A letter receives a "Mailed" tracking event. Only enabled for certain Print & Mail Editions. |
| `letter.in_transit` | true | A letter receives an "In Transit" tracking event. |
| `letter.in_local_area` | true | A letter receives an "In Local Area" tracking event. |
| `letter.processed_for_delivery` | true | A letter receives a "Processed for Delivery" tracking event. |
| `letter.delivered` | true | A letter receives a "Delivered" tracking event. |
| `letter.failed` | false | A letter receives a "Failed" rendering error or tracking event. |
| `letter.re-routed` | true | A letter receives a "Re-Routed" tracking event. |
| `letter.returned_to_sender` | true | A letter receives a "Returned to Sender" tracking event. |
| `letter.international_exit` | true | A letter receives a "International Exit" tracking event. |
| `letter.viewed` | false | A letter's QR code or URL was scanned or viewed by the recipient. |
| `letter.certified.mailed` | true | A certified letter receives a "Mailed" tracking event. Only enabled for certain Print & Mail Editions. |
| `letter.certified.in_transit` | true | A certified letter receives an "In Transit" tracking event. |
| `letter.certified.in_local_area` | true | A certified letter receives an "In Transit" tracking event. |
| `letter.certified.processed_for_delivery` | true | A certified letter receives a "Processed for Delivery" tracking event. |
| `letter.certified.re-routed` | true | A certified letter receives a "Re-Routed" tracking event. |
| `letter.certified.returned_to_sender` | true | A certified letter receives a "Returned to Sender" tracking event. |
| `letter.certified.delivered` | true | A certified letter receives a "Delivered" tracking event. |
| `letter.certified.pickup_available` | true | A certified letter receives a "Pickup Available" tracking event. |
| `letter.certified.issue` | true | A certified letter receives an "Issue" tracking event. |
| `letter.return_envelope.created` | false | A return envelope is created (occurs simultaneously with letter creation). |
| `letter.return_envelope.in_transit` | true | A return envelope receives an "In Transit" tracking event. |
| `letter.return_envelope.in_local_area` | true | A return envelope receives an "In Local Area" tracking event. |
| `letter.return_envelope.processed_for_delivery` | true | A return envelope receives a "Processed for Delivery" tracking event. |
| `letter.return_envelope.re-routed` | true | A return envelope receives a "Re-Routed" tracking event. |
| `letter.return_envelope.returned_to_sender` | true | A return envelope receives a "Returned to Sender" tracking event. |
| `letter.informed_delivery.email_sent` | true | An informed delivery email was sent to the recipient. |
| `letter.informed_delivery.email_opened` | true | An informed delivery email was opened by the recipient. |
| `letter.informed_delivery.email_clicked_through` | true | The link in an informed delivery email was clicked on. |

## Checks

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `check.created` | false | A check is successfully created (Lob returns a 200 status code). |
| `check.rejected` | false | A check was not successfully created (Usually happens when one or more checks fail the creation step during a batch request). |
| `check.rendered_pdf` | false | A check's PDF proof is successfully rendered. |
| `check.rendered_thumbnails` | false | A check's thumbnails are successfully rendered. |
| `check.deleted` | false | A check is successfully canceled. |
| `check.mailed` | true | A check receives a "Mailed" tracking event. Only enabled for certain Print & Mail Editions. |
| `check.in_transit` | true | A check receives an "In Transit" tracking event. |
| `check.in_local_area` | true | A check receives an "In Local Area" tracking event. |
| `check.processed_for_delivery` | true | A check receives a "Processed for Delivery" tracking event. |
| `check.delivered` | true | A check receives a "Delivered" tracking event. |
| `check.failed` | false | A check receives a "Failed" rendering error or tracking event. |
| `check.re-routed` | true | A check receives a "Re-Routed" tracking event. |
| `check.returned_to_sender` | true | A check receives a "Returned to Sender" tracking event. |
| `check.informed_delivery.email_sent` | true | An informed delivery email was sent to the recipient. |
| `check.informed_delivery.email_opened` | true | An informed delivery email was opened by the recipient. |
| `check.informed_delivery.email_clicked_through` | true | The link in an informed delivery email was clicked on. |

## Addresses

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `address.created` | false | An address is successfully created (Lob returns a 200 status code). |
| `address.deleted` | false | An address is successfully deleted. |

## Bank Accounts

| Event Type | Live-Only | When Event Type Occurs |
|---|---|---|
| `bank_account.created` | false | A bank account is successfully created (Lob returns a 200 status code). |
| `bank_account.deleted` | false | A bank account is successfully deleted. |
| `bank_account.verified` | false | A bank account is successfully verified. |