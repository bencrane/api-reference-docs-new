# Video Events Spec

Learn the syntax and general conventions for sending events when tracking videos.

* * *

  * __14 minute read

  * 


RudderStack’s video specification lets you capture data on how a customer engages with your videos and the related ad content.

This documentation lists the conventions and best practices for sending video tracking events. It also clarifies the overall structure and classification of these events.

> ![warning](/docs/images/warning.svg)
> 
> Not all RudderStack destinations support video tracking. Refer to the individual [destination’s docs](<https://www.rudderstack.com/docs/destinations/overview/>) to check if it supports video tracking.

This guide is organized into the following three event categories:

  * Playback
  * Content
  * Ads


## Playback

Playback events are associated with the actual playback of video content and track information about the video player.

For example, when a customer plays a video, a `Video Playback Started` event is sent along with a unique `session_id`. All subsequent events generated from this session are tied to this `session_id`.

If a web page has two video players, two separate sessions and `session_id` would be associated to them. But if two separate videos are played on the same video player that would be a single session with two contents associated to it.

> ![info](/docs/images/info.svg)
> 
> All playback events are tracked and recorded at the session level.

### Playback events

This section details all video playback events.

> ![info](/docs/images/info.svg)
> 
> For more information on each of the properties associated with these events, refer to the Playback Event Properties section.

#### Video Playback Started

This event triggers when the user pressing the play button on the video player.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Started",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "ad_asset_id": ["ad1", "ad0"],
          "ad_pod_id": ["adRudderA", "adRudderB"],
          "ad_type": ["mid-roll", "post-roll"],
          "position": 0,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Paused

This event triggers when the user pauses the video.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Paused",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 0,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Interrupted

This event triggers when video playback stops unintentionally. Common reasons include network loss, user closing the browser, and redirect. You can pass the cause within the property `method`.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Interrupted",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 0,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false,
          "method":"network loss"
        }
    }
    

#### Video Playback Buffer Started

This event triggers when content or an ad is buffering.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Buffer Started",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 0,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Buffer Completed

This event triggers when buffering for content or an ad finishes.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Buffer Completed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 0,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Seek Started

This event triggers when a user starts manually seeking a certain position of the video or ad in the playback. The `position` property indicates where the user is seeking from (time in seconds) and the `seek_position` indicates the position in the playback where the user is seeking to.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Seek Started",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 47,
          "seek_position": 120,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Seek Completed

This event triggers after a user manually seeks to a certain position of the video or ad in the playback. The `position` property indicates where the user resumes the playback.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Seek Completed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 120,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Resumed

This event triggers when the user resumes video playback after pausing.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Resumed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 120,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

#### Video Playback Completed

This event triggers when playback is complete and only when the session is finished. Note that the `position` property is equal to the `total_length` property.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Playback Resumed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "content_asset_ids": ["0129370"],
          "content_pod_ids": ["RudderA", "RudderB"],
          "position": 300,
          "total_length": 300,
          "bitrate": 128,
          "framerate": 24.00,
          "video_player": "youtube",
          "sound": 68,
          "full_screen": true,
          "ad_enabled": true,
          "quality": "hd1080",
          "livestream": false
        }
    }
    

### Playback event properties

All playback events share the same properties to describe the current state of the video player.

Here are the properties of this playback event:

Property| Type| Description  
---|---|---  
`session_id`| String| Unique ID that ties all events generated from a specific playback session. These events include playback, content, and ad events.  
`content_asset_id` or `content_asset_ids`| String or Array [String]| Content asset ID/s of the video/s playing or about to play. For `Video Playback Started` events, an array of unique asset IDs should be sent. For other playback events, a single content asset ID at the time of the event should be sent.  
`content_pod_id` or `content_pod_ids`| String or Array [String]| Content pod ID/s of the video/s playing or about to play. For `Video Playback Started` events, an array of unique pod IDs should be sent. For other playback events, a single content pod ID associated with the current content pod at the time of the event should be sent.  
`ad_asset_id`| String or Array [String]| Ad asset ID/s of the video/s playing or about to play. For `Video Playback Started` events, an array of unique ad asset IDs should be sent. For other playback events, a sinule ad asset ID at the time of the event should be sent.  
`ad_pod_id`| String or Array [String]| Ad pod ID/s of the video/s playing or about to play. For `Video Playback Started` events, an array of unique ad pod IDs should be sent. For other playback events, a single ad pod ID at the time of the event should be sent.  
`ad_type`| Enum| Type of ad playing. The values can be `pre-roll`, `mid-roll`, or `post-roll`.  
`position`| Integer| Current index position of the playhead in seconds. It includes the time of any seen ads. If the playback is a livestream, refer to the documentation of the relevant destination for steps on correctly passing the playhead position.  
`seek_position`| Integer| Index position of the playhead the user is seeking to. Only available for `Video Playback Seek Started` events. On Video Playback Seek Completed events, the `seek_position` should be equal to `position`.  
`total_length`| Integer| Total duration of the video playback in seconds. Includes the total time of all content and ads in the session. Set to `null` in case of livestream playback.  
`bitrate`| Integer| Bit rate of the video playback in `kbps`.  
`framerate`| Float| Average frame rate of the video playback in `fps`.  
`video_player`| String| Name of the video player. Example: `youtube`, `vimeo`, etc.  
`sound`| Integer| Sound level of the video playback. Range is from 0-100, where 0 is mute and 100 is full volume.  
`full_screen`| Boolean| `true` if the playback is in fullscreen mode.  
`ad_enabled`| Boolean| `false` if the user has an ad blocker. If the user can view your video ads, it is set to `true`.  
`quality`| String| Quality of the video. Examples: `hd1080`, `highres`  
`method`| String| For the `Video Playback Interrupted` events, you can send this property noting how the playback was interrupted. Some examples include `device lock`, `call`, and `browser redirect`.  
`livestream`| Boolean| `true` if the playback is live stream.  
  
