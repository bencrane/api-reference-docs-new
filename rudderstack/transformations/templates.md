# Transformation Templates

Use prebuilt transformations to implement specific use cases on your event data.

* * *

  * __11 minute read

  * 


RudderStack’s transformation templates provide prebuilt JavaScript functions that you can use to create transformations and implement use cases on your event data. These include data cleaning and enrichment, event filtering and sampling, PII management, and more.

> ![info](/docs/images/info.svg)
> 
> Currently, transformation templates are only available for JavaScript.

## Using transformation templates

To use transformation templates, go to **Collect** > **Transformations** and click **Create Transformation**.

Under **Transformation templates** , select the prebuilt template depending on your use case. To write a transformation from scratch, click **Custom transformation**.

[![Choose a template](/docs/images/features/transformations/transformation-templates-overview.webp)](</docs/images/features/transformations/transformation-templates-overview.webp>)

## PII management and privacy

Use the following transformation templates to easily apply rules for PII management.

### IP Anonymization

This transformation changes the last octet of the IP address to zero. For example, the IP `12.214.31.144` is transformed to `12.214.31.0`. This protects the privacy rights of your users and reduces the risk of accidentally disclosing their IP addresses.

The transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      const ip = event.request_ip;
      if (ip) event.request_ip = ip.replace(/\d{1,3}$/, "0");
      return event;
    }
    

### Replace PII

This transformation replaces or masks sensitive personal data, for example, email, birthday, or social security number, reducing the risk of accidentally disclosing Personally Identifiable Information (PII). You can specify the properties to be masked or replaced and define the masking logic in the code.

The following transformation masks a social security number with zeros:
    
    
    export function transformEvent(event, metadata) {
      if (event.context?.traits?.ssn) event.context.traits.ssn = "000-00-000"; // Change property
      return event;
    }
    

### Hash PII

This transformation hashes any sensitive user information like their email, social security number, etc., using SHA256 encryption.

The transformation hashing the user’s email is shown below:
    
    
    import { sha256 } from "@rs/hash/v1";
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email;
      if (email) event.context.traits.email = sha256(email);
      return event;
    }
    

The following templates leverage the `JSEncrypt` library for encrypting/decrypting PII in your events:

### Encryption

This transformation encrypts any Personally Identifiable Information (PII) including those stored in the cookies.

The transformation encrypting the user’s email is shown below:
    
    
    import { JSEncrypt } from "@rs/encrypt/v1";
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email;
      if (email) {
        const crypt = new JSEncrypt();
        
        // Fetches the RSA public key from the credential store
        crypt.setKey(getCredential('rsa_public_key'));
        event.context.traits.email = crypt.encrypt(email);
      }
      return event;
    }
    

The above transformation fetches the RSA public key from the `rsa_public_key`secret defined in your [credential store](<https://www.rudderstack.com/docs/transformations/credentials/#create-secrets>).

### Decryption

This transformation decrypts the user’s Personally Identifiable Information (PII).

The transformation decrypting the user’s email is shown below:
    
    
    import { JSEncrypt } from "@rs/encrypt/v1";
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email;
      if (email) {
        const crypt = new JSEncrypt();
        
        // Fetches the RSA private key from the credential store
        crypt.setKey(getCredential('rsa_private_key'));
        event.context.traits.email = crypt.decrypt(email);
      }
      return event;
    }
    

The above transformation fetches the RSA private key from the `rsa_private_key` secret defined in your [credential store](<https://www.rudderstack.com/docs/transformations/credentials/#create-secrets>).

## Event filtering and sampling

Use the following templates for your event filtering and sampling use cases.

### Allowlist

This transformation allows events to reach a downstream destination only if a specific property contains certain values.

Some examples of how you can use this template are:

  * Allow only certain event names, like `Product Added` or `Order Completed`.
  * Send certain event types to a particular destination, like [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) or [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>).
  * Send only the events that have a tracking plan linked to the source.


The allowlist transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      const property = event.event; // Edit property; here it is event name
      const allowlist = ["<VALUE>", "<OTHER_VALUE>"]; // Edit allowlist contents
      if (!property || !allowlist.includes(property)) return;
      return event;
    }
    

### Denylist

This transformation blocks the events from reaching a downstream destination if a specific property contains certain values. For example, you can block all `Product Added` and `Order Completed` events or block certain event types (`identify`, `track`, etc.).

The denylist transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      const property = event.event; // Edit property, here it is event name
      const denylist = ["<VALUE>", "<OTHER_VALUE>"]; // Edit denylist contents
      if (property && denylist.includes(property)) return;
      return event;
    }
    

### Event Sampling

This transformation sends only a subset of events to a downstream destination. You can anonymize the events and select a random subset from the anonymous events; this allows you to work with a small, manageable amount of data in the destination.

