# Admin settings - Homepage  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/admin-panel-general-homepage

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting a default homepage for your instance
  * Setting a homepage for a specific user or group




Was this helpful?
Send feedback 
#  Admin settings - Homepage
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting a default homepage for your instance
  * Setting a homepage for a specific user or group


The **Homepage** page in the **General** section of Looker's **Admin** menu lets admins configure a default homepage for their Looker instance. Looker admins can also set a homepage for a specific user or group with the `landing_page` user attribute.
## Setting a default homepage for your instance
The Looker homepage appears when users log in to Looker or navigate to the homepage by clicking **Home** in the left navigation panel or by clicking the Looker logo. By default, the homepage for your instance is the pre-built Looker homepage, which displays a user's favorite content, that user's recently viewed content, and the recently viewed content at the organization. However, you can change this default to a URL within Looker.
The homepage options for your instance are available on the **Homepage** page under **Set a default homepage for your organization** :
  * **Looker's pre-built homepage** : The pre-built Looker homepage displays tabs for recently viewed content and favorited content. This setting is the default.
  * **A URL within Looker** : You can set the default homepage to a specific page within Looker (such as the **Favorites** page), a board, a folder, or a Markdown file (such as a README or document file in a project) by specifying a relative URL such as `/browse/boards/2`. If you set the homepage in your instance to a specific page within Looker or to a board, the **Home** button in the left navigation panel updates to the name of the page or the board.


If you have configured group or user homepage settings with the `landing_page` user attribute, those settings will override the default homepage that you have chosen for your instance. Users with group or user homepages will still be able to access a link to the instance-wide default homepage from the left navigation.
## Setting a homepage for a specific user or group
In addition to setting a homepage for your entire instance, you can configure homepage settings for specific users or groups with the `landing_page` user attribute.
You can assign a specific homepage to a user or to a group by setting the value of the `landing_page` user attribute to a relative URL within Looker. If you want to assign a specific homepage to multiple users, we recommend that you create a new group specifically for that homepage option.
> Setting a homepage for a specific group overrides the default homepage for your instance for members of the group. Setting a user-specific homepage also overrides any group homepage settings as well as the default homepage.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


