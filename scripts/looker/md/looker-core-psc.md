# Create a Looker (Google Cloud core) Private Service Connect instance

**Source:** https://cloud.google.com/looker/docs/looker-core-psc

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Create a Private Service Connect instance
    * Check the status of the instance
  * Set up Private Service Connect for external services
    * Service attachment URI
  * Update a Looker (Google Cloud core) Private Service Connect instance
    * Specify southbound connections
    * Update allowed VPCs
  * Northbound access to your instance




Send feedback 
#  Create a Looker (Google Cloud core) Private Service Connect instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Create a Private Service Connect instance
    * Check the status of the instance
  * Set up Private Service Connect for external services
    * Service attachment URI
  * Update a Looker (Google Cloud core) Private Service Connect instance
    * Specify southbound connections
    * Update allowed VPCs
  * Northbound access to your instance


This page describes the process for using the gcloud CLI or Google Cloud console to create a Looker (Google Cloud core) production or non-production instance with Private Service Connect enabled.
Private Service Connect can be enabled for a Looker (Google Cloud core) instance that meets the following criteria:
  * The Looker (Google Cloud core) instance must be new. Private Service Connect can be enabled only at the time of instance creation.
  * The instance edition must be Enterprise (`core-enterprise-annual`) or Embed (`core-embed-annual`).


## Before you begin
  1. Work with Sales to ensure that your annual contract is completed and that you have quota allocated in your project.
  2. Make sure that billing is enabled for your Google Cloud project.
  3. In the Google Cloud console, on the project selector page, select the project where you want to create the Private Service Connect instance. 
Go to project selector
  4. Enable the Looker API for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 
Enable the API
  5. Set up an OAuth client and create authorization credentials. The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different authentication method to authenticate users into your instance.
  6. If you want to use VPC Service Controls or customer-managed encryption keys (CMEK) with the Looker (Google Cloud core) instance that you are creating, additional setup is required prior to instance creation. Additional edition and network configuration may also be required during instance creation.


### Required roles
To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
You may also need additional IAM roles to set up VPC Service Controls or customer-managed encryption keys (CMEK). Visit the documentation pages for those features to learn more.
## Create a Private Service Connect instance
More
  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, the **Instances** page will open. 
Go to Looker (Google Cloud core)
  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **OAuth Application Credentials** section, enter the OAuth client ID and OAuth secret that you created when you set up your OAuth client.
  5. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the quota for your project is allocated. Available regions are listed on the Looker (Google Cloud core) locations documentation page.
You cannot change the region once the instance has been created.
  6. In the **Edition** section, choose an **Enterprise** or **Embed** (production or non-production) edition option. The edition type affects some of the features that are available for the instance. Make sure that you choose the same edition type as listed in your annual contract and that you have quota allocated for that edition type.
     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale
     * Non-production editions: If you want a staging and testing environment, select one of the non-production editions. For more information, see the Non-production instances documentation.
Editions cannot be changed after instance creation. If you want to change an edition, you can use import and export to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  7. In the **Customize your instance** section, click **SHOW CONFIGURATION OPTIONS** to display a group of additional settings that you can customize for the instance.
  8. In the **Connections** section, under **Instance IP assignment** , choose either **Private IP** only or both **Private IP** and **Public IP**. The type of network connection that you select impacts the Looker features that are available to the instance. The following network connection options are available:
     * **Public IP** : Assigns an external, internet-accessible IP address.
     * **Private IP** : Assigns an internal, customer-defined IP address that is accessible in a Virtual Private Cloud (VPC) for ingress. To communicate to VPC and on-premises or multi-cloud workloads, you must deploy service attachments for egress traffic. If you want to use VPC Service Controls, you must select **Private IP** only.
     * **Private IP** and **Public IP** : Incoming traffic uses the public IP, and responses are also public. Traffic that is initiated by Looker (Google Cloud core) uses the private IP for outbound routing. The Looker (Google Cloud core) instance won't use the public IP for initiating internet-bound outbound traffic.
  9. Under **Private IP Type** , select **Private Service Connect (PSC)**.
  10. If you are creating an instance that uses only private IP, set at least one allowed VPC that will be granted northbound access into the instance. Under **Allowed VPCs** , click **Add Item** to add each VPC. In the **Project** field, select the project in which the network was created. In the **Network** drop-down menu, select the network.
