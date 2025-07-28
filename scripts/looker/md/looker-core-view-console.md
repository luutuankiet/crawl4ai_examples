# View and edit the details of a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-view-console

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Viewing instance information
    * The Instances page
  * Edit Looker (Google Cloud core) instance settings
    * Editing settings




Was this helpful?
Send feedback 
#  View and edit the details of a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Viewing instance information
    * The Instances page
  * Edit Looker (Google Cloud core) instance settings
    * Editing settings


You can find and edit information about a project's Looker (Google Cloud core) instances in the Google Cloud console.
## Viewing instance information
Looker (Google Cloud core) instances that are associated with the selected Google Cloud project are listed on the **Instances** page in the Google Cloud console — including instances that are created by other users in your organization.
### Required role
To view information on the **Instances** page, you must have the Looker Admin (`roles/looker.admin`) or the Looker Viewer (`roles/looker.viewer`) role.
You might also be able to get this permission with custom roles or other predefined roles.
### The Instances page
The **Instances** page displays this information about each instance:
  * **Status** : 
    * A green circle with a check mark is shown if the instance was created successfully and is active.
    * A loading icon is shown if the instance creation is in progress.
  * **Name** : The name of the instance that was provided by the instance creator when the instance was created. Click the name to navigate to the **Details** tab, which shows additional information about the selected instance.
  * **Instance URL** : The URL at which an instance using public IP can be accessed. By default, instance URLs take the form `https://hostname.looker.app`, where the hostname is randomly assigned. Click the URL to navigate to the instance.
  * **Version** : The Looker version that's running on the instance.
  * **Region** : The region in which the instance is hosted.
  * **Created Date** : The date on which the instance was created.


### Instance tabs
From the **Instances** page, click an instance's name to view more information about the instance. After you click the name, an instance configuration page appears with information in the following tabs:
  * **Looker Studio Pro**


####  **Details** tab
The **Details** tab shows additional instance metadata:
  * **Platform Edition** : The instance's edition. Options are **Standard** , **Enterprise** , and **Embed**.
  * **Create Time** : The time at which the instance was created.
  * **Update Time** : The time at which the instance was most recently updated.
  * **Public IP Enabled** : Whether the instance's network connection is enabled for public IP. If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **Private IP Enabled** : Whether the instance's network connection is enabled for private IP (private services access) connection. If it's enabled, **true** is shown. If it's not enabled, **false** is shown. This setting shows **false** if the instance's network connection uses Private Service Connect.
  * **PSC Enabled** : Whether the instance's network connection is enabled for Private Service Connect. If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **PSC Configuration** : This setting appears if **PSC Enabled** is **true** , along with the following subsettings:
    * **Looker Service Attachment URI** : This setting displays the URI for the Private Service Connect service attachment for Looker (Google Cloud core).
    * **Allowed VPCs** : This setting contains a list of the VPCs that have authorized northbound access into the Private Service Connect instance.
    * **PSC Endpoints** : This setting contains a list of the southbound (egress) connections for the Private Service Connect instance, using the following subsettings:
      * **Local FQDN** : The fully qualified domain name of the service that the instance is connecting to.
      * **Target Service Attachment URI** : The service attachment URI for the service that the Looker (Google Cloud core) instance is connecting to.
      * **Connection Status** : The status of the connection, which can be one of the following:
        * **ACCEPTED** : Connection is established and functioning normally.
        * **PENDING** : Connection is not established (Looker tenant project hasn't been allowlisted).
        * **NEEDS ATTENTION** : Issue with target service attachment, such at NAT subnet is exhausted.
        * **REJECTED** : Connection is not established (Looker) tenant project is explicitly in the reject list).
        * **CLOSED** : Target service attachment doesn't exist. This status is a terminal state.
        * **UNKNOWN** : Connection status is unspecified.
  * **Egress Public IP** : The egress public IP address, which was automatically assigned when the instance was created (for instances with a public IP network connection). If no value has been assigned, **No value** is shown.
  * **Ingress Public IP** : The ingress public IP address, which was automatically assigned when the instance was created (for instances with a public IP network connection).
  * **Ingress Private IP** : The ingress private IP address for the instance (for instances with a private IP (private services access) network connection). If the instance was created with only a public IP network connection or with Private Service Connect, **No value** is shown.
  * **Associated Network** : The network selected to make a private connection (for instances with a private IP network connection). If the instance was created with only a public IP network connection, **No value** is shown.
  * **Allocated IP Range** : The range of IP addresses assigned by the instance creator or by Google when the instance was created (for instances with a private IP network connection). If the instance was created with only a public IP network connection, **No value** is shown. 
  * **Maintenance Window** : The day of the week and the hour in which Looker (Google Cloud core) schedules maintenance, if a maintenance window has been defined for your instance. Maintenance windows last for one hour. If a maintenance window has not been defined, **No value** is shown. 
  * **Scheduled Maintenance** : The scheduled date and time of upcoming maintenance for your instance. If maintenance has not been scheduled, **No value** is shown. 
  * **Deny Maintenance Period** : A time period during which Looker (Google Cloud core) does not schedule maintenance, if a deny maintenance period has been configured for your instance.
    * **Start Date** : The start date for the deny maintenance period. If a deny maintenance period has not been scheduled, **No value** is shown.
    * **End Date** : The end date for the deny maintenance period. If a deny maintenance period has not been scheduled, **No value** is shown.
    * **Time** : The time at which the deny maintenance period begins and ends on the start date and end date you specified. If a deny maintenance period has not been scheduled, **No value** is shown. 
  * **Last Deny Maintenance Period** : The start date and end date for the most recent deny maintenance period. You must allow at least 14 days of maintenance availability between any two deny maintenance periods.
    * **Start Date** : The start date for the most recent deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
    * **End Date** : The end date for the deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
    * **Time** : The time at which the previous deny maintenance period began and ended on the start date and end date for that deny maintenance period. If a deny maintenance period was not scheduled previously, **No value** is shown.
  * **Encryption** : The type of encryption for the Looker (Google Cloud core) instance. If the instance was created with the default Google-managed encryption, **Google-managed encryption key** is shown. If the instance was created with CMEK, **Customer-managed encryption key (CMEK)** is shown, along with the key identifier and a link to the key. You may need a Cloud KMS IAM role or permission on the key being used to see the status of the CMEK encryption key.
  * **Email Domain Allowlist for Scheduled Content** : The **Email Domain Allowlist for Scheduled Content** setting defines the email domains to which your Looker (Google Cloud core) users can deliver Looker content — Looks, dashboards, queries with visualizations — or alert notifications through email. By default, there are no domains in the allowlist at the time of instance creation, and Looker (Google Cloud core) users who have the appropriate Looker permissions to email content can email content to any domain. To limit content deliveries and alert notifications to email addresses from a specific domain, edit the instance configuration to restrict the domain(s) to which users can send emails. To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the Email domain allowlist for scheduled content documentation.
  * **Gemini** : Whether the Gemini in Looker is enabled for the instance. If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
  * **Gemini AI Configuration** : This setting appears if **Gemini** is enabled, along with the following subsettings:
    * **Trusted Tester features** : If it's enabled, **true** is shown. If it's not enabled, **false** is shown.
    * **Trusted Tester data use** : If it's enabled, **true** is shown. If it's not enabled, **false** is shown.


