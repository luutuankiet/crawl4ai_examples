# Manage maintenance policies for a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-maintenance

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Maintenance settings
  * Set a preferred window for maintenance
  * Configure a deny maintenance period
  * Maintenance example
  * Upcoming maintenance notifications
    * Opt in to maintenance notifications
  * Find scheduled maintenance




Was this helpful?
Send feedback 
#  Manage maintenance policies for a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Maintenance settings
  * Set a preferred window for maintenance
  * Configure a deny maintenance period
  * Maintenance example
  * Upcoming maintenance notifications
    * Opt in to maintenance notifications
  * Find scheduled maintenance


Once per month, Looker (Google Cloud core) schedules maintenance periods during which your instance will be upgraded. During a maintenance period, your instance will be restarted and you will be temporarily unable to access your instance. You can specify a maintenance window for your instance, in the form of a day of the week and time of day during which maintenance will take place. If you do not specify a preferred maintenance window, upgrades will take place within two weeks of the rollout of a new Looker (Google Cloud core) version. You can also specify a **Deny Maintenance Period** to block maintenance from taking place during the time you specified.
This page discusses finding scheduled maintenance, setting a preferred window for maintenance, specifying a maintenance deny period, and receiving and configuration settings for notifications about upcoming maintenance for a Looker (Google Cloud core) instance.
## Required role
To get the permissions that you need to configure maintenance settings for a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
## Maintenance settings
Looker (Google Cloud core) lets you configure maintenance updates through a set of maintenance settings.
You can configure maintenance to be scheduled at times when brief downtime causes the lowest impact to your instance. You can configure the following:
  * **Maintenance Window**: The day of the week and the hour in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour.
  * **Deny Maintenance Period**: A block of days in which Looker (Google Cloud core) does not schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.


You can update maintenance policies when you create your Looker (Google Cloud core) instance or by editing the configuration for an existing instance.
## Set a preferred window for maintenance
To specify a preferred window during which Looker (Google Cloud core) will schedule maintenance, select one of the following options:
More
  1. In the Google Cloud console, create a Looker (Google Cloud core) instance or edit the configuration for an existing Looker (Google Cloud core) instance.
  2. Under **Maintenance Window** , in the **Preferred Maintenance** section, configure the following settings for the maintenance window:
     * **Day** : The day of the week on which your instance will be updated
     * **Time window** : The approximate time of the day that the instance maintenance will begin
  3. Select **Save**.


Use the `gcloud looker instances create` command if you're creating the instance, or use the `gcloud looker instances update` command if you're updating the instance, and include the following parameters:
```
--maintenance-window-day=MAINTENANCE_WINDOW_DAY
--maintenance-window-time=MAINTENANCE_WINDOW_TIME

```

Replace the following:
  * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`
  * `MAINTENANCE_WINDOW_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45)


Once you have specified a maintenance window, your changes to the setting will take up to a week to take effect.
## Configure a deny maintenance period
If you want to defer the scheduled maintenance to a later time, you can change the instance's deny maintenance period. A deny maintenance period can be up to 60 days long.
You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.
To specify a preferred window during which Looker (Google Cloud core) won't perform maintenance, select one of the following options:
More
  1. In the Google Cloud console, create a Looker (Google Cloud core) instance, or edit the configuration for an existing Looker (Google Cloud core) instance.
  2. Under the **Deny Maintenance Period** section, configure the following settings for the deny maintenance period:


  * **Start date** : Choose the start date of the period during which maintenance will not occur.
  * **End date** : Choose the end date of the period during which maintenance will not occur.
  * **Start/End time** : Define the specific time at which the **Deny Maintenance Period** begins (on the date you specified for **Start date**) and ends (on the date you specified for **End date**).


  1. Select **Save**.


Use the `gcloud looker instances create` command if you're creating the instance, or use the `gcloud looker instances update` command if you're updating the instance, and include the following parameters:
```
--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
      --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
      --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME

```

Replace the following:
  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
  * `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).


## Maintenance example
As an example, you can set your production instance's maintenance settings as follows:
  * **Maintenance Window** : Sundays between 12:00 AM and 1:00 AM ET
  * **Deny Maintenance Period** : December 1 at 10:00 PM through January 15 at 10:00 PM


## Upcoming maintenance notifications
You can have a notification about upcoming maintenance sent to your email up to one week before maintenance is scheduled. If you want to set an email filter for notifications, the email title is **[Looker (Google Cloud core) Advanced Maintenance Notification] Your instance is scheduled for maintenance.**
Maintenance notifications are not sent out by default. If you want to get a notification for an upcoming maintenance, you must follow all these steps:
  1. Set a maintenance window.
  2. Opt in to maintenance notifications at the project level.
  3. To receive notification about your scheduled maintenance, you need to complete both steps at least seven days before the next scheduled maintenance update for your Looker (Google Cloud core) instance.


Notifications are sent to the email address associated with your Google account. It's not possible to configure a custom email alias (for instance, a team email alias).
You can opt into maintenance notifications for all Looker (Google Cloud core) instances that have maintenance windows in a given project. You receive one notification per instance.
### Opt in to maintenance notifications
To turn on maintenance notifications:
  1. Go to the **Communication** page in the Google Cloud console:
Communication
  2. Select the **Product Notifications** tab.
  3. Select your project from the drop-down menu.
  4. In the row for Looker (Google Cloud core), set the email toggle to **ON**.


## Find scheduled maintenance
If maintenance has been scheduled for your instance, you can view it by following these steps:
  1. Go to the **Looker (Google Cloud core)** page in the Google Cloud console.
  2. Select the name of the instance that you want to view scheduled maintenance for.
  3. When you view configuration details for your instance, on the **DETAILS** page, you can view the following information:
     * **Scheduled Maintenance**
     * **Deny Maintenance Period**
     * **Last Deny Maintenance Period**


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


