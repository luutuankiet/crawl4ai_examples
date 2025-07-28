# Delete or restart a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-delete-restart

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Delete a Looker (Google Cloud core) instance
  * Restart a Looker (Google Cloud core) instance




Was this helpful?
Send feedback 
#  Delete or restart a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Delete a Looker (Google Cloud core) instance
  * Restart a Looker (Google Cloud core) instance


You can delete or restart a Looker (Google Cloud core) instance.
## Required role
To get the permissions that you need to delete or restart a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
## Delete a Looker (Google Cloud core) instance
Instance deletion is permanent and unrecoverable.
Deleting a Looker (Google Cloud core) instance that is associated with a Looker Studio Pro subscription immediately converts any in-use complimentary Looker Studio Pro licenses to paid licenses.
To delete a Looker (Google Cloud core) instance, select one of the following options:
More
  1. On the **Instances** page, click the three-dot menu beside the instance.
  2. Select **Delete Instance**. If the instance is currently being modified, you will not be able to delete it.
  3. In the pop-up, confirm that you want to delete your instance by typing the instance name in the provided field and clicking **DELETE**.


You can also delete an instance from its configuration page by clicking **DELETE** in the instance configuration page icon bar.
```
gcloud looker instances delete INSTANCE_NAME --region=REGION --async

```

Replace the following:
  * INSTANCE_NAME: the name of the Looker (Google Cloud core) instance
  * REGION: the region the instance was created in


## Restart a Looker (Google Cloud core) instance
Restarting a Looker (Google Cloud core) instance stops any in-process Looker processes on the instance — including running queries, schedules, and alerts — and then restarts the instance. Once the restart has been completed, the instance will automatically resume its normal operations. Any queries that were running at the time of restart won't be completed unless you reinitiate them. Schedules and alerts will run on their specified cadence, but any jobs that were scheduled or that were being executed during the restart won't be completed.
If the instance is currently being modified, wait for it to complete its updates before you attempt a restart.
To restart a Looker (Google Cloud core) instance, select one of the following options:
More
  1. On the **Instances** page, click the name of the instance to view its configuration settings.
  2. Click **RESTART** in the instance configuration page icon bar.

```
gcloud looker instances restart INSTANCE_NAME --region=REGION --async

```

Replace the following:
  * INSTANCE_NAME: the name of the Looker (Google Cloud core) instance
  * REGION: the region the instance was created in


## What's next
  * Create a Looker (Google Cloud core) instance
  * Administer a Looker (Google Cloud core) instance from the Google Cloud Google Cloud console
  * Back up and restore a Looker (Google Cloud core) instance
  * Looker (Google Cloud core) admin settings


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


