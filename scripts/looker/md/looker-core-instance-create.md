# Create a public IP Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-instance-create

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Create a Looker (Google Cloud core) instance




Was this helpful?
Send feedback 
#  Create a public IP Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Create a Looker (Google Cloud core) instance


This page discusses how to provision a public IP Looker (Google Cloud core) production or non-production instance.
## Before you begin
  1. Work with Sales to ensure that your annual contract is completed and that you have quota allocated in your project.
  2. Make sure that billing is enabled for your Google Cloud project.
  3. In the Google Cloud console, on the project selector page, create a Google Cloud project or navigate to an existing one. 
Go to project selector
  4. Enable the Looker API for your project in the Google Cloud console. When enabling the API, you may need to refresh the console page to confirm that the API has been enabled. 
Enable the API
  5. Set up an OAuth client and create authorization credentials. The OAuth client lets you authenticate and access the instance. You must set up OAuth to create a Looker (Google Cloud core) instance, even if you are using a different authentication method to authenticate users into your instance.
  6. If you want to use VPC Service Controls, you must create a private IP instance instead of a public IP instance.


### Required roles
To get the permissions that you need to create a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project the instance will reside in. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
You may also need additional IAM roles if you want to set up customer-managed encryption keys (CMEK). Visit the Access control with IAM page of the Cloud Key Management Service documentation to learn more.
## Create a Looker (Google Cloud core) instance
> Looker (Google Cloud core) requires approximately 60 minutes to generate a new instance.
To create your Looker (Google Cloud core) instance, select one of the following options:
More
  1. Navigate to the Looker (Google Cloud core) product page from your project in the Google Cloud console. If you have already created a Looker (Google Cloud core) instance within this project, this will open the **Instances** page. 
Go to Looker (Google Cloud core)
  2. Click **CREATE INSTANCE**.
  3. In the **Instance name** section, provide a name for your Looker (Google Cloud core) instance. The instance name isn't associated with the URL of the Looker (Google Cloud core) instance once it is created. The instance name cannot be changed after instance creation.
  4. In the **OAuth Application Credentials** section, enter the OAuth client ID and OAuth secret that you created when you set up your OAuth client.
  5. In the **Region** section, select the appropriate option from the drop-down menu to host your Looker (Google Cloud core) instance. Select the region that matches the region in the subscription contract, which is where the quota for your project is allocated. Available regions are listed on the Looker (Google Cloud core) locations documentation page. You cannot change the region once the instance has been created.
  6. In the **Edition** section, set the instance edition according to your organization's needs. The edition type affects some of the features that are available for the instance. Make sure that you choose the same edition type as listed in your annual contract and that you have quota allocated for that edition type. These are the edition options:
     * **Standard** : Looker (Google Cloud core) platform for small organizations or teams with fewer than 50 users
     * **Enterprise** : Looker (Google Cloud core) platform with enhanced security features for addressing a wide variety of internal BI and analytics use cases
     * **Embed** : Looker (Google Cloud core) platform for deploying and maintaining reliable external analytics and custom applications at scale
     * Non-production editions: If you want a staging and testing environment, select one of the non-production editions. For more information, see the Non-production instances documentation.
Editions cannot be changed after instance creation. If you want to change an edition, you can use import and export to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
  7. In the **Customize your instance** section, click **SHOW CONFIGURATION OPTIONS** to display a group of additional settings that you can customize for the instance.
  8. In the **Connections** section, select only **Public IP**. A public IP connection setting assigns an external, internet-accessible IP address and is available for all edition types.
  9. If you are creating an **Enterprise** or **Embed** edition instance, you will see the **Encryption** section. In the **Encryption** section, you can select the type of encryption to use on your instance. The following encryption options are available:
     * **Google-managed encryption key**: This option is the default and doesn't require any additional configuration.
     * **Customer-managed encryption key (CMEK)**: See the Using customer-managed encryption keys with Looker (Google Cloud core) documentation page for more information on CMEK and how to configure it during instance creation. The type of encryption cannot be changed after instance creation.
     * **EnableFIPS 140-2 Validated Encryption**: See the Enable FIPS 140-2 level 1 compliance on a Looker (Google Cloud core) instance documentation page for more information on FIPS 140-2 support on Looker (Google Cloud core). 
  10. In the **Maintenance Window** section, you can optionally specify the day of the week and the hour in which Looker (Google Cloud core) schedules maintenance. Maintenance windows last for one hour. By default, the **Preferred Window** option in the **Maintenance Window** is set to **Any window**.
  11. In the **Deny Maintenance Period** section, you can optionally specify a block of days in which Looker (Google Cloud core) doesn't schedule maintenance. Deny maintenance periods can be up to 60 days long. You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.
  12. In the **Gemini in Looker** section, you can optionally make Gemini in Looker features available for the Looker (Google Cloud core) instance. To enable Gemini in Looker, select **Gemini** , and then select **Trusted Tester features**. When **Trusted Tester features** is enabled, users can access the Trusted Tester capabilities of Gemini in Looker. You may request access to the non-public Trusted Tester capabilities through the Gemini in Looker preview form on a per-user basis. You must enable this setting to use Gemini during the pre-GA preview. Optionally, select **Trusted Tester data use**. When this setting is enabled, you consent to your data being used by Google as described in the Gemini for Google Cloud Trusted Tester Program terms. To disable Gemini for a Looker (Google Cloud core) instance, clear the **Gemini** setting.
  13. Click **Create**.


  1. If you are using CMEK, then create the Looker service account and follow the instructions for setting up CMEK first.
  2. Use the `gcloud looker instances create` command to create the instance:
