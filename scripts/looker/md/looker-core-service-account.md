# The Looker service account  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/looker-core-service-account

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  The Looker service account
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
Looker (Google Cloud core) uses a service agent, called a _Looker service account_ , to perform certain activities. A single Looker service account works on behalf of all Looker (Google Cloud core) instances in a given Google Cloud project. The Looker service account is automatically created the first time a Looker (Google Cloud core) instance is created in a project.
The service account allows Looker (Google Cloud core) to connect to other services, such as BigQuery.
Sometimes, such as when you're using Application Default Credentials (ADC) with a connection to BigQuery in another project, you need to view information about the Looker service account, such as its email address.
Or, if you are planning to use CMEK and are going to use the Google Cloud CLI, Terraform, or the API to configure CMEK before you create the Looker (Google Cloud core) instance, you must create the Looker service account manually _before_ you create the instance.
To view or create the Looker service account, select one of the following options:
More
To view the Looker service account:
  1. In the Google Cloud console, go to the **IAM** page.Go to IAM
  2. Select the project that the Looker (Google Cloud core) instance resides in.
  3. Select the **Include Google-provided role grants** checkbox.


To create or view the Looker service account:
```

gcloud beta services identity create --service=looker.googleapis.com --project=PROJECT_ID


```

Replace `PROJECT_ID` with the project that the Looker (Google Cloud core) instance resides in.
The service account name will be `Looker Service Account`. The email will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