####  **Custom domain** tab
The **Custom domain** tab provides an optional means to customize the URL to access the instance with a custom domain.
####  **Looker Studio Pro** tab
In the **Looker Studio Pro** tab, you can accept the complimentary Looker Studio Pro licenses that have been allocated to your Looker (Google Cloud core) instance. If the **Accept Looker Studio Pro licenses** toggle is enabled, you have accepted the complimentary licenses.
This tab also indicates the name of the Google Cloud project that hosts your Looker Studio Pro subscription content.
## Edit Looker (Google Cloud core) instance settings
### Required role
To get the permissions that you need to edit Looker (Google Cloud core) instance settings, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project in which the instance was created. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
### Editing settings
To modify instance settings, select one of the following options:
More
On the instance **Details** tab, click **Edit** to modify these settings:
  * **OAuth Application Credentials:** Before you edit this setting, be sure to set up the new credentials and add the instance's domain to the **Authorized redirect URIs** field in the OAuth client.
  * **Connections** : Your instance configuration _must_ specify a network connection. If you have an instance that uses private IP, you can add or remove a public IP connection. Otherwise, this setting cannot be edited.
  * **Allowed VPCs** : If you have a Private Service Connect instance, you can edit the VPCs that are allowed ingress into the instance. You can update the existing settings for a VPC. You can delete a VPC by clicking the **Delete item** trash icon that appears when you hold the pointer over the network. Or, you can add a VPC by clicking **Add Item** , selecting the project in which the network was created in the **Project** field, and then selecting the network in the **Network** drop-down menu.
  * **Service Attachments** : If you have a Private Service Connect instance, you can edit the southbound service attachments. You can update the existing settings for a service attachment. You can delete a service attachment by clicking the **Delete item** trash icon that appears when you hold the pointer over it. Or, you can add a service attachment by clicking **Add Item**. When adding a service attachment, enter the fully qualified domain name of the service in the **Local FQDN** field and the service attachment URI in the **Target Service Attachment URI** field.
  * **Maintenance Window** : You can optionally specify the day of the week and the hour in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.
  * **Deny Maintenance Period** : You can optionally specify a block of days in which Looker (Google Cloud core) does not schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between deny maintenance windows.
  * **Email Domain Allowlist for Scheduled Content** : When there are no domains in the **Allowed Domains** field, email domains are not restricted. To restrict domains, enter the domain or domains to be allowed in the format `domain.suffix`, and then click **Enter** on your keyboard. If you make changes to the **Email Domain Allowlist for Scheduled Content** setting for an instance, the Looker (Google Cloud core) instance must restart, and, if there are any running persistent derived tables within the instance, they will be regenerated. To learn more about the email domain allowlist setting and how it interacts with permissions and user attributes, see the Email domain allowlist for scheduled content documentation page.
  * **Gemini in Looker** : When the **Gemini** setting is enabled, Gemini in Looker features are available for the Looker (Google Cloud core) instance. When the **Trusted Tester features** setting is enabled, users on the instance can access the Trusted Tester capabilities that are available for Gemini in Looker. When the **Trusted Tester data use** setting is enabled, Google is granted access to Gemini in Looker user data as described in the Gemini for Google Cloud Trusted Tester Program terms. To learn more about Gemini in Looker features and how to administer them for a Looker (Google Cloud core) instance, see the Administer Gemini on your Looker (Google Cloud core) documentation page.


