# Sharing data to Segment  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/segment

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Setting up a Segment integration
  * Adding Segment tags to your LookML model
  * Sending a Look or an Explore to Segment




Was this helpful?
Send feedback 
#  Sharing data to Segment
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Setting up a Segment integration
  * Adding Segment tags to your LookML model
  * Sending a Look or an Explore to Segment


With the Segment integration, available in the Looker Action Hub, you can send Looks and Explores to a variety of integrations managed by Segment, including third-party applications like Marketo, Hubspot, and others.
To start using Segment in Looker:
  1. A Looker admin sets up a Segment integration. This step is only required once.
  2. A Looker developer sets up Segment tags. This step is only required once.
  3. A Looker user selects Segment as the destination of a delivery.


## Setting up a Segment integration
To set up a Segment integration:
  1. In your Segment workspace, search the **Catalog** for the Looker source and select it.
  2. In **Source setup** , give your source a name (typically `Looker`), and select **Add Source**.
  3. Segment will display a write key for your source. Copy this write key.
  4. In your Looker instance, navigate to the **Actions** page in the **Platform** section of the **Admin** panel.
  5. Select **Enable** next to the Segment action you want to enable.
  6. Paste the Segment write key from step 3 into the **Segment Write Key** field.
  7. Select **Save**.


To finish setting up your Segment integration, add Segment tags to your LookML model.
## Adding Segment tags to your LookML model
To send or schedule Looks and Explores with Segment attributes, first add LookML tags to the appropriate fields in your Looker model. For a complete list of allowed tags for each action, see the tags (for fields) documentation page.
Most actions require at least the `email` and `user_id` tags. Add these tags to the fields in your LookML model that correspond to Segment user email addresses and user IDs, respectively. For example:
```
dimension: email {
  sql: ${TABLE}.email ;;
  tags: ["email"]
}

dimension: user_id {
  sql: ${TABLE}.user_id ;;
  tags: ["user_id"]
}

```

## Sending a Look or an Explore to Segment
Once you have set up the Segment integration and defined LookML tags, you can send Looks and Explores to Segment.
  1. Create a Look or build an Explore using one or more fields with a Segment LookML tag.
  2. Select the gear icon. For Looks, select either **Send** or **Schedule**. For Explores, select either **Send** or **Save and schedule**.
  3. Select your Segment destination.
  4. Configure other delivery settings as desired and select **Send** or **Save**.
  5. Confirm that Segment is receiving your Segment attributes using the Segment debugger.


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


