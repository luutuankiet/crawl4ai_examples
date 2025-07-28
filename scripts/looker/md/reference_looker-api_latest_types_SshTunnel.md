# SshTunnel  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/reference/looker-api/latest/types/SshTunnel

Skip to main content 


  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体

Console  Sign in


Send feedback 
#  SshTunnel
Stay organized with collections  Save and categorize content based on your preferences. 
Version 4.0.25.10 (latest) 
Datatype
Description
(object)
object 
tunnel_id
_lock_
string 
Unique ID for the tunnel
ssh_server_id
string 
SSH Server ID
ssh_server_name
_lock_
string 
SSH Server name
ssh_server_host
_lock_
string 
SSH Server Hostname or IP Address
ssh_server_port
_lock_
integer 
SSH Server port
ssh_server_user
_lock_
string 
Username used to connect to the SSH Server
last_attempt
_lock_
string 
Time of last connect attempt
local_host_port
integer 
Localhost Port used by the Looker instance to connect to the remote DB
database_host
string 
Hostname or IP Address of the Database Server
database_port
integer 
Port that the Database Server is listening on
status
_lock_
string 
Current connection status for this Tunnel
## Related Methods
  * Connection/create_ssh_tunnel
  * Connection/update_ssh_tunnel
  * Connection/test_ssh_tunnel


Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


