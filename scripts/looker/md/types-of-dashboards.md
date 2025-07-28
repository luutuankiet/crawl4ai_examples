# Comparing user-defined and LookML dashboards  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/types-of-dashboards

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  Comparing user-defined and LookML dashboards
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
A Looker dashboard is a collection of queries displayed as visualizations on a screen. Users can alter filters on dashboards, apply alerts to tiles, set up dashboard delivery schedules, and download a dashboard's data, among other things.
There are two types of Looker dashboards: user-defined dashboards and LookML dashboards.
Each type of dashboard has different benefits and constraints:
Characteristic | User-Defined Dashboard | LookML Dashboard  
---|---|---  
Generally created and edited by | Business users and Looker developers. | A select group of LookML developers.  
Defined | By adding query tiles, Look-linked tiles, or text in the user interface; arranging them using drag-and-drop operations; and adding and formatting dashboard filters and other options (as described on the Creating user-defined dashboards documentation page). | Written and edited in a YAML-based dashboard file, as described in the Creating a LookML dashboard file section of the Building LookML dashboards documentation page.  
Updated | When the dashboard is edited or the corresponding saved Looks are updated. | When the LookML file for the dashboard is edited.  
Stored | In a user's personal folder or in a shared folder for easy collaboration across a wider group of users. | As version-controlled files that are associated with the project in a Git repository. By default, LookML dashboards are accessible for viewing in the **LookML dashboards** folder located in the **All folders** top-level folder. They can also be moved to other folders as desired. LookML dashboards are not shown in the **Recently Viewed** tab of the homepage or on the **Recently viewed** page.  
Convertible | To LookML dashboards, as described in the Getting dashboard LookML from a dashboard section of the Viewing dashboards documentation page. | To user-defined dashboards, as explained on the Converting from LookML to user-defined dashboards documentation page.  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