When you have made your changes, click **Save**.
To update the settings, use the `gcloud looker instances update` command:
```

gcloud looker instances update (INSTANCE_NAME : --region=REGION)
    [--allowed-email-domains=[ALLOWED_EMAIL_DOMAINS,...]] [--async]
    [--oauth-client-id=OAUTH_CLIENT_ID]
    [--oauth-client-secret=OAUTH_CLIENT_SECRET] [--public-ip-enabled] [--no-public-ip-enabled]
    [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
      --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
      --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
    [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
      --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
    [--psc-service-attachment  domain=DOMAIN_1,attachment=SERVICE_ATTACHMENT_URI_1 \
    --psc-service-attachment domain=DOMAIN_2,attachment=SERVICE_ATTACHMENT_URI_2 \]
    [--psc-allowed-vpcs=ALLOWED_VPC_1,ALLOWED_VPC_2 ]
    [--clear-psc-allowed-vpcs]

```

Replace the following:
  * `INSTANCE_NAME`: the name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
  * ALLOWED_EMAIL_DOMAINS: when there are no domains in `--allowed-email-domains`, email domains are not restricted. To restrict domains, add the domain or domains to be allowed in the format `domain.suffix`. If you make changes to the allowed email domains for an instance, the Looker (Google Cloud core) instance must restart, and, if there are any running persistent derived tables within the instance, they will be regenerated. To learn more about the email domain allowlist and how it interacts with permissions and user attributes, see the Email domain allowlist for scheduled content documentation.
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you have set up with your OAuth client.
  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
  * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).
  * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the Manage maintenance policies for Looker (Google Cloud core) documentation page for more information about maintenance window settings.
  * DOMAIN_1 and DOMAIN_2: The domain name(s) of any published services that you want to connect to a Looker (Google Cloud core) instance by using Private Service Connect. See the Create a Looker (Google Cloud core) Private Service Connect instance documentation page for more information.
  * `SERVICE_ATTACHMENT_URI_1` and `SERVICE_ATTACHMENT_URI_2`: The full service attachment URI(s) of any published services that you want to connect to a Looker (Google Cloud core) instance using Private Service Connect. See the Create a Looker (Google Cloud core) Private Service Connect instance documentation page for more information.
  * `ALLOWED_VPC_1` and `ALLOWED_VPC_2`: The VPCs that will be allowed ingress into a Looker (Google Cloud core) instance that uses Private Service Connect. See the Create a Looker (Google Cloud core) Private Service Connect instance documentation page for more information.


You may also include the following flags:
  * `--public-ip-enabled` enables public IP.
  * `--no-public-ip-enabled` disables public IP.
  * `--clear-psc-allowed-vpcs` removes all VPCs from an instance that uses Private Service Connect.


If you have an instance that uses private IP, you can add or remove a public IP connection. You cannot add or remove a private IP connection.
Before you update OAuth credentials, be sure to set up the new credentials and add the instance's domain to the **Authorized redirect URIs** field in the OAuth client.
## What's next
  * Looker (Google Cloud core) admin settings
  * Import or export data from a Looker (Google Cloud core) instance
  * Delete or restart a Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


