# Real-time Personalization

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Real-time Personalization

Personalize your webpage and app in real time with data from your customer 360.

* * *

  * __4 minute read

  * 


RudderStack’s **Real-time Personalization App** combines several of RudderStack’s API and integration features to make your customer 360 data available for personalization use cases. Instead of significant custom work, you can hand your website and app developers a ready-made endpoint with whatever customer 360 data your product or marketing team needs.

The Real-time Personalization App leverages three components:

  * Your customer 360 data set (generated through Profiles).
  * A Redis cache, where you push your customer 360 data.
  * RudderStack’s Activation API, which gives you real-time access to the data in your Redis cache.


## Implement real-time personalization with RudderStack

  1. Set up and run a Profiles project to generate the data you want to make available in real-time.
  2. Turn on the Activation API and add your Redis credentials.
  3. Integrate the API into your website or app.


### Step 1: Build a Profiles project

If you aren’t already running Profiles, the first step is to [create a new Profiles Project](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/create-new-project/>) to resolve user identities, and build features that drive personalization logic and content.

> ![info](/docs/images/info.svg)
> 
> Ensure that you have a [feature view](<https://www.rudderstack.com/docs/archive/profiles/0.20/concepts/feature-views/>) for the ID you will be using in your website or app (for example,`user_name` or `anonymous_id`)

### Step 2: Turn on Activation API

Once the Profiles project has been run in the RudderStack UI, turn on the [Activation API](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/activation-api/>).

[![RudderStack Activation API](/docs/images/profiles/activation-api-toggle-v2.webp)](</docs/images/profiles/activation-api-toggle-v2.webp>)

This will sync your data with your Redis cache.

[![Redis cache](/docs/images/profiles/redis_cache.webp)](</docs/images/profiles/redis_cache.webp>)

### Step 3: Integrate Activation API into website or app

> ![info](/docs/images/info.svg)
> 
> See [How we built RudderStack’s real-time personalization engine](<https://www.rudderstack.com/blog/how-we-built-rudderstacks-real-time-personalization-engine/>) for a detailed example on integrating the Activation API with your website.

Once you enable the Activation API, your frontend and mobile developers can integrate it into your websites and apps to deliver last-mile personalized experiences.

At a high level, the implementation consists of:

  * Accessing a unique identifier for the visitor or app user.
  * Sending that ID to the API endpoint, looking up the user, and returning additional available data.
  * Customizing the experience based on the features received from the endpoint.


## Website personalization sample code

This section contains several code samples for implementing personalization on a website running Next.js.

### Access and decrypt user’s unique identifier

For website personalization, to minimize delay, you can intercept the server request and then decrypt the `anonymousId` utilizing [@rudderanalytics/analytics-js-cookies](<https://www.npmjs.com/package/@rudderstack/analytics-js-cookies>).

A sample code from a website built on Next.js:
    
    
    import { NextRequest, NextResponse } from 'next/server'
    import { RequestCookies, ResponseCookies } from '@edge-runtime/cookies'
    import { getDecryptedValue, anonymousUserIdKey } from '@rudderstack/analytics-js-cookies'
    
    export default async function middleware(request: NextRequest) {
      const headers = new Headers()
      const requestCookies = new RequestCookies(request.headers)
      const anonCookie = requestCookies.get(anonymousUserIdKey)
    
      if (anonCookie?.value) {
        const anonymousId = getDecryptedValue(anonCookie.value)
        // next step...  
      }
      
      return NextResponse.next({ headers })
    }
    

### Make an async request to Activation API

Once you have the decrypted identifier, you can pass it to the Activation API endpoint to look up a user and pull down their data from Redis.

A sample code from a website built on Next.js:
    
    
    export default async function middleware(request: NextRequest) {
      // previous code here
    
      if (anonCookie?.value) {
        const anonymousId = getDecryptedValue(anonCookie.value)
        const profilesAPI = 'https://profiles.rudderstack.com/v1/activation'
    
        const profilesRes = await fetch(profilesAPI, {
          method: 'POST',
          body: JSON.stringify({
            entity: 'user',
            destinationId: /* YOUR DESTINATION ID HERE */,
            id: {
              type: 'anonymous_id',
              value: anonymousId
            }
          }),
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${process.env.PROFILES_BEARER_TOKEN}`
          },
          cache: 'no-cache'
        })
        // next step...
      }
    
      return NextResponse.next({ headers })
    }
    

### Set `ResponseCookies` with values required for personalization

Lastly, you can set a ResponseCookie with the values required for personalization.

A sample code from a website built on Next.js:
    
    
    export default async function middleware(request: NextRequest) { 
      // previous code here
    
      if (anonCookie?.value) {
    
        // previous code here
    
        let userAppSignUp = false
        const { data }: ProfilesResponseType = await profilesRes.json()
        
        if (Object.keys(data).length !== 0) {
          const { USER_APP_SIGN_UP } = data['WEB_PERSONALIZATION:FEATURES_BY_ANON']
          if (USER_APP_SIGN_UP !== null && Number(USER_APP_SIGN_UP) === 1) { 
            userAppSignUp = true
          }
        }
    
        const signupValue = Boolean(userAppSignUp).toString()
        const expiryDate = new Date(Number(new Date()) + cookieExpiry)
        responseCookies.set('rs_activation_signed_up', signupValue, {
          expires: expiryDate,
          secure: true,
          path: '/'
        })
      }
    
      return NextResponse.next({ headers })
    }
    

### Access `ResponseCookie`

Once you’ve added a new ResponseCookie to the headers, you’re able to receive that on the frontend and use it to trigger the personalized experience.

A sample code from a website built on Next.js is shown below. Note that this example utilizes the `universal-cookie` library.
    
    
    /* ~/utils/cookies */
    
    import Cookies from 'universal-cookie'
    
    const cookies = new Cookies()
    const PROFILES_COOKIE = 'rs_activation_signed_up'
    
    export const getSignedUpFromCookie = () => {
      if (typeof window === 'undefined') return {}
      
      const cookie = cookies.get(PROFILES_COOKIE)
      return cookie
    }
    

### Deliver the last mile experience

At this point, your developers can leverage the data to drive the logic (and content) of personalized experiences.

A sample code from a website built on Next.js is shown below. In this example, the code changes a button based on a user’s signup status.
    
    
    import { getSignedUpFromCookie } from '~/utils/cookies'
    
    export const HeaderCTAButton = () => {
      const signedUp = getSignedUpFromCookie()
      const buttonClass = signedUp ? 'signed-up' : 'default'
      const buttonText = signedUp ? 'Request Demo' : 'Try for free'
      const buttonURL = signedUp ? '/request-demo' : '/try-for-free'
    
      return (
        <a className={`button ${buttonClass}`} href={buttonURL}>{buttonText}</a>
      )
    }
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/data-apps/propensity/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/additional-resources/>)