## Content

A content **pod** refers to a part / group / segment of the video content or the ad within the playback.

Suppose a video playback session has a video and one mid-roll advertisement. The mid-roll ad splits the playback into two separate content pods and a single ad pod.

The flow is:

  * First Content Pod: from the start of the playback to the start of the mid-roll ad
  * Ad Pod: from the start to finish of the ad
  * Second Content Pod: from the the restart of the playback to completion


> ![info](/docs/images/info.svg)
> 
> All of these events happen within the flow of one playback start.

### Content events

This section details all video content events.

> ![info](/docs/images/info.svg)
> 
> For more information on the properties associated with these events, refer to the Content Event Properties section.

#### Video Content Started

This event triggers when a video content segment starts within a playback.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Content Started",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "program": "Planet of the Apes",
          "title": "Introduction",
          "description": "Sample description",
          "season": "3",
          "position": 0,
          "total_length": 300,
          "genre": "SciFi",
          "publisher": "Amazon",
          "full_episode": true,
          "keywords": ["apes", "forests", "zoo"]
        }
    }
    

#### Video Content Playing

These events are heartbeats triggering every `n` seconds to track the user’s current position in the video content, determined by the `position` property.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Content Playing",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "program": "Planet of the Apes",
          "title": "Introduction",
          "description": "Sample description",
          "season": "3",
          "position": 234,
          "total_length": 300,
          "genre": "SciFi",
          "publisher": "Amazon",
          "full_episode": true,
          "keywords": ["apes", "forests", "zoo"]
        }
    }
    

#### Video Content Completed

This event triggers once the video segment, within playback, is completed. Note that the `position` property is equal to the `total_length` property.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Content Completed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "program": "Planet of the Apes",
          "title": "Introduction",
          "description": "Sample description",
          "season": "3",
          "position": 300,
          "total_length": 300,
          "genre": "SciFi",
          "publisher": "Amazon",
          "full_episode": true,
          "keywords": ["apes", "forests", "zoo"]
        }
    }
    

### Content event properties

All content events share the same properties describing the current state of the video content being viewed by the user.

Here are the content event properties:

Property| Type| Description  
---|---|---  
`session_id`| String| Unique ID that ties all events generated from a specific playback session. The value should be same for playback, content, and ad events from the same session.  
`asset_id`| String| Unique ID of the video content asset  
`pod_id`| String| Unique ID of the video content pod  
`title`| String| Title of the video content  
`description`| String| Short description of video content  
`keywords`| Array [String]| Array of keywords to describe or categorie the video content  
`season`| String| Season number, if applicable  
`episode`| String| Episode number, if applicable  
`genre`| String| Genre of the video content asset  
`program`| String| Name of the program/show, if applicable  
`publisher`| String| Publisher/creator/author of the video content asset  
`channel`| String| Channel the video content is playing  
`full_episode`| Boolean| True if the video content asset is a full episode  
`livestream`| Boolean| True if a live stream  
`airdate`| ISO 8601 Date String| Original date of the video content airing/publishing  
`position`| Integer| Current index position of the video content **in seconds**. This does not include any ads played in this duration. In case of live streams, refer to the specific [destination’s docs](<https://www.rudderstack.com/docs/destinations/overview/>) for details on how to pass `position`.  
`total_length`| Integer| Total length of video content in seconds. This does not include any ads in the playback. For livestream playback this should be set to null.  
`bitrate`| Integer| Current bit rate in kbps.  
`framerate`| Float| Frame rate in fps.  
  
## Ads

### Ad events

For more information on each of the properties associated with these events, refer to the Ad Event Properties section.

#### Video Ad Started

This event triggers when an ad starts playing in the video playback.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Ad Started",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "type": "mid-roll",
          "title": "Our Planet",
          "position": 0,
          "total_length": 25,
          "publisher": "BBC",
          "load_type": "linear"
        }
    }
    

