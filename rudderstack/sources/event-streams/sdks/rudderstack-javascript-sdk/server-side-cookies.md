# How to Use Server-side Cookies in JavaScript SDK v3

> Version: Latest (v3)v1.1

# How to Use Server-side Cookies in JavaScript SDK v3

Learn how to implement server-side cookies in the RudderStack JavaScript SDK for effective tracking and session management.

* * *

  * __11 minute read

  * 


As the user privacy measures evolve, modern web browsers, particularly Safari, have introduced [Intelligent Tracking Prevention](<https://webkit.org/blog/7675/intelligent-tracking-prevention/>) (ITP) to limit user tracking through cookies. This poses serious challenges for businesses relying on cookies for authentication, personalization, and analytics. To address these limitations, the JavaScript SDK offers a server-side cookie management solution to ensure data tracking without compromising user privacy.

RudderStack’s server-side cookie management solution allows you to set RudderStack’s cookies on the server, providing full control over attributes like expiration and extending cookie lifespans unaffected by ITP’s restrictions.

## Key features

  * **Extended cookie lifespan** : Server-side cookies are not subject to ITP’s client-side cookie restrictions
  * **Enhanced privacy compliance** : Better control over cookie attributes and storage
  * **Cross-browser compatibility** : Consistent behavior across different browsers and platforms
  * **Improved user experience** : Seamless tracking and personalization capabilities


## What is ITP?

Intelligent Tracking Prevention (ITP) is a privacy feature introduced in Safari in 2017 to prevent advertisers from tracking users across websites. It restricts third-party cookies and may significantly shorten the lifespan of first-party cookies if they appear to be used for cross-site tracking.

ITP also affects how developers can use cookies for:

  * User authentication
  * Content personalization
  * Analytics and cross-site tracking
  * Session management and user experience continuity


The JavaScript SDK traditionally uses client-side cookies. With the introduction of ITP, it also implements server-side cookies to achieve:

  * Extended lifespan than the client-managed cookies.
  * Consistent and uniform experience across all the browsers.


## Enable server-side cookies

Set the `useServerSideCookies` configuration option to `true` while [loading the JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>), as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      useServerSideCookies: true // Default is false
    });
    

Once enabled, the SDK makes network requests to the website’s server to set cookies via the response headers.

To ensure that the cookies are set successfully, you must make the request only to the website’s domain (or parent domain) server. RudderStack supports the following use cases:

Website| Server| Cookies  
---|---|---  
Parent domain website| Parent domain server| Cookies are created for the parent domain.  
Sub-domain website| Sub-domain server| Cookies are created for the sub-domain.  
Sub-domain website| Parent domain server| Cookies are created for the parent domain.  
  
> ![warning](/docs/images/warning.svg)
> 
> For sub-domain websites to set cookies for the parent domain, `secure` and `sameSite` cookie attributes are set to `true` and `None` respectively.
> 
> Otherwise, the browser will **not** set the server-side cookies.

A sample request flow is illustrated below:

[![](/docs/images/event-stream-sources/server-side-cookies.webp)](</docs/images/event-stream-sources/server-side-cookies.webp>)

The JavaScript SDK makes explicit `POST` requests to the server to set cookies via the `/rsaRequest` endpoint:

[![](/docs/images/event-stream-sources/rsa-request.webp)](</docs/images/event-stream-sources/rsa-request.webp>)

The response includes `Set-Cookie` headers which set the `rl_anonymous_id` cookie (user’s `anonymousId` value which is persisted through the server-side cookie).

[![](/docs/images/event-stream-sources/set-cookie-header.webp)](</docs/images/event-stream-sources/set-cookie-header.webp>)

### Configure cookies