The event sampling transformation is shown below:
    
    
    import { cyrb53 } from "@rs/hash/v1";
    
    export function transformEvent(event, metadata) {
      const userId = event.userId;
      if (userId && parseInt(cyrb53(userId)) % 10 < 5) return;
      return event;
    }
    

### Split event into multiple events

This transformation conditionally splits a single event into multiple events. Its workflow is explained below:

  * Clones the event if it matches specific criteria.
  * Modifies the cloned event’s name.
  * Returns both the original and modified events.
  * If the event does not match the specified condition, it returns the original event.


    
    
    export function transformEvent(event, metadata) {
    
      // Rename the event to originalEvent for clarity in the transformations below
      const originalEvent = event;
    
      if (originalEvent.type === "track" && originalEvent.event === "Your Event Name Here") {
    
        // Deep clone the original event
        const additionalEvent = JSON.parse(JSON.stringify(event))
    
        // Apply additional transformations to the new event
        additionalEvent.event = "Your New Event Name";
    
        // Send both the original and new event to the destination.
        return [originalEvent, additionalEvent];
    
      } else {
        // Otherwise just return the original event.
        return originalEvent;
      }
    }
    

Note that you can modify the conditional logic as per your requirement.

## Data enrichment

Use the following templates for your data enrichment use cases.

### Geolocation Enrichment

This transformation enriches events with the geolocation data using an IP-to-geolocation API. This lets you easily query your events based on the geolocation data, for example, country or city.

The transformation is shown below:
    
    
    export async function transformEvent(event, metadata) {
      if (event.request_ip) {
        try {
          const res = await fetchV2("<YOUR_API_ENDPOINT>" + event.request_ip); // Use your paid IP-to-geolocation API endpoint.
          event.context.geolocation = res.body;
        } catch {}
      }
      return event;
    }
    

### Parse User Agent

This transformation lets you add the user’s browser, engine, OS, device, and CPU-related information to the events. Adding this user metadata to your user events is helpful when you want to perform downstream actions later, for example, filter events coming from mobile devices.

> ![info](/docs/images/info.svg)
> 
> This template uses the standard RudderStack library [User Agent Parser](<https://www.rudderstack.com/docs/transformations/libraries/#user-agent-parser>) which you can use for your custom transformations.

The transformation is shown below:
    
    
    import { UAParser } from "@rs/userAgentParser/v1";
    
    export function transformEvent(event, metadata) {
      const userAgent = event.context?.userAgent;
      if (userAgent) {
        const parser = new UAParser();
        const parsedUserAgent = parser.setUA(userAgent).getResult();
        event.context.parsedUserAgent = parsedUserAgent;
      }
      return event;
    }
    

### User Enrichment

This transformation enriches the events by fetching user data like location, employment, or social media details using the Clearbit API and their email address. It is helpful when sending events with additional user metadata to various downstream destinations.

The transformation is shown below:
    
    
    export async function transformEvent(event) {
      const email = event.context?.traits?.email;
      if (email) {
        const res = await fetch("<https://person.clearbit.com/v2/combined/find?email=>" + email, {
          headers: {
            "Authorization": "Bearer <your_clearbit_secure_key"
          }
        });
        event.context.traits.enrichmentInfo = res;
      }
      return event;
    }
    

### Extract URL Parameters

This transformation lets you programmatically extract the query parameters from a URL. For example, in the URL `rudderstack.com/transformations?publish=true`, this transformation identifies the query parameter `publish`.

The transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      const search = event.context?.page?.search;
      if (search) {
        event.context.page.parameters = {};
        search.substring(1).split("&").forEach(parameter => {
          const [key, value] = parameter.split("=");
          event.context.page.parameters[key] = value;
        });
      }
      return event;
    }
    

### Localize Apple Device Model

This transformation lets you use the localized version of the Apple device model present in your event’s `context.device.model`. It converts the standard Apple device model information (for example, `iPhone 13,1`) into a human-readable format (`iPhone 12 Mini`).

> ![info](/docs/images/info.svg)
> 
> This transformation template uses the `localizeAppleDeviceModel` RudderStack library which leverages the device model mappings based on open source information. If you find any discrepancies, open an issue in the [`rudder-libraries`](<https://github.com/rudderlabs/rudder-libraries>) GitHub repository.

The transformation is shown below:
    
    
    import { getLocalizedDeviceModel } from "@rs/localizeAppleDeviceModel/v1";
    
     export function transformEvent(event, metadata) {
     const localizedDeviceModel = getLocalizedDeviceModel(event);
      if(localizedDeviceModel && event?.context?.device?.model) {
        event.context.device.model = localizedDeviceModel;
      }
      return event;
    }
    

## Data cleaning

Use the following templates for your data cleaning use cases.

### Remove Null Properties

This transformation removes all event properties with null values; this is helpful when you want to reduce the number of unnecessary fields generated in downstream destinations.

The transformation is shown below:
    
    
    export function transformEvent(event) {
      if (event.properties) {
        const keys = Object.keys(event.properties);
        if (keys) {
          keys.forEach(key => {
            if (event.properties[key] === null) delete event.properties[key];
          });
        }
      }
      return event;
    }
    

### Rename properties

This transformation renames the properties to conform with the appropriate naming convention expected by the downstream destination, for example, `first_name` to `firstName`.

The transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      const firstName = event.context?.traits?.first_name;
      if (firstName) {
        event.context.traits.firstName = firstName;
        delete event.context.traits.first_name;
      }
      return event;
    }
    