#### Video Ad Playing

This event triggers every `n` seconds while the ad is playing and is determined by the `position` property.

Here is a sample event:
    
    
    {
        "type": "track",
        "event": "Video Ad Playing",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "type": "pre-roll",
          "title": "Our Planet",
          "position": 3,
          "total_length": 25,
          "publisher": "BBC",
          "load_type": "linear"
        }
    }
    

#### Video Ad Completed

This event triggers after the ad is complete. Note that the `position` property is equal to the `total_length` property.
    
    
    {
        "type": "track",
        "event": "Video Ad Completed",
        "userId": "user12345",
        "properties": {
          "session_id": "12345",
          "asset_id": "123",
          "pod_id": "RudderA",
          "type": "pre-roll",
          "title": "Our Planet",
          "position": 25,
          "total_length": 25,
          "publisher": "BBC",
          "load_type": "linear"
        }
    }
    

### Ad event properties

All the ad events share the same properties that describe the current state of the video ad content in the playback.

Here are the ad event properties:

Property| Type| Description  
---|---|---  
`session_id`| String| Unique ID that ties all events generated from a specific playback session. The value should be same for playback, content, and ad events from the same session.  
`asset_id`| String| Unique ID of the ad asset  
`pod_id`| String| Unique ID of the ad pod  
`pod_position`| Integer| Position of the ad asset relative to other ads in the same pod  
`pod_length`| Integer| Number of ad assets in the current ad pod  
`type`| Enum| Type of ad. Values can be either `pre-roll`, `mid-roll`, or `post-roll`.  
`title`| String| Title of the ad  
`publisher`| String| Author/creator/publisher of the ad  
`position`| Integer| Current position in the ad, in seconds.  
`total_length`| Integer| Length of the ad asset in seconds.  
`load_type`| Enum| If the ad is loaded dynamically or is the same for all users. Values can be `dynamic` or `linear`.  
`content`| Object| Some destinations require content metadata to be sent with ad events. Send all metadata as a Content Event Object under this property.  
`quartile`| Integer| For Video Ad Playing events, indicates when a specific ad quartile is reached. If you are using a client-side library to track your video events, this property is optional as RudderStack automatically tracks the ad quartiles.  
  
## Resuming playback

Every `Video Playback Resumed` the event should be followed by a heartbeat event (`Video Content Playing`) or a `Video Ad Playing` event, depending on what asset the playback resumes to.

## Video quality

RudderStack lets you track and analyze the performance and quality of your video content during playback.

When a user changes the video quality during playback, a Video Quality Updated event triggers along with the following properties:

  * `bitrate`: Updated bit rate in `kbps`.
  * `framerate`: Updated frame rate in `fps`.
  * `startupTime`: Time when the video quality was changed by the user.
  * `droppedFrames`: If any frames were dropped during the video quality change.


## Events lifecycle

The following event flow demonstrates how you can implement the RudderStack video specification:

#### 1\. User presses play on a video player
    
    
    rudderanalytics.track("Video Playback Started", {
      session_id: "12345",
      content_asset_ids: ["123"],
      content_pod_ids: ["RudderA"],
      ad_asset_ids: ["ad1"],
      ad_pod_ids: ["adRudderA"],
      ad_types: ["mid-roll"],
      position: 0,
      total_length: 300,
      bitrate: 128,
      video_player: "youtube",
      sound: 66,
      full_screen: true,
      ad_enabled: false,
      quality: "hd1080",
    })
    

#### 2\. Video playback starts playing the content
    
    
    rudderanalytics.track("Video Content Started", {
      session_id: "12345",
      asset_id: "123",
      pod_id: "RudderA",
      title: "Our Planet!",
      description: "Deep look into our amazing planet",
      keywords: ["nature", "entertainment"],
      season: "1",
      episode: "90",
      genre: "entertainment",
      program: "BBC",
      publisher: "BBC",
      position: 0,
      total_length: 300,
      channel: "ten",
      full_episode: true,
      livestream: false,
      airdate: "2020-04-23",
    })
    

