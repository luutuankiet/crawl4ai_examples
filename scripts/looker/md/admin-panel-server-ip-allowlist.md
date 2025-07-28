# Admin settings - IP Allowlist  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-server-ip-allowlist

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Adding your IP address
  * Adding a new rule




Was this helpful?
Send feedback 
#  Admin settings - IP Allowlist
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Adding your IP address
  * Adding a new rule


The **IP Allowlist** page lets you specify a list of IP addresses that can access your Looker instance. For a list of specific IPs to allow based on your region, see Enabling secure database access. When the IP allowlist is enabled, your Looker instance filters IP addresses at the application level, allowing connections from _only_ the IP addresses on the allowlist. Looker refuses connection attempts from all other IP addresses. When the IP allowlist is disabled, your Looker instance can accept connections from any IP address.
The **IP Allowlist** page is available only for Looker-hosted instances. Customer-hosted instances won't see this option in the **Admin** menu. To view the **IP Allowlist** page, from the **Server** section of the **Admin** menu, select **IP Allowlist**.
The **IP Allowlist** page lists the rules that you use to configure which IP addresses and subnet masks can access your Looker instance. Each rule also defines whether users from those IP addresses can log in only from the Looker UI, only from the Looker API, or from both sources.
In addition to viewing existing IP allowlist rules, you can perform the following tasks:
  * Enable or disable the IP allowlist with the **Enable Allowlist** switch. When the allowlist is active, only users from listed IP address can connect.
  * Define a new rule, which adds more IP addresses to the allowlist.
  * Enable, disable, edit, or delete an existing rule.


## Adding your IP address
If the IP allowlist has no rules defined, as when you first access the list, Looker will display two alerts:
  * a tooltip next to the **Enable Allowlist** switch displays a warning icon
  * a note reading **Your IP address is not allowlisted** appears next to the switch


Select the **Your IP address is not allowlisted** text to obtain your detected IP address. Select **Add Rule** to add your IP address to the allowlist by using the following instructions.
## Adding a new rule
Select **Add Rule** to add an IP address or a range of addresses to the allowlist. Looker displays the **New IP Allowlist Rule** dialog. To add a new rule, follow these steps:
  1. Enter a name for the new rule in the **Label** field.
  2. Enter a range of approved IP addresses in the **IP Range** field using an IP address and a subnet mask, as described in CIDR notation.
  3. Specify whether the new rule applies only to login attempts from the Looker UI, only to login attempts from the Looker API, or to login attempts from both sources in the **UI or API?** drop-down menu.
  4. Select **Save**.


## Things to know
While configuring your IP allowlist, keep the following considerations in mind:
  * Adding more than 50 rules may negatively impact Looker's performance.
  * Certain Looker Action Hub features such as the Slack integration and OAuth-enabled actions don't work when the IP allowlist is enabled.
  * To integrate Git pull requests with any LookML projects, you need to add to the allowlist the range of IP addresses from which your Git provider makes outbound requests. For example, GitHub IP addresses are available from their meta API endpoint. IPs are subject to change and will be different for other Git providers.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