### Clean Auth0 UserID

When using the [Auth0 source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/auth0/>) to generate events from your website, the `userId` is prefixed with characters containing `Auth0` followed by a pipe (`|`). This transformation removes any Auth0 `userId` prefixes.

A sample transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
        if(event.userId){
            const cleanedUserId = String(event.userId).split("|")[1];
            event.userId = cleanedUserId ? cleanedUserId : event.userId;
        }
        return event;
    }
    

## Webhooks

Use the following templates to transform events sent to your webhook destinations:

### Dynamic Headers

This transformation sets the HTTP headers for your webhook destinations dynamically. It lets you set the headers based on the values in your data.

The transformation is shown below:
    
    
    export function transformEvent(event, metadata) {
      event.header = {
        Authorization: "Basic <credentials>", // Change headers and values
        header_2: "value"
      };
      return event;
    }
    

### Dynamic Path

This transformation dynamically appends to the URL specified in your webhook destination configuration. This lets you send events to different paths based on the values in your event data. For example, you can send `identify` events to only to the `/users` URL path and the `group` events only to `/organizations`.

The following transformation appends a `/search?email=${email}` path to the webhook URL based on the `email` property present in the event:
    
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email; // Change property
      if (email) event.appendPath = `/search?email=${email}`; // Change property and appendPath
      return event;
    }
    

## Community contributions

The following transformation templates are contributed by the RudderStack community:

### Filter Bot Traffic