If you select both **Private IP** and **Public IP** in the **Connections** section, the **Allowed VPCs** section doesn't appear. You can set up access to the instance through the instance's web URL.
  11. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:
     * **Google-managed encryption key**: This option is the default and doesn't require any additional configuration.
     * **Customer-managed encryption key (CMEK)**: See the Using customer-managed encryption keys with Looker (Google Cloud core) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **EnableFIPS 140-2 Validated Encryption**: See the Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance documentation page for more information on FIPS 140-2 support on Looker (Google Cloud core).
  12. In the **Maintenance Window** section, you can optionally specify the day of the week and the hour in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.
  13. In the **Deny Maintenance Period** section, you can optionally specify a block of days on which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.
  14. In the **Gemini in Looker** section, you can optionally make Gemini in Looker features available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the Gemini in Looker preview form on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms. To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.
  15. Click **Create**.


To create a Private Service Connect instance, run the `gcloud looker instances create` command with all the following flags:
```

gcloud looker instances create INSTANCE_NAME \
--psc-enabled \
--oauth-client-id=OAUTH_CLIENT_ID \
--oauth-client-secret=OAUTH_CLIENT_SECRET \
--region=REGION \
--edition=EDITION \
[--psc-allowed-vpcs=ALLOWED_VPC,ADDITIONAL_ALLOWED_VPCS]
[--no-public-ip-enabled]
[--public-ip-enabled]
--async


```

Replace the following:
  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it is not associated with the instance URL.
  * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you set up your OAuth client. After the instance has been created, enter the instance's URL in the **Authorized redirect URIs** section of the OAuth client.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the Looker (Google Cloud core) locations documentation page.
  * `EDITION`: the edition and environment type (production or non-production) for the instance. Its possible values are `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-enterprise-annual`, or `nonprod-core-embed-annual`. Editions cannot be changed after instance creation. If you want to change an edition, you can use import and export to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  * `ALLOWED_VPC`: If you are creating an instance that uses only private IP, list a VPC that will be allowed northbound (ingress) access into Looker (Google Cloud core). To access the instance from outside the VPC that the instance is located in, you must list at least one VPC. Specify a VPC using one of the following formats:
    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
If you are creating an instance that uses both private IP and public IP, you don't need to set an allowed VPC.
  * `ADDITIONAL_ALLOWED_VPCS`: any additional VPCs to be allowed northbound access into Looker (Google Cloud core) can be added to the `--psc-allowed-vpcs` flag in a comma-separated list.


You must also include **one** of the following flags to enable or disable public IP:
  * `--public-ip-enabled` enables public IP. If you enable public IP for the instance, incoming traffic will be routed through public IP, and outgoing traffic will be routed through Private Service Connect.
  * `--no-public-ip-enabled` disables public IP.


If you want, you can add more parameters to apply other instance settings: 
```
  [--maintenance-window-day=MAINTENANCE_WINDOW_DAY
          --maintenance-window-time=MAINTENANCE_WINDOW_TIME]
  [--deny-maintenance-period-end-date=DENY_MAINTENANCE_PERIOD_END_DATE
          --deny-maintenance-period-start-date=DENY_MAINTENANCE_PERIOD_START_DATE
          --deny-maintenance-period-time=DENY_MAINTENANCE_PERIOD_TIME]
  --kms-key=KMS_KEY_ID
  [--fips-enabled]
  
```
Replace the following:
  * `MAINTENANCE_WINDOW_DAY`: must be one of the following: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. See the Manage maintenance policies for Looker (Google Cloud core) documentation page for more information about maintenance window settings.
  * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC in 24-hour format (for example, 13:00, 17:45).
  * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
  * `KMS_KEY_ID`: must be the key that is created when setting up customer-managed encryption keys (CMEK).


You may include the `--fips-enabled` flag to enable FIPS 140-2 level 1 compliance.
The process for creating a Private Service Connect instance differs from the process for creating a Looker (Google Cloud core) (private services access) instance in the following ways:
  * With Private Service Connect setup, the `--consumer-network` and `--reserved-range` flags are not necessary.
  * Private Service Connect instances require an additional flag: `--psc-enabled`.
  * The `--psc-allowed-vpcs` flag is a comma-separated list of VPCs. You can specify as many VPCs as you like in the list.