All the [configuration parameters](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#cookie-settings>) for client-side cookies are applicable for server-side cookies as well.

Additionally, there are two parameters which determine the cookies’ domain and the request URL:

Parameter| Description  
---|---  
[`sameDomainCookiesOnly`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>)| Enables strict domain-level cookie scoping for server-side cookies.  
  
**Default value** : `false` — the SDK stores cookies at the top-level domain (for example, `.example.com`), allowing them to be shared across all subdomains (for example, `app.example.com`, `blog.example.com`).  
  
When set to `true`, the SDK sets cookies only for the exact domain where the SDK is loaded. These cookies cannot be accessed by subdomains or the top-level domain.  
  
**Example** : If the SDK is loaded on `app.example.com` and `sameDomainCookiesOnly` is set to `true`, cookies are scoped only to `app.example.com` and are not accessible from `blog.example.com` or `example.com`.  
[`storage.cookie.domain`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#cookie-settings:~:text=value: /-,domain,-String>)| Specifies the domain of the cookies.  
  
### Sample behavior

Suppose there are two websites where the server-side cookies feature is enabled in the JavaScript SDK, namely `https://example.com` (parent website) and `https://sub.example.com` (sub-domain).

The following are the possible combinations of the configuration options and cookie domains:

  * **Parent domain website** : `https://example.com`

Domain| Expected behavior  
---|---  
Default| 

  * **Request URL:** Default endpoint (`https://example.com/rsaRequest`)
  * **Cookie domain:** `.example.com`
  * **Shared with sub-domain websites?** Yes, for example `https://sub.example.com`

  
Same domain cookies  
(`sameDomainCookiesOnly` must be set to `true`)| 

  * **Request URL:** Default endpoint (`https://example.com/rsaRequest`)
  * **Cookie domain:** `example.com` (without leading `.`)
  * **Shared with sub-domain websites?** No

  
Custom domain| 

  * Since this is already the parent domain website, the server-side cookies cannot be created for any domain other than the current one.
  * If you set the value of `storage.cookie.domain` to any value other than `example.com` or `.example.com`, the browser will not set any cookies.

  
  
  * **Sub-domain website** : `https://sub.example.com`

Domain| Expected behavior  
---|---  
Default| 

  * **Request URL:** Default endpoint (`https://example.com/rsaRequest`)
  * **Cookie domain:** `.example.com`
  * **Shared with sub-domain websites?** Yes, with the parent and any of its peer sub-domain websites, for example `https://sub2.example.com`

  
Same domain cookies  
(`sameDomainCookiesOnly` must be set to `true`)| 

  * **Request URL:** `https://sub.example.com/rsaRequest`
  * **Cookie domain:** `sub.example.com` (without leading `.`)
  * **Shared with sub-domain websites?** No

  
Custom domain  
(`storage.cookie.domain` set to `.sub.example.com`.)| 

  * **Request URL:** `https://sub.example.com/rsaRequest`
  * **Cookie domain:** `.sub.example.com`
  * **Shared with sub-domain websites?** Yes, with all of its sub-domain websites, for example `https://level2.sub.example.com`

  
  
## Implementation

If you have implemented a different endpoint than the default (`rsaRequest`), update your instrumentation as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      useServerSideCookies: true, // Default: false
      dataServiceEndpoint: <custom_endpoint>
      ...
    });
    

The JavaScript SDK can successfully manage cookies if your website’s server is proficient to handle these requests and responds with the appropriate cookie headers. You can ensure this by using any of the following methods:

### Proxy

> ![info](/docs/images/info.svg)
> 
> RudderStack’s data plane handles these cookie requests out of the box.

This method involves setting up a proxy between the RudderStack data plane and the website to handle the cookie requests from the SDK.

[![](/docs/images/event-stream-sources/server-side-cookies-js-sdk.webp)](</docs/images/event-stream-sources/server-side-cookies-js-sdk.webp>)

Depending on the existing setup of your website, you can implement proxy as follows:

#### CDN

If your website is served via CDN, you can update it to support the cookie requests endpoint.

The following steps outline how to configure AWS CloudFront to proxy the requests to data plane. The configuration process is more or less similar for the other tools.

  1. Create a custom origin

Setting| Description  
---|---  
Origin Domain| Enter the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) from your RudderStack dashboard.  
Name| Provide a unique name for this origin.  
[![](/docs/images/event-stream-sources/server-side-cookies-js-sdk-4.webp)](</docs/images/event-stream-sources/server-side-cookies-js-sdk-4.webp>)

  2. Create behavior for `/rsaRequest` endpoint

