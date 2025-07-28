# Viewing your scheduled data deliveries  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/user-schedules

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Viewing your scheduled data deliveries
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


Once you have set up a recurring delivery of a dashboard or Look, Looker displays that schedule on the **Schedules** page. This option is only visible if your Looker admin has given you permission to schedule dashboards and Looks.
To reach the **Schedules** page, select the user profile picture and choose **Schedules**.
The **Schedules** page provides information about all the schedules that you have created and that have not been deleted.
The columns in the **Schedules You've Created** table show these settings:
  * **ID** : A unique ID number associated with each of your scheduled data deliveries.
  * **Updated** : The time and date at which your schedule was created or most recently modified.
  * **Name** : The name of the schedule, which you can set when creating or editing the schedule.
  * **Scheduled Times** : The time and frequency of each of your schedules. For schedules based on a time, the column will show the time of delivery. If delivery is triggered by a datagroup, it will show the name of that datagroup.
  * **Last Time Ran** : The most recent time that the data delivery occurred.
  * **Recipients** : The recipients' email addresses or the destination address of the data delivery.
  * **Type** : Whether the schedule is for the delivery of a Look or a dashboard.


### Filtering
You can limit the schedules Looker displays, based on criteria that you specify.
For example, to view only schedules whose titles contain the word _customer_ , enter the word `customer` in the Search bar. Or, if you want to view data deliveries that are scheduled only for weekdays, search on the term _weekdays_.
### Sorting
You can sort your schedules based on the **ID** , **Updated** , **Name** , **Last Time Ran** , or **Type** column in either ascending or descending order by clicking on the column heading.
### Deleting
> If all recipients unsubscribe from a scheduled email delivery, that schedule is deleted from Looker and from this page.
To delete a schedule, click the **Delete** button for that schedule's listing. Looker will display a window asking you to confirm the deletion.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


