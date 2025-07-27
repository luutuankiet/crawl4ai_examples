# Configure Lightdash to use external storage - Lightdash

**Source:** https://docs.lightdash.com/self-host/customize-deployment/configure-lightdash-to-use-external-object-storage

Lightdash home page
Search...
Ctrl KAsk AI
Search...
Navigation
Customize deployment
Configure Lightdash to use external storage
##### Introduction
  * Welcome to Lightdash
  * Setting up a new project


##### Explore and analyze
  * Quickstart
  * Guides
  * Reference


##### Build your semantic layer
  * Developer quickstart
  * CLI quickstart
  * Guides
  * Reference


##### Workspace and user management
  * Guides
  * Reference


##### Integrations


##### Embedding and SDKs
  * Embedding quickstart
  * Embedding reference


##### Self-hosting and deployment
  * Self-Host Lightdash
  * Lightdash Cloud vs. Self-Hosted
  * Updating Lightdash
  * Customize deployment
    * Standalone scheduler worker
    * Environment variables
    * Resource recommendations
    * Secure Lightdash with HTTPS


##### Contact


On this page
  * Configure cloud storage on Google Cloud Platform
  * Configure cloud storage on AWS
  * Configure cloud storage using MinIO
  * Azure Storage
  * Configure Lightdash to use S3 credentials
  * Using IAM roles


On Lightdash, we generate some files like:
  * Images for Slack unfurl and scheduled deliveries
  * Results on JSONL/CSV/Excel format

These files need to be stored in a S3 Compatible Cloud storage. Some options are GCP Buckets, S3 Storage and MinIO.
##  Configure cloud storage on Google Cloud Platform
Go into GCP: Cloud storage Create a new bucket with the following details:
  * give it an unique `Bucket name` like - `lightdash-cloud-file-storage-eu`
  * Select region (like multi US or multi EU or single region EU-west-1)
  * select storage class: default standard
  * disable `enforce public access` and select `fine-grained`
  * Protection: `none`

Go to settings > Interoperability and create a `Access key for service account`
  * Copy the `access key` and `secret`

`S3_ENDPOINT` for google is `https://storage.googleapis.com` `S3_REGION` for google is `auto`
##  Configure cloud storage on AWS
  * Navigate to the S3 section of the AWS Management Console and click on the Create Bucket button.
  * Give your bucket a name and select the region where you want to store your data.
  * Next, you need to set the permissions for your bucket. Make it private.

To export your S3 credentials, you need to follow these steps:
  * Navigate to the IAM section and click on the Users tab.
  * Click on the user whose credentials you want to export.
  * Click on the Security Credentials tab and locate the Access Keys section.
  * Click on the Create Access Key button.
  * Download the CSV file that contains your Access Key ID and Secret Access Key.

Check this guide to see what’s the right `S3_ENDPOINT` for your bucket
##  Configure cloud storage using MinIO
Creating a bucket in MinIO
  * Login to the MinIO console and click on “Buckets” in the side bar
  * Click on “Create Bucket”
  * Give your bucket a name and click “Create Bucket”

Creating access credentials in MinIO
  * Click on “Access Keys” in the side bar
  * Click “Create access key”
  * Give a name to your new access key and click “Create”
  * Download the JSON file containing both your Access Key ID and Secret Access Key

MinIO needs path style bucket URLs, for this you will need to set `S3_FORCE_PATH_STYLE: true` in your environment variables.
##  Azure Storage
Azure Blob Storage is not natively compatible with the S3 API. While Lightdash supports external object storage by allowing integration with S3-compatible APIs, Azure’s storage service does not provide this compatibility out of the box. This means that you **cannot use Azure Blob Storage as a drop-in replacement for S3** in Lightdash deployments. Instead, you can use one of the following S3-compatible solutions within your Azure setup:
  * **MinIO****:** S3-compatible object storage
  * **s3proxy****:** A lightweight proxy that adds an S3-compatible API layer on top of Azure Blob Storage.


##  Configure Lightdash to use S3 credentials
To enable Lightdash to use your S3 bucket for cloud storage, you’ll need to set the following environment variables:
Copy
Ask AI
```
S3_ENDPOINT        # required
S3_REGION          # required
S3_BUCKET          # required
S3_ACCESS_KEY      # optional if using IAM role
S3_SECRET_KEY      # optional if using IAM role
S3_EXPIRATION_TIME # optional, defaults to 259200 seconds (3 days)

```

For a comprehensive list of all possible S3-related environment variables and other configurations, please visit the Environment Variables documentation.
###  Using IAM roles
Lightdash also supports authentication via IAM roles. If you omit the `S3_ACCESS_KEY` and `S3_SECRET_KEY` variables, the S3 library will automatically attempt to use IAM roles. For more details on how this works, refer to the AWS SDK for JavaScript documentation on setting credentials in Node.js. If you are using an IAM role to generate signed URLs, be aware that these URLs have a maximum validity of 7 days due to AWS limitations, independently of the `S3_EXPIRATION_TIME` configuration.
Use External DatabaseLogging
Assistant
Responses are generated using AI and may contain mistakes.