Setting| Description  
---|---  
Path Pattern| Enter `/rsaRequest`.  
Origin and origin groups| Select the **Name** created in the previous step.  
Viewer Protocol Policy| Set to `HTTPS Only` or `Redirect HTTP to HTTPS`, as required.  
Allowed HTTP Methods| Select `GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE`.  
[![](/docs/images/event-stream-sources/server-side-cookies-js-sdk-1.webp)](</docs/images/event-stream-sources/server-side-cookies-js-sdk-1.webp>)

  3. Edit the origin request policy

Setting| Description  
---|---  
Name| Enter the name of custom origin request policy, for example `Custom-Origin-Request-Policy`.  
Headers| Select headers as shown below, allowing even the sub-domain sites to make cookie requests. Otherwise, you will face CORS errors for the `OPTION` requests.  
[![](/docs/images/event-stream-sources/server-side-cookies-js-sdk-3.webp)](</docs/images/event-stream-sources/server-side-cookies-js-sdk-3.webp>)

  4. Enter the following settings

Setting| Description  
---|---  
Cache key and origin requests| Select `Cache policy and origin policy (recommended)`  
Cache Policy| Select `CachingDisabled` as these are POST requests.  
Origin Request Policy| Select the name of custom origin request policy created in the previous step.  
[![](/docs/images/event-stream-sources/server-side-cookies-js-sdk-2.webp)](</docs/images/event-stream-sources/server-side-cookies-js-sdk-2.webp>)

By following the above steps, you can configure CloudFront to proxy specific requests to a different origin using behaviours and custom cache policies.

You can also enable logging in CloudFront to monitor requests and troubleshoot any issues. See [AWS CloudFront documentation](<https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>) for more information.

#### Reverse proxy

This method outlines the changes to the reverse proxy configuration to handle the cookie requests from the SDK.

The following sample snippet is for Nginx but the implementation is similar for other proxies like Apache or HAProxy.
    
    
    daemon off;
    events {
    }
    http {
        server {
            listen 8080;
            location /rsaRequest/ {
                proxy_pass <DATA_PLANE_URL>$request_uri;
            }
        }
    }
    

> ![info](/docs/images/info.svg)
> 
> Ensure that the request and response headers are not stripped off in the Nginx proxy configuration.

### Custom implementation

If you have another custom implementation of your website, [contact the RudderStack team](<mailto:support@rudderstack.com>) to share a sample implementation for your endpoint to handle the cookie requests from the JavaScript SDK.

