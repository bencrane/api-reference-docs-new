# Feature Development

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Feature Development

Use unified profiles and enrich them with the required features/traits to drive targeted campaigns.

* * *

  * __3 minute read

  * 


Once you have [performed identity stitching](<https://www.rudderstack.com/docs/archive/profiles/0.10/identity-stitching/#how-to-perform-identity-stitching>) to map the individual entities to known identifiers, you can enhance the unified profiles with additional data points and features.

To develop user features, you can use a **entity traits 360** to define the features/traits in your warehouse tables. You can perform calculations over this data to devise meaningful outcomes, which can help marketing teams to run effective campaigns.

## How to define features?

You can use RudderStack’s [Entity Traits 360 model](<https://www.rudderstack.com/docs/archive/profiles/0.10/example/feature-table/>) to write feature definitions. The Profiles project generates and runs SQL in the background and automatically adds the resulting features to a entity traits 360.

You can produce a entity traits 360 or a feature table for specific projects like personalization, recommendations, or analytics.

> ![success](/docs/images/tick.svg)
> 
> You can combine the features to create even more features. You can also use [custom SQL queries](<https://www.rudderstack.com/docs/archive/profiles/0.10/feature-development/sql-models/>) to enrich unified user profiles for advanced use cases.

A sample configuration file to create a entity traits 360 model:
    
    
    var_groups:
      - name: vars
        entity_key: session
        vars:
            - entity_var:
                name: campaign_source_first_touch
                select: first_value(context_campaign_source) # Window functions are supported in entity_vars, as long as the value is unique for a given user id
                window:
                # All the window functions in entity_vars are partitioned by main_id by default. It can take only order_by as a parameter.
                    order_by:
                    # In this example, we take the oldest occurence of the campaign source, so we sort the rows by timestamp in ascending order
                        - timestamp asc
                from: inputs/rsIdentifies
                where: context_campaign_source is not null and context_campaign_source != ''
            - entity_var:
                name: first_seen_tracks
                select: min(timestamp::date) # Get oldest timestamp from the tracks table
                from: inputs/rsTracks
                description: First seen timestamp from tracks table.
                is_feature: false
            - entity_var:
                name: first_seen_identifies
                select: min(timestamp::date)
                from: inputs/rsIdentifies
                description: First seen timestamp from identifies table
                is_feature: false
            - entity_var:
                # Once min timestamps from both tracks and identifies are defined, we pick the earliest timestamp of both here.
                # The prev two are temp features used to derive this feature.
                name: first_seen_date
                select: to_date(least(coalesce('{{session.Var("first_seen_tracks")}}','{{session.Var("first_seen_identifies")}}'), coalesce('{{session.Var("first_seen_identifies")}}','{{session.Var("first_seen_tracks")}}')
            - entity_var:
                name: orders_completed_in_past_365_days
                select: count( * ) # SQL function to count all rows from tracks table where event_type = 'order_completed'
                from: inputs/rsTracks
                where: event = 'order_completed' and datediff(day, date(timestamp), current_date()) <= 365
                description: Number of orders completed in the past 365 days.
            - entity_var:
                name: n_active_days_total
                select: count(distinct(timestamp::date)) # SQL function to first convert timestamp to date, then count the distinct dates
                from: inputs/rsTracks # Refering to the tracks table defined in the inputs.yaml file
                description: Number of days since the user first visited the app.
    

## Benefits

  * You can use the output of the identity graph to define or compute features across multiple entity traits 360s.
  * As the number of features/traits increases, Profiles makes the maintenance process much easier by using a configuration file (as opposed to large and complex SQL queries).
  * Profiles generates highly performant SQL to build entity traits 360s, which helps mitigate computing costs and engineering resources when the data sets become large, dependencies become complex, and features require data from multiple sources.


## Use-cases

  * Create analytics queries like demographic views, user activity views, etc.
  * Send data using a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipeline to various cloud destinations.
  * Use RudderStack Audiences to send customer profiles to marketing tools (available for beta customers).


#### See also

  * [Sample entity traits 360 project](<https://www.rudderstack.com/docs/archive/profiles/0.10/example/feature-table/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.10/identity-stitching/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.10/feature-development/sql-models/>)