This transformation lets you identify and filter events from potential bots by checking an event’s user agent against a list of known bot user agents obtained from [`crawler-user-agents.json`](<https://raw.githubusercontent.com/monperrus/crawler-user-agents/master/crawler-user-agents.json>).
    
    
    export function transformEvent(event, metadata) {
      const lower_user_agent = event["context"]["userAgent"]
      const known_bot_filter_list = ['bot', 'crawler', 'spider', 'feedfetcher-google', 'mediapartners-google', 'apis-google', 'slurp', 'python-urllib', 'python-requests', 'aiohttp', 'httpx', 'libwww-perl', 'httpunit', 'nutch', 'go-http-client', 'biglotron', 'teoma', 'convera', 'gigablast', 'ia_archiver', 'webmon ', 'httrack', 'grub.org', 'netresearchserver', 'speedy', 'fluffy', 'findlink', 'panscient', 'ips-agent', 'yanga', 'yandex', 'yadirectfetcher', 'cyberpatrol', 'postrank', 'page2rss', 'linkdex', 'ezooms', 'heritrix', 'findthatfile', 'europarchive.org', 'mappydata', 'eright', 'apercite', 'aboundex', 'summify', 'ec2linkfinder', 'facebookexternalhit', 'yeti', 'retrevopageanalyzer', 'sogou', 'wotbox', 'ichiro', 'drupact', 'coccoc', 'integromedb', 'siteexplorer.info', 'proximic', 'changedetection', 'cc metadata scaper', 'g00g1e.net', 'binlar', 'a6-indexer', 'admantx', 'megaindex', 'ltx71', 'bubing', 'qwantify', 'lipperhey', 'addthis', 'metauri', 'scrapy', 'capsulechecker', 'sonic', 'sysomos', 'trove', 'deadlinkchecker', 'slack-imgproxy', 'embedly', 'iskanie', 'skypeuripreview', 'google-adwords-instant', 'whatsapp', 'electricmonk', 'yahoo link preview', 'xenu link sleuth', 'pcore-http', 'appinsights', 'phantomjs', 'jetslide', 'newsharecounts', 'tineye', 'linkarchiver', 'digg deeper', 'snacktory', 'okhttp', 'nuzzel', 'omgili', 'pocketparser', 'um-ln', 'muckrack', 'netcraftsurveyagent', 'appengine-google', 'jetty', 'upflow', 'thinklab', 'traackr.com', 'twurly', 'mastodon', 'http_get', 'brandverity', 'check_http', 'ezid', 'genieo', 'meltwaternews', 'moreover', 'scoutjet', 'seoscanners', 'hatena', 'google web preview', 'adscanner', 'netvibes', 'baidu-yunguance', 'btwebclient', 'disqus', 'feedly', 'fever', 'flamingo_searchengine', 'flipboardproxy', 'g2 web services', 'vkshare', 'siteimprove.com', 'dareboost', 'feedspot', 'seokicks', 'tracemyfile', 'zgrab', 'pr-cy.ru', 'datafeedwatch', 'zabbix', 'google-xrawler', 'axios', 'amazon cloudfront', 'pulsepoint', 'cloudflare-alwaysonline', 'google-structured-data-testing-tool', 'wordupinfosearch', 'webdatastats', 'httpurlconnection', 'outbrain', 'w3c_validator', 'w3c-checklink', 'w3c-mobileok', 'w3c_i18n-checker', 'feedvalidator', 'w3c_css_validator', 'w3c_unicorn', 'google-physicalweb', 'blackboard', 'bazqux', 'twingly', 'rivva', 'dataprovider.com', 'theoldreader.com', 'anyevent', 'nmap scripting engine', '2ip.ru', 'clickagy', 'google favicon', 'hubspot', 'chrome-lighthouse', 'headlesschrome', 'simplescraper', 'fedoraplanet', 'friendica', 'nextcloud', 'tiny tiny rss', 'datanyze', 'google-site-verification', 'trendsmapresolver', 'tweetedtimes', 'gwene', 'simplepie', 'searchatlas', 'superfeedr', 'freewebmonitoring sitechecker', 'pandalytics', 'seewithkids', 'cincraw', 'freshrss', 'google-certificates-bridge', 'viber', 'evc-batch', 'virustotal', 'uptime-kuma', 'feedbin', 'snap url preview service', 'ruxitsynthetic', 'google-read-aloud', 'mediapartners', 'wget', 'wget', 'ahrefsgot', 'ahrefssiteaudit', 'wesee:search', 'y!j', 'collection@infegy.com', 'deusu', 'bingpreview', 'daum', 'pingdom', 'barkrowler', 'yak', 'ning', 'ahc', 'apache-httpclient', 'buck', 'newspaper', 'sentry', 'fetch', 'miniflux', 'validator.nu', 'grouphigh', 'checkmarknetwork', 'www.uptime.com', 'mixnodecache', 'domains project', 'pagepeeker', 'vigil', 'php-curl-class', 'ptst', 'seostar.co']
    
      if (known_bot_filter_list.map((bot_name) => lower_user_agent.includes(bot_name)).some((elem) => !!elem)) {
        return
      } else {
        return event
      }
    }
    

### Timestamp Conversion

This template lets you convert an ISO-8601 timestamp into local date and time based on the user’s timezone.
    
    
    export function transformEvent(event) {
    
      const timeZone = event.context?.timezone;
      const originalTimestamp = event.originalTimestamp;
      const locale = event.context?.locale || "en-US";
    
      if (timeZone && originalTimestamp) {
        const date = new Date(originalTimestamp);
        const localDateTime = date.toLocaleString(locale, {
          ...options,
          timeZone
        });
        event.localTimestamp = localDateTime;
      }
    
      return event;
    }
    
    const options = {
      year: "numeric",
      month: "2-digit",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      second: "numeric"
    }
    

### Extraction of Keywords

This template lets you extract keywords useful for data aggregation and analysis of text-heavy event properties:
    
    
    export function transformEvent(event, metadata) {
      let message = event.properties?.message;
    
      if (message) {
        const punctuation = ['"', "'", "!", "?", ".", "-", ":", ","];
    
        punctuation.forEach(mark => {
          message = message.replaceAll(mark, "")
        })
    
        const stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    
        const lower_message = message.toLowerCase()
        const words = lower_message.split(" ")
    
        let unigram_counts = {}
        new Set(words).forEach(word => {
          if (!stop_words.includes(word)) {
            unigram_counts = {
              ...unigram_counts,
              [word]: lower_message.split(word).length - 1
            };
          }
        })
        const top_unigrams = Object.fromEntries(Object.entries(unigram_counts).sort(([, a], [, b]) => b - a).slice(0, 5));
    
    
        let bigrams_counts = {}
        new Set(words.map((el, index) => {
          if (words.slice(index, index + 2).map(word => !stop_words.includes(word)).every(elem => !!elem)) {
            return words.slice(index, index + 2).join(' ')
          }
        })).forEach(bigram => {
          if (bigram) bigrams_counts = {
            ...bigrams_counts,
            [bigram]: lower_message.split(bigram).length - 1
          }
        })
        const top_bigrams = Object.fromEntries(Object.entries(bigrams_counts).sort(([, a], [, b]) => b - a).slice(0, 5));
    
        event["properties"]["keywords"] = {
          "oneWord": top_unigrams,
          "twoWords": top_bigrams
        }
      }
    
      return event;
    }