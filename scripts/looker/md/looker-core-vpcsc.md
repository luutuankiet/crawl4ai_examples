# VPC Service Controls support for Looker (Google Cloud core)

**Source:** https://cloud.google.com/looker/docs/looker-core-vpcsc

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Removing the default route
  * Connecting to resources or services outside the VPC Service Controls perimeter
  * Adding CMEK keys to a perimeter




Was this helpful?
Send feedback 
#  VPC Service Controls support for Looker (Google Cloud core)
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Removing the default route
  * Connecting to resources or services outside the VPC Service Controls perimeter
  * Adding CMEK keys to a perimeter


VPC Service Controls can improve your ability to mitigate the risk of data exfiltration from Google Cloud services. You can use VPC Service Controls to create service perimeters that help protect the resources and data of services that you explicitly specify.
To add the Looker (Google Cloud core) service to a VPC Service Controls service perimeter, follow the instructions about how to create a service perimeter on the Create a service perimeter documentation page, and select **Looker (Google Cloud core) API** in the **Specify services to restrict** dialog. To learn more about using VPC Service Controls, visit the Overview of VPC Service Controls documentation page.
VPC Service Controls supports Looker (Google Cloud core) instances that meet two criteria:
  * Instance editions must be **Enterprise** or **Embed**
  * Instance network configurations must use private IP only


## Required roles
To understand the required IAM roles for setting up VPC Service Controls, visit the Access control with IAM page of the VPC Service Controls documentation.
## Removing the default route
When a Looker (Google Cloud core) instance is created inside a Google Cloud project that is within a VPC Service Controls perimeter, or is inside a project that gets added to a VPC Service Controls perimeter, you must remove the default route to the internet.
To remove the default route to the internet, select one of the following options:
More
```
gcloud services vpc-peerings enable-vpc-service-controls --network=NETWORK --service=servicenetworking.googleapis.com

```

Replace `NETWORK` with your Looker (Google Cloud core) instance's VPC network.
For more information, visit the gcloud services vpc-peerings enable-vpc-service-controls documentation page.
HTTP method and URL:
```
PATCH https://servicenetworking.googleapis.com/v1/{parent=services/*}:enableVpcServiceControls

```

Request JSON body:
```
{
"consumerNetwork": NETWORK
}

```

Replace `NETWORK` with your Looker (Google Cloud core) instance's VPC network.
For more information, visit the Method: services.enableVpcServiceControls documentation page.
## Connecting to resources or services outside the VPC Service Controls perimeter
To connect to another Google Cloud resource or service, you may need to set up ingress and egress rules if the project that the resource is in is located outside the VPC Service Controls perimeter.
For information about accessing other external resources, follow the instructions for the type of resource that you want to connect to on either the Access external services using private services access or the Looker (Google Cloud core) southbound access to external services using Private Service Connect documentation page (depending on whether your instance uses private services access or Private Service Connect).
## Adding CMEK keys to a perimeter
Sometimes, a Looker (Google Cloud core) instance that is enabled with customer-managed encryption keys (CMEK) has the Cloud KMS key hosted in a different Google Cloud project. For this scenario, when you enable VPC Service Controls, you must add the KMS key hosting project to the security perimeter.
## What's next?
  * Connect Looker (Google Cloud core) to your database
  * Set up the Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


