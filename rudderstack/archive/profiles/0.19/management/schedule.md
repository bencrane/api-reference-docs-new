# Schedule

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Schedule

Schedule your Profiles project in the RudderStack dashboard.

* * *

  * __less than a minute

  * 


Once you have [imported your Profiles project from Git repository](<https://www.rudderstack.com/docs/archive/profiles/0.19/management/import-from-git/>) in the RudderStack app, you can schedule it to run at the specified frequency and time interval.

Go to the **Settings** tab of your project and click the edit icon in the **Schedule info** section:

[![Schedule Profiles project](/docs/images/profiles/schedule-settings.webp)](</docs/images/profiles/schedule-settings.webp>)

### Basic

Use this setting to run syncs at a given time interval and specified time (in UTC).

[![Schedule Profiles project](/docs/images/profiles/predictive-features-snowflake/schedule-basic.webp)](</docs/images/profiles/predictive-features-snowflake/schedule-basic.webp>)

  * **Frequency** \- You can choose the data sync frequency from the following options:

    * 15 minutes
    * 30 minutes
    * 1 hour
    * 3 hours
    * 6 hours
    * 12 hours
    * 24 hours
  * **Sync Starting At** \- Specify the time (in UTC) at which the data sync should start.


### CRON

Schedule your project using CRON expressions for more specific scheduling, for example, daily on Tuesdays and Thursdays.

> ![info](/docs/images/info.svg)
> 
> Use the [CRON scheduler utility](<https://crontab.guru/>) to get the CRON expression.

[![Schedule Profiles project](/docs/images/profiles/predictive-features-snowflake/schedule-cron.webp)](</docs/images/profiles/predictive-features-snowflake/schedule-cron.webp>)

### Manual

This setting lets you run the Profiles project manually. RudderStack won’t start the run until you explicitly trigger it by navigating to the **History** tab of your project and clicking **Run**.

[![Schedule Profiles project run manually](/docs/images/profiles/profiles-run-manual.webp)](</docs/images/profiles/profiles-run-manual.webp>)

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/management/import-from-git/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/management/activations/>)