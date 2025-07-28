# Looker integration: Google Ads Customer Match  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/how-to-use-the-google-ads-integration

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Enabling the action
  * Configuring your Looker query
  * Sending data to Google Ads Customer Match
  * Removing the action




Was this helpful?
Send feedback 
#  Looker integration: Google Ads Customer Match
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Enabling the action
  * Configuring your Looker query
  * Sending data to Google Ads Customer Match
  * Removing the action


> Customer-hosted instances may be unable to enable actions from the Looker Action Hub, especially actions that support streamed results or that use OAuth, if the customer-hosted Looker instance doesn't fulfill the Looker Action Hub requirements. 
> See the Sharing data through an action hub documentation page for suggested solutions to this potential issue. 
Looker offers an integration called Google Ads Customer Match to allow users to send segments and audiences based on first-party data from Looker directly to Google Ads. You can authenticate with your Google credentials and send one-off or recurring data deliveries to the Google Ads destination. 
## Enabling the action
A Looker admin must enable this action by following these steps: 
  1. Navigate to the **Actions** page from the Looker **Admin** panel. 
  2. Next to the **Google Ads Customer Match** action, click **Enable**. Click the **Refresh** button if the actions don't appear in the list. 
  3. Switch on the **Enable** toggle and click **Save**. 


Once enabled, this action will show up as a destination option for data deliveries in the Scheduler. 
> An individual Google account can be connected to one Looker instance only. 
## Configuring your Looker query
Before you can use the Google Ads Customer Match action, ensure that the column labels in your Looker query map correctly to the user identifiers in Google Ads. 
Looker checks each column label in the query against the following regex sets and maps the column label to the user identifiers in Google Ads based on its first regex match. All regex conditions are case-insensitive. 
You can choose to either upload CRM data or mobile device data. Note that mobile device data cannot be combined with any other types of CRM data. 
These are the regex conditions for user identifiers for CRM data: 
```
[/email/i, "hashed_email"],
[/phone/i, "hashed_phone_number"],
[/first/i, "address_info.hashed_first_name"],
[/last/i, "address_info.hashed_last_name"],
[/street|address/i, "address_info.hashed_street_address"],
[/city/i, "address_info.city"],
[/state/i, "address_info.state"],
[/country/i, "address_info.country_code"],
[/postal|zip/i, "address_info.postal_code"]

```

These are the regex conditions for user identifiers for mobile device IDs: 
```
  [/idfa|identifier.for.advertising/i, "mobile_id"],
  [/aaid|advertiser.assigned.user|google.advertising/i, "third_party_user_id"]

```

This means that a field can have a label value of "AAID", "Advertiser Assigned User", or "Google Advertising"; and any label will match and map to the `third_party_user_id` identifier.
Although each column label maps to only one identifier, there can be multiple column labels that map to the same identifier. For example, in a query that contains just `work_email` and `home_email`, both will be mapped to the email identifier. 
If your column labels don't match any identifiers, a Looker developer can perform one of the following actions: 
  * Updating the column's label in the query's LookML to include the appropriate term to match your identifiers in Google Ads 
  * Using a custom field to duplicate the column and give it a new label 


## Sending data to Google Ads Customer Match
You can send data from Explores and Looks to the Google Ads Customer Match action destination from the Looker Scheduler. 
> Make sure that your Google Ads account meets the Customer Match criteria and is enabled for Customer Match before you use this Looker integration. 
From your selected Explore or Look, click the gear menu in the upper right corner. For Looks or Explores, select **Send** for one-time deliveries. For Looks, select **Schedule** for recurring deliveries. For Explores, because there is no option to send a recurring delivery, you must select **Save & Schedule** to first save the Explore as a Look and then schedule the Look for a recurring delivery. 
> For more information about scheduling data deliveries, see the Using the Looker Scheduler to deliver content documentation page. 
Selecting a delivery option opens the Scheduler for Explores and Looks. Enter a title for your delivery. To deliver to the Google Ads Customer Match destination: 
  1. Select the **Google Ads Customer Match** icon from the **Where should this data go?** section of the Scheduler: 
  2. The first time you deliver to this destination, you must authenticate with your Google OAuth credentials. In the **Google Ads Customer Match** section of the Scheduler, click the **Sign in with Google** button. 
  3. In the **Sign in with Google OAuth** screen, select the appropriate Google account. Check the box next to the permissions you would like to grant the Looker app. Click **Continue** to confirm your choice to grant the requested permissions. If your login is successful, you will see a message to close the browser tab and return to the Scheduler. An individual Google account can be connected to one Looker instance only. 
  4. Back in the **Google Ads Customer Match** section of the Scheduler, click the **Verify credentials** button. 
  5. Once your credentials are verified, a **Choose login account** field appears. Select the appropriate login account from the drop-down. To reset the selection, you must close and reopen the form. 
  6. Select a target account from the **Choose target account** drop-down. The target account is where you want to send data, such as where the audience lists are defined in Customer Match. 
  7. In the **Create a new list or append to existing?** drop-down, choose whether to create a new list or append to an existing list. Looker recommends appending the list to help optimize the Google Ads bidding algorithm. Uploading a new list every time isn't a best practice as it resets the bidding algorithms. 
     * If you select **Append to existing** , pick which list you want to append to from the **Choose list to update** drop-down. 
     * If you select **Create new list** , enter values for the list name and description in the **New list name** and **New list description** fields. 
  8. Determine if you want the data to be hashed prior to delivery. All personal data must be normalized and hashed before it can be to Google Ads. If your data isn't yet hashed, select **Yes** and Looker will attempt to hash the data according to Google Ads requirements. If you select **No** , then the data will be sent as it appears in Looker, which means that the data should already be normalized and hashed within your database. 
> If the data isn't hashed correctly, your customer list won't match any audiences in Google Ads. 
  9. For recurring deliveries, set the trigger for the delivery. For **Repeating interval** triggers, set the frequency with which you would like to deliver this data. For **Datagroup update** triggers, choose the triggering datagroup from the **Select Datagroup** drop-down. Apply any additional filters to the scheduled delivery in the **Filters** section of the Scheduler. 
  10. Expand the **Advanced options** menu in the Scheduler. __Make sure to select**All Results**__. For recurring deliveries, select any additional scheduling conditions you would like to place on the delivery. 
  11. Review your delivery settings. For one-time deliveries, click **Send**. For recurring deliveries, click **Save All**. 


## Troubleshooting
  * If the target account you selected in the previous step 6 doesn't have at least one CRM-based user list open for memberships, you will see an error if you select **Append to existing**. To solve this problem, create a new list by sending the delivery as a one-off or by creating a new list in Google Ads. Once the list is created, it will be available to select as an option when Append to existing is selected from the **Create a new list or append to existing?** drop-down. 
  * If your Google Ads account isn't enabled for Customer Match, you won't be able to use this Looker integration. Make sure that your Google Ads account meets the requirements for the Customer Match policy. 
  * An individual Google account can be connected to only a single Looker instance. If you want to connect the Customer Match action to Google Ads from another Looker instance, you must remove Looker's access to your Google account and then reauthorize Looker's access to your Google account from that Looker instance. 


## Removing the action
To remove this integration, go to your Google user account and remove account access from the Looker application. 
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