### Check the status of the instance
It takes approximately 40-60 minutes for the instance to be created.
More
As the instance is being created, you can view its status on the **Instances** page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu. On the **Details** page for the instance, its status will show **Active** once it's created.
To check the status, use the `gcloud looker instances describe` command:
```
gcloud looker instances describe INSTANCE_NAME --region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


The instance is ready once it reaches the `ACTIVE` state.
## Set up Private Service Connect for external services
For your Looker (Google Cloud core) instance to be able to connect to an external service, that external service must be published using Private Service Connect. Follow the instructions for publishing services by using Private Service Connect for any service that you want to publish.
Services can be published with automatic approval or with explicit approval. If you choose to publish with explicit approval, you must configure the service attachment as follows:
  * Set your service attachment allowlist to use projects (not networks).
  * Add the Looker tenant project ID to the allowlist.


You can find your Looker tenant project ID after your instance has been created by running the following command:
```
gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


In the command output, the `looker_service_attachment_uri` field will contain your Looker tenant project ID. It will have the following format: `projects/{Looker tenant project ID}/regions/…`
### Service attachment URI
When you later update your Looker (Google Cloud core) instance to connect to your service, you'll need the full service attachment URI for the external service. The URI will be specified as follows, using the project, region, and name that you used to create the service attachment:
```
projects/{project}/regions/{region}/serviceAttachments/{name}

```

## Update a Looker (Google Cloud core) Private Service Connect instance
Once your Looker (Google Cloud core) Private Service Connect instance has been created, you can make the following changes:
  * Specify southbound (egress) connections
  * Update allowed VPCs


In addition, you can make other changes after instance creation by editing the instance settings.
### Specify southbound connections
More
  1. On the **Instances** page, click the name of the instance for which you want to enable southbound (egress) connections.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. To edit an existing service attachment, update the fully qualified domain name of the service in the **Local FQDN** field and the service attachment URI in the **Target Service Attachment URI** field.
  5. To add a new service attachment, click **Add Item**. Then, enter the fully qualified domain name of the service in the **Local FQDN** field and the service attachment URI in the **Target Service Attachment URI** field.
  6. Click **Save**.


Use `--psc-service-attachment` flags to enable southbound (egress) connections to external services for which you have already set up Private Service Connect:
```
gcloud looker instances update INSTANCE_NAME \
--psc-service-attachment  domain=DOMAIN_1,attachment=SERVICE_ATTACHMENT_URI_1 \
--psc-service-attachment domain=DOMAIN_2,attachment=SERVICE_ATTACHMENT_URI_2 \
--region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `DOMAIN_1` and `DOMAIN_2`: If you are connecting to a public service, use the service's domain name. If you are connecting to a private service, use your choice of a fully qualified domain name. The following restrictions apply to the domain name:
  * Each southbound connection supports a single domain.
  * The domain name must consist of at least three parts. For example, `mydomain.github.com` is acceptable, but `github.com` is not acceptable.
  * The last part of the name cannot be any the following:
    * `googleapis.com`
    * `google.com`
    * `gcr.io`
    * `pkg.dev`
When you set up a connection to your service from within your Looker (Google Cloud core) instance, use this domain as the alias for your service.
  * `SERVICE_ATTACHMENT_1` and `SERVICE_ATTACHMENT_2`: the full service attachment URI for the published service you are connecting to. Each service attachment URI can be accessed by a single domain.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


If you are connecting to a non-Google managed service in a region other than the region where your Looker (Google Cloud core) instance is located, enable global access on the producer load balancer.
#### Include all connections that should be enabled
Each time you run an update command with `--psc-service-attachment` flags, you must include every connection that you want to be enabled, including connections that were already enabled previously. For example, suppose you have previously connected an instance called `my-instance` to the `www.cloud.com` domain as follows:
```
gcloud looker instances update my-instance --psc-service-attachment \
domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud

```

Running the following command to add a new `www.me.com` connection would delete the `www.cloud.com` connection:
```
gcloud looker instances update my-instance --psc-service-attachment \
domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa

```

To prevent deletion of the `www.cloud.com`connection when you add the new `www.me.com` connection, include a separate `psc-service-attachment` flag for both the existing connection and the new connection within the update command as follows:
```
gcloud looker instances update my-instance --psc-service-attachment \
domain=www.cloud.com,attachment=projects/123/regions/us-central1/serviceAttachment/cloud \
--psc-service-attachment domain=www.me.com,attachment=projects/123/regions/us-central1/serviceAttachment/my-sa

```

#### Check southbound connection status
You can check the status of your southbound (egress) connections through Google Cloud CLI or in the console.
More
View the connection status on the **Details** tab of the instance configuration page in the console. The **Connection Status** field shows the status for each target service attachment.
Run the `gcloud looker instances describe --format=json` command to check southbound connection status. Each service attachment should be populated with a `connection_status` field.
#### Delete all southbound connections
To delete all southbound (egress) connections, run the following command:
```
gcloud looker instances update MY_INSTANCE --clear-psc-service-attachments \
--region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


### Update allowed VPCs
If you chose to use only private IP in the Looker (Google Cloud core) instance, you must allow at least one VPC access to the instance. Complete the following steps to update the VPCs that have access to the instance.
More
  1. On the **Instances** page, click the name of the instance for which you want to update the VPCs that are allowed northbound access into the instance.
  2. Click **Edit**.
  3. Expand the **Connections** section.
  4. To add a new VPC, click **Add Item**. Then, select the project in which the VPC in the **Project** field, and select the network from the **Network** drop-down menu.
  5. To delete a VPC, click the **Delete item** trash icon that appears when you hold the pointer over the network.
  6. Click **Save**.


Use the `--psc-allowed-vpcs` flag to update the list of VPCs that have authorized northbound access into the instance.
When you update the allowed VPCs, you must specify the entire list that you want to be in effect after your update. For example, suppose VPC `ALLOWED_VPC_1` is already allowed, and you want to add VPC `ALLOWED_VPC_2`. To add VPC `ALLOWED_VPC_1` while making sure that VPC `ALLOWED_VPC_2` continues to be allowed, add the `--psc-allowed-vpcs` flag as follows:
```
gcloud looker instances update INSTANCE_NAME \
--psc-allowed-vpcs=ALLOWED_VPC_1,ALLOWED_VPC_2 --region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `ALLOWED_VPC_1` and `ALLOWED_VPC_2`: the VPCs that will be allowed ingress into Looker (Google Cloud core). Specify each allowed VPC using one of the following formats: 
    * `projects/{project}/global/networks/{network}`
    * `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


#### Delete all allowed VPCs
To delete all allowed VPCs, run the following command:
```
gcloud looker instances update MY_INSTANCE --clear-psc-allowed-vpcs \
--region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
  * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.


## Northbound access to your instance
After the Looker (Google Cloud core) (Private Service Connect) instance is created, you can set up northbound access to allow your users to access the instance.
If you chose both public IP and private IP when setting up the instance, you can set up northbound access through the web URL for the instance. That URL can be found on the **Instances** page of the Google Cloud console, or the **Custom domain** tab of the instance details page, if you set up a custom domain.
If you selected private IP only when setting up the instance, you can set up northbound access to the instance from another VPC network by following the instructions for creating a Private Service Connect endpoint. Follow these guidelines when creating the endpoint:
  * Make sure that the network is allowed northbound access to your Looker (Google Cloud core) instance by adding it to the allowed VPC's list.
  * Set the **Target service** field (for the Google Cloud console) or the `SERVICE_ATTACHMENT` variable (if following Google Cloud CLI or API instructions) to the Looker service attachment URI, which you can find by checking the **Details** tab on the instance configuration page of the console or by running the following command:
```
gcloud looker instances describe INSTANCE_NAME --region=REGION--format=json
```

Replace the following:
    * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
    * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted.
  * You can use any subnet that is hosted in the same region as the Looker (Google Cloud core) instance.
  * Don't enable global access.


To access your instance from a hybrid networking environment, you can follow the instructions on the Northbound access to a Looker (Google Cloud core) instance using Private Service Connect documentation page to set up a custom domain and access the instance.
## What's next
  * Northbound access to a Looker (Google Cloud core) instance using Private Service Connect


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