```
gcloud looker instances create INSTANCE_NAME \
--project=PROJECT_ID \
--oauth-client-id=OAUTH_CLIENT_ID \
--oauth-client-secret=OAUTH_CLIENT_SECRET \
--region=REGION \
--edition=EDITION \
[--consumer-network=CONSUMER_NETWORK --private-ip-enabled --reserved-range=RESERVED_RANGE]
[--no-public-ip-enabled]
[--public-ip-enabled]
[--async]

```

Replace the following:
     * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL.
     * `PROJECT_ID`: the name of the Google Cloud project in which you are creating the Looker (Google Cloud core) instance.
     * `OAUTH_CLIENT_ID` and `OAUTH_CLIENT_SECRET`: the OAuth client ID and OAuth secret that you created when you set up your OAuth client. After the instance has been created, set up the authorized redirect URI in the OAuth client that you previously created.
     * `REGION`: the region in which your Looker (Google Cloud core) instance is hosted. Select the region that matches the region in the subscription contract. Available regions are listed on the Looker (Google Cloud core) locations documentation page. You cannot change the region once the instance has been created.
     * `EDITION`: the edition and environment type (production or non-production) for the instance. Its possible values are `core-standard-annual`, `core-enterprise-annual`, `core-embed-annual`, `nonprod-core-standard-annual`, `nonprod-core-enterprise-annual`, or `nonprod-core-embed-annual`. Editions cannot be changed after instance creation. If you want to change an edition, you can use import and export to move your Looker (Google Cloud core) instance data into a new instance that is configured with a different edition.
     * `CONSUMER_NETWORK`: your VPC network or Shared VPC. Must be set if you're creating a private IP instance.
     * `RESERVED_RANGE`: the range of IP addresses within the VPC in which Google will provision a subnetwork for your Looker (Google Cloud core) instance. Don't define a range if you're enabling a private IP network connection for your instance.
Also include these flags:
     * `--public-ip-enabled` is used to enable public IP.
     * `--async` is recommended when you're creating a Looker (Google Cloud core) instance.
  3. You can add more parameters to apply other instance settings: 
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
     * `MAINTENANCE_WINDOW_TIME` and `DENY_MAINTENANCE_PERIOD_TIME`: must be in UTC time in 24-hour format (for example, 13:00, 17:45).
     * `DENY_MAINTENANCE_PERIOD_START_DATE` and `DENY_MAINTENANCE_PERIOD_END_DATE`: must be in the format `YYYY-MM-DD`.
     * `KMS_KEY_ID`: must be the key that is created when setting up customer-managed encryption keys (CMEK).
You may include the `--fips-enabled` flag to enable FIPS 140-2 level 1 compliance.


Use the following Terraform resource to provision a **Standard** Looker (Google Cloud core) instance with basic functionality:
```
# Creates a Standard edition Looker (Google Cloud core) instance with basic functionality enabled.
resource "google_looker_instance" "main" {
  name             = "my-instance"
  platform_edition = "LOOKER_CORE_STANDARD"
  region           = "us-central1"
  oauth_config {
    client_id     = "my-client-id"
    client_secret = "my-client-secret"
  }
}
```

