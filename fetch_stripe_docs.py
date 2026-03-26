#!/usr/bin/env python3
"""Fetch all Stripe API reference documentation pages and save them as markdown files."""

import subprocess
import os
import time
import re
import sys

BASE_DIR = "/Users/benjamincrane/api-reference-docs-new/stripe"

# Each entry: (category, resource_slug, [(url_suffix, filename), ...])
# URL pattern: https://docs.stripe.com/api/{resource_slug}/{url_suffix}
# File pattern: stripe/{category}/{resource_folder}/{filename}.md

RESOURCES = [
    # ── core-resources ──
    ("core-resources", "balance", [
        ("", "the-balance-object"),
        ("balance_retrieve", "retrieve"),
    ]),
    ("core-resources", "balance-transactions", [
        ("", "the-balance-transaction-object"),
        ("balance_transaction_retrieve", "retrieve"),
        ("balance_transaction_list", "list"),
    ]),
    ("core-resources", "charges", [
        ("", "the-charge-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("capture", "capture"),
        ("list", "list"),
        ("search", "search"),
    ]),
    ("core-resources", "customers", [
        ("", "the-customer-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
        ("search", "search"),
    ]),
    ("core-resources", "disputes", [
        ("", "the-dispute-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("close", "close"),
        ("list", "list"),
    ]),
    ("core-resources", "events", [
        ("", "the-event-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
        ("types", "types"),
    ]),
    ("core-resources", "files", [
        ("", "the-file-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("core-resources", "file-links", [
        ("", "the-file-link-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("core-resources", "mandates", [
        ("", "the-mandate-object"),
        ("retrieve", "retrieve"),
    ]),
    ("core-resources", "payment-intents", [
        ("", "the-payment-intent-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("confirm", "confirm"),
        ("capture", "capture"),
        ("cancel", "cancel"),
        ("list", "list"),
        ("search", "search"),
        ("increment_authorization", "increment-authorization"),
        ("verify_microdeposits", "verify-microdeposits"),
        ("apply_customer_balance", "apply-customer-balance"),
    ]),
    ("core-resources", "setup-intents", [
        ("", "the-setup-intent-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("confirm", "confirm"),
        ("cancel", "cancel"),
        ("list", "list"),
        ("verify_microdeposits", "verify-microdeposits"),
    ]),
    ("core-resources", "setup-attempts", [
        ("", "the-setup-attempt-object"),
        ("list", "list"),
    ]),
    ("core-resources", "payouts", [
        ("", "the-payout-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("reverse", "reverse"),
        ("list", "list"),
    ]),
    ("core-resources", "refunds", [
        ("", "the-refund-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("core-resources", "tokens", [
        ("", "the-token-object"),
        ("create_card", "create-card"),
        ("create_bank_account", "create-bank-account"),
        ("create_pii", "create-pii"),
        ("create_account", "create-account"),
        ("create_person", "create-person"),
        ("create_cvc_update", "create-cvc-update"),
        ("retrieve", "retrieve"),
    ]),

    # ── payment-methods ──
    ("payment-methods", "payment-methods", [
        ("", "the-payment-method-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("customer_list", "customer-list"),
        ("attach", "attach"),
        ("detach", "detach"),
    ]),
    ("payment-methods", "payment-method-configurations", [
        ("", "the-payment-method-configuration-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("payment-methods", "payment-method-domains", [
        ("", "the-payment-method-domain-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("validate", "validate"),
    ]),
    ("payment-methods", "bank-accounts", [
        ("", "the-bank-account-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("verify", "verify"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("payment-methods", "cards", [
        ("", "the-card-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("payment-methods", "sources", [
        ("", "the-source-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("attach", "attach"),
        ("detach", "detach"),
    ]),

    # ── products ──
    ("products", "products", [
        ("", "the-product-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
        ("search", "search"),
    ]),
    ("products", "prices", [
        ("", "the-price-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("search", "search"),
    ]),
    ("products", "coupons", [
        ("", "the-coupon-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("products", "promotion-codes", [
        ("", "the-promotion-code-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("products", "tax-rates", [
        ("", "the-tax-rate-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("products", "shipping-rates", [
        ("", "the-shipping-rate-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),

    # ── checkout ──
    ("checkout", "sessions", [
        ("", "the-session-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("expire", "expire"),
        ("list_line_items", "list-line-items"),
    ]),

    # ── payment-links ──
    ("payment-links", "payment-links", [
        ("", "the-payment-link-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("list_line_items", "list-line-items"),
    ]),

    # ── billing ──
    ("billing", "credit-notes", [
        ("", "the-credit-note-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("void", "void"),
        ("preview", "preview"),
        ("credit_note_line_item", "credit-note-line-item"),
        ("lines", "lines"),
        ("preview_lines", "preview-lines"),
    ]),
    ("billing", "customer-balance-transactions", [
        ("", "the-customer-balance-transaction-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("billing", "customer-portal-sessions", [
        ("", "the-portal-session-object"),
        ("create", "create"),
    ]),
    ("billing", "customer-portal-configurations", [
        ("", "the-portal-configuration-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("billing", "customer-tax-ids", [
        ("", "the-tax-id-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("billing", "invoices", [
        ("", "the-invoice-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("finalize", "finalize"),
        ("pay", "pay"),
        ("send", "send"),
        ("void", "void"),
        ("mark_uncollectible", "mark-uncollectible"),
        ("list", "list"),
        ("search", "search"),
        ("upcoming", "upcoming"),
        ("upcoming_invoice_lines", "upcoming-lines"),
        ("create_preview", "create-preview"),
        ("add_lines", "add-lines"),
        ("remove_lines", "remove-lines"),
        ("update_lines", "update-lines"),
    ]),
    ("billing", "invoice-items", [
        ("", "the-invoiceitem-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("billing", "invoice-line-items", [
        ("", "the-invoice-line-item-object"),
        ("invoice_line_item_update", "update"),
    ]),
    ("billing", "invoice-rendering-templates", [
        ("", "the-invoice-rendering-template-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
        ("archive", "archive"),
        ("unarchive", "unarchive"),
    ]),
    ("billing", "meters", [
        ("", "the-billing-meter-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("deactivate", "deactivate"),
        ("reactivate", "reactivate"),
    ]),
    ("billing", "meter-events", [
        ("", "the-billing-meter-event-object"),
        ("create", "create"),
    ]),
    ("billing", "meter-event-summaries", [
        ("", "the-billing-meter-event-summary-object"),
        ("list", "list"),
    ]),
    ("billing", "plans", [
        ("", "the-plan-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("billing", "quotes", [
        ("", "the-quote-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("finalize", "finalize"),
        ("accept", "accept"),
        ("cancel", "cancel"),
        ("list", "list"),
        ("pdf", "pdf"),
        ("list_line_items", "list-line-items"),
        ("list_computed_upfront_line_items", "list-upfront-line-items"),
    ]),
    ("billing", "subscriptions", [
        ("", "the-subscription-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("list", "list"),
        ("search", "search"),
        ("resume", "resume"),
    ]),
    ("billing", "subscription-items", [
        ("", "the-subscription-item-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("billing", "subscription-schedules", [
        ("", "the-subscription-schedule-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("release", "release"),
        ("list", "list"),
    ]),
    ("billing", "tax-ids", [
        ("", "the-tax-id-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("billing", "usage-records", [
        ("", "the-usage-record-object"),
        ("create", "create"),
        ("list", "list"),
    ]),

    # ── connect ──
    ("connect", "accounts", [
        ("", "the-account-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("reject", "reject"),
        ("list", "list"),
    ]),
    ("connect", "login-links", [
        ("", "the-login-link-object"),
        ("create", "create"),
    ]),
    ("connect", "account-links", [
        ("", "the-account-link-object"),
        ("create", "create"),
    ]),
    ("connect", "account-sessions", [
        ("", "the-account-session-object"),
        ("create", "create"),
    ]),
    ("connect", "application-fees", [
        ("", "the-application-fee-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("connect", "application-fee-refunds", [
        ("", "the-fee-refund-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("connect", "capabilities", [
        ("", "the-capability-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("connect", "country-specs", [
        ("", "the-country-spec-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("connect", "external-accounts", [
        ("", "the-external-account-object"),
        ("account_create_bank_account", "create-bank-account"),
        ("account_create_card", "create-card"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("connect", "persons", [
        ("", "the-person-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("connect", "top-ups", [
        ("", "the-top-up-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("connect", "transfers", [
        ("", "the-transfer-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("connect", "transfer-reversals", [
        ("", "the-transfer-reversal-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("connect", "secret-management", [
        ("", "the-secret-object"),
        ("set", "set"),
        ("find", "find"),
        ("delete", "delete"),
        ("list", "list"),
    ]),

    # ── fraud ──
    ("fraud", "early-fraud-warnings", [
        ("", "the-early-fraud-warning-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("fraud", "reviews", [
        ("", "the-review-object"),
        ("retrieve", "retrieve"),
        ("approve", "approve"),
        ("list", "list"),
    ]),
    ("fraud", "value-lists", [
        ("", "the-value-list-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("fraud", "value-list-items", [
        ("", "the-value-list-item-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("delete", "delete"),
        ("list", "list"),
    ]),

    # ── issuing ──
    ("issuing", "authorizations", [
        ("", "the-issuing-authorization-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("approve", "approve"),
        ("decline", "decline"),
        ("list", "list"),
    ]),
    ("issuing", "cardholders", [
        ("", "the-issuing-cardholder-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("issuing", "cards", [
        ("", "the-issuing-card-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("issuing", "disputes", [
        ("", "the-issuing-dispute-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("submit", "submit"),
        ("list", "list"),
    ]),
    ("issuing", "funding-instructions", [
        ("", "the-issuing-funding-instructions-object"),
        ("create", "create"),
        ("list", "list"),
    ]),
    ("issuing", "personalization-designs", [
        ("", "the-issuing-personalization-design-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("issuing", "physical-bundles", [
        ("", "the-issuing-physical-bundle-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("issuing", "tokens", [
        ("", "the-issuing-token-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("issuing", "transactions", [
        ("", "the-issuing-transaction-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),

    # ── terminal ──
    ("terminal", "connection-tokens", [
        ("", "the-terminal-connection-token-object"),
        ("create", "create"),
    ]),
    ("terminal", "locations", [
        ("", "the-terminal-location-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
    ("terminal", "readers", [
        ("", "the-terminal-reader-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
        ("process_payment_intent", "process-payment-intent"),
        ("process_setup_intent", "process-setup-intent"),
        ("set_reader_display", "set-reader-display"),
        ("cancel_action", "cancel-action"),
    ]),
    ("terminal", "hardware-orders", [
        ("", "the-terminal-hardware-order-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
        ("cancel", "cancel"),
        ("confirm", "confirm"),
        ("mark_as_shipped", "mark-as-shipped"),
        ("mark_as_delivered", "mark-as-delivered"),
        ("mark_as_undeliverable", "mark-as-undeliverable"),
    ]),
    ("terminal", "hardware-products", [
        ("", "the-terminal-hardware-product-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("terminal", "hardware-shipping-methods", [
        ("", "the-terminal-hardware-shipping-method-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("terminal", "configurations", [
        ("", "the-terminal-configuration-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),

    # ── treasury ──
    ("treasury", "financial-accounts", [
        ("", "the-treasury-financial-account-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("treasury", "financial-account-features", [
        ("", "the-treasury-financial-account-features-object"),
        ("update", "update"),
        ("retrieve", "retrieve"),
    ]),
    ("treasury", "transactions", [
        ("", "the-treasury-transaction-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("treasury", "transaction-entries", [
        ("", "the-treasury-transaction-entry-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("treasury", "outbound-transfers", [
        ("", "the-treasury-outbound-transfer-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("treasury", "outbound-payments", [
        ("", "the-treasury-outbound-payment-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("treasury", "inbound-transfers", [
        ("", "the-treasury-inbound-transfer-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("treasury", "received-credits", [
        ("", "the-treasury-received-credit-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("treasury", "received-debits", [
        ("", "the-treasury-received-debit-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("treasury", "credit-reversals", [
        ("", "the-treasury-credit-reversal-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("treasury", "debit-reversals", [
        ("", "the-treasury-debit-reversal-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── entitlements ──
    ("entitlements", "features", [
        ("", "the-entitlements-feature-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("entitlements", "active-entitlements", [
        ("", "the-active-entitlement-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── sigma ──
    ("sigma", "scheduled-queries", [
        ("", "the-scheduled-query-run-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── reporting ──
    ("reporting", "report-runs", [
        ("", "the-report-run-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("reporting", "report-types", [
        ("", "the-report-type-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── financial-connections ──
    ("financial-connections", "accounts", [
        ("", "the-financial-connections-account-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
        ("disconnect", "disconnect"),
        ("refresh", "refresh"),
        ("subscribe", "subscribe"),
        ("unsubscribe", "unsubscribe"),
    ]),
    ("financial-connections", "account-owners", [
        ("", "the-financial-connections-account-owner-object"),
        ("list", "list"),
    ]),
    ("financial-connections", "sessions", [
        ("", "the-financial-connections-session-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
    ]),
    ("financial-connections", "transactions", [
        ("", "the-financial-connections-transaction-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── tax ──
    ("tax", "calculations", [
        ("", "the-tax-calculation-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list_line_items", "list-line-items"),
    ]),
    ("tax", "registrations", [
        ("", "the-tax-registration-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
    ]),
    ("tax", "settings", [
        ("", "the-tax-settings-object"),
        ("retrieve", "retrieve"),
        ("update", "update"),
    ]),
    ("tax", "transactions", [
        ("", "the-tax-transaction-object"),
        ("create_from_calculation", "create-from-calculation"),
        ("create_reversal", "create-reversal"),
        ("retrieve", "retrieve"),
        ("list_line_items", "list-line-items"),
    ]),

    # ── identity ──
    ("identity", "verification-sessions", [
        ("", "the-verification-session-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("list", "list"),
        ("cancel", "cancel"),
        ("redact", "redact"),
    ]),
    ("identity", "verification-reports", [
        ("", "the-verification-report-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── climate ──
    ("climate", "orders", [
        ("", "the-climate-order-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("cancel", "cancel"),
        ("list", "list"),
    ]),
    ("climate", "products", [
        ("", "the-climate-product-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),
    ("climate", "suppliers", [
        ("", "the-climate-supplier-object"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── forwarding ──
    ("forwarding", "requests", [
        ("", "the-forwarding-request-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("list", "list"),
    ]),

    # ── webhooks ──
    ("webhooks", "webhook-endpoints", [
        ("", "the-webhook-endpoint-object"),
        ("create", "create"),
        ("retrieve", "retrieve"),
        ("update", "update"),
        ("delete", "delete"),
        ("list", "list"),
    ]),
]


def build_url(resource_slug, url_suffix):
    """Build the full Stripe docs URL."""
    # Map resource slugs to their Stripe API URL paths
    # Most resources use the same slug, but some have different URL paths
    URL_SLUG_MAP = {
        "balance-transactions": "balance_transactions",
        "file-links": "file_links",
        "payment-intents": "payment_intents",
        "setup-intents": "setup_intents",
        "setup-attempts": "setup_attempts",
        "payment-methods": "payment_methods",
        "payment-method-configurations": "payment_method_configurations",
        "payment-method-domains": "payment_method_domains",
        "bank-accounts": "customer_bank_accounts",
        "promotion-codes": "promotion_codes",
        "tax-rates": "tax_rates",
        "shipping-rates": "shipping_rates",
        "checkout-sessions": "checkout/sessions",
        "payment-links": "payment_links",
        "credit-notes": "credit_notes",
        "customer-balance-transactions": "customer_balance_transactions",
        "customer-portal-sessions": "customer_portal/sessions",
        "customer-portal-configurations": "customer_portal/configurations",
        "customer-tax-ids": "customer_tax_ids",
        "invoice-items": "invoiceitems",
        "invoice-line-items": "invoice_line_item",
        "invoice-rendering-templates": "invoice_rendering_templates",
        "meter-events": "billing/meter-events",
        "meter-event-summaries": "billing/meter-event-summaries",
        "subscription-items": "subscription_items",
        "subscription-schedules": "subscription_schedules",
        "tax-ids": "tax_ids",
        "usage-records": "usage_records",
        "login-links": "account_links",  # will override below
        "account-links": "account_links",
        "account-sessions": "account_sessions",
        "application-fees": "application_fees",
        "application-fee-refunds": "fee_refunds",
        "country-specs": "country_specs",
        "external-accounts": "external_accounts",
        "top-ups": "topups",
        "transfer-reversals": "transfer_reversals",
        "secret-management": "apps/secrets",
        "early-fraud-warnings": "radar/early_fraud_warnings",
        "value-lists": "radar/value_lists",
        "value-list-items": "radar/value_list_items",
        "connection-tokens": "terminal/connection_tokens",
        "hardware-orders": "terminal/hardware_orders",
        "hardware-products": "terminal/hardware_products",
        "hardware-shipping-methods": "terminal/hardware_shipping_methods",
        "financial-accounts": "treasury/financial_accounts",
        "financial-account-features": "treasury/financial_account_features",
        "transaction-entries": "treasury/transaction_entries",
        "outbound-transfers": "treasury/outbound_transfers",
        "outbound-payments": "treasury/outbound_payments",
        "inbound-transfers": "treasury/inbound_transfers",
        "received-credits": "treasury/received_credits",
        "received-debits": "treasury/received_debits",
        "credit-reversals": "treasury/credit_reversals",
        "debit-reversals": "treasury/debit_reversals",
        "active-entitlements": "entitlements/active_entitlements",
        "scheduled-queries": "sigma/scheduled_query_runs",
        "report-runs": "reporting/report_runs",
        "report-types": "reporting/report_types",
        "verification-sessions": "identity/verification_sessions",
        "verification-reports": "identity/verification_reports",
        "account-owners": "financial_connections/account_owners",
        "personalization-designs": "issuing/personalization_designs",
        "physical-bundles": "issuing/physical_bundles",
        "funding-instructions": "issuing/funding_instructions",
        "webhook-endpoints": "webhook_endpoints",
    }

    # Handle resources in categories that use category prefix in URL
    CATEGORY_PREFIX_MAP = {
        ("issuing", "authorizations"): "issuing/authorizations",
        ("issuing", "cardholders"): "issuing/cardholders",
        ("issuing", "cards"): "issuing/cards",
        ("issuing", "disputes"): "issuing/disputes",
        ("issuing", "tokens"): "issuing/tokens",
        ("issuing", "transactions"): "issuing/transactions",
        ("terminal", "locations"): "terminal/locations",
        ("terminal", "readers"): "terminal/readers",
        ("terminal", "configurations"): "terminal/configurations",
        ("treasury", "transactions"): "treasury/transactions",
        ("financial-connections", "accounts"): "financial_connections/accounts",
        ("financial-connections", "sessions"): "financial_connections/sessions",
        ("financial-connections", "transactions"): "financial_connections/transactions",
        ("tax", "calculations"): "tax/calculations",
        ("tax", "registrations"): "tax/registrations",
        ("tax", "settings"): "tax/settings",
        ("tax", "transactions"): "tax/transactions",
        ("climate", "orders"): "climate/orders",
        ("climate", "products"): "climate/products",
        ("climate", "suppliers"): "climate/suppliers",
        ("forwarding", "requests"): "forwarding/requests",
        ("entitlements", "features"): "entitlements/features",
        ("billing", "meters"): "billing/meters",
    }

    # Look up in URL slug map first, then category prefix map
    url_resource = URL_SLUG_MAP.get(resource_slug)
    if url_resource is None:
        # Check category prefix map - we need the category for this
        url_resource = resource_slug

    if url_suffix:
        return f"https://docs.stripe.com/api/{url_resource}/{url_suffix}"
    else:
        return f"https://docs.stripe.com/api/{url_resource}"


def get_url_resource(category, resource_slug):
    """Get the URL resource path for a given category/resource combination."""
    URL_SLUG_MAP = {
        "balance-transactions": "balance_transactions",
        "file-links": "file_links",
        "payment-intents": "payment_intents",
        "setup-intents": "setup_intents",
        "setup-attempts": "setup_attempts",
        "payment-methods": "payment_methods",
        "payment-method-configurations": "payment_method_configurations",
        "payment-method-domains": "payment_method_domains",
        "bank-accounts": "customer_bank_accounts",
        "promotion-codes": "promotion_codes",
        "tax-rates": "tax_rates",
        "shipping-rates": "shipping_rates",
        "payment-links": "payment_links",
        "credit-notes": "credit_notes",
        "customer-balance-transactions": "customer_balance_transactions",
        "customer-portal-sessions": "customer_portal/sessions",
        "customer-portal-configurations": "customer_portal/configurations",
        "customer-tax-ids": "customer_tax_ids",
        "invoice-items": "invoiceitems",
        "invoice-line-items": "invoice_line_item",
        "invoice-rendering-templates": "invoice_rendering_templates",
        "meter-events": "billing/meter-events",
        "meter-event-summaries": "billing/meter-event-summaries",
        "subscription-items": "subscription_items",
        "subscription-schedules": "subscription_schedules",
        "tax-ids": "tax_ids",
        "usage-records": "usage_records",
        "login-links": "login_links",
        "account-links": "account_links",
        "account-sessions": "account_sessions",
        "application-fees": "application_fees",
        "application-fee-refunds": "fee_refunds",
        "country-specs": "country_specs",
        "external-accounts": "external_accounts",
        "top-ups": "topups",
        "transfer-reversals": "transfer_reversals",
        "secret-management": "apps/secrets",
        "early-fraud-warnings": "radar/early_fraud_warnings",
        "value-lists": "radar/value_lists",
        "value-list-items": "radar/value_list_items",
        "connection-tokens": "terminal/connection_tokens",
        "hardware-orders": "terminal/hardware_orders",
        "hardware-products": "terminal/hardware_products",
        "hardware-shipping-methods": "terminal/hardware_shipping_methods",
        "financial-accounts": "treasury/financial_accounts",
        "financial-account-features": "treasury/financial_account_features",
        "transaction-entries": "treasury/transaction_entries",
        "outbound-transfers": "treasury/outbound_transfers",
        "outbound-payments": "treasury/outbound_payments",
        "inbound-transfers": "treasury/inbound_transfers",
        "received-credits": "treasury/received_credits",
        "received-debits": "treasury/received_debits",
        "credit-reversals": "treasury/credit_reversals",
        "debit-reversals": "treasury/debit_reversals",
        "active-entitlements": "entitlements/active_entitlements",
        "scheduled-queries": "sigma/scheduled_query_runs",
        "report-runs": "reporting/report_runs",
        "report-types": "reporting/report_types",
        "verification-sessions": "identity/verification_sessions",
        "verification-reports": "identity/verification_reports",
        "account-owners": "financial_connections/account_owners",
        "personalization-designs": "issuing/personalization_designs",
        "physical-bundles": "issuing/physical_bundles",
        "funding-instructions": "issuing/funding_instructions",
        "webhook-endpoints": "webhook_endpoints",
    }

    CATEGORY_PREFIX_MAP = {
        ("issuing", "authorizations"): "issuing/authorizations",
        ("issuing", "cardholders"): "issuing/cardholders",
        ("issuing", "cards"): "issuing/cards",
        ("issuing", "disputes"): "issuing/disputes",
        ("issuing", "tokens"): "issuing/tokens",
        ("issuing", "transactions"): "issuing/transactions",
        ("terminal", "locations"): "terminal/locations",
        ("terminal", "readers"): "terminal/readers",
        ("terminal", "configurations"): "terminal/configurations",
        ("treasury", "transactions"): "treasury/transactions",
        ("financial-connections", "accounts"): "financial_connections/accounts",
        ("financial-connections", "sessions"): "financial_connections/sessions",
        ("financial-connections", "transactions"): "financial_connections/transactions",
        ("tax", "calculations"): "tax/calculations",
        ("tax", "registrations"): "tax/registrations",
        ("tax", "settings"): "tax/settings",
        ("tax", "transactions"): "tax/transactions",
        ("climate", "orders"): "climate/orders",
        ("climate", "products"): "climate/products",
        ("climate", "suppliers"): "climate/suppliers",
        ("forwarding", "requests"): "forwarding/requests",
        ("entitlements", "features"): "entitlements/features",
        ("billing", "meters"): "billing/meters",
        ("checkout", "sessions"): "checkout/sessions",
    }

    # Check category prefix map first (more specific)
    key = (category, resource_slug)
    if key in CATEGORY_PREFIX_MAP:
        return CATEGORY_PREFIX_MAP[key]

    # Then check slug map
    if resource_slug in URL_SLUG_MAP:
        return URL_SLUG_MAP[resource_slug]

    # Default: use slug as-is
    return resource_slug


def fetch_page(url):
    """Fetch a page using curl and return the content."""
    try:
        result = subprocess.run(
            ["curl", "-sL", "--max-time", "30", url],
            capture_output=True, text=True, timeout=35
        )
        return result.stdout
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def html_to_markdown(html_content):
    """Basic HTML to markdown conversion."""
    if not html_content:
        return ""

    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
    content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL)

    # Convert common HTML elements to markdown
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<code>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)
    content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', content, flags=re.DOTALL)
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL)
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', content, flags=re.DOTALL)
    content = re.sub(r'<tr[^>]*>(.*?)</tr>', r'\1\n', content, flags=re.DOTALL)
    content = re.sub(r'<td[^>]*>(.*?)</td>', r'\1 | ', content, flags=re.DOTALL)
    content = re.sub(r'<th[^>]*>(.*?)</th>', r'**\1** | ', content, flags=re.DOTALL)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&#x27;', "'")
    content = content.replace('&#x2F;', '/')

    # Clean up whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    return content


def main():
    # Count total pages
    total = sum(len(pages) for _, _, pages in RESOURCES)
    print(f"Fetching {total} Stripe API documentation pages across {len(RESOURCES)} resources...")

    count = 0
    skipped = 0
    failed = 0
    succeeded = 0

    for category, resource_slug, pages in RESOURCES:
        url_resource = get_url_resource(category, resource_slug)

        for url_suffix, filename in pages:
            count += 1
            file_path = os.path.join(BASE_DIR, category, resource_slug, f"{filename}.md")

            # Skip if already exists
            if os.path.exists(file_path):
                print(f"[{count}/{total}] SKIP (exists): {category}/{resource_slug}/{filename}")
                skipped += 1
                continue

            # Build URL
            if url_suffix:
                url = f"https://docs.stripe.com/api/{url_resource}/{url_suffix}"
            else:
                url = f"https://docs.stripe.com/api/{url_resource}"

            print(f"[{count}/{total}] Fetching: {url}")

            # Create directory
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            # Fetch and save
            html = fetch_page(url)
            if html and len(html) > 500:  # Basic check for real content
                markdown = html_to_markdown(html)
                if len(markdown) > 100:  # Ensure we got meaningful content
                    with open(file_path, 'w') as f:
                        f.write(markdown)
                    print(f"  -> Saved: {file_path} ({len(markdown)} chars)")
                    succeeded += 1
                else:
                    print(f"  -> FAILED (empty after conversion): {url}")
                    failed += 1
            else:
                print(f"  -> FAILED (no content): {url}")
                failed += 1

            # Small delay to be respectful
            time.sleep(0.3)

    print(f"\nDone! Total: {total}, Succeeded: {succeeded}, Skipped: {skipped}, Failed: {failed}")


if __name__ == "__main__":
    main()
