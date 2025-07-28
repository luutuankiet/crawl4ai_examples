# Error: Could not find the model or view requested  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/error-could-not-find-the-model-or-view-requested

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Troubleshooting
    * Change the URL of a single query
    * Use the Content Validator
  * I'm still seeing this error. Now what?




Was this helpful?
Send feedback 
#  Error: Could not find the model or view requested
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Troubleshooting
    * Change the URL of a single query
    * Use the Content Validator
  * I'm still seeing this error. Now what?


## The error
You may see the following error on an Explore, a Look, or a dashboard: 
```
Could not find the model or view requested.

```

## Common causes
Some common causes of this error include the following: 
  * **Typo in the URL:** If you manually created an Explore URL, check the model and Explore name in the URL to make sure that they are correct. 
  * **Explore or model name has changed:** Each Look or dashboard query is based on a model and an Explore. If the model name or Explore name changes, the Look or dashboard query will still reference the old name until you update it with the new name. For example, if the name of an Explore is changed from `old-name` to `new-name`, any associated Looks or dashboard queries will still try to use the `old-name` Explore until you update them. 


## Troubleshooting
There are multiple ways to resolve this error, but you can resolve most instances just by replacing the incorrect model or Explore name with a valid name. Use the following methods to update either a single query or all Looks and dashboards on your Looker instance: 
  * Change the URL of a single query
  * Use the Content Validator


### Change the URL of a single query
If you know that an Explore name or a model name has been changed, you can fix individual Looks and dashboards by using the expanded URL. The expanded URL contains the model name, the Explore name, and the field names. You can take advantage of this function to change the Explore or model name of the query. 
  1. Select **Explore from here** from the Look or dashboard query. 
  2. Select the **Explore actions** gear menu next to **Run** and **Edit** , and then select **Share**. 
  3. Copy the expanded URL and paste it somewhere else, such as into a document or your browser's address bar. (If you paste the URL into your browser's address bar, do not press Enter yet; if you do, the expanded URL will be turned into a shortened URL.) 
  4. Modify the URL text to change the name of the Explore. The URL takes the following form: ```
https://instance_name.looker.com/explore/MODEL_NAME/EXPLORE_NAME?fields=...
```

  5. If necessary, copy and paste the expanded URL into your browser, and press Enter or Return to navigate to the URL. 
  6. Save the Explore as a Look or dashboard query.


### Use the Content Validator
The Content Validator has a find-and-replace function. You can use this to replace the Explore name across all Looks. This will change _every_ Look and dashboard query that uses `old-name`, however, so take this step with caution. 
## I'm still seeing this error. Now what?
If you've tried the previous steps and continue to see the error, check with a Looker admin at your company to make sure that the requested model and Explore exist on your Looker instance. If you're still stuck, contact Looker support for further troubleshooting.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