Use the following Terraform resource to provision a **Standard** Looker (Google Cloud core) instance with additional settings applied:
```
# Creates a Standard edition Looker (Google Cloud core) instance with full functionality enabled.

resource "google_looker_instance" "main" {
  name              = "my-instance"
  platform_edition  = "LOOKER_CORE_STANDARD"
  region            = "us-central1"
  public_ip_enabled = true
  admin_settings {
    allowed_email_domains = ["google.com"]
  }
  // User metadata config is only available when platform edition is LOOKER_CORE_STANDARD.
  user_metadata {
    additional_developer_user_count = 10
    additional_standard_user_count  = 10
    additional_viewer_user_count    = 10
  }
  maintenance_window {
    day_of_week = "THURSDAY"
    start_time {
      hours   = 22
      minutes = 0
      seconds = 0
      nanos   = 0
    }
  }
  deny_maintenance_period {
    start_date {
      year  = 2050
      month = 1
      day   = 1
    }
    end_date {
      year  = 2050
      month = 2
      day   = 1
    }
    time {
      hours   = 10
      minutes = 0
      seconds = 0
      nanos   = 0
    }
  }
  oauth_config {
    client_id     = "my-client-id"
    client_secret = "my-client-secret"
  }
}

```

Use the following Terraform resource to provision an **Enterprise** Looker (Google Cloud core) instance with a private network connection:
```
# Creates an Enterprise edition Looker (Google Cloud core) instance with full, Private IP functionality.
resource "google_looker_instance" "main" {
  name               = "my-instance"
  platform_edition   = "LOOKER_CORE_ENTERPRISE_ANNUAL"
  region             = "us-central1"
  private_ip_enabled = true
  public_ip_enabled  = false
  reserved_range     = google_compute_global_address.main.name
  consumer_network   = data.google_compute_network.main.id
  admin_settings {
    allowed_email_domains = ["google.com"]
  }
  encryption_config {
    kms_key_name = google_kms_crypto_key.main.id
  }
  maintenance_window {
    day_of_week = "THURSDAY"
    start_time {
      hours   = 22
      minutes = 0
      seconds = 0
      nanos   = 0
    }
  }
  deny_maintenance_period {
    start_date {
      year  = 2050
      month = 1
      day   = 1
    }
    end_date {
      year  = 2050
      month = 2
      day   = 1
    }
    time {
      hours   = 10
      minutes = 0
      seconds = 0
      nanos   = 0
    }
  }
  oauth_config {
    client_id     = "my-client-id"
    client_secret = "my-client-secret"
  }
  depends_on = [
    google_service_networking_connection.main,
    google_kms_crypto_key.main
  ]
}

resource "google_kms_key_ring" "main" {
  name     = "keyring-example"
  location = "us-central1"
}

resource "google_kms_crypto_key" "main" {
  name     = "crypto-key-example"
  key_ring = google_kms_key_ring.main.id
}

resource "google_service_networking_connection" "main" {
  network                 = data.google_compute_network.main.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.main.name]
}

resource "google_compute_global_address" "main" {
  name          = "looker-range"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 20
  network       = data.google_compute_network.main.id
}

data "google_project" "main" {}

data "google_compute_network" "main" {
  name = "default"
}

resource "google_kms_crypto_key_iam_member" "main" {
  crypto_key_id = google_kms_crypto_key.main.id
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  member        = "serviceAccount:service-${data.google_project.main.number}@gcp-sa-looker.iam.gserviceaccount.com"
}
```

To learn how to apply or remove a Terraform configuration, see Basic Terraform commands.
Instance creation cannot be paused or terminated once it has been initiated. When your Terraform resource has been provisioned successfully, your terminal will print the following message:
```
Creation complete after ms [id=projects/PROJECT-ID/locations/REGION/instances/my-instance-randomly-generated-name]
 added,  changed,  destroyed.

```

To view the status of your new instance, which will be assigned a randomly generated name, visit the **Instances** page within the console.
As the instance is being created, you can view its status on the **Instances** page within the console. You can also see your instance creation activity by clicking on the notifications icon in the Google Cloud console menu.
Once the public IP instance is created, the instance's public URL will appear in the **Instance URL** column of the **Instances** page.
After the instance has been created, set up the authorized redirect URI in the OAuth client that you previously created.
After the instance is created and you have completed OAuth setup, you can view the instance by navigating to the instance URL, which will be shown on the **Instances** page.
## What's next
  * Set up and access a custom domain for a public IP Looker (Google Cloud core) instance
  * Connect Looker (Google Cloud core) to your database
  * Prepare a Looker (Google Cloud core) instance for users
  * Manage users within Looker (Google Cloud core)


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


