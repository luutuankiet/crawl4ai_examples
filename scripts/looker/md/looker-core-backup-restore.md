# Back up and restore a Looker (Google Cloud core) instance

**Source:** https://cloud.google.com/looker/docs/looker-core-backup-restore

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Requirements and cautions
  * Automatic backups
  * Backup retention
  * Restore a backup
  * Backups and CMEK
  * Backups and Looker reports
  * Disabling backups




Was this helpful?
Send feedback 
#  Back up and restore a Looker (Google Cloud core) instance
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Requirements and cautions
  * Automatic backups
  * Backup retention
  * Restore a backup
  * Backups and CMEK
  * Backups and Looker reports
  * Disabling backups


Backups of a Looker (Google Cloud core) instance contain a point-in-time snapshot of an instance's data, and they allow restoration of that instance's data to the time that the backup was created. Restoring a Looker (Google Cloud core) version doesn't upgrade or downgrade the Looker version for the instance. If a version change has occurred between the time of backup and the time of restore, the Looker (Google Cloud core) instance retains the Looker version that the instance is already using.
Backups can be restored only to the same instance that the backup was taken from; if you want to move data from one instance to another, use import and export.
Each backup, whether automatic or manual, contains a record of all the data in the instance's internal database and in the instance's file server, which is most of the operational data for the Looker (Google Cloud core) instance. However, the data for Elite System Activity is not backed up.
There is no disruption to Looker (Google Cloud core) performance during a backup.
## Required roles
To get the permissions that you need to back up or restore a Looker (Google Cloud core) instance, ask your administrator to grant you the Looker Admin  (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see Manage access to projects, folders, and organizations. 
You might also be able to get the required permissions through custom roles or other predefined roles. 
## Requirements and cautions
Your Looker (Google Cloud core) instance must meet several criteria to successfully back up and restore:
  * The Looker API must be enabled. Disabling the Looker API disables the ability to create manual or automatic instance backups.
Enable the API
  * If your Looker (Google Cloud core) instance uses a Google-owned and Google-managed encryption key, which is the default for Looker (Google Cloud core) instances, the local key used by the Looker (Google Cloud core) instance must be the same at the time that the backup was created as it is when the backup gets restored.


Additionally, be aware of the following things before taking manual backups or restoring:
  * Restoring a backup overwrites the existing database and fileserver data, with the data as it was at the time of backup creation. For that reason, restoring an instance can result in the loss of data that was created after the time of backup creation.
  * If your Looker (Google Cloud core) instance uses customer-managed encryption keys (CMEK), see the Backups and CMEK section.
  * If your Looker (Google Cloud core) instance is enabled for Looker reports, see the Backups and Looker reports section.
  * Restoration takes minutes to hours, depending on instance size, and during that time, users cannot log into or use the instance.
  * You can't cancel a backup or restore operation once it has started.


## Automatic backups
Looker (Google Cloud core) instances are backed up automatically every 24 hours.
## Manual backups
You can take manual backups of your Looker (Google Cloud core) instance at any time.
Complete the following steps to manually back up your instance:
More
```
gcloud looker backups create --instance=INSTANCE_NAME --region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance you want to back up; it is not associated with the instance URL.
  * `REGION`: the region the instance was created in.


To see the status of a backup after you have taken one, view the backups. The status of the backup will show as ACTIVE or FAILED.
## View backups
You can view all automatic and manual backups for your Looker (Google Cloud core) instance for the last 30 days. Complete the following steps to view backups:
More
```
gcloud looker backups list --instance=INSTANCE_NAME --region=REGION

```

Replace the following:
  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance for which you want to list backups; it is not associated with the instance URL.
  * `REGION`: the region the instance was created in.


This command returns the following information:
  * **NAME** : the alphanumeric ID of the backup
  * **STATUS** : **ACTIVE** or **FAILED**
  * **CREATE TIME** : a timestamp of the creation of the backup
  * **EXPIRE TIME** : a timestamp of the time the backup will be automatically deleted


## Backup retention
Automated and manual backups are retained for 30 days.
## Delete backups
You can manually delete a manual or an automatic backup.
More
```
gcloud looker backups delete BACKUP_ID --instance=INSTANCE_NAME --region=REGION

```

Replace the following:
  * `BACKUP_ID`: the ID of the backup. This ID can be found by viewing the backups.
  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance that the backup was created from; it is not associated with the instance URL.
  * `REGION`: the region the instance was created in.


After you delete a backup, you can view your backups to confirm the deletion.
## Restore a backup
A backup can be restored to only the Looker (Google Cloud core) instance from which it was created.
If you restore a backup, Looker (Google Cloud core) retains any backups that were made before or after the backup that was used for restoration.
If your Looker (Google Cloud core) instance uses CMEK, see the Backups and CMEK section.
Complete the following steps to restore a backup:
More
```
gcloud looker instances restore INSTANCE_NAME --backup=BACKUP_ID --region=REGION --async

```

Replace the following:
  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance that you want to restore; it is not associated with the instance URL.
  * `BACKUP_ID`: the ID of the backup. This ID can be found by viewing the backups.
  * `REGION`: the region the instance was created in.


The `--async` flag must be included.
Restoration takes minutes to hours, depending on instance size. The restoration process can be monitored by checking the **Status** of the instance on the **Details** tab on the **Instances** page in the Google Cloud console. An **Updating** status means the restoration is in progress; an **Active** status indicates the restoration has been completed.
If you experience any issues with a restoration, contact technical support.
## Backups and CMEK
If your Looker (Google Cloud core) instance uses CMEK for encryption, you can see the CMEK key version used in your instance on the **Details** tab of the **Instances** page in the Google Cloud console. You can see the CMEK key version that the backup uses when you view your backups.
When you want to back up or restore a Looker (Google Cloud core) instance that uses CMEK, keep the following requirements in mind:
  * For a restoration to be successful when CMEK is in use, the CMEK key version that was enabled at the time of backup must still be enabled at the time of restoration.
  * If the CMEK key version that is used by the backup is no longer enabled, make sure to enable the key again before restoration, or the restoration will fail.
  * If the CMEK key version that is used by the backup is deleted or no longer enabled, and if the key version cannot be re-enabled, the backup cannot be restored.
  * If you rotate your CMEK key, Google recommends that you keep your previous key version enabled for 45 days to help ensure that your backups remain accessible.


If an instance is restored with a backup that uses a different key version, the instance will update to use the key version that is current for the instance at the time of restoration. The data in the Looker (Google Cloud core) instance remains encrypted with the instance's CMEK key version after the restore has completed.
## Backups and Looker reports
If your Looker (Google Cloud core) instance has the Looker reports feature enabled, backup and restore actions have the following effects for Looker reports data.
  * **Deleted Looker reports can't be restored.** Even if a backup was taken before a report was deleted, the report won't be recovered after the backup is restored.
  * **Lookerfolder access changes won't propagate to Looker Studio.** Restoring a backup that was taken when folder access settings were different than the current settings may update folder access within Looker (Google Cloud core), but not within Looker Studio.
  * **Changes to the Looker reports option won't propagate to Looker Studio.** Restoring a backup that was taken when the setting for the **Looker reports** option was different than the current setting will update the setting within Looker (Google Cloud core), but not within Looker Studio, and the restoration won't change the enablement status of Looker reports.
  * **Hidden Looker reports can be accessed through its URL.** If a Looker report is created after a backup is taken, and then that backup is restored, the report is hidden. However, you can access the report through its URL.


## Disabling backups
Instance backups are disabled if any of the following actions occur:
  * The Looker API is disabled in the Google Cloud project that the instance is hosted in.
  * The Looker service account loses access to the Google Cloud project that the instance is hosted in.
  * The **Looker Service Agent** IAM role is removed from the Looker service account.


## What's next
  * Delete and restart a Looker (Google Cloud core) instance


Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