#### Sample snippets
    
    
        type CookieData = {
          name: string;
          value: string;
        };
    
        type CookiesReqData = {
          options: {
            expires?: Date;
            maxAge?: number;
            path?: string;
            domain?: string;
            sameSite?: 'Lax' | 'Strict' | 'None';
            secure?: boolean;
          };
          cookies: CookieData[];
        };
    
        type RequestData = CookiesReqData;
    
        const ALLOWED_COOKIES = [
          'rl_user_id',
          'rl_trait',
          'rl_anonymous_id',
          'rl_group_id',
          'rl_group_trait',
          'rl_page_init_referrer',
          'rl_page_init_referring_domain',
          'rl_session',
          'rl_auth_token'
        ];
    
        const encode = (value: string) => {
          try {
            return encodeURIComponent(value);
          } catch (err) {
            return undefined;
          }
        };
    
        const generateCookieStrings = (data: RequestData): string[] => {
          try {
            const { cookies, options } = data;
            return cookies.filter((cookie: CookieData) => ALLOWED_COOKIES.includes(cookie.name)).map((cookie: CookieData) => {
              let cookieStr = `${encode(cookie.name)}=${encode(cookie.value)}`;
    
              let expires = options.expires;
    
              // Calculate expires from maxAge if provided
              if (cookie.value === '') {
                expires = new Date(Date.now() - 600 * 1000); // Set to past time to delete cookie
              } else if (options.maxAge) {
                expires = new Date(Date.now() + options.maxAge * 1000);
              }
    
              if (options.path) cookieStr += `; Path=${options.path}`;
              if (options.domain) cookieStr += `; Domain=${options.domain}`;
              if (expires) cookieStr += `; Expires=${expires.toUTCString()}`;
              if (options.sameSite) cookieStr += `; SameSite=${options.sameSite}`;
              if (options.secure) cookieStr += '; Secure';
    
              return cookieStr;
            });
          } catch (err) {
            return [];
          }
        };
    
        export default function cookieRequestHandler (ctx: Context) {
          const requestData: RequestData = ctx.request.body;
          const cookieStrings = generateCookieStrings(requestData);
          cookieStrings.forEach(cookieStr => {
            ctx.response.append('Set-Cookie', cookieStr);
          });
          ctx.status = 200;
        }
    
    
    
        type CookieData = {
          name: string;
          value: string;
        };
    
        type CookiesReqData = {
          options: {
            expires?: Date;
            maxAge?: number;
            path?: string;
            domain?: string;
            sameSite?: 'Lax' | 'Strict' | 'None';
            secure?: boolean;
          };
          cookies: CookieData[];
        };
    
        type RequestData = CookiesReqData;
    
        const ALLOWED_COOKIES = [
          'rl_user_id',
          'rl_trait',
          'rl_anonymous_id',
          'rl_group_id',
          'rl_group_trait',
          'rl_page_init_referrer',
          'rl_page_init_referring_domain',
          'rl_session',
          'rl_auth_token'
        ];
    
        const encode = (value: string) => {
          try {
            return encodeURIComponent(value);
          } catch (err) {
            return undefined;
          }
        };
    
        const generateCookieStrings = (data: RequestData): string[] => {
          try {
            const { cookies, options } = data;
            return cookies.filter((cookie: CookieData) => ALLOWED_COOKIES.includes(cookie.name)).map((cookie: CookieData) => {
              let cookieStr = `${encode(cookie.name)}=${encode(cookie.value)}`;
    
              let expires = options.expires;
    
              // Calculate expires from maxAge if provided
              if (cookie.value === '') {
                expires = new Date(Date.now() - 600 * 1000); // Set to past time to delete cookie
              } else if (options.maxAge) {
                expires = new Date(Date.now() + options.maxAge * 1000);
              }
    
              if (options.path) cookieStr += `; Path=${options.path}`;
              if (options.domain) cookieStr += `; Domain=${options.domain}`;
              if (expires) cookieStr += `; Expires=${expires.toUTCString()}`;
              if (options.sameSite) cookieStr += `; SameSite=${options.sameSite}`;
              if (options.secure) cookieStr += '; Secure';
    
              return cookieStr;
            });
          } catch (err) {
            return [];
          }
        };
    
        export default function cookieRequestHandler(
          req: NextApiRequest,
          res: NextApiResponse
        ) {
          const requestData: RequestData = req.body;
          const cookieStrings = generateCookieStrings(requestData);
          cookieStrings.forEach(cookieStr => {
            res.append('Set-Cookie', cookieStr);
          });
          res.status(200);
        }
    
    
    
        $allowedCookies = [
            'rl_user_id', 'rl_trait', 'rl_anonymous_id', 'rl_group_id',
            'rl_group_trait', 'rl_page_init_referrer', 'rl_page_init_referring_domain',
            'rl_session', 'rl_auth_token'
        ];
    
        function isAllowedCookie($name) {
            return in_array($name, $GLOBALS['allowedCookies']);
        }
    
        function setCookiesFromRequest($data) {
            $cookies = $data['cookies'];
            $options = $data['options'];
    
            foreach ($cookies as $cookie) {
                if (!isAllowedCookie($cookie['name'])) {
                    continue;
                }
    
                $cookieOptions = []; // Array to hold cookie-specific options
                $maxAge = isset($options['maxAge']) ? $options['maxAge'] : null;
    
                if ($cookie['value'] === '') {
                    $maxAge = -600; // Set negative to ensure cookie is deleted (in seconds)
                }
    
                $expires = null;
                if (isset($maxAge)) {
                    $expires = time() + $maxAge;
                } elseif (isset($options['expires'])) {
                    $expires = strtotime($options['expires']);
                }
    
                // Set each option only if it's explicitly provided
                if (isset($expires)) {
                    $cookieOptions['expires'] = $expires;
                }
                if (isset($options['path'])) {
                    $cookieOptions['path'] = $options['path'];
                }
                if (isset($options['domain'])) {
                    $cookieOptions['domain'] = $options['domain'];
                }
                if (isset($options['secure'])) {
                    $cookieOptions['secure'] = $options['secure'];
                }
                if (isset($options['sameSite'])) {
                    $cookieOptions['samesite'] = $options['sameSite'];
                }
    
                setcookie($cookie['name'], $cookie['value'], $cookieOptions);
            }
        }
    
        function cookieRequestHandler() {
            $jsonData = json_decode(file_get_contents('php://input'), true);
            setCookiesFromRequest($jsonData);
        }
    
    
    
        ALLOWED_COOKIES = [
          'rl_user_id', 'rl_trait', 'rl_anonymous_id', 'rl_group_id',
          'rl_group_trait', 'rl_page_init_referrer', 'rl_page_init_referring_domain',
          'rl_session', 'rl_auth_token'
        ].freeze
    
        def cookie_request_handler
          data = JSON.parse(request.body.read)
          cookies_data = data['cookies']
          options = data['options'].symbolize_keys
    
          cookies_data.each do |cookie|
            next unless ALLOWED_COOKIES.include?(cookie['name'])
    
            value = cookie['value']
    
            cookie_options = {
              value: value
            }
    
            # Calculate expires from maxAge if provided
            if value.blank?
              cookie_options[:expires] = 600.seconds.ago # Set to past time to delete cookie
            elsif options[:maxAge]
              cookie_options[:expires] = Time.current + options[:maxAge].seconds
            elsif options[:expires]
              cookie_options[:expires] = options[:expires]
            end
    
            # Only set optional parameters if they are provided
            cookie_options[:path] = options[:path] if options[:path]
            cookie_options[:domain] = options[:domain] if options[:domain]
            cookie_options[:secure] = options[:secure] if options[:secure]
            cookie_options[:same_site] = options[:sameSite] if options[:sameSite]
    
            cookies[cookie['name']] = cookie_options
          end
          head :ok
        end
    
    
    
        import (
            "encoding/json"
            "net/http"
            "time"
        )
    
        var allowedCookies = []string{
            "rl_user_id", "rl_trait", "rl_anonymous_id", "rl_group_id",
            "rl_group_trait", "rl_page_init_referrer", "rl_page_init_referring_domain",
            "rl_session", "rl_auth_token",
        }
    
        func isAllowedCookie(name string) bool {
            for _, allowed := range allowedCookies {
                if allowed == name {
                    return true
                }
            }
            return false
        }
    
        func parseSameSite(s string) http.SameSite {
            switch s {
            case "Strict":
                return http.SameSiteStrictMode
            case "Lax":
                return http.SameSiteLaxMode
            case "None":
                return http.SameSiteNoneMode
            default:
                return http.SameSiteDefaultMode
            }
        }
    
        func cookieRequestHandler(w http.ResponseWriter, r *http.Request) {
            var data struct {
                Cookies []struct {
                    Name  string `json:"name"`
                    Value string `json:"value"`
                } `json:"cookies"`
                Options struct {
                    Expires  *time.Time `json:"expires"`
                    MaxAge   *int       `json:"maxAge"`
                    Path     string     `json:"path"`
                    Domain   string     `json:"domain"`
                    SameSite string     `json:"sameSite"`
                    Secure   bool       `json:"secure"`
                } `json:"options"`
            }
            json.NewDecoder(r.Body).Decode(&data)
    
            for _, cookie := range data.Cookies {
                if !isAllowedCookie(cookie.Name) {
                    continue
                }
    
                var expires time.Time
    
                // Calculate expires from maxAge if provided, or use expires if provided
                if cookie.Value == "" {
                    expires = time.Now().Add(-600 * time.Second) // Set to past time to delete cookie
                } else if data.Options.MaxAge != nil {
                    expires = time.Now().Add(time.Duration(*data.Options.MaxAge) * time.Second)
                } else if data.Options.Expires != nil {
                    expires = *data.Options.Expires
                }
    
                http.SetCookie(w, &http.Cookie{
                    Name:     cookie.Name,
                    Value:    cookie.Value,
                    Expires:  expires,
                    Path:     data.Options.Path,
                    Domain:   data.Options.Domain,
                    Secure:   data.Options.Secure,
                    SameSite: parseSameSite(data.Options.SameSite),
                })
            }
            w.WriteHeader(http.StatusOK)
        }
    

## FAQ

#### Are the server-side cookies applicable for device mode integrations as well?

No, RudderStack does not control the cookies set by any integration platform.

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/decrypt-persisted-data/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/consent-management/>)