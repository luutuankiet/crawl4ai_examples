# Restrict TLS cipher suites on a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-tls-cipher-suites

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Before you begin
  * Setting the organization policy
  * Policy violations




Was this helpful?
Send feedback 
#  Restrict TLS cipher suites on a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Before you begin
  * Setting the organization policy
  * Policy violations


Google Cloud supports multiple TLS cipher suites. To meet security or compliance requirements, you may want to deny requests from clients that use less secure TLS cipher suites.
The `gcp.restrictTLSCipherSuites` organization policy constraint provides this capability.
## Before you begin
To get the permissions that you need to set, change, or delete organization policies, ask your administrator to grant you the Organization Policy Administrator  (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
## Setting the organization policy
The `gcp.restrictTLSCipherSuites` organization policy constraint can be applied to Looker (Google Cloud core) instances that use a public IP networking configuration.
You can apply the constraint before or after you create the instance.
Follow the instructions on the Restrict TLS cipher suites documentation page to set the organization policy. Looker (Google Cloud core) is compliant with the Google-managed MODERN SSL policy profile and supports the cipher suites that are in that profile.
If you set or change the organization policy after the Looker (Google Cloud core) instance is created, you must perform one of the following actions to apply the organization policy update to the Looker (Google Cloud core) instance:
  * Restart the instance.
  * Edit a Looker (Google Cloud core) setting within the Google Cloud console or through the `gcloud` CLI.


## Policy violations
If you set the organization policy restraint to allow no MODERN cipher suites supported by Looker (Google Cloud core), you will be unable to create, update, or restart the Looker (Google Cloud core) instance and will receive the following error:
```
com.google.apps.framework.request.FailedPreconditionException:
Constraint`constraints/gcp.restrictTLSCipherSuites`for`resourcemanager_projects``PROJECT_ID`
```

This output includes the `PROJECT_ID` value, which is the ID of the project that is hosting the Looker (Google Cloud core) instance.
To address the violation, update the `gcp.restrictTLSCipherSuites` organization policy to allow at least one supported cipher suite.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


