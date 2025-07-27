# Admin settings - Sessions  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-authentication-sessions

Skip to main content 
  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português – Brasil
  * 中文 – 简体
  * 中文 – 繁體

Console  Sign in




Send feedback 
#  Admin settings - Sessions
Stay organized with collections  Save and categorize content based on your preferences. 
By default, when a user logs in to Looker, they are given an option to stay logged in. This option appears as a checkbox at the bottom of the login page.
The **Sessions** page, in the **Authentication** section of the **Admin** menu, lets you configure whether users have the option to stay logged in, how long they stay logged in if they don't choose that option, and whether they can stay logged in from multiple devices.
## Inactivity Logout
By default, a user stays logged in to Looker for a set length of time that is determined by the **Persistent Sessions** and **Session Duration** settings, regardless of whether the user is actively using Looker.
If you enable **Inactivity Logout** , users are automatically logged out of Looker after 15 minutes of inactivity. Activity is defined as a user clicking anywhere in Looker, or touching the screen in the case of touchscreens, or typing anything into Looker. Therefore, if this setting is enabled, a user is logged out if they don't click or type anything for 15 minutes.
Two minutes before the user will be logged out, Looker displays a dialog to warn the user and give them the opportunity to stay logged in.
When a user is forcibly logged out as a result of inactivity, they are logged out of their inactive session. A session is unique to each browser, so if a user has multiple tabs open and logged in to Looker, they are logged out on all tabs. But, if they are logged in through multiple browsers, they are logged out only of the session on the inactive browser.
Any unsaved changes in the Looker IDE are stored. When the user logs back in and loads a file that has any unsaved changes in it, they are given the option to restore the unsaved changes.
When **Inactivity Logout** is enabled, **Persistent Sessions** is automatically disabled. In addition, **Session Duration** is set to a default of one day. The **Session Duration** setting can still be changed. The value set in **Session Duration** remains the maximum length of time a user can stay logged in, even if they are active the entire time.
For example, if **Inactivity Logout** is enabled and **Session Duration** is set to 5 hours, a user will be logged out under these circumstances:
  * If the user remains inactive for 15-minutes at any time during the 5-hour period, they will be logged out after the 15-minute inactivity period.
  * If the user has been active during the entire 5-hour session, a dialog screen will prompt them to re-authenticate to continue working. If the user doesn't re-authenticate, they will be logged out.


Additionally, with these settings, a user who has been active for 4 hours and 50 minutes before becoming inactive for 10 minutes will still be logged out after the 10-minute inactivity period. **Session Duration** remains the maximum time a user can stay logged in. Users who access Looker using either the Looker API or a signed embed are _not_ affected by **Inactivity Logout**.
## Persistent Sessions
When a user selects the option to stay logged in, they will be authorized to access Looker for 30 days. When they close and reopen their browser, they can navigate to Looker without being required to log in again.
Disabling **Persistent Sessions** removes the "Stay logged in" option from the login screen. Users will be automatically logged out after the amount of time specified in the **Session Duration** section, or whenever they close their browser. This forces users to re-authenticate the next time they access Looker.
**Persistent Sessions** is automatically disabled when **Inactivity Logout** is enabled.
## Session Duration
By default, when a user does not select the option to stay logged in, their session will expire after 30 minutes.
Two minutes before a session expires, the user is given the option to extend the session. If the user doesn't extend their session, their session ends and they are logged out of Looker.
The **Session Duration** field lets you change the amount of time a user can stay logged in before they will be notified and their session will expire. You can set this value from 5 minutes to 30 days.
  * If the **Session Duration** is 30 minutes or less, then the extended session will be the same duration as the session duration. For example, if the **Session Duration** is 5 minutes, then the extended session will also be 5 minutes.
  * If the **Session Duration** is more than 30 minutes, then the extended session will still be 30 minutes. For example, if the **Session Duration** is 1 day, then the extended session will be 30 minutes.


If **Inactivity Logout** is enabled, **Session Duration** must be set to a value between 15 minutes and 1 day. If **Session Duration** is set to a value outside of this range, the value will be set to 1 day.
## Concurrent Sessions
By default, users can remain logged in to Looker from multiple browsers and devices simultaneously. Disabling **Concurrent Sessions** lets you require users to log in from only one browser and device at a time. When **Concurrent Sessions** is disabled, a user is automatically logged out of any other browser session when they log in from a different browser or device.
## Session Location
If **Session Location** is enabled, a user's location will be tracked when they log in to Looker. This location information is based on the user's browser IP address and is available to users and admins on the **Sessions** page for visibility and management of sessions. The location information can help admins determine which sessions are current and which sessions should be deleted.
If **Session Location** is disabled, whenever a user logs in to Looker, their location won't be tracked.
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


