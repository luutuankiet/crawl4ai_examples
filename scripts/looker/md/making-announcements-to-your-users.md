# Making announcements to your users  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/making-announcements-to-your-users

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Changing a sidebar title or description
  * Rearranging cards
  * Linking to Markdown documents




Was this helpful?
Send feedback 
#  Making announcements to your users
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Changing a sidebar title or description
  * Rearranging cards
  * Linking to Markdown documents


If your company uses the Looker pre-built homepage, admins or users who have the `manage_homepage` permission can share text, links, and images with all Looker users in the right-hand announcement sidebar:
If the announcement sidebar has been closed, it can be re-opened by selecting **Welcome Guide** from the **Help** menu in the Looker header.
Admins and users who have the `manage_homepage` permission can add or edit the sidebar. Before content is added to the sidebar, non-admin users will see the pre-built homepage without the sidebar. Admins and users who have the `manage_homepage` permission will see prompts to add content to the sidebar.
## Adding a card
  1. At the top of the sidebar, click **+ Add New Card**.
  2. Under **Title** , enter a title for the card. The title appears as header text that is always visible on the card. Titles that are more than 25 characters long may not display properly %mdash; the end may be cut off.
  3. Optionally, enter the following: 
     * **Description** : Text that appears after the title on the card. The **Description** field has a 250-character limit.
     * **Link** : URL that opens in a new browser tab when a user clicks on the card. Enter the full URL, including the `https://` or `http://`. The URL path does not appear to the user, but the card title and text will appear blue if the card is a link or will appear black if the card is not a link. You can also use the **Description** field to add a text description of the link target, such as its title.
     * **Upload Image** : Click the **Upload Image** button to upload an image that appears in the card.
  4. When your new card is finished, click **Create**.


## Editing a card
  1. Click the three-dot **Content Card Menu** icon on the card you would like to edit, and select **Edit**.
  2. Optionally, edit the following: 
     * **Title** : Bold text that is always visible on the card
     * **Description** : Text that appears after the title on the card
     * **Link** : URL that opens in a new browser tab when a user clicks on the card
  3. Optionally, click the trash bin icon to delete the card's image. If you want to upload a new image, click **Upload Image** to navigate to and upload a new image for the card.
  4. Select **Save** to save the card.


## Changing a sidebar title or description
  1. Hover over the sidebar title or description to reveal the **Edit** pencil icon. Click the **Edit** pencil icon.
  2. Select the existing title or description and replace it with a new sidebar title or description.
  3. To save changes, click the **Done** checkmark icon.


## Rearranging cards
Click and drag the six-dot **Drag handle** icon in the bottom left of a card to move the card's order in the sidebar.
## Deleting a card
  1. Click the three-dot **Content Card Menu** icon on the card that you would like to edit, and select **Delete**.
  2. To confirm the deletion, click **Confirm**.


## Linking to Markdown documents
You can write documentation, announcements, or information for Looker projects using GitHub-flavored Markdown and link to the documentation files in the sidebar.
Users with develop privileges can navigate to and obtain the URL for a Markdown document by following these steps:
  1. Navigate to the project.
  2. Select the name of the document (or create a new document).
  3. From the document menu, select **View Document**.
  4. From the new browser window, copy the URL for the document.
  5. Paste the Markdown file URL into the **Link** field of a sidebar card.


Now, users can click that sidebar card and Looker will open the document in a new browser tab.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


