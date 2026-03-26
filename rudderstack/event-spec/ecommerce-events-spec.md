# Ecommerce Events Specification

Understand the various ecommerce events captured by RudderStack.

* * *

  * __3 minute read

  * 


This guide gives you a detailed description of the various RudderStack SDKs ecommerce events along with their properties. It also describes how RudderStack uses this data to help you define customer journey on an ecommerce platform.

## Event lifecycle overview

RudderStack supports the following ecommerce events that form a vital part of the customer’s product journey:

### Browsing

The following events are associated with a user’s browsing activities on the website:

Event| Context  
---|---  
[Products Searched](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#products-searched>)| User searching for products  
[Product List Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#product-list-viewed>)| User views a list or category of products  
[Product List Filtered](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/browsing/#product-list-filtered>)| User filters a product list or category  
  
### Promotions

The following events are associated with a user’s interaction with the website promotions:

Event| Context  
---|---  
[Promotion Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/promotions/#promotion-viewed>)| User views a promotion on the website  
[Promotion Clicked](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/promotions/#promotion-clicked>)| User clicks on a promotion on the website  
  
### Ordering

The following events are associated with a user’s product ordering activities:

Event| Context  
---|---  
[Product Clicked](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-clicked>)| User clicks on a product  
[Product Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-viewed>)| User views a product and its details  
[Product Added](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-added>)| User adds a product to their shopping cart  
[Product Removed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#product-removed>)| User removes a product from their shopping cart  
[Cart Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#cart-viewed>)| User views their shopping cart  
[Checkout Started](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-started>)| User starts checkouts process  
[Checkout Step Viewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-step-viewed>)| User views a checkout step  
[Checkout Step Completed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#checkout-step-completed>)| User completes a checkout step  
[Payment Info Entered](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#payment-info-entered>)| User adds payment information  
[Order Completed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-completed>)| User completes an order  
[Order Updated](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-updated>)| User updates a placed order  
[Order Refunded](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-refunded>)| User initiates an order refunded  
[Order Cancelled](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-cancelled>)| User cancels an order  
  
### Coupons

The following events are associated with a user’s interactions with the website’s coupon facilities for availing discounts:

Event| Context  
---|---  
[Coupon Entered](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/coupons/#coupon-entered>)| User enters a coupon  
[Coupon Applied](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/coupons/#coupon-applied>)| Coupon is applied successfully to an order or shopping cart  
[Coupon Denied](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/coupons/#coupon-denied>)| Coupon is not valid and denied  
[Coupon Removed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/coupons/#coupon-removed>)| User removes a coupon from an order or shopping cart  
  
### Wishlist

The following actions are associated with a user’s activities related to adding or removing product/s from their wishlist:

Event| Context  
---|---  
[Product Added to Wishlist](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/wishlisting/#product-added-to-wishlist>)| User adds a product to their wishlist  
[Product Removed from Wishlist](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/wishlisting/#product-removed-from-wishlist>)| User removes a product from their wishlist  
[Wishlist Product Added to Cart](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/wishlisting/#wishlist-product-added-to-cart>)| User adds a wishlisted product to their cart  
  
### Sharing

The following events are associated with user activities when they share the product or cart list others:

Event| Context  
---|---  
[Product Shared](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/sharing/#product-shared>)| User shares a product with one or more friends  
[Cart Shared](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/sharing/#cart-shared>)| User shares a shopping cart with one or more friends  
  
### Reviewing

The following events are associated with a user posting a product review:

Event| Context  
---|---  
[Product Reviewed](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/reviewing/#product-reviewed>)| User reviews a product  
  
## FAQ

#### Which RudderStack destinations do not adhere to the ecommerce event spec?

The below destinations **do not** adhere to the ecommerce spec strictly:

[![Adobe Analytics logo](/docs/images/logos/destinations/adobe-analytics.svg)Adobe Analytics](</docs/destinations/streaming-destinations/adobe-analytics/>)[![Algolia Insights logo](/docs/images/logos/destinations/algolia.webp)Algolia Insights](</docs/destinations/streaming-destinations/algolia-insights/>)[![AppsFlyer logo](/docs/images/logos/destinations/appsflyer.svg)AppsFlyer](</docs/destinations/streaming-destinations/appsflyer/>)[![Branch logo](/docs/images/logos/destinations/branch.webp)Branch](</docs/destinations/streaming-destinations/branchio/>)[![Braze logo](/docs/images/logos/destinations/braze.svg)Braze](</docs/destinations/streaming-destinations/braze/>)[![Drip logo](/docs/images/logos/destinations/drip.webp)Drip](</docs/destinations/streaming-destinations/drip/>)[![Facebook App Events logo](/docs/images/logos/destinations/facebook.svg)Facebook App Events](</docs/destinations/streaming-destinations/facebook-app-events/>)[![Facebook Pixel logo](/docs/images/logos/destinations/facebook.svg)Facebook Pixel](</docs/destinations/streaming-destinations/fb-pixel/>)[![Google Ads \(gtag.js\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads (gtag.js)](</docs/destinations/streaming-destinations/google-ads/>)[![Google Analytics 4 logo](/docs/images/logos/destinations/ga.svg)Google Analytics 4](</docs/destinations/streaming-destinations/google-analytics-4/>)[![Klaviyo logo](/docs/images/logos/destinations/klaviyo.svg)Klaviyo](</docs/destinations/streaming-destinations/klaviyo/>)[![Matomo logo](/docs/images/logos/destinations/matomo.svg)Matomo](</docs/destinations/streaming-destinations/matomo/>)[![Monetate logo](/docs/images/logos/destinations/monetate.webp)Monetate](</docs/destinations/streaming-destinations/monetate/>)[![Ometria logo](/docs/images/logos/destinations/ometria.webp)Ometria](</docs/destinations/streaming-destinations/ometria/>)[![Pinterest Tag logo](/docs/images/logos/destinations/pinterest.webp)Pinterest Tag](</docs/destinations/streaming-destinations/pinterest-ads/>)[![Podsights logo](/docs/images/logos/destinations/podsights.svg)Podsights](</docs/destinations/streaming-destinations/podsights/>)[![Revenue Cat logo](/docs/images/logos/destinations/revenuecat.webp)Revenue Cat](</docs/destinations/streaming-destinations/revenue-cat/>)[![Snap Pixel logo](/docs/images/logos/destinations/snapchat.svg)Snap Pixel](</docs/destinations/streaming-destinations/snap-pixel/>)[![Snapchat Conversion logo](/docs/images/logos/destinations/snapchat.svg)Snapchat Conversion](</docs/destinations/streaming-destinations/snapchat-conversion/>)[![TikTok Ads logo](/docs/images/logos/destinations/tiktok-ads.svg)TikTok Ads](</docs/destinations/streaming-destinations/tiktok-ads/>)[![TikTok Ads Offline Events logo](/docs/images/logos/destinations/tiktok-ads.svg)TikTok Ads Offline Events](</docs/destinations/streaming-destinations/tiktok-ads-offline-events/>)[![Yandex.Metrica logo](/docs/images/logos/destinations/yandex-metrica.svg)Yandex.Metrica](</docs/destinations/streaming-destinations/yandex-metrica/>)