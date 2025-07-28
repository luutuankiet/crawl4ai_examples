# Get All SSH Servers  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/methods/Connection/all_ssh_servers

Skip to main content 


  * Español – América Latina

Console 
  * On this page
  * Get information about all SSH Servers.




Was this helpful?
Send feedback 
#  Get All SSH Servers
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Get information about all SSH Servers.


Version 4.0.25.10 (latest) 
### Get information about all SSH Servers.
## Request
GET /ssh_servers 
Datatype
Description
Request
HTTP Request 
query
HTTP Query 
Expand HTTP Query definition... 
fields
string 
Requested fields.
## Response
200: SSH Server400: Bad Request404: Not Found429: Too Many Requests More
Datatype
Description
(array)
ssh_server_id
_lock_
string 
A unique id used to identify this SSH Server
ssh_server_name
string 
The name to identify this SSH Server
ssh_server_host
string 
The hostname or ip address of the SSH Server
ssh_server_port
integer 
The port to connect to on the SSH Server
ssh_server_user
string 
The username used to connect to the SSH Server
finger_print
_lock_
string 
The md5 fingerprint used to identify the SSH Server
sha_finger_print
_lock_
string 
The SHA fingerprint used to identify the SSH Server
public_key
_lock_
string 
The SSH public key created for this instance
status
_lock_
string 
The current connection status to this SSH Server
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
Datatype
Description
(object)
message
_lock_
string 
Error details
documentation_url
_lock_
string 
Documentation link
## Examples
More
https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift   
---  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


