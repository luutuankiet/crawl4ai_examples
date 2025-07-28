# View information about a Looker (Google Cloud core) custom domain

**Source:** https://cloud.google.com/looker/docs/looker-core-custom-domain-settings

Skip to main content 
  * Español – América Latina

Console 




Was this helpful?
Send feedback 
#  View information about a Looker (Google Cloud core) custom domain
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
You can view information about the custom domain that is mapped to your instance on the **CUSTOM DOMAIN** tab of the instance details page in the Google Cloud console. You navigate to the instance details page by clicking on the instance name from the **Instances** page. The settings are as follows:
  * **Status** : An icon that summarizes the status of the domain, as described in more detail in the second **Status** column.
  * **Domain** : The domain that is associated with the instance.
  * **Record Type** : The type of DNS record that is associated with the domain.
  * **Data** : The IP address that is associated with the domain's DNS record.
  * **Status** : A description of where the domain is in the provisioning and verification process.
    * **Unverified** : A DNS record has not been created, or the record's IP address doesn't match the appropriate IP address for the type of network connection that the instance is using.
    * **Verifying** : The domain verification is in progress.
    * **Modifying** : The domain modification is in progress.
    * **Available** : The custom domain is ready to use.
    * **Unavailable** : The custom domain is provisioned to the Looker (Google Cloud core) instance but the SSL certificate is not ready.
  * **VERIFY DOMAIN** : For domains that are unverified, a **VERIFY DOMAIN** button appears. Click the button to verify the domain. An error appears in a window on the page if the domain cannot be verified.
  * **Delete** : The **Delete** trash icon lets you delete a custom domain.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


