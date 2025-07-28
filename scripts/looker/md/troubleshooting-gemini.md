# Troubleshooting Gemini in Looker issues  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/troubleshooting-gemini

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Troubleshooting resources
    * Gemini in Looker resources and troubleshooting
    * Gemini in Looker enablement troubleshooting
  * How to submit in-product feedback
  * How to get support
  * Related resources




Was this helpful?
Send feedback 
#  Troubleshooting Gemini in Looker issues
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Troubleshooting resources
    * Gemini in Looker resources and troubleshooting
    * Gemini in Looker enablement troubleshooting
  * How to submit in-product feedback
  * How to get support
  * Related resources


Gemini in Looker is a product in the Gemini for Google Cloud portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data. Gemini in Looker can provide assistance for tasks in Looker (original) instances, in Looker (Google Cloud core) instances, and in Looker Studio.
Learn how and when Gemini for Google Cloud uses your data.
This page describes the following topics:
  * Known limitations, troubleshooting, and tips for writing better prompts for each task that is supported by Gemini in Looker
  * Troubleshooting that is related to Gemini in Looker enablement
  * How to submit in-product feedback about Gemini in Looker tasks
  * How to get support
  * Related resources


## Troubleshooting resources
### Gemini in Looker resources and troubleshooting
Task performed with Gemini assistance | Available platforms | Limitations of Gemini assistance | Troubleshooting Gemini in Looker tasks | Sample Gemini prompts  
---|---|---|---|---  
Query data in natural language with Conversational Analytics |  Looker (original) Looker (Google Cloud core) Looker Studio |  Visualizations Data source-specific limitations Supported questions |  User and platform requirements Supported data sources Setting up a data source Writing effective prompts  
Create calculated fields | Looker Studio | Limitations on calculated field creation |  User and platform requirements Query result errors  
Add Looker Studio content to Google Slides | Looker Studio | Limitations on adding Looker Studio content to Slides |  User and platform requirements Common error messages and possible solutions  
Write LookML using natural language |  Looker (original) Looker (Google Cloud core) | Tips for using Gemini in the Looker IDE |  Sample prompt: Create a dimension based on longitude or latitude Sample prompt: Create a measure for today's total sales  
Create custom Looker visualizations using natural language |  Looker (original) Looker (Google Cloud core) | Visualization Assistant is available only for HighCharts-based visualizations. | Creating successful prompts  
### Gemini in Looker enablement troubleshooting
Platform | Platform requirements to enable Gemini in Looker | Permissions required to enable Gemini in Looker | Troubleshooting  
---|---|---|---  
Looker (original) |  The instance must be Looker-hosted. The instance must be on Looker 25.0 or later to enable Gemini in Looker. The instance must be on Looker 25.2 or later to use Conversational Analytics. We recommend that instances participating in Extended Support Release Program are on Looker 25.6 or later to use Conversational Analytics. | Looker Admin role |  Make sure that the Trusted Testers settings are enabled. Accepted Looker Studio Pro licenses must be associated with the same Google Cloud project as the Looker Studio Pro subscription. Gemini in Looker supports English-language prompts and responses only. Make sure that the `gemini_in_looker` permission is assigned to the appropriate users. The Gemini role and the `gemini_in_looker` permission cannot be assigned to embed users.  
Looker (Google Cloud core) |  Conversational Analytics doesn't support Looker (Google Cloud core) instances that use CMEK or VPC Service Controls. Connecting a Looker (Google Cloud core) instance that uses a private IP network connection that is within a VPC Service Controls perimeter to Conversational Analytics in Looker Studio Pro isn't supported and doesn't meet VPC Service Controls compliance requirements. |  Looker Admin (`roles/looker.admin`) IAM role on the project in which the instance resides |  Make sure that the Trusted Testers settings are enabled. Accepted Looker Studio Pro licenses must be associated with the same Google Cloud project as the Looker Studio Pro subscription. Gemini in Looker supports English-language prompts and responses only. Make sure that the `gemini_in_looker` permission is assigned to the appropriate users. The Gemini role and the `gemini_in_looker` permission cannot be assigned to embed users of an Embed Looker (Google Cloud core) edition instance.  
Looker Studio Pro subscription |  For a standard self-service subscription: a role that contains the `lookerstudio.pro.manage` IAM permission for the Google Cloud project that you use for your Looker Studio Pro subscription. For a "whole organization, active user" (MAU) subscription: a role that contains the Manage Looker Studio Settings Workspace privilege, which is included in the Workspace Services Admin and the Workspace Super Admin roles. |  Make sure that the Trusted Testers settings are enabled. Gemini in Looker supports English-language prompts and responses only.  
## How to submit in-product feedback
Submit in-product feedback to rate the quality and accuracy of Gemini in Looker previews.
You can submit in-product feedback about each Gemini in Looker task by using the thumb_upthumb_down
## How to get support
Reach out to Support if you encounter any of the following issues:
  * Gemini in Looker features are slow to respond or generate content.
  * Gemini in Looker features return blank or empty responses.
  * The instance, report, or chart returns a timeout error.
  * The instance or page returns an internal server error.


Be sure to include a clear description of the problem and the expected behavior, the steps that you took prior to encountering the issue, and any additional relevant details.
For details on how to contact Support, see the documentation for your Looker platform type:
  * Looker (Google Cloud core)
  * Looker Studio Pro
  * Users of no-cost Looker Studio can report issues in the Looker Studio Community


## Related resources
  * Write better prompts for Gemini for Google Cloud
  * Gemini for Google Cloud limitations


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