#### 3\. User views the content for 10 seconds followed by a 10 second heartbeat
    
    
    rudderanalytics.track("Video Content Playing", {
      session_id: "12345",
      asset_id: "123",
      pod_id: "RudderA",
      title: "Our Planet!",
      description: "Deep look into our amazing planet",
      keywords: ["nature", "entertainment"],
      season: "1",
      episode: "90",
      genre: "entertainment",
      program: "BBC",
      publisher: "BBC",
      position: 10,
      total_length: 300,
      channel: "ten",
      full_episode: true,
      livestream: false,
      airdate: "2020-04-23",
    })
    

#### 4\. Video playback is paused
    
    
    rudderanalytics.track("Video Playback Paused", {
      session_id: "12345",
      content_asset_id: "123",
      content_pod_id: "RudderA",
      ad_asset_id: null,
      ad_pod_id: null,
      ad_type: null,
      position: 11,
      total_length: 300,
      video_player: "youtube",
      sound: 66,
      bitrate: 128,
      full_screen: true,
      ad_enabled: false,
      quality: "hd1080",
    })
    

#### 5\. User resumes the video playback
    
    
    rudderanalytics.track("Video Playback Resumed", {
      session_id: "12345",
      content_asset_id: "123",
      content_pod_id: "RudderA",
      ad_asset_id: null,
      ad_pod_id: null,
      ad_type: null,
      position: 11,
      total_length: 300,
      video_player: "youtube",
      sound: 66,
      bitrate: 128,
      full_screen: true,
      ad_enabled: false,
      quality: "hd1080",
    })
    

#### 6\. Ad (mid-roll) starts playing
    
    
    rudderanalytics.track("Video Ad Started", {
      session_id: "12345",
      asset_id: "ad1",
      pod_id: "adRudderA",
      type: "mid-roll",
      title: "Thumbs Up",
      publisher: "Coca Cola",
      position: 0,
      total_length: 15,
      load_type: "linear",
    })
    

#### 7\. Ad 10 second heartbeat
    
    
    rudderanalytics.track("Video Ad Playing", {
      session_id: "12345",
      asset_id: "ad1",
      pod_id: "adRudderA",
      type: "mid-roll",
      title: "Thumbs Up",
      publisher: "Coca Cola",
      position: 10,
      total_length: 15,
      load_type: "linear",
    })
    

#### 8\. Ad plays completely
    
    
    rudderanalytics.track("Video Ad Completed", {
      session_id: "12345",
      asset_id: "ad1",
      pod_id: "adRudderA",
      type: "mid-roll",
      title: "Thumbs Up",
      publisher: "Coca Cola",
      position: 15,
      total_length: 15,
      load_type: "linear",
    })
    

#### 9\. Video content resumes playing. Heartbeats sent every 10 seconds
    
    
    rudderanalytics.track("Video Content Playing", {
      session_id: "12345",
      asset_id: "123",
      pod_id: "RudderA",
      title: "Our Planet!",
      description: "Deep look into our amazing planet",
      keywords: ["nature", "entertainment"],
      season: "1",
      episode: "90",
      genre: "entertainment",
      program: "BBC",
      publisher: "BBC",
      position: 11,
      total_length: 300,
      channel: "ten",
      full_episode: true,
      livestream: false,
      airdate: "2020-04-23",
    })
    

#### 10\. User finishes watching the video content
    
    
    rudderanalytics.track("Video Content Completed", {
      session_id: "12345",
      asset_id: "123",
      pod_id: "RudderA",
      title: "Our Planet!",
      description: "Deep look into our amazing planet",
      keywords: ["nature", "entertainment"],
      season: "1",
      episode: "90",
      genre: "entertainment",
      program: "BBC",
      publisher: "BBC",
      position: 300,
      total_length: 300,
      channel: "ten",
      full_episode: true,
      livestream: false,
      airdate: "2020-04-23",
    })
    

#### 11\. Video playback finished
    
    
    rudderanalytics.track("Video Playback Completed", {
      session_id: "12345",
      content_asset_id: null,
      content_pod_id: null,
      ad_asset_id: "ad1",
      ad_pod_id: "adRudderA",
      ad_type: null,
      position: 300,
      total_length: 300,
      sound: 66,
      bitrate: 128,
      full_screen: true,
      video_player: "youtube",
      ad_enabled: false,
      quality: "hd1080",
    })
    

## FAQ

#### What are pre-roll, mid-roll, and post-roll ads?

  * Pre-roll: Ads that appear before the start of the video playback
  * Mid-roll: Ads that appear in the middle of the video playback
  * Post-roll: Ads that appear after the video playback


These ads can be a promotional video by the sponsors or a piece of content offered by the content provider.