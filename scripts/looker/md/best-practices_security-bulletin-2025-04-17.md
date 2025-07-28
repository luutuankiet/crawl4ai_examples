# Security Bulletins  |  Customer Care  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/best-practices/security-bulletin-2025-04-17

Skip to main content 
  * Español – América Latina

Console 


  * On this page




Was this helpful?
Send feedback 
#  Security Bulletins
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page


The following security bulletins are related to Google Cloud products.
Use this XML feed to subscribe to security bulletins for this page. 
## GCP-2025-041
**Published:** 2025-07-21
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Ubuntu nodes: 
  * CVE-2025-37890

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-040
**Published:** 2025-07-15
### Description
Description | Severity | Notes  
---|---|---  
Per advisory VMSA-2025-0013, multiple vulnerabilities in VMware ESXi were privately reported to Broadcom. We've either already patched these vulnerabilities or are in the process of applying the necessary patches supplied by Broadcom. There are no known workarounds for these reported vulnerabilities. Once patched, your VMware Engine deployments should be running ESXi 7.0U3w or ESXi 8.0U3f or greater.
#### What should I do?
Google recommends customers to monitor their workloads on VMware Engine for any unusual activities. | Medium to Critical | 

  
## GCP-2025-039
**Published:** 2025-07-15
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-38083

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-038
**Published:** 2025-07-09
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-37752

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-037
**Published:** 2025-07-08
Description | Severity | Notes  
---|---|---  
AMD has disclosed two vulnerabilities affecting AMD EPYC 2nd generation (Rome), 3rd generation (Milan), and 4th generation (Genoa) CPUs. The vulnerabilities allow an attacker to infer data from previous stores or the L1D cache, potentially resulting in leakage of sensitive information.  Google has rolled out a mitigation that prevents this leakage of information between VMs.  There is still the potential that processes within a single VM can exploit these vulnerabilities. 
#### What should I do?
After July 8, 2025, a guest-level mitigation that protects against intra-guest attacks is available to the following VMs: 
  * VMs that are started for the first time.
  * VMs that are fully stopped and started again. Operating system reboots will not enable the mitigation, and the VM itself must be fully restarted to enable the mitigation. Guest operating system kernels must support this mitigation for it to be effective. 

For more information see AMD security bulletin AMD-SB-7029.  | Medium | 

  
## GCP-2025-036
**Published:** 2025-07-01
**Updated:** 2025-07-21
### Description
Description | Severity | Notes  
---|---|---  
**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-38001

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-035
**Published:** 2025-06-17
**Updated:** 2025-07-21
### Description
Description | Severity | Notes  
---|---|---  
**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-37997

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-034
**Published:** 2025-06-17
**Updated:** 2025-07-21
### Description
Description | Severity | Notes  
---|---|---  
**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-38000

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-033
**Published:** 2025-06-06
### Description
Description | Severity | Notes  
---|---|---  
A security issue was discovered where attackers might be able to bypass workload isolation restrictions on GKE clusters. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| Medium |  N/A   
## GCP-2025-032
**Published:** 2025-06-03
**Updated:** 2025-07-21
### Description
Description | Severity | Notes  
---|---|---  
**2025-07-21 Update:** Added patch versions for Ubuntu node pools on GKE.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-37798

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-031
**Published:** 2025-06-03
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-37797

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-030
**Published:** 2025-05-23
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0017, an SQL-injection vulnerability in VMware Aria Automation was privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.
#### What should I do?
We recommend upgrading to VMware Aria Automation KB325790.  | Important | 

  
## GCP-2025-029
**Published:** 2025-05-23
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2025-0006, a local privilege escalation vulnerability in VMware Aria Operations was responsibly reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.
#### What should I do?
We recommend upgrading to VMware Aria Operations 8.18 HF5.  | Important | 

  
## GCP-2025-028
**Published:** 2025-05-23
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2025-0003, multiple vulnerabilities in VMware Aria Operations for logs and VMware Aria Operations were privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.
#### What should I do?
We recommend upgrading to VMware Aria Operations for Logs 8.18.3 and VMware Aria Operations to 8.18.3.  | Important | 

  
## GCP-2025-027
**Published:** 2025-05-16
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability was detected in the classic Application Load Balancer service prior to April 26, 2025.
#### What should I do?
No customer action is required. The issue was resolved in the Classic Application Load Balancer service on April 26, 2025.
#### What vulnerabilities are being addressed?
CVE-2025-4600 allowed attackers to smuggle requests to classic Application Load Balancers due to incorrect parsing of oversized chunk bodies. When parsing the request body of an HTTP request using chunked transfer-encoding, the classic Application Load Balancer allows oversized chunk bodies. Consequently, it was feasible to hide bytes within this ignored trailing data that an upstream HTTP server might incorrectly interpret as a line terminator. This vulnerability was addressed within the classic Application Load Balancer service on April 26, 2025 through improved input validation and parsing logic.
#### We're here to help
If you have any questions or require assistance, contact Cloud Customer Care. | High  
## GCP-2025-026
**Published:** 2025-05-15
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2025-0008, a DOM based Cross-Site Scripting (XSS) vulnerability in VMware Aria Automation was privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.
#### What should I do?
We recommend upgrading to VMware Aria Automation 8.18.1 patch 2.  | Important | 

  
## GCP-2025-025
**Published:** 2025-05-13
### Description
Description | Severity | Notes  
---|---|---  
Intel has notified Google about a new side channel vulnerability affecting the following Intel processors: CascadeLake, Ice Lake XeonSP, Ice Lake XeonD, Sapphire Rapids and Emerald Rapids. Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.
#### What should I do?
No customer action is required. Fixes have already been applied to the Google server fleet to protect customers.
#### What vulnerabilities are being addressed?
CVE-2024-45332. For more information, see Intel advisory INTEL-SA-01247.
#### We're here to help
If you have any questions or require assistance, please contact Cloud Customer Care and reference issue number 417536835. | High  
## GCP-2025-024
**Published:** 2025-05-12
**Updated:** 2025-05-13
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-13 Update:** If you have any questions or require assistance, please contact Cloud Customer Care and reference issue number 417458390. Intel has notified Google about a new speculative execution vulnerability affecting Intel Cascade Lake processors and Intel Ice Lake processors. Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.
#### What should I do?
No customer action is required. Mitigations have already been applied to the Google server fleet. Further mitigations from Intel Original Equipment Manufacturers (OEMs) and other operating system partners will be deployed as soon as they become available to mitigate the same-mode Indirect Target Selection (ITS) vulnerability. After the operating system mitigations have been applied, customers with long-running 3rd generation or later VMs may experience some unintended performance degradation
#### What vulnerabilities are being addressed?
CVE-2024-28956. For more information, see Intel security advisory INTEL-SA-01153. | High  
## GCP-2025-023
**Published:** 2025-05-05
### Description
Description | Severity | Notes  
---|---|---  
Potential security gaps which could be exploited if not addressed in the JavaCallout and PythonScript policies were discovered and addressed.  For instructions and more details see the  Apigee security bulletin.  | High  
## GCP-2025-022
**Published:** 2025-05-01
**Updated:** 2025-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-21702

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-021
**Published:** 2025-04-29
**Updated:** 2025-06-02
### Description
Description | Severity | Notes  
---|---|---  
**2025-06-02 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-21971

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-020
**Published:** 2025-04-29
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability in Looker allowed users with admin permissions (specifically: `manage_project_connections_restricted`) in Looker to read files from the underlying host filesystem and query internal network endpoints. This issue is now resolved, and no user action is required for Looker-hosted customers using Looker (Google Cloud core) and Looker (original). Self-hosted Looker instances are advised to update to the latest supported version. This vulnerability has been patched in all supported versions of customer-hosted Looker, which are available on the Looker download page.
### What should I do?
  * For all Looker-hosted instances, including both Looker (Google Cloud core) and Looker (original) instances, there are no actions you need to take.
  * For Looker customer-hosted instances, please update to the latest supported version of Looker as soon as possible. The versions below have all been updated to protect from this vulnerability. You can download these versions at the Looker download page: 
    * 25.4 -> 25.4.29+
    * 25.2 -> 25.2.34+
    * 25.0 -> 25.0.55+
    * 24.18 -> 24.18.185+
    * 24.12 -> 24.12.95+
    * 24.6 -> 24.6.107+

| High  
## GCP-2025-019
**Published:** 2025-04-25
**Updated:** 2025-06-26
### Description
Description | Severity | Notes  
---|---|---  
**2025-06-26 Update:** Added patch versions for GDC software for VMware. **2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2025-21701

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-018
**Published:** 2025-04-23
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2025-40364

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-017
**Published:** 2025-04-17
**Updated:** 2025-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.  **2025-05-05 Update:** Added patch versions for GDC software for VMware. Updated severity for GDC software for VMware to High. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-21756

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-016
**Published:** 2025-04-16
**Updated:** 2025-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.  **2025-04-29 Update:** Added patch version for GDC software for VMware. Updated severity for GDC software for VMware to High.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2023-52927

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-015
**Published:** 2025-04-15
**Updated:** 2025-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.  **2025-04-17 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to High. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-21700

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-014
**Published:** 2025-04-10
**Updated:** 2025-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-05-22 Update:** Added patch versions for Ubuntu node pools on GKE.  **2025-05-05 Update:** Added patch versions for GDC software for VMware. Updated severity for GDC software for VMware to High. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2025-21703

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-013
**Published:** 2025-03-24
### Description
Description | Severity | Notes  
---|---|---  
Several security issues have been discovered in the NGINX Ingress Controller, `ingress-nginx`, an open source software component that runs inside Kubernetes clusters to help manage network traffic coming into the cluster. The most critical is CVE-2025-1974. For the full details and a complete list, see the Kubernetes CVE feed. These issues affect `ingress-nginx`. If you do not have `ingress-nginx` installed on your cluster, you are not affected. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| None  
## GCP-2025-012
**Published:** 2025-03-19
**Updated:** 2025-04-10
### Description
Description | Severity | Notes  
---|---|---  
**2025-04-10 Update:** Added patch versions for Ubuntu GKE nodes and GDC software for VMware. Updated severity for GDC software for VMware to High.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-53164

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-011
**Published:** 2025-03-06
Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in VMSA-2025-0004 that impact ESXi components deployed in customer environments.
#### VMware Engine impact
Your private clouds are either already patched or are in the process of being updated to address the security vulnerability. As part of the VMware Engine service, all customers get dedicated bare metal hosts with local attached disks that are physically isolated from other hardware. This means that the vulnerability is scoped to guest VMs within your specific private cloud only. Your private clouds will be updated to 7.0u3s Build number 24534642. This is equivalent to 7.0U3s: Build number 24585291.
#### What should I do?
Follow instructions from Broadcom and your security vendors regarding this vulnerability.  | Critical | 

  
## GCP-2025-010
**Published:** 2025-03-05
**Updated:** 2025-06-02
### Description
Description | Severity | Notes  
---|---|---  
**2025-06-02 Update:** Added patch versions for Ubuntu node pools on GKE.  **2025-04-10 Update:** Added patch versions for GDC software for VMware. Updated severity for GDC software for VMware to High.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-56770

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-009
**Published:** 2025-03-05
### Description
Description | Severity | Notes  
---|---|---  
The Envoy project recently announced several new security vulnerabilities (CVE-2024-53269, CVE-2024-53270, and CVE-2024-53271) that could allow an attacker to crash Envoy. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High | 

  
## GCP-2025-008
**Published:** 2025-02-19
**Updated:** 2025-04-10
### Description
Description | Severity | Notes  
---|---|---  
**2025-04-10 Update:** Added patch versions for GDC software for VMware. Updated severity for GDC software for VMware to High.  The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-53141

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-007
**Published:** 2025-02-03
### Description
Description | Severity | Notes  
---|---|---  
Google has discovered a vulnerability in AMD Zen-based CPUs that affects Confidential VM instances with AMD SEV-SNP enabled. This vulnerability allows attackers with root access in a physical machine to compromise the confidentiality and integrity of the Confidential VM instance. Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google. **What should I do?** No customer action is required. Customers who want to verify the fix can check the Trusted Computing Base (TCB) version in the attestation report from their Confidential VM instance with AMD SEV-SNP. The minimum versions that mitigate this vulnerability are as follows: ```
SNP TCB SVN: 0x18 0d24
tcb_version {
  psp_bootloader_version: 4
  snp_firmware_version: 24 (0x18)
  microcode_version: 219
}
```
For more information, see AMD security bulletin  AMD-SB-3019. | High |  CVE-2024-56161  
## GCP-2025-006
**Published:** 2025-01-23
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability in the Google Secret Manager Provider for Secret Store CSI Driver allows an attacker with Pod and Secret creation permissions in a namespace to exfiltrate the CSI driver's Kubernetes service account token by mounting a malicious volume on a Pod.  For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| Medium  
## GCP-2025-005
**Published:** 2025-01-22
### Description
Description | Severity | Notes  
---|---|---  
Servers that use Google authentication libraries and Cloud Client Libraries to authenticate to Google Cloud with a credential configuration controlled by an attacker could be susceptible to server-side request forgery and arbitrary file reads. 
#### What should I do?
If you accept a credential configuration (credential JSON, file, or stream) from an external source for authentication to Google Cloud, you must validate it before providing it to Google authentication libraries or Cloud Client Libraries. Providing an unvalidated credential configuration to Google libraries can compromise the security of your systems and data. For more information, see  Validate credential configurations from external sources. 
#### What vulnerabilities are being addressed?
Some types of credential configurations include endpoints and file paths, which the authentication libraries use to acquire a token. When a service or application accepts externally sourced credential configurations and uses them with Google authentication libraries or Cloud Client Libraries without validation, an attacker can provide a credential configuration that contains a malicious endpoint or path. This allows the attacker to exfiltrate data or tokens from the service or the machine the service is running on. To prevent this, validations should be performed on the externally sourced credential configuration as described in  Validate credential configurations from external sources.  To inform application developers, we have updated our documentation with the validations to perform when accepting credential configurations that are obtained from external sources.  | High  
## GCP-2025-004
**Published:** 2025-01-16
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2025-0001, a server-side request forgery (SSRF) vulnerability in VMware Aria Automation was responsibly reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.
#### What should I do?
We recommend upgrading to VMware Aria Automation 8.18.2 HF.  | Medium | 

  
## GCP-2025-003
**Published:** 2025-01-09
**Updated:** 2025-01-23
### Description
Description | Severity | Notes  
---|---|---  
**2025-01-23 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-50264

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-002
**Published:** 2025-01-09
**Updated:** 2025-01-23
### Description
Description | Severity | Notes  
---|---|---  
**2025-01-23 Update:** Added patch versions for Ubuntu node pools on GKE. **2025-01-22 Update:** Added patch versions for GDC (VMware). Updated severity for GDC (VMware) to Medium. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-53057

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2025-001
**Published:** 2025-01-08
**Updated:** 2025-01-23
### Description
Description | Severity | Notes  
---|---|---  
**2025-01-23 Update:** Updated the **Affected resources** section in the GKE tab. **2025-01-08 Update:** Corrected the start date and time of the issue. A security issue impacted resources in VPCs with GKE Multi-Cluster Gateway (MCG) configured. MCG is an optional feature that is used by a small subset of GKE customers. We are individually notifying customers who had the feature enabled during that time period. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High |  None   
## GCP-2024-065
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2024-53269: Happy Eyeballs: Validate that additional_address are IP addresses instead of crashing when sorting.
  * CVE-2024-53270: HTTP/1: Sending overload crashes when the request is reset beforehand.
  * CVE-2024-53271: HTTP/1.1 Multiple issues with envoy.reloadable_features.http1_balsa_delay_reset.

For instructions and more details, see the Cloud Service Mesh security bulletin. | High | 

  
## GCP-2024-064
**Published:** 2024-12-10
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0022, multiple vulnerabilities in VMware Aria Operations were responsibly reported to VMware. Updates are available to remediate these vulnerabilities in the affected VMware product.
#### What should I do?
We recommend upgrading to VMware Aria Operations 8.18.2.  | Important | 

  
## GCP-2024-063
**Published:** 2024-12-06
Description | Severity | Notes  
---|---|---  
A vulnerability was discovered in the Vertex AI API serving Gemini multimodal requests, allowing bypass of VPC Service Controls. An attacker may be able to abuse the `fileURI` parameter of the API to exfiltrate data.  **What should I do?** No actions needed. We've implemented a fix to return an error message when a media file URL is specified in the fileUri parameter and VPC Service Controls is enabled. Other use cases are unaffected.  **What vulnerabilities are being addressed?** The Cloud Support API serving Gemini multimodal requests lets you include media files by specifying the URL of the media file in the `fileUri` parameter. This capability can be used to bypass VPC Service Controls perimeters. An attacker inside the service perimeter could encode sensitive data in the `fileURI` parameter to bypass the service perimeter.  | Medium  
## GCP-2024-062
**Published:** 2024-12-02
**Updated:** 2025-01-22
### Description
Description | Severity | Notes  
---|---|---  
**2025-01-22 Update:** Added patch versions for GDC (VMware). Updated GDC (VMware) severity from Pending to High. **2024-12-12 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-46800

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-061
**Published:** 2024-11-25
### Description
Description | Severity | Notes  
---|---|---  
A security issue discovered in Kubernetes clusters could result in remote code execution using a `gitRepo` volume. If the git repository is maliciously constructed, a user with the ability to create a Pod and associate a `gitRepo` volume could execute arbitrary commands beyond the container boundary. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-060
**Published:** 2024-10-17
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0020, multiple vulnerabilities in VMware NSX were responsibly reported to VMware. The version NSX-T running on your VMware Engine environment is not impacted by CVE-2024-38815, CVE-2024-38818, or CVE-2024-38817.
#### What should I do?
Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Medium | 

  
## GCP-2024-059
**Published:** 2024-10-16
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0021, an authenticated SQL injection vulnerability in VMware HCX was privately reported to VMware. We have applied the mitigation approved by VMware to address this vulnerability. This fix addresses a security vulnerability described in CVE-2024-38814. The image versions running in your VMware Engine private cloud don't reflect any change at this time to indicate the changes applied. Appropriate mitigations have been installed and your environment is secured from this vulnerability.
#### What should I do?
We recommend upgrading to VMware HCX version 4.9.2.  | High | 

  
## GCP-2024-058
**Published:** 2024-10-16
### Description
Description | Severity | Notes  
---|---|---  
Migrate to Containers for Windows versions 1.1.0 to 1.2.2 created a local `m2cuser` with administrator privileges. This posed a security risk if the `analyze` or `generate` commands were interrupted by the user or due to an internal error causing skipping the action to delete the local user `m2cuser`. 
#### What should I do?
The following versions of Migrate to Containers CLI for Windows have been updated with code to fix this vulnerability. We recommend that you manually upgrade your Migrate to Containers CLI to the following version or higher:
  * Migrate to Containers CLI for Windows 1.2.3 released on October 8, 2024 -  Migrate to Containers CLI release notes | Google Cloud


#### What vulnerabilities are being addressed?
The vulnerability, CVE-2024-9858, allows an attacker to gain administrator access to impacted Windows machines using the local administrator user created by the Migrate to Containers software. | Medium  
## GCP-2024-057
**Published:** 2024-10-03
**Updated:** 2024-11-19
### Description
Description | Severity | Notes  
---|---|---  
**2024-11-19 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-10-15 Update:** Added patch versions for GDC (VMware). Updated GKE and GDC (VMware) severity levels. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-45016

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| Medium  
## GCP-2024-056
**Published:** 2024-09-27
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability chain (CVE-2024-47076, CVE-2024-47175, CVE-2024-47176, CVE-2024-47177) that could result in remote code execution was discovered in the CUPS printing system used by some Linux distributions. An attacker can exploit this vulnerability if the CUPS services are listening on UDP port 631 and they can connect to it.  For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| None | 

  
## GCP-2024-055
**Published:** 2024-09-24
### Description
Description | Severity | Notes  
---|---|---  
An HTTP Request Smuggling vulnerability in Looker allowed an unauthorized attacker to capture HTTP responses destined for legitimate users.  There are two Looker versions that are hosted by Looker:
  * Looker (Google Cloud core) was found to be vulnerable. This issue has already been mitigated and our investigation has found no signs of exploitation.
  * Looker (original) was not vulnerable to this issue.

Customer-hosted Looker instances were found to be vulnerable and must be upgraded to one of the versions below.  This vulnerability has been patched in all supported versions of customer-hosted Looker, which are available on the Looker download page. 
### What should I do?
  * For all Looker-hosted instances, including Looker (Google Cloud core) instances, there are no actions you need to take.
  * For Looker customer-hosted instances, please update to the latest supported version of Looker as soon as possible. The versions below have all been updated to protect from this vulnerability. You can download these versions at the Looker download page: 
    * 23.12 -> 23.12.123+
    * 23.18 -> 23.18.117+
    * 24.0 -> 24.0.92+
    * 24.6 -> 24.6.77+
    * 24.8 -> 24.8.66+
    * 24.10 -> 24.10.78+
    * 24.12 -> 24.12.56+
    * 24.14 -> 24.14.37+


### What vulnerabilities are being addressed?
The vulnerability, CVE-2024-8912, allows an attacker to send crafted HTTP request headers to Looker, possibly resulting in the interception of HTTP responses destined for other users.  These responses could contain sensitive information.  This vulnerability is only exploitable under certain specific configurations.  | Medium  
## GCP-2024-054
**Published:** 2024-09-23
### Description
Description | Severity | Notes  
---|---|---  
A security issue was discovered in Kubernetes clusters with Windows nodes where `BUILTIN\Users` may be able to read container logs and `NT AUTHORITY\Authenticated` Users may be able to modify container logs.  For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| Medium  
## GCP-2024-053
**Published:** 2024-09-19
### Description
Description | Severity | Notes  
---|---|---  
When parsing unknown fields in the Protobuf Java Full and Lite libraries, a maliciously crafted message can cause a StackOverflow error and lead to a program crash. **What should I do?** We have been working diligently to address this issue and have released a mitigation that is available now. We encourage that you're using the latest versions of the following software packages:
  * protobuf-java (3.25.5, 4.27.5, 4.28.2)
  * protobuf-javalite (3.25.5, 4.27.5, 4.28.2)
  * protobuf-kotlin (3.25.5, 4.27.5, 4.28.2)
  * protobuf-kotlin-lite (3.25.5, 4.27.5, 4.28.2)
  * com-protobuf [JRuby gem only] (3.25.5, 4.27.5, 4.28.2)

**What vulnerabilities are addressed by this patch?** This vulnerability is a potential Denial of Service. Parsing nested groups as unknown fields with DiscardUnknownFieldsParser or Java Protobuf Lite parser, or against Protobuf map fields, creates unbounded recursions that can be abused by an attacker. |  CVSS4.0 score 8.7 High  
## GCP-2024-052
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2024-45807: oghttp2 crash on OnBeginHeadersForStream
  * CVE-2024-45808: Malicious log injection via access logs
  * CVE-2024-45806: Potential to manipulate `x-envoy` headers from external sources
  * CVE-2024-45809: JWT filter crash in the clear route cache with remote JWKs
  * CVE-2024-45810: Envoy crashes for LocalReply in http async client

For instructions and more details, see the Cloud Service Mesh security bulletin.  | Medium to High | 

  
## GCP-2024-051
**Published:** 2024-09-18
Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in VMSA-2024-0019 that impact vCenter components deployed in customer environments. 
#### VMware Engine impact
  * Google has already disabled any potential exploit of this vulnerability. For example, Google has blocked the ports through which this vulnerability could be exploited. 
  * In addition, Google ensures all future deployments of vCenter are not exposed to this vulnerability. 


#### What should I do?
No further action is required at this time.  | Critical | 

  
## GCP-2024-050
**Published:** 2024-09-04
### Description
Description | Severity | Notes  
---|---|---  
A new remote code execution vulnerability (CVE-2024-38063) has been discovered in Windows. An attacker could remotely exploit this vulnerability by sending specially crafted IPv6 packets to a host. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| None  
## GCP-2024-049
**Published:** 2024-08-21
**Updated:** 2024-11-01
### Description
Description | Severity | Notes  
---|---|---  
**2024-11-01 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware). The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-36978

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-048
**Published:** 2024-08-20
**Updated:** 2024-10-30
### Description
Description | Severity | Notes  
---|---|---  
**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-10-25 Update:** Added patch versions and updated Severity for GDC (VMware). The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-41009

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-047
**Published:** 2024-08-19
**Updated:** 2024-10-30
### Description
Description | Severity | Notes  
---|---|---  
**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware). The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-39503

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-046
**Published:** 2024-08-05
### Description
Description | Severity | Notes  
---|---|---  
AMD has notified Google about 3 new (2 medium risk, 1 high risk) firmware vulnerabilities affecting SEV-SNP in AMD EPYC 3rd generation (Milan) and 4th generation (Genoa) CPUs. Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google. **What should I do?** No customer action is required. Fixes have already been applied to the Google server fleet. For more information, see AMD security bulletin  AMD-SN-3011. | Medium–High |  CVE-2023-31355 CVE-2024-21978 CVE-2024-21980  
## GCP-2024-045
**Published:** 2024-07-17
**Updated:** 2024-09-19
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-19 Update:** Added patch versions for GDC software for VMware. **2024-08-21 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26925

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-044
**Published:** 2024-07-16
**Updated:** 2024-10-30
### Description
Description | Severity | Notes  
---|---|---  
**2024-10-30 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-10-21 Update:** Added patch versions and updated Severity for GDC (VMware). The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-36972

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-043
**Published:** 2024-07-16
**Updated:** 2024-10-02
### Description
Description | Severity | Notes  
---|---|---  
**2024-10-02 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-09-20 Update:** Added patch versions for GDC software for VMware. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26921

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-042
**Published:** 2024-07-15
**Updated:** 2024-07-18
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-18 Update:** Clarified that Autopilot clusters in the default configuration aren't impacted. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26809

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-041
**Published:** 2024-07-08
**Updated:** 2024-09-16
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-16 Update:** Added patch versions for GDC software for VMware. **2024-07-19 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-52654
  * CVE-2023-52656

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High | 

  
## GCP-2024-040
**Published:** 2024-07-01
**Updated:** 2024-07-16
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-16 Updates:** Some Serverless VPC Access customers are potentially impacted by a vulnerability in OpenSSH (CVE-2024-6387). In the case of successful exploit, this could allow a remote, unauthenticated attacker to execute arbitrary code as root on the target virtual machine. Exploitation is believed to be difficult. For example, customers can't access the VMs and the VMs don't have public IPs. We are not aware of any exploitation attempts.  **What should I do?** Serverless VPC Access deployments have been automatically updated by Google where possible. However, you should verify that the Google-managed service agent has its required role. If not, your Serverless VPC Access connector might still be vulnerable. We recommend that you migrate to Direct VPC egress, or deploy a new connector and delete the old connector, to ensure that you have the required update with the fix.  **2024-07-11 Update:** Added patch versions for GDC software for VMware, GKE on AWS, and GKE on Azure. For details, in the GKE documentation, see the following bulletins: 
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin

**2024-07-10 Update:**
  * Added security bulletin for Migrate to Virtual Machines.

**2024-07-09 Updates:** Some App Engine flexible environment customers are potentially impacted by a vulnerability in OpenSSH (CVE-2024-6387). In the case of successful exploit, this could allow a remote, unauthenticated attacker to execute arbitrary code as root on the target virtual machine.  **What should I do?** Google has already updated flexible environment deployments automatically where possible. However some customers who disabled the Google-managed service agent, or made changes to the Google Cloud APIs or other default configurations, could not be updated and might still be vulnerable. You should deploy a new version of your app to pick up the update with the fix.  Please note that updated deployments will report ssh version `OpenSSH_9.6p1`. This version has been patched with a fix for CVE-2024-6387. **What vulnerabilities are being addressed?** The vulnerability CVE-2024-6387, which allows a remote, unauthenticated attacker to execute arbitrary code as root on the target machine.  **2024-07-08 Updates:** Dataproc clusters on Google Compute Engine running on image version 2.2 (all operating systems) and 2.1 (Debian only) are impacted by a vulnerability in OpenSSH (CVE-2024-6387) which in case of successful exploit could allow a remote, unauthenticated attacker to execute arbitrary code as root on the target machine. Dataproc on Google Compute Engine image versions 2.0 and 1.5, as well as Dataproc images version 2.1 not running on Debian, are not impacted. Dataproc clusters with Personal Authentication enabled are not impacted. Dataproc Serverless is also not impacted. **What should I do?** Please update your Dataproc clusters on Google Compute Engine to one the following versions: 
  * 2.2.24 or later
  * 2.1.58 or later

In case you are not able to update your Dataproc clusters to one of the versions above, we recommend using the initialization action available at this location: `gs://dataproc-initialization-actions/hotfixes/openssh-CVE-2024-6387-mitigation.sh` Please follow these instructions on how to specify initialization actions for Dataproc. Please note that the initialization action has to be run on every node (masters and workers) for pre-existing clusters.  **2024-07-03 Updates:**
  * Added patch versions for GKE.
  * Added security bulletin for GDC connected.

**2024-07-02 Updates:**
  * Clarified that Autopilot clusters are impacted and will require user action.
  * Added impact assessments and mitigation steps for GDC software for VMware, GKE on AWS, and GKE on Azure.
  * Corrected the GDC software for bare metal security bulletin to clarify that GDC software for bare metal isn't directly affected and that customers should check with OS vendors for patches.

A remote code execution vulnerability, CVE-2024-6387, was recently discovered in OpenSSH. The vulnerability exploits a race condition that can be used to obtain access to a remote shell, enabling attackers to gain root access. At the time of publication, exploitation is believed to be difficult and take several hours per machine being attacked. We are not aware of any exploitation attempts.  For instructions and more details, see the following bulletins:
  * Compute Engine security bulletin
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin
  * Google Cloud VMware Engine security bulletin
  * Apigee security bulletin
  * Dataflow security bulletin
  * GDC connected security bulletin
  * Migrate to Virtual Machines security bulletin

| Critical  
## GCP-2024-039
**Published:** 2024-06-28
**Updated:** 2024-09-25
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-25 Update:** Added patch versions for GDC software for VMware. **2024-08-20 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26923

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-038
**Published:** 2024-06-26
**Updated:** 2024-09-17
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-17 Update:** Added patch versions for GDC software for VMware. **2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26924

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GDC software for VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GDC software for bare metal security bulletin

| High  
## GCP-2024-037
**Published:** 2024-06-18
Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in VMSA-2024-0012 that impact vCenter components deployed in customer environments. 
#### Google Cloud VMware Engine impact
  * The vulnerability can be exploited by accessing specific ports in vCenter Server. Google has already blocked the vulnerable ports on vCenter server, which prevents any potential exploits of this vulnerability. 
  * In addition, Google ensures all future deployments of vCenter are not exposed to this vulnerability. 


#### What should I do?
No further action is required at this time.  | Critical | 

  
## GCP-2024-036
**Published:** 2024-06-18
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-26584

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-035
**Published:** 2024-06-12
**Updated:** 2024-07-18
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE and added a patch version for version 1.27 on Container-Optimized OS node pools. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26584

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-034
**Published:** 2024-06-11
**Updated:** 2024-07-10
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-10 Update:** Added patch versions for Container-Optimized OS nodes running minor version 1.26 and 1.27 and added patch versions for Ubuntu nodes. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2024-26583

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-033
**Published:** 2024-06-10
**Updated:** 2024-09-26
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-26 Update:** Added patch versions for GDC software for VMware. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes: 
  * CVE-2022-23222

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-032
**Published:** 2024-06-04
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2024-23326: Envoy incorrectly accepts HTTP 200 response for entering upgrade mode.
  * CVE-2024-32974: Crash in EnvoyQuicServerStream::OnInitialHeadersComplete().
  * CVE-2024-32975: Crash in QuicheDataReader::PeekVarInt62Length().
  * CVE-2024-32976: Endless loop while decompressing Brotli data with extra input.
  * CVE-2024-34362: Crash (use-after-free) in EnvoyQuicServerStream.
  * CVE-2024-34363: Crash due to uncaught nlohmann JSON exception.
  * CVE-2024-34364: Envoy OOM vector from HTTP async client with unbounded response buffer for mirror response.

For instructions and more details, see the Cloud Service Mesh security bulletin.  | High | 

  
## GCP-2024-031
**Published:** 2024-05-24
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability (CVE-2024-4323) has been discovered in Fluent Bit that could result in remote code execution. Fluent Bit versions 2.0.7 through 3.0.3 are affected. GKE, GKE on VMware, GKE on AWS, GKE on Azure, and GKE on Bare Metal don't use a vulnerable version of Fluent Bit and are **unaffected**. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| None  
## GCP-2024-030
**Published:** 2024-05-15
**Updated:** 2024-07-18
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-52620

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-029
**Published:** 2024-05-14
**Updated:** 2024-08-19
### Description
Description | Severity | Notes  
---|---|---  
**2024-08-19 Update:** Added patch versions for Ubuntu node pools on GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26642

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-028
**Published:** 2024-05-13
**Updated:** 2024-05-22
### Description
Description | Severity | Notes  
---|---|---  
**2024-05-22 Update:** Added patch versions for Ubuntu The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26581

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-027
**Published:** 2024-05-08
**Updated:** 2024-09-25
### Description
Description | Severity | Notes  
---|---|---  
**2024-09-25 Update:** Added patch versions for GDC software for VMware. **2024-05-15 Update:** Added patch versions for GKE Ubuntu node pools.  **2024-05-09 Update:** Corrected severity from Medium to High and clarified that GKE Autopilot clusters in the default configuration are not impacted. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26808

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-026
**Published:** 2024-05-07
**Updated:** 2024-08-06
### Description
Description | Severity | Notes  
---|---|---  
**2024-08-06 Update:** Added patch versions for Ubuntu node pools on GKE. **2024-05-09 Update:** Corrected severity from Medium to High. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26643

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-025
**Published:** 2024-04-26
### Description
Description | Severity | Notes  
---|---|---  
Looker fixed vulnerabilities reported by an external researcher via the Google and Alphabet Vulnerability Reward Program (VRP) program, but found no evidence of exploitation. These issues are now resolved and no user action is required for Looker-hosted customers on Looker (Google Cloud core) and Looker (original). Self-hosted Looker instances are advised to update to the latest supported version. **What should I do?** **Looker-hosted instances: Looker (Google Cloud core) and Looker (original) instances** No customer action is required. **Self-hosted Looker instances only** If your Looker instance is self-hosted, we recommend upgrading your Looker instances to one of the following versions:
  * 24.6.12+
  * 24.4.27+
  * 24.2.58+
  * 24.0.65+
  * 23.18.100+
  * 23.12.105+
  * 23.6.163+

**How was this fixed?** Google disabled direct administrative access to the internal database from the Looker application, removed elevated privileges that enabled cross-tenant access, and rotated the exposed secrets. Additionally, we have patched path traversal vulnerabilities that potentially exposed service account credentials. We are also conducting a thorough review of our code and systems to identify and address any similar potential vulnerabilities. | Critical  
## GCP-2024-024
**Published:** 2024-04-25
**Updated:** 2024-07-18
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-18 Update:** Added patch versions for Ubuntu node pools on GKE The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-26585

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-023
**Published:** 2024-04-24
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2024-27919: HTTP/2: memory exhaustion due to CONTINUATION frame flood.
  * CVE-2024-30255: HTTP/2: CPU exhaustion due to CONTINUATION frame flood
  * CVE-2024-32475: Abnormal termination when using 'auto_sni' with ':authority' header longer than 255 characters.
  * CVE-2023-45288: HTTP/2 CONTINUATION frames can be utilized for DoS attacks.

For instructions and more details, see the Cloud Service Mesh security bulletin.  | High | 

  
## GCP-2024-022
**Published:** 2024-04-03
**Updated:** 2024-07-17
### Description
Description | Severity | Notes  
---|---|---  
**2024-07-17 Update:** Added patch versions for GKE on VMware **2024-07-09 Update:** Added patch versions for GKE on Bare Metal **2024-04-24 Update:** Added patch versions for GKE. A Denial-of-Service (DoS) vulnerability (CVE-2023-45288) was recently discovered in multiple implementations of the HTTP/2 protocol, including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-021
**Published:** 2024-04-03
### Description
Description | Severity | Notes  
---|---|---  
Compute Engine is not affected by CVE-2024-3094, which affects versions 5.6.0 and 5.6.1 of the xz-utils package in the liblzma library, and could lead to compromise of the OpenSSH utility. For more details, see the Compute Engine security bulletin. | Medium  
## GCP-2024-020
**Published:** 2024-04-02
### Description
Description | Severity | Notes  
---|---|---  
Researchers discovered a vulnerability (CVE-2023-48022) in Ray. Ray is a third-party, open source tool for AI workloads. Because Ray does not require authentication, threat actors can achieve remote code execution through submitting jobs to publicly exposed instances. The vulnerability has been disputed by Anyscale, the developer of Ray. Ray maintains its functions are an intended, core product feature, and that security must instead be implemented outside of a Ray cluster, as any unintended network exposure of the Ray cluster could lead to compromise.  Based on the response, this CVE is disputed and may not show up in vulnerability scanners. Regardless, it is being actively exploited in the wild and users should configure their usage as suggested below.  **What should I do?** Follow Ray best practices and guidelines, including running trusted code on trusted networks, in order to secure your Ray workloads. Deployment of ray.io in customer cloud instances falls under the model of shared responsibility.  Google Kubernetes Engine (GKE) security has published a blog on hardening Ray on GKE.  For further information on ways to add authentication and authorization to Ray services, consult the Identity-Aware Proxy (IAP) documentation. GKE users can implement IAP following this guidance or by repurposing Terraform modules linked in the blog.  | High  
## GCP-2024-018
**Published:** 2024-03-12
**Updated:** 2024-04-04, 2024-05-06
### Description
Description | Severity | Notes  
---|---|---  
**2024-05-06 Update:** Added patch versions for GKE Ubuntu node pools. **2024-04-04 Update:** Corrected minimum versions for GKE Container-Optimized OS node pools. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-1085

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-017
**Published:** 2024-03-06
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-3611

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-016
**Published:** 2024-03-05
Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in VMSA-2024-0006 that impact ESXi components deployed in customer environments. 
#### Google Cloud VMware Engine impact
Your private clouds have been updated to address the security vulnerability. 
#### What should I do?
No action is needed on your part.  | Critical | 

  
## GCP-2024-014
**Published:** 2024-02-26
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-3776

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-013
**Published:** 2024-02-27
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-3610

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-012
**Published:** 2024-02-20
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2024-0193

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-011
**Published:** 2024-02-15
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes: 
  * CVE-2023-6932

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-010
**Published:** 2024-02-14
**Updated:** 2024-04-17
### Description
Description | Severity | Notes  
---|---|---  
**2024-04-17 Update:** Added patch versions for GKE on VMware. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-6931

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-009
**Published:** 2024-02-13
### Description
Description | Severity | Notes  
---|---|---  
On February 13, 2024, AMD disclosed two vulnerabilities affecting SEV-SNP on EPYC CPUs based on third generation "Milan" and fourth generation "Genoa" Zen cores. The vulnerabilities allow privileged attackers to access stale data from guests or cause a loss of guest integrity. Google has applied fixes to affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google. **What should I do?** No customer action is required. Fixes have already been applied to the Google server fleet for Google Cloud, including Compute Engine. For more information, see AMD security bulletin AMD-SN-3007. | Moderate | 

  
## GCP-2024-008
**Published:** 2024-02-12
### Description
Description | Severity | Notes  
---|---|---  
CVE-2023-5528 allows an attacker to create pods and persistent volumes on Windows nodes in a way that enables admin privilege escalation on those nodes. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-007
**Published:** 2024-02-08
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2024-23322: Envoy crashes when idle and requests per try timeout occur within the backoff interval.
  * CVE-2024-23323: Excessive CPU usage when URI template matcher is configured using regex.
  * CVE-2024-23324: External authorization can be bypassed when Proxy protocol filter sets invalid UTF-8 metadata.
  * Envoy crashes when using an address type that isn't supported by the OS.
  * CVE-2024-23327: Crash in proxy protocol when command type is `LOCAL`.

For instructions and more details, see the Cloud Service Meshsecurity bulletin.  | High | 

  
## GCP-2024-006
**Published:** 2024-02-5
### Description
Description | Severity | Notes  
---|---|---  
When an Apigee API Management proxy connects to a target endpoint or  target server, the proxy does not perform hostname validation for the certificate presented by the target endpoint or target server by default. If hostname validation is not enabled using one of the following options, Apigee proxies connecting to a target endpoint or target server may be at risk for a man-in-the-middle attack by an authorized user. For more information, see Configuring TLS from Edge to the backend (Cloud and Private Cloud).  Apigee proxy deployments on the following Apigee platforms are affected:
  * Apigee Edge for Public Cloud
  * Apigee Edge for Private Cloud

For instructions and more details, see the Apigee security bulletin. | High  
## GCP-2024-005
**Published:** 2024-01-31 **Updated:** 2024-04-02, 2024-05-06
### Description
Description | Severity | Notes  
---|---|---  
**2024-05-06 Update** : Added patch versions for GKE on AWS and GKE on Azure. **2024-04-02 Update** : Added patch versions for GKE on Bare Metal **2024-03-06 Update** : Added patch versions for GKE on VMware **2024-02-28 Update** : Added patch versions for Ubuntu **2024-02-15 Update** : Clarified that the 1.25 and 1.26 Ubuntu patch versions in the 2024-02-14 update might cause unhealthy nodes. **2024-02-14 Update** : Added patch versions for Ubuntu **2024-02-06 Update:** Added patch versions for Container-Optimized OS. A security vulnerability, CVE-2024-21626, has been discovered in `runc` where a user with permission to create Pods on Container-Optimized OS and Ubuntu nodes might be able to gain full access to the node filesystem. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-004
**Published:** 2024-01-24 **Updated:** 2024-02-07
### Description
Description | Severity | Notes  
---|---|---  
**2024-02-07 Update:** Added patch versions for Ubuntu. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-6817

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-003
**Published:** 2024-01-19 **Updated:** 2024-01-26
### Description
Description | Severity | Notes  
---|---|---  
**2024-01-26 Update:** Clarified the number of affected clusters and the actions that we took to help mitigate the impact. For details, see the GCP-2024-003 security bulletin. We have identified several clusters where users have granted Kubernetes privileges to the `system:authenticated` group, which includes all users with a Google account. These types of bindings are not recommended, as they violate the principle of least privilege and grant access to very large groups of users. See guidance under 'What should I do' for instructions on how to find these types of bindings. For instructions and more details, see the following bulletins:
  * GKE security bulletin

| Medium  
## GCP-2024-002
**Published:** 2024-01-17
**Updated:** 2024-02-20
### Description
Description | Severity | Notes  
---|---|---  
**2024-02-20 Update:** Added patch versions for GKE on VMware. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS nodes. 
  * CVE-2023-6111

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2024-001
**Published:** 2024-01-09 
### Description
Description | Severity | Notes  
---|---|---  
Several vulnerabilities were discovered in the TianoCore EDK II UEFI firmware. This firmware is used in Google Compute Engine VMs. If exploited, the vulnerabilities could allow a bypass of secure boot, which would provide false measurements in the secure boot process, including when used in Shielded VMs.
#### What should I do?
No action is required. Google has patched this vulnerability across Compute Engine and all VMs are protected from this vulnerability.
#### What vulnerabilities are addressed by this patch?
The patch mitigated the following vulnerabilities:
  * CVE-2022-36763
  * CVE-2022-36764
  * CVE-2022-36765

| Medium | 

  
## GCP-2023-051
**Published:** 2023-12-28
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-3609

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2023-050
**Published:** 2023-12-27
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-3389

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2023-049
**Published:** 2023-12-20
### Description
Description | Severity | Notes  
---|---|---  
The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-3090

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2023-048
**Published:** 2023-12-15
**Updated:** 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-3390

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2023-047
**Published:** 2023-12-14
### Description
Description | Severity | Notes  
---|---|---  
An attacker who has compromised the Fluent Bit logging container could combine that access with high privileges required by Cloud Service Mesh (on clusters that have enabled it) to escalate privileges in the cluster.  For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| Medium  
## GCP-2023-046
**Published:** 2023-11-22 **Updated:** 2024-03-04
### Description
Description | Severity | Notes  
---|---|---  
**2024-03-04 Update:** Added GKE versions for GKE on VMware. **2024-01-22 Update:** Added Ubuntu patch versions The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-5717

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * GKE on Bare Metal security bulletin

| High  
## GCP-2023-045
**Published:** 2023-11-20
**Updated:** 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-5197

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-044
**Published:** 2023-11-15
### Description
Description | Severity | Notes  
---|---|---  
On November 14, AMD disclosed multiple vulnerabilities that impact various AMD server CPUs. Specifically, the vulnerabilities impact EPYC Server CPUs leveraging Zen core generation 2 "Rome," gen 3 "Milan," and gen 4 "Genoa." Google has applied fixes to affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.  **What should I do?** No customer action is required. Fixes have already been applied to the Google server fleet for Google Cloud, including Google Compute Engine.  **What vulnerabilities are being addressed?** The patch mitigated the following vulnerabilities:
  * CVE-2022-23820
  * CVE-2021-46774
  * CVE-2023-20533
  * CVE-2023-20519
  * CVE-2023-20592
  * CVE-2023-20566
  * CVE-2023-20521
  * CVE-2021-46766
  * CVE-2022-23830
  * CVE-2023-20526
  * CVE-2021-26345

For more information, see AMD's security advisory AMD-SN-3005: "AMD INVD Instruction Security Notice", also published as CacheWarp, and AMD-SN-3002: "AMD Server Vulnerabilities – November 2023". | Moderate | 

  
## GCP-2023-043
**Published:** 2023-11-14
### Description
Description | Severity | Notes  
---|---|---  
Intel disclosed a CPU vulnerability in select processors. Google has taken steps to mitigate its server fleet, including Google Compute Engine for Google Cloud, and Chrome OS devices to ensure customers are protected. The vulnerability details:
  * CVE-2023-23583

**What should I do?** No customer action is required. The mitigation provided by Intel for the affected processors has been applied to the Google server fleet, including Google Compute Engine for Google Cloud. At this time, Google Distributed Cloud Edge requires an update from the OEM. Google will remediate this product once the update has been made available, and this bulletin will be updated accordingly. Chrome OS devices with the affected processors received the fix automatically as part of releases 119, 118, and 114 (LTS). **What vulnerabilities are being addressed?** CVE-2023-23583. For details, see Intel Security Advisory INTEL-SA-00950. | High  
## GCP-2023-042
**Published:** 2023-11-13 **Updated:** 2023-11-15
### Description
Description | Severity | Notes  
---|---|---  
**2023-11-15 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4147

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-041
**Published:** 2023-11-08
**Updated:** 2023-11-21, 2023-12-05, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-12-05 Update:** Added additional GKE versions for Container-Optimized OS node pools. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4004

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-040
**Published:** 2023-11-06
**Updated:** 2023-11-21, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4921

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-039
**Published:** 2023-11-06
**Updated:** 2023-11-21, 2023-11-16
### Description
Description | Severity | Notes  
---|---|---  
**2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. **2023-11-16 Update:** The vulnerability associated with this security bulletin is CVE-2023-4622. CVE-2023-4623 was incorrectly listed as the vulnerability in a previous version of the security bulletin. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4623

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-038
**Published:** 2023-11-06
**Updated:** 2023-11-21, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4623

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-037
**Published:** 2023-11-06
**Updated:** 2023-11-21, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4015

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-036
**Published:** 2023-10-30
### Description
Description | Severity | Notes  
---|---|---  
Deep Learning VM Images is a set of prepackaged virtual machine images with a deep learning framework that are ready to be run out of the box. Recently, an out-of-bounds write vulnerability was discovered in the `ReadHuffmanCodes()` function in the `libwebp` library. This might impact images that use this library. Google Cloud continuously scans its publicly published images and updates the packages to assure patched distros are included in the latest releases available for customer adoption. Deep Learning VM Images have been updated to ensure that the latest VM images include the patched distros. Customers adopting the latest VM images are not exposed to this vulnerability. **What should I do?** Google Cloud customers using published VM images should ensure that they are adopting the latest images and that their environments are up to date as per the shared responsibility model. CVE-2023-4863 could be exploited by an attacker to execute arbitrary code. This vulnerability was identified in Google Chrome prior to 116.0.5845.187 and in `libwebp` prior to 1.3.2 and is being listed under CVE-2023-4863. | High  
## GCP-2023-035
**Published:** 2023-10-26
**Updated:** 2023-11-21, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-4206
  * CVE-2023-4207
  * CVE-2023-4208
  * CVE-2023-4128

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-4206CVE-2023-4207, CVE-2023-4208, CVE-2023-4128  
## GCP-2023-034
**Published:** 2023-10-25
**Updated:** 2023-10-27
### Description
Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in VMSA-2023-0023 that impact vCenter components deployed in customer environments.
#### Cloud Customer Care impact
  * The vulnerability can be exploited by accessing specific ports in vCenter Server. These ports are not exposed to the public internet.
  * If your vCenter ports 2012/tcp, 2014/tcp, and 2020/tcp are not accessible by untrusted systems, then you are not exposed to this vulnerability.
  * Google has already blocked the vulnerable ports on vCenter server, preventing any potential exploit of this vulnerability.
  * In addition, Google will ensure all future deployments of vCenter server are not exposed to this vulnerability.
  * At the time of the bulletin, VMware is not aware of any exploitation "in the wild". For more details please refer to the VMware documentation for more information.


#### What should I do?
No further action is required at this time | Critical |  CVE-2023-34048,CVE-2023-34056  
## GCP-2023-033
**Published:** 2023-10-24
**Updated:** 2023-11-21, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted and GKE Sandbox workloads are not impacted. **2023-11-21 Update:** Clarify that only the listed minor versions need to upgrade to a corresponding patched version for GKE. The following vulnerabilities were discovered in the Linux kernel that can lead to a privilege escalation on Container-Optimized OS and Ubuntu nodes. 
  * CVE-2023-3777

For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-032
**Published:** 2023-10-13
**Updated:** 2023-11-03
### Description
Description | Severity | Notes  
---|---|---  
**2023-11-03 Update:** Added  known issue for Apigee Edge for Private Cloud.  A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the Apigee Ingress (Cloud Service Mesh) service used by Apigee X and Apigee Hybrid. The vulnerability could lead to a DoS of Apigee API management functionality.  For instructions and more details see the  Apigee security bulletin.  | High  
## GCP-2023-031
**Published:** 2023-10-10
### Description
Description | Severity | Notes  
---|---|---  
A denial of service attack can affect the data plane when using the HTTP/2 protocol. For instructions and more details, see the Cloud Service Mesh security bulletin.  | High  
## GCP-2023-030
**Published:** 2023-10-10
**Updated:** 2024-03-20
### Description
Description | Severity | Notes  
---|---|---  
**2024-03-20 Update:** Added patch versions for GKE on AWS and GKE on Azure with the latest patches for CVE-2023-44487. **2024-02-14 Update:** Added patch versions for GKE on VMware. **2023-11-09 Update:** Added CVE-2023-39325. Updated GKE versions with the latest patches for CVE-2023-44487 and CVE-2023-39325.  A Denial-of-Service (DoS) vulnerability was recently discovered in multiple implementations of the HTTP/2 protocol (CVE-2023-44487), including the golang HTTP server used by Kubernetes. The vulnerability could lead to a DoS of the Google Kubernetes Engine (GKE) control plane. GKE clusters with authorized networks configured are protected by limiting network access, but all other clusters are affected. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-44487, CVE-2023-39325  
## GCP-2023-029
**Published:** 2023-10-03
### Description
Description | Severity | Notes  
---|---|---  
TorchServe is used to host PyTorch machine learning models for online prediction. Vertex AI provides prebuilt PyTorch model serving containers which depend on TorchServe. Vulnerabilities were recently discovered in TorchServe which would allow an attacker to take control of a TorchServe deployment if its model management API is exposed. Customers with PyTorch models deployed to Vertex AI online prediction are not affected by these vulnerabilities, since Vertex AI does not expose TorchServe's model management API. Customers using TorchServe outside of Vertex AI should take precautions to ensure their deployments are set up securely. **What should I do?** Vertex AI customers with deployed models using Vertex AI's prebuilt PyTorch serving containers do not need to take any action to address the vulnerabilities, since Vertex AI's deployments do not expose TorchServe's management server to the internet. Customers who are using the prebuilt PyTorch containers in other contexts, or who are using a custom-built or third-party distribution of TorchServe, should do the following:
  * Ensure that TorchServe's model management API is not exposed to the internet. The model management API can be restricted to local access only by ensuring that the is bound to `127.0.0.1`.
  * Use the setting to ensure that models can be loaded from intended sources only. 
  * Upgrade TorchServe to version 0.8.2, which includes mitigations for this issue, as soon as possible. As a precaution, Vertex AI will release fixed prebuilt containers by 2023-10-13.

**What vulnerabilities are being addressed?** TorchServe's management API is bound to `0.0.0.0` by default in most TorchServe Docker images, including those released by Vertex AI, making it accessible to external requests. The default IP address for the management API is changed to `127.0.0.1` in TorchServe 0.8.2, mitigating this issue. CVE-2023-43654 and CVE-2022-1471 allow a user with access to the management API to load models from arbitrary sources and remotely execute code. Mitigations for both of these issues are included in TorchServe 0.8.2: the remote code execution path is removed, and a warning is emitted if the default value for `allowed_urls` is used. | High |  CVE-2023-43654, CVE-2022-1471  
## GCP-2023-028
**Published:** 2023-09-19
**Updated:** 2024-05-29
### Description
Description | Severity | Notes  
---|---|---  
**2024-05-29 Update** : The new feeds no longer use the shared service account, but it remains active for existing feeds to avoid service disruptions. Changes to the source in older feeds are blocked to prevent misuse of the shared service account. Customers can continue using their old feeds normally, as long as they don't change the source.  Customers can configure Google Security Operations to ingest data from customer-owned Cloud Storage buckets using an ingestion feed. Until recently, Google Security Operations provided a shared service account that customers used to grant permission to the bucket. An opportunity existed such that one customer's Google Security Operations instance could be configured to ingest data from another customer's Cloud Storage bucket. After performing an impact analysis, we found no current or prior exploitation of this vulnerability. The vulnerability was present in all versions of Google Security Operations prior to Sept 19, 2023.  **What should I do?** As of Sept 19, 2023, Google Security Operations has been updated to address this vulnerability. No customer action is required. **What vulnerabilities are being addressed?** Previously, Google Security Operations provided a shared service account that customers used to grant permission to a bucket. Because different customers gave the same Google Security Operations service account permission to their bucket, an exploitation vector existed that allowed one customer's feed to access a different customer's bucket when a feed was being created or modified. This exploitation vector required knowledge of the bucket URI. Now, during feed creation or modification, Google Security Operations uses unique service accounts for each customer. | High  
## GCP-2023-027
**Published:** 2023-09-11 
Description | Severity | Notes  
---|---|---  
VMware vCenter Server updates address multiple memory corruption vulnerabilities (CVE-2023-20892, CVE-2023-20893, CVE-2023-20894, CVE-2023-20895, CVE-2023-20896)
#### Customer Care impact
VMware vCenter Server (vCenter Server) and VMware Cloud Foundation (Cloud Foundation).
#### What should I do?
Customers are not impacted and no action needs to be taken. | Medium | 

  
## GCP-2023-026
**Published:** 2023-09-06
### Description
Description | Severity | Notes  
---|---|---  
Three vulnerabilities (CVE-2023-3676, CVE-2023-3955, CVE-2023-3893) have been discovered in Kubernetes where a user that can create Pods on Windows nodes may be able to escalate to admin privileges on those nodes. These vulnerabilities affect the Windows versions of Kubelet and the Kubernetes CSI proxy. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-3676, CVE-2023-3955,  CVE-2023-3893  
## GCP-2023-025
**Published:** 2023-08-08 
Description | Severity | Notes  
---|---|---  
Intel recently announced Intel Security Advisory INTEL-SA-00828 impacting some of their processor families. You are encouraged to assess your risks based on the advisory.
#### Google Cloud VMware Engine impact
Our fleet utilizes the impacted processor families. In our deployment, the entire server is dedicated to one customer. Hence, our deployment model doesn't add any additional risk to your assessment of this vulnerability. We are working with our partners to obtain necessary patches and will be deploying these patches on priority across the fleet using the standard upgrade process in the next several weeks.
#### What should I do?
No action is needed on your part, we are working on upgrading all the impacted systems. | High | 

  
## GCP-2023-024
**Published:** 2023-08-08
**Updated:** 2023-08-10, 2024-06-04
### Description
Description | Severity | Notes  
---|---|---  
**2024-06-04 Update:** The following missing products have now been updated to fix this vulnerability: 
  * Google Distributed Cloud Hosted
  * Google Distributed Cloud Edge

**2023-08-10 Update:** Added ChromeOS LTS version number.  Intel disclosed a vulnerability in select processors (CVE-2022-40982). Google has taken steps to mitigate its server fleet, including Google Cloud, to ensure customers are protected.  The vulnerability details:
  * CVE-2022-40982 (Intel IPU 2023.3, "GDS" aka "Downfall")

**What should I do?** No customer action is required. All available patches have already been applied to the Google server fleet for Google Cloud, including Google Compute Engine.  At this time, the following products require additional updates from partners and vendors. 
  * Google Cloud VMware Engine
  * Google Distributed Cloud Hosted
  * Google Distributed Cloud Edge
  * Google Cloud Bare Metal Solution
  * Evolved Packet Core

Google will remediate these products once these patches have been made available, and this bulletin will be updated accordingly.  Google Chromebook and ChromeOS Flex customers automatically received the Intel provided mitigations in Stable (115), LTS (108), Beta (116), and LTC (114). Chromebook and ChromeOS Flex customers pinned to an older release should consider unpinning and moving to Stable or LTS releases to ensure they receive this and other vulnerability fixes.  **What vulnerabilities are being addressed?** CVE-2022-40982 - For more information, see Intel Security Advisory INTEL-SA-00828.  | High  
## GCP-2023-023
**Published:** 2023-08-08
### Description
Description | Severity | Notes  
---|---|---  
AMD disclosed a vulnerability in select processors (CVE-2023-20569). Google has taken steps to mitigate its server fleet, including Google Cloud, to ensure customers are protected.  The vulnerability details:
  * CVE-2023-20569 (AMD SB-7005 aka "Inception")

**What should I do?** Users of Compute Engine VMs should consider OS provided mitigations if using intra-instance untrusted code execution. We recommend customers to contact their OS vendors for more specific guidance.  Fixes have already been applied to the Google server fleet for Google Cloud, including Google Compute Engine.  **What vulnerabilities are being addressed?** CVE-2023-20569 - For more information, see AMD SB-7005.  | Moderate  
## GCP-2023-022
**Published:** 2023-08-03
### Description
Description | Severity | Notes  
---|---|---  
Google identified a vulnerability in gRPC C++ Implementations prior to the 1.57 release. This was a Denial-of-Service vulnerability within the gRPC's C++ implementation. These have been fixed in the 1.53.2, 1.54.3, 1.55.2, 1.56.2, and 1.57 releases. **What should I do?** Ensure that you're using the latest versions of the following software packages:
  * gRPC (C++, Python, Ruby) versions 1.53, 1.54, 1.55, and 1.56 need to upgrade to the following patch releases:
    * 1.53.2
    * 1.54.3
    * 1.55.2
    * 1.56.2
  * gRPC (C++, Python, Ruby) versions 1.52 and earlier need to upgrade to one of the approved patch releases. For example, 1.53.2, 1.54.3, 1.53.4, etc.

**What vulnerabilities are being addressed?** These patches mitigate the following vulnerabilities:
  * Denial-Of-Service vulnerability in gRPC C++ implementations: Specially crafted requests can cause a termination of connection between a proxy and a backend.

| High  
## GCP-2023-021
**Updated:** 2023-07-26
**Published:** 2023-07-25
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2023-35941: A malicious client is able to construct credentials with permanent validity in some specific scenarios. For example, the combination of host and expiration time in the HMAC payload can be always valid in OAuth2 filter's HMAC check.
  * CVE-2023-35942: gRPC access loggers using the listener's global scope can cause a use-after-free crash when the listener is drained. This can be triggered by an LDS update with the same gRPC access log configuration.
  * CVE-2023-35943: If `origin` header is configured to be removed with `request_headers_to_remove: origin`, CORS filter will `segfault` and crash Envoy.
  * CVE-2023-35944: Attackers can send mixed scheme requests to bypass scheme checks in Envoy. For example, if a request with mixed scheme HTTP is sent to the OAuth2 filter, it will fail the exact-match checks for HTTP, and inform the remote endpoint the scheme is HTTPS, thus potentially bypassing OAuth2 checks specific to HTTP requests.

For instructions and more details, see the Cloud Service Mesh security bulletin.  | High | 

  
## GCP-2023-020
**Updated:** 2023-07-26
**Published:** 2023-07-24
### Description
Description | Severity | Notes  
---|---|---  
AMD has released a microcode update that addresses a hardware security vulnerability (CVE-2023-20593). Google has applied the necessary fixes for this vulnerability to its server fleet, including servers for the Google Cloud Platform. Testing indicates there is no impact to the performance of systems. **What should I do?** No customer action is required, as fixes have already been applied to the Google server fleet for Google Cloud Platform. **What vulnerabilities are being addressed?** CVE-2023-20593 addresses a vulnerability in some AMD CPUs. More information can be found here. | High  
## GCP-2023-019
**Published:** 2023-07-18
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability (CVE-2023-35945) has been discovered in Envoy where a specifically crafted response from an untrusted upstream service can cause a denial of service through memory exhaustion. This is caused by Envoy's HTTP/2 codec which may leak a header map and bookkeeping structures upon receiving `RST_STREAM` immediately followed by the `GOAWAY` frames from an upstream server. For instructions and more details, see the Cloud Service Mesh security bulletin.  | High  
## GCP-2023-018
**Published:** 2023-06-27
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability (CVE-2023-2235) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE Autopilot clusters are affected as GKE Autopilot nodes always use Container-Optimized OS node images. GKE Standard clusters with versions 1.25 or later that are running Container-Optimized OS node images are affected. GKE clusters are not affected if they are running only Ubuntu node images, or running versions before 1.25, or using GKE Sandbox. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-017
**Published:** 2023-06-26
**Updated:** 2023-07-11
### Description
Description | Severity | Notes  
---|---|---  
**2023-07-11 Update:** New GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-31436. A new vulnerability (CVE-2023-31436) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. GKE clusters, including Autopilot clusters, are affected. GKE clusters using GKE Sandbox are not affected. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-016
**Published:** 2023-06-26
### Description
Description | Severity | Notes  
---|---|---  
A number of vulnerabilities have been discovered in Envoy, which is used in Cloud Service Mesh that allow a malicious attacker to cause a denial of service or crash Envoy. These were reported separately as GCP-2023-002.  For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-27496, CVE-2023-27488, CVE-2023-27493, CVE-2023-27492, CVE-2023-27491, CVE-2023-27487  
## GCP-2023-015
**Published:** 2023-06-20
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability, CVE-2023-0468, has been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges to root when io_poll_get_ownership will keep increasing req->poll_refs on every io_poll_wake then overflow to 0 which will fput req->file twice and cause a struct file refcount issue. GKE clusters, including Autopilot clusters, with Container-Optimized OS using Linux Kernel version 5.15 are affected. GKE clusters using Ubuntu images or using GKE Sandbox are unaffected. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium  
## GCP-2023-014
**Updated:** 2023-08-11 **Published:** 2023-06-15
### Description
Description | Severity | Notes  
---|---|---  
**2023-08-11 Update:** Added patch versions for GKE on VMware, GKE on AWS, GKE on Azure, and Google Distributed Cloud Virtual for Bare Metal. Two new security issues were discovered in Kubernetes where users may be able to launch containers that bypass policy restrictions when using ephemeral containers and either ImagePolicyWebhook (CVE-2023-2727) or the ServiceAccount admission plugin (CVE-2023-2728). For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium |  CVE-2023-2727, CVE-2023-2728  
## GCP-2023-013
**Published:** 2023-06-08
### Description
Description | Severity | Notes  
---|---|---  
When you enable the Cloud Build API in a project, Cloud Build automatically creates a default service account to execute builds on your behalf. This Cloud Build service account previously had the `logging.privateLogEntries.list` IAM permission, which allowed builds to have access to list private logs by default. This permission has now been revoked from the Cloud Build service account to adhere to the security principle of least privilege. For instructions and more details, see the Cloud Build security bulletin. | Low  
## GCP-2023-010
**Published:** 2023-06-07
### Description
Description | Severity | Notes  
---|---|---  
Google identified three new vulnerabilities in the gRPC C ++ implementation. These will be published soon publicly as CVE-2023-1428, CVE-2023-32731 and CVE-2023-32732. In April, we identified two vulnerabilities in 1.53 and 1.54 releases. One was a Denial-of-Service vulnerability within the gRPC's C++ implementation and the other was a remote data exfiltration vulnerability. These have been fixed in 1.53.1, 1.54.2 and later releases. Previously in March, our internal teams discovered a Denial-of-Service vulnerability within the gRPC's C++ implementation while performing routine fuzzing activities. It was found in the gRPC 1.52 release, and has been fixed in the 1.52.2 and 1.53 releases.
#### What should I do?
Ensure that you're using the latest versions of the following software packages:
  * grpc (C++, Python, Ruby) version 1.52, 1.53, and 1.54 need to upgrade to the following patch releases;
    * 1.52.2 
    * 1.53.1 
    * 1.54.2 
  * grpc (C++, Python, Ruby) version 1.51 and earlier are not affected, so users with these versions can take no action


#### What vulnerabilities are addressed by these patches?
These patches mitigate the following vulnerabilities:
  * 1.53.1, 1.54.2 and later releases address the following: Denial-Of-Service vulnerability in gRPC C++ implementation. Specially crafted requests can cause a termination of connection between a proxy and a backend. Remote data exfiltration vulnerability: Desynchronisation in the HPACK table due to header size limitations can lead to proxy backends leaking header data from other clients connected to a proxy. 
  * 1.52.2, 1.53, and later releases address the following: Denial-of-Service vulnerability within the gRPC's C++ implementation. Parsing some specifically formed requests can lead to a crash impacting a server. 

We recommend upgrading to the latest versions of the following software packages as listed above. | High (CVE-2023-1428, CVE-2023-32731). Medium (CVE-2023-32732) |  CVE-2023-1428,  CVE-2023-32731,  CVE-023-32732  
## GCP-2023-009
**Published:** 2023-06-06
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability (CVE-2023-2878) has been discovered in the secrets-store-csi-driver where an actor with access to the driver logs could observe service account tokens. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| None  
## GCP-2023-008
**Published:** 2023-06-05
### Description
Description | Severity | Notes  
---|---|---  
A new vulnerability (CVE-2023-1872) has been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2023-007
**Published:** 2023-06-02
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability was recently discovered in Cloud SQL for SQL Server that allowed customer administrator accounts to create triggers in the `tempdb` database and use those to gain `sysadmin` privileges in the instance. The `sysadmin` privileges would give the attacker access to system databases and partial access to the machine running that SQL Server instance. Google Cloud resolved the issue by patching the security vulnerability by March 1, 2023. Google Cloud didn't find any compromised customer instances. For instructions and more details, see the Cloud SQL security bulletin. | High  
## GCP-2023-005
**Published:** 2023-05-18
**Updated:** 2023-06-06
### Description
Description | Severity | Notes  
---|---|---  
**2023-06-06 Update:** New GKE versions have been updated to include the latest Ubuntu versions that patch CVE-2023-1281 and CVE-2023-1829. Two new vulnerabilities (CVE-2023-1281, CVE-2023-1829) have been discovered in the Linux kernel that can lead to a privilege escalation to root on the node. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-1281 CVE-2023-1829  
## GCP-2023-004
**Published:** 2023-04-26
### Description
Description | Severity | Notes  
---|---|---  
Two vulnerabilities (CVE-2023-1017 and CVE-2023-1018) were discovered in Trusted Platform Module (TPM) 2.0. The vulnerabilities could have allowed a sophisticated attacker to exploit a 2-byte out of bounds read/write on certain Compute Engine VMs. For instructions and more details, see the Compute Engine security bulletin. | Medium | 

  
## GCP-2023-003
**Published:** 2023-04-11
**Updated:** 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. Two new vulnerabilities, CVE-2023-0240 and CVE-2023-23586, have been discovered in the Linux kernel that could allow an unprivileged user to escalate privileges. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2023-0240, CVE-2023-23586  
## GCP-2023-002
### Description
Description | Severity | Notes  
---|---|---  
The following CVEs expose Cloud Service Mesh to exploitable vulnerabilities:
  * CVE-2023-27496: If Envoy is running with the OAuth filter enabled exposed, a malicious actor could construct a request which would cause denial of service by crashing Envoy.
  * CVE-2023-27488: The attacker can use this vulnerability to bypass auth checks when ext_authz is used.
  * CVE-2023-27493: Envoy configuration must also include an option to add request headers that were generated using inputs from the request, such as the peer certificate SAN.
  * CVE-2023-27492: Attackers can send large request bodies for routes that have Lua filter enabled and trigger crashes.
  * CVE-2023-27491: Attackers can send specifically crafted HTTP/2 or HTTP/3 requests to trigger parsing errors on HTTP/1 upstream service.
  * CVE-2023-27487: The header `x-envoy-original-path` should be an internal header, but Envoy does not remove this header from the request at the beginning of request processing when it is sent from an untrusted client.

For instructions and more details, see the Cloud Service Mesh security bulletin.:  | High | 

  
## GCP-2023-001
**Published:** 2023-03-01, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. A new vulnerability (CVE-2022-4696) has been discovered in the Linux kernel that can lead to a privilege escalation on the node. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-026
**Published:** 2023-01-11
### Description
Description | Severity | Notes  
---|---|---  
Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium | 

  
## GCP-2022-025
**Published:** 2022-12-21 **Updated:** 2023-01-19, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-01-19 Update:** Added information that GKE version 1.21.14-gke.14100 is available. Two new vulnerabilities (CVE-2022-3786 and CVE-2022-3602) have been discovered in OpenSSL v3.0.6 that can potentially cause a crash. For instructions and more details, see the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium | 

  
## GCP-2022-024
**Published:** 2022-11-09 
**Updated:** 2023-01-19
### Description
Description | Severity | Notes  
---|---|---  
**2023-01-19 Update:** Added information that GKE version 1.21.14-gke.14100 is available. **2022-12-16 Update:** Added patch versions for GKE and GKE on VMware.  Two new vulnerabilities (CVE-2022-2585 and CVE-2022-2588) have been discovered in the Linux kernel that can lead to a full container break out to root on the node. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High | 

  
## GCP-2022-023
**Published:** 2022-11-04
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability, CVE-2022-39278, has been discovered in Istio, which is used in Cloud Service Mesh, that allows a malicious attacker to crash the control plane. For instructions and more details, see the following bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-022
**Published:** 2022-10-28
**Updated:** 2022-12-14
### Description
Description | Severity | Notes  
---|---|---  
**2022-12-14 Update:** Added patch versions for GKE and GKE on VMware.  A new vulnerability, CVE-2022-20409, has been discovered in the Linux kernel that could allow an unprivileged user to escalate to system execution privilege.  For instructions and more details, see the following bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-021
**Published:** 2022-10-27
**Updated:** 2023-01-19, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2023-01-19 Update:** Added information that GKE version 1.21.14-gke.14100 is available. **2022-12-15 Update:** Updated information that version 1.21.14-gke.9400 of Google Kubernetes Engine is pending rollout and may be superseded by a higher version number.  **2022-11-22 Update:** Added patch versions for GKE on VMware, GKE on AWS, and GKE on Azure.  A new vulnerability, CVE-2022-3176, has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve full container breakout to root on the node. For instructions and more details, see the following bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-020
**Published:** 2022-10-05
**Updated:** 2022-10-12
### Description
Description | Severity | Notes  
---|---|---  
The Istio control plane `istiod` is vulnerable to a request processing error, allowing a malicious attacker that sends a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017, but does not require any authentication from the attacker. For instructions and more details, see the Cloud Service Mesh security bulletin. | High  
## GCP-2022-019
**Published:** 2022-09-22
### Description
Description | Severity | Notes  
---|---|---  
A message parsing and memory management vulnerability in ProtocolBuffer’s C++ and Python implementations can trigger an out of memory (OOM) failure when processing a specially crafted message. This could lead to a denial of service (DoS) on services using the libraries. 
#### What should I do?
Ensure that you're using the latest versions of the following software packages: 
  * protobuf-cpp (3.18.3, 3.19.5, 3.20.2, 3.21.6)
  * protobuf-python (3.18.3, 3.19.5, 3.20.2, 4.21.6)


#### What vulnerabilities are addressed by this patch?
The patch mitigates the following vulnerability: A specially constructed small message that causes the running service to allocate large amounts of RAM. The small size of the request means that it is easy to take advantage of the vulnerability and exhaust resources. C++ and Python systems that consume untrusted protobufs would be vulnerable to DoS attacks if they contain a `MessageSet` object in their RPC request.  | Medium  
## GCP-2022-018
**Published:** 2022-08-01
**Updated:** 2022-09-14, 2023-12-21
### Description
Description | Severity | Notes  
---|---|---  
**2023-12-21 Update:** Clarify that GKE Autopilot clusters in the default configuration are not impacted. **2022-09-14 Update:** Added patch versions for GKE on VMware, GKE on AWS, and GKE on Azure.  A new vulnerability (CVE-2022-2327) has been discovered in the Linux kernel that can lead to local privilege escalation. This vulnerability allows an unprivileged user to achieve a full container breakout to root on the node. For instructions and more details, see the following bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-017
**Published:** 2022-06-29 **Updated:** 2022-11-22
### Description
Description | Severity | Notes  
---|---|---  
**2022-11-22 Update:** Workloads using GKE Sandbox are not affected by these vulnerabilities. **2022-07-21 Update:** additional information on GKE on VMware. A new vulnerability (CVE-2022-1786) has been discovered in the Linux kernel versions 5.10 and 5.11. This vulnerability allows an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. Only clusters that run Container-Optimized OS are affected. GKE Ubuntu versions use either version 5.4 or 5.15 of the kernel and are not affected. For instructions and more details, see the:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-016
**Published:** 2022-06-23 **Updated:** 2022-11-22
### Description
Description | Severity | Notes  
---|---|---  
**2022-11-22 Update:** Autopilot clusters are not affected by by CVE-2022-29581 but are vulnerable to CVE-2022-29582 and CVE-2022-1116. Three new memory corruption vulnerabilities (CVE-2022-29581, CVE-2022-29582, CVE-2022-1116) have been discovered in the Linux kernel. These vulnerabilities allow an unprivileged user with local access to the cluster to achieve a full container breakout to root on the node. All Linux clusters (Container-Optimized OS and Ubuntu) are affected. For instructions and more details, refer to the following bulletins:
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High | 

  
## GCP-2022-015
**Published:** 2022-06-09 **Updated:** 2022-06-10
### Description
Description | Severity | Notes  
---|---|---  
**2022-06-10 Update:** The Cloud Service Mesh versions have been updated. For instructions and more details, see the Cloud Service Mesh security bulletin.  The following Envoy and Istio CVEs expose Cloud Service Mesh and Istio on GKE to remotely exploitable vulnerabilities:
  * CVE-2022-31045: Istio data plane can potentially access memory unsafely when the Metadata Exchange and Stats extensions are enabled.
  * CVE-2022-29225: Data can exceed intermediate buffer limits if a malicious attacker passes a small highly compressed payload (zip bomb attack).
  * CVE-2021-29224: Potential null pointer dereference in GrpcHealthCheckerImpl.
  * CVE-2021-29226: OAuth filter allows trivial bypass.
  * CVE-2022-29228: OAuth filter can corrupt memory (earlier versions) or trigger an ASSERT() (later versions).
  * CVE-2022-29227: Internal redirects crash for requests with body or trailers.

For instructions and more details, see the Cloud Service Mesh security bulletin.  | Critical | 

  
## GCP-2022-014
**Published:** 2022-04-26 **Updated:** 2022-11-22
### Description
Description | Severity | Notes  
---|---|---  
**2022-11-22 Update:** GKE Autopilot clusters and workloads running in GKE Sandbox are unaffected. **2022-05-12 Update:** The GKE on AWS and GKE on Azure versions have been updated. For instructions and more details, see the: 
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

Two security vulnerabilities, CVE-2022-1055 and CVE-2022-27666 have been discovered in the Linux kernel. Each can lead to a local attacker being able to perform a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all GKE node operating systems (Container-Optimized OS and Ubuntu). For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High |  CVE-2022-1055 CVE-2022-27666  
## GCP-2022-013
**Published:** 2022-04-11 **Updated:** 2022-04-22
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability, CVE-2022-23648, has been discovered in containerd's handling of path traversal in the OCI image volume specification. Containers launched through containerd's CRI implementation with a specially-crafted image configuration could gain full read access to arbitrary files and directories on the host. This vulnerability may bypass any policy-based enforcement on container setup (including a Kubernetes Pod Security Policy). For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium  
## GCP-2022-012
**Published:** 2022-04-07 **Updated:** 2022-11-22
### Description
Description | Severity | Notes  
---|---|---  
**2022-11-22 Update:** For GKE clusters in both modes, Standard and Autopilot, workloads using GKE Sandbox are unaffected. A security vulnerability, CVE-2022-0847, has been discovered in the Linux kernel version 5.8 and later that can potentially escalate container privileges to root. This vulnerability affects the following products:
  * GKE node pool versions 1.22 and later that use Container-Optimized OS images (Container-Optimized OS 93 and later)
  * GKE on VMware v1.10 for Container-Optimized OS images
  * GKE on AWS v1.21 and GKE on AWS (previous generation) v1.19, v1.20, v1.21, which use Ubuntu
  * Managed clusters of GKE on Azure v1.21 which use Ubuntu

For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2022-011
**Published:** 2022-03-22 **Updated:** 2022-08-11
### Description
Description | Severity  
---|---  
**Update 2022-08-11:** Added more information about the Simultaneous Multi-Threading (SMT) configuration. SMT was intended to be disabled, but was enabled on the versions listed.  If you manually enabled SMT for a sandboxed node pool, SMT will remain manually enabled despite this issue. There is a misconfiguration with Simultaneous Multi-Threading (SMT), also known as Hyper-threading, on GKE Sandbox images. The misconfiguration leaves nodes potentially exposed to side channel attacks such as Microarchitectural Data Sampling (MDS) (for more context, see GKE Sandbox documentation). We do not recommend using the following affected versions: 
  * 1.22.4-gke.1501
  * 1.22.6-gke.300
  * 1.23.2-gke.300
  * 1.23.3-gke.600

For instructions and more details, see the: GKE security bulletin. | Medium  
## GCP-2022-010
### Description
Description | Severity | Notes  
---|---|---  
The following Istio CVE exposes Cloud Service Mesh to a remotely exploitable vulnerability:
  * CVE-2022-24726: The Istio control plane, `istiod`, is vulnerable to a request processing error, allowing a malicious attacker that sends a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017 but does not require any authentication from the attacker.

For instructions and more details, see the following security bulletin: 
  * Cloud Service Mesh security bulletin.

| High | 

  
## GCP-2022-009
**Published:** 2022-03-01 
### Description
Description | Severity  
---|---  
Some unexpected paths to access the node VM on GKE Autopilot clusters could have been used to escalate privileges in the cluster. These issues have been fixed and **no further action is required**. The fixes address issues reported through our Vulnerability Reward Program. For instructions and more details, see the GKE security bulletin | Low  
## GCP-2022-008
**Published:** 2022-02-23 **Updated:** 2022-04-28
### Description
Description | Severity | Notes  
---|---|---  
**2022-04-28 Update:** Added versions of GKE on VMware that fix these vulnerabilities. For details, see the GKE on VMware security bulletin. The Envoy project recently discovered a set of vulnerabilities. All issues listed below are fixed in Envoy release 1.21.1. 
  * CVE-2022-23606: When a cluster is deleted via Cluster Discovery Service (CDS) all idle connections established to endpoints in that cluster are disconnected. A recursion was erroneously introduced in Envoy version 1.19 to the procedure of disconnecting idle connections that can lead to stack exhaustion and abnormal process termination when a cluster has a large number of idle connections.
  * CVE-2022-21655: Envoy's internal redirect code assumes that a route entry exists. When an internal redirect is done to a route which has a direct response entry and no route entry, it results in dereferencing a null pointer and crashing.
  * CVE-2021-43826: When Envoy is configured to use tcp_proxy which uses upstream tunneling (over HTTP), and downstream TLS termination, Envoy will crash if the downstream client disconnects during the TLS handshake while the upstream HTTP stream is still being established. The downstream disconnect can be either client or server initiated. The client can disconnect for any reason. The server may disconnect if, for example, it has no TLS ciphers or TLS protocol versions compatible with the client. It may be possible to trigger this crash in other downstream configurations as well.
  * CVE-2021-43825: Sending a locally generated response must stop further processing of request or response data. Envoy tracks the amount of buffered request and response data and aborts the request if the amount of buffered data is over the limit by sending 413 or 500 responses. However when locally generated response is sent because of the internal buffer overflows while response is processed by the filter chain the operation may not be aborted correctly and result in accessing a freed memory block.
  * CVE-2021-43824: Envoy crashes when using the JWT filter with a "safe_regex" match rule and a specially crafted request like "CONNECT host:port HTTP/1.1". When reaching the JWT filter, a "safe_regex" rule should evaluate the URL path but there is none here, and Envoy crashes with segfaults.
  * CVE-2022-21654: Envoy would incorrectly allow TLS session resumption after mTLS validation settings had been reconfigured. If a client certificate was allowed with the old configuration but disallowed with the new configuration, the client could resume the previous TLS session even though the current configuration should disallow it. Changes to the following settings are affected: 
    * match_subject_alt_names
    * CRL changes
    * allow_expired_certificate
    * Trust_chain_verification
    * only_verify_leaf_cert_crl
  * CVE-2022-21657: Envoy does not restrict the set of certificates it accepts from the peer, either as a TLS client or a TLS server, to only those certificates that contain the necessary extendedKeyUsage (id-kp-serverAuth and id-kp-clientAuth, respectively). This means that a peer may present an e-mail certificate (e.g. id-kp-emailProtection), either as a leaf certificate or as a CA in the chain, and it will be accepted for TLS. This is particularly bad when combined with CVE-2022-21656 , in that it allows a Web PKI CA that is intended only for use with S/MIME, and thus exempted from audit or supervision, to issue TLS certificates that will be accepted by Envoy.
  * CVE-2022-21656: The validator implementation used to implement the default certificate validation routines has a "type confusion" bug when processing subjectAltNames. This processing allows, for example, an rfc822Name or uniformResourceIndicator to be authenticated as a domain name. This confusion allows for the bypassing of nameConstraints, as processed by the underlying OpenSSL/BoringSSL implementation, exposing the possibility of impersonation of arbitrary servers.

For detailed instructions regarding specific products, see the following security bulletins: 
  * Cloud Service Mesh security bulletin


  * Istio on GKE security bulletin


  * Google Distributed Cloud Virtual for Bare Metal

**What should I do?** Envoy users managing their own Envoys should ensure that they are using Envoy release 1.21.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which Google Cloud products will switch to 1.21.1.  | High |  CVE-2022-23606 CVE-2022-21655 CVE-2021-43826 CVE-2021-43825 CVE-2021-43824 CVE-2022-21654 CVE-2022-21657 CVE-2022-21656  
## GCP-2022-007
**Published:** 2022-02-22 
### Description
Description | Severity | Notes  
---|---|---  
The following Envoy and Istio CVEs expose Cloud Service Mesh and Istio on GKE to remotely exploitable vulnerabilities:
  * CVE-2022-23635: Istiod crashes upon receiving requests with a specially crafted `authorization` header.
  * CVE-2021-43824: Potential null pointer dereference when using JWT filter `safe_regex` match
  * CVE-2021-43825: Use-after-free when response filters increase response data, and increased data exceeds downstream buffer limits.
  * CVE-2021-43826: Use-after-free when tunneling TCP over HTTP, if downstream disconnects during upstream connection establishment.
  * CVE-2022-21654: Incorrect configuration handling allows mTLS session re-use without re-validation after validation settings have changed.
  * CVE-2022-21655: Incorrect handling of internal redirects to routes with a direct response entry.
  * CVE-2022-23606: Stack exhaustion when a cluster is deleted via Cluster Discovery Service.

For instructions and more details, see the following security bulletins: 
  * Cloud Service Mesh security bulletin.
  * Istio on GKE security bulletin.

| High | 

  
## GCP-2022-006
**Published:** 2022-02-14 **Updated:** 2022-05-16 
### Description
Description | Severity | Notes  
---|---|---  
**2022-05-16 Update:** Added GKE version 1.19.16-gke.7800 or later to the list of versions that have code to fix this vulnerability. For details, see the GKE security bulletin. **2022-05-12 Update:** The GKE, GKE on VMware, GKE on AWS, and GKE on Azure versions have been updated. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin

A security vulnerability, CVE-2022-0492, has been discovered in the Linux kernel's `cgroup_release_agent_write` function. The attack uses unprivileged user namespaces and under certain circumstances this vulnerability can be exploitable for container breakout. | Low |  For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * GKE on Azure security bulletin

  
## GCP-2022-005
**Published:** 2022-02-11 **Updated:** 2022-02-15 
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability, CVE-2021-43527, has been discovered in any binary that links to the vulnerable versions of libnss3 found in NSS (Network Security Services) versions prior to 3.73 or 3.68.1. Applications using NSS for certificate validation or other TLS, X.509, OCSP or CRL functionality may be impacted, depending on how NSS is used/configured. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on Azure security bulletin

| Medium  
## GCP-2022-004
**Published:** 2022-02-04 
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability, CVE-2021-4034, has been discovered in pkexec, a part of the Linux policy kit package (polkit), that allows an authenticated user to perform a privilege escalation attack. PolicyKit is generally used only on Linux desktop systems to allow non-root users to perform actions such as rebooting the system, installing packages, restarting services etc, as governed by a policy. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on Azure security bulletin

| None  
## GCP-2022-002
**Published:** 2022-02-01 **Updated:** 2022-02-25 
### Description
Description | Severity | Notes  
---|---|---  
**2022-02-25 Update:** The GKE versions have been updated. For instructions and more details, see the: 
  * GKE security bulletin

**2022-02-23 Update:** The GKE and GKE on VMware versions have been updated. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin

**2022-02-04 Update: The rollout start date for GKE patch versions was February 2.** Three security vulnerabilities, CVE-2021-4154, CVE-2021-22600, and CVE-2022-0185, have been discovered in the Linux kernel, each of which can lead to either a container breakout, privilege escalation on the host, or both. These vulnerabilities affect all node operating systems (COS and Ubuntu) on GKE, GKE on VMware, GKE on AWS (current and previous generation), and GKE on Azure. Pods using GKE Sandbox are not vulnerable to these vulnerabilities. See the COS release notes for more details.  For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin

| High | 

  
## GCP-2022-001
**Published:** 2022-01-06 
### Description
Description | Severity | Notes  
---|---|---  
A potential Denial of Service issue in `protobuf-java` was discovered in the parsing procedure for binary data. **What should I do?** Ensure that you're using the latest versions of the following software packages:
  * `protobuf-java` (3.16.1, 3.18.2, 3.19.2) 
  * `protobuf-kotlin` (3.18.2, 3.19.2)
  * `google-protobuf` [JRuby gem] (3.19.2)

Protobuf "javalite" users (typically Android) are not affected. **What vulnerabilities are addressed by this patch?** The patch mitigates the following vulnerability: An implementation weakness in how unknown fields are parsed in Java. A small (~800 KB) malicious payload can occupy the parser for several minutes by creating large numbers of short-lived objects that cause frequent, repeated garbage collection pauses. | High   
## GCP-2021-024
**Published:** 2021-10-21 
### Description
Description | Severity | Notes  
---|---|---  
A security issue was discovered in the Kubernetes **ingress-nginx** controller, CVE-2021-25742. Ingress-nginx custom snippets allows retrieval of ingress-nginx service account tokens and secrets across all namespaces.  For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| None  
## GCP-2021-019
**Published:** 2021-09-29 
### Description
Description | Severity | Notes  
---|---|---  
There is a known issue where updating a `BackendConfig` resource using the `v1beta1` API removes an active Google Cloud Armor security policy from its service. For instructions and more details, see the GKE security bulletin. | Low  
## GCP-2021-022
**Published:** 2021-09-22 
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability has been discovered in the GKE Enterprise Identity Service (AIS) LDAP module of GKE on VMware versions 1.8 and 1.8.1 where a seed key used in generating keys is predictable. With this vulnerability, an authenticated user could add arbitrary claims and escalate privileges indefinitely.  For instructions and more details, see the GKE on VMware security bulletin. | High  
## GCP-2021-021
**Published:** 2021-09-22 
### Description
Description | Severity | Notes  
---|---|---  
A security vulnerability, CVE-2020-8561, has been discovered in Kubernetes where certain webhooks can be made to redirect kube-apiserver requests to private networks of that API server. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium  
## GCP-2021-023
**Published:** 2021-09-21 
### Description
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0020, VMware received reports of multiple vulnerabilities in vCenter. VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have already applied the patches provided by VMware for the vSphere stack to Google Cloud VMware Engine per the VMware security advisory. This update addresses the security vulnerabilities described in CVE-2021-22005, CVE-2021-22006, CVE-2021-22007, CVE-2021-22008, and CVE-2021-22010. Other non-critical security issues will be addressed in the upcoming VMware stack upgrade (per the advance notice sent in July, more details will be provided soon on the specific timeline of the upgrade).
#### VMware Engine impact
Based on our investigations, no customers were found to be impacted.
#### What should I do?
Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Critical | 

  
## GCP-2021-020
**Published:** 2021-09-17 
### Description
Description | Severity | Notes  
---|---|---  
Certain Google Cloud load balancers routing to an Identity-Aware Proxy (IAP) enabled Backend Service could have been vulnerable to an untrusted party under limited conditions. This addresses an issue reported through our Vulnerability Reward Program. The conditions were that the servers:
  * Were HTTP(S) load balancers **and**
  * Used a default backend or a backend that had a wildcard host mapping rule (that is, host="*")

In addition, a user in your organization must have clicked a specifically-crafted link sent by an untrusted party.  This issue has now been resolved. IAP has been updated to issue cookies only to authorized hosts as of September 17, 2021. A host is considered authorized if it matches at least one Subject Alternative Name (SAN) in one of the certificates installed on your load balancers. 
#### What to do
Some of your users may experience an HTTP 401 Unauthorized response with an IAP error code 52 while trying to access apps or services. This error code means that the client sent a **`Host`**header which does not match any Subject Alternative Names associated with the load balancer's SSL certificate(s). The load balancer administrator needs to update the SSL certificate to ensure that the Subject Alternative Name (SAN) list contains all the hostnames through which users are accessing the IAP-protected apps or services. Learn more aboutIAP error codes.  | High  
## GCP-2021-018
**Published:** 2021-09-15 **Updated:** 2021-09-20 
### Description
Description | Severity | Notes  
---|---|---  
A security issue was discovered in Kubernetes, CVE-2021-25741, where a user may be able to create a container with subpath volume mounts to access files & directories outside of the volume, including on the host filesystem. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| High  
## GCP-2021-017
**Published:** 2021-09-01 **Updated:** 2021-09-23 
### Description
Description | Severity | Notes  
---|---|---  
**2021-09-23 update:** Containers running inside of GKE Sandbox are unaffected by this vulnerability for attacks originating inside the container. Two security vulnerabilities, CVE-2021-33909 and CVE-2021-33910, have been discovered in the Linux kernel that can lead to an OS crash or an escalation to root by an unprivileged user. This vulnerability affects all GKE node operating systems (COS and Ubuntu). For instructions and more details, see the following security bulletins: 
  * GKE security bulletin.
  * GKE on AWS security bulletin.

| High |  CVE-2021-33909, CVE-2021-33910  
## GCP-2021-016
**Published:** 2021-08-24 
### Description
Description | Severity | Notes  
---|---|---  
The following Envoy and Istio CVEs expose Cloud Service Mesh and Istio on GKE to remotely exploitable vulnerabilities:
  * CVE-2021-39156: HTTP requests with a fragment (a section in the end of a URI that begins with a `#` character) in the URI path could bypass Istio's URI path-based authorization policies.
  * CVE-2021-39155: HTTP requests could potentially bypass an Istio authorization policy when using rules based on `hosts` or `notHosts`.
  * CVE-2021-32781: Affects Envoy's `decompressor`, `json-transcoder`, or `grpc-web` extensions or proprietary extensions that modify and increase the size of request or response bodies. Modifying and increasing the size of the body in an Envoy's extension beyond the internal buffer size could lead to Envoy accessing deallocated memory and terminating abnormally.
  * CVE-2021-32780: An untrusted upstream service could cause Envoy to terminate abnormally by sending the `GOAWAY` frame followed by the `SETTINGS` frame with the `SETTINGS_MAX_CONCURRENT_STREAMS` parameter set to `0`. _(Not applicable to Istio on GKE)_
  * CVE-2021-32778: An Envoy client opening and then resetting a large number of HTTP/2 requests could lead to excessive CPU consumption. _(Not applicable to Istio on GKE)_
  * CVE-2021-32777: HTTP requests with multiple value headers could do an incomplete authorization policy check when the `ext_authz` extension is used.

For instructions and more details, see the following security bulletins: 
  * Cloud Service Mesh security bulletin.
  * Istio on GKE security bulletin.

| High | 

  
## GCP-2021-015
**Published:** 2021-07-13 **Updated:** 2021-07-15 
### Description
Description | Severity | Notes  
---|---|---  
A new security vulnerability, CVE-2021-22555, has been discovered where a malicious actor with `CAP_NET_ADMIN` privileges can potentially cause a container breakout to root on the host. This vulnerability affects all GKE clusters and GKE on VMware running Linux version 2.6.19 or later. For instructions and more details, see the following security bulletins: 
  * GKE security bulletin.
  * GKE on VMware security bulletin.

| High  
## GCP-2021-014
**Published:** 2021-07-05 
### Description
Description | Severity | Notes  
---|---|---  
Microsoft published a security bulletin on a Remote code execution (RCE) vulnerability, CVE-2021-34527, that affects the print spooler in Windows servers. The CERT Coordination Center (CERT/CC) published an update note on a related vulnerability, dubbed "PrintNightmare" that also affects Windows print spoolers - PrintNightmare, Critical Windows Print Spooler Vulnerability For instructions and more details, see the GKE security bulletin.  | High  
## GCP-2021-012
**Published:** 2021-06-24 **Updated:** 2021-07-09 
### Description
Description | Severity | Notes  
---|---|---  
The Istio project recently announced a security vulnerability where credentials specified in the Gateway and DestinationRule credentialName field can be accessed from different namespaces.  For product-specific instructions and more details, see:
  * Cloud Service Mesh security bulletin. 
  * GKE Enterprise security bulletin GCP-2021-012 for information specific to Google Kubernetes Engine, Google Distributed Cloud Virtual for Bare Metal, and GKE on VMware. 

| High  
## GCP-2021-011
**Published:** 2021-06-04 **Updated:** 2021-10-19 
### Description
Description | Severity | Notes  
---|---|---  
**2021-10-19 update:** For instructions and more details, see the following security bulletins: 
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

The security community recently disclosed a new security vulnerability (CVE-2021-30465) found in `runc` that has the potential to allow full access to a node filesystem. For GKE, because exploiting this vulnerability requires the ability to create pods, we have rated the severity of this vulnerability at MEDIUM. For instructions and more details, see the  GKE security bulletin.  | Medium  
## GCP-2021-010
**Published:** 2021-05-25 
### Description
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0010, remote code execution and authentication bypass vulnerabilities in vSphere Client (HTML5) were privately reported to VMware. VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have applied the patches provided by VMware for the vSphere stack per the VMware security advisory. This update addresses security vulnerabilities described in CVE-2021-21985 and CVE-2021-21986. The image versions running in your VMware Engine private cloud do not reflect any change at this time to indicate the patches applied. Please rest assured that appropriate patches have been installed and your environment is secured from these vulnerabilities.
#### VMware Engine impact
Based on our investigations, no customers were found to be impacted.
#### What should I do?
Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Critical | 

  
## GCP-2021-008
**Published:** 2021-05-17 
### Description
Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an external client can access unexpected services in the cluster, bypassing authorization checks, when a gateway is configured with `AUTO_PASSTHROUGH` routing configuration.  For instructions and more details, see the Cloud Service Mesh security bulletin. | High  
## GCP-2021-007
**Published:** 2021-05-17 
### Description
Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an HTTP request path with multiple slashes or escaped slash characters (`%2F` or `%5C`) could potentially bypass an Istio authorization policy when path based authorization rules are used.  For instructions and more details, see the Cloud Service Mesh security bulletin. | High  
## GCP-2021-006
**Published:** 2021-05-11 
### Description
Description | Severity | Notes  
---|---|---  
The Istio project recently disclosed a new security vulnerability (CVE-2021-31920) affecting Istio.  Istio contains a remotely-exploitable vulnerability where an HTTP request with multiple slashes or escaped slash characters can bypass Istio authorization policy when path based authorization rules are used.  For instructions and more details, see the: 
  * GKE security bulletin

| High  
## GCP-2021-005
**Published:** 2021-05-11 
### Description
Description | Severity | Notes  
---|---|---  
A reported vulnerability has shown that Envoy does not decode escaped slash sequences `%2F` and `%5C` in HTTP URL paths in Envoy versions 1.18.2 and earlier. In addition, some Envoy-based products do not enable path normalization controls. A remote attacker may craft a path with escaped slashes (for example, `/something%2F..%2Fadmin,`), to bypass access control (for example, a block on `/admin`). A backend server could then decode slash sequences and normalize the path to provide an attacker access beyond the scope provided for by the access control policy. 
#### What should I do?
If backend servers treat `/` and `%2F` or `\` and `%5C` interchangeably and a URL path based matching is configured, we recommend reconfiguring the backend server to not treat `\` and `%2F` or `\` and `%5C` interchangeably, if feasible. 
#### What behavioral changes were introduced? 
Envoy's normalize_path and merge adjacent slashes options were enabled to address other common path confusion vulnerabilities in Envoy-based products.  | High  
## GCP-2021-004
**Published:** 2021-05-06 
### Description
Description | Severity | Notes  
---|---|---  
The Envoy and Istio projects recently announced several new security vulnerabilities (CVE-2021-28683, CVE-2021-28682 and CVE-2021-29258), that could allow an attacker to crash Envoy.  Google Kubernetes Engine clusters do not run Istio by default and are not vulnerable. If Istio has been installed in a cluster and configured to expose services to the internet, those services may be vulnerable to denial of service.  Google Distributed Cloud Virtual for Bare Metal and GKE on VMware use Envoy by default for Ingress, so Ingress services may be vulnerable to denial of service.  For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium | 

  
## GCP-2021-003
**Published:** 2021-04-19 
### Description
Description | Severity | Notes  
---|---|---  
The Kubernetes project recently  announced a new security vulnerability,  CVE-2021-25735, that could allow node updates to bypass a Validating Admission Webhook.  In a scenario where an attacker has sufficient privileges and where a Validating Admission Webhook is implemented that uses old `Node` object properties (for example fields in `Node.NodeSpec`), the attacker could update properties of a node that could lead to a cluster compromise. None of the policies enforced by GKE and Kubernetes built-in admission controllers are affected, but we recommend customers check any additional admission webhooks they have installed.  For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin

| Medium |  CVE-2021-25735  
## GCP-2021-002
**Published:** 2021-03-05 
### Description
Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0002, VMware received reports of multiple vulnerabilities in VMware ESXi and vSphere Client (HTML5). VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have applied the officially documented workarounds for the vSphere stack per the VMware security advisory. This update addresses security vulnerabilities described in CVE-2021-21972, CVE-2021-21973, and CVE-2021-21974.
#### VMware Engine impact
Based on our investigations, no customers were found to be impacted.
#### What should I do?
Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Critical | 

  
## GCP-2021-001
**Published:** 2021-01-28 
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability was recently discovered in the Linux utility `sudo`, described in CVE-2021-3156, that may allow an attacker with unprivileged local shell access on a system with `sudo` installed to escalate their privileges to root on the system. The underlying infrastructure that runs Compute Engine is not impacted by this vulnerability. All Google Kubernetes Engine (GKE), GKE on VMware, GKE on AWS, and Google Distributed Cloud Virtual for Bare Metal clusters are not affected by this vulnerability. For instructions and more details, see the following security bulletins: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin
  * Google Distributed Cloud Virtual for Bare Metal security bulletin
  * Compute Engine security bulletin

| None  
## GCP-2020-015
**Published:** 2020-12-07 **Updated:** 2020-12-22 
### Description
Description | Severity | Notes  
---|---|---  
**Updated: 2021-12-22** The command for GKE in the following section should use `gcloud beta` instead of the `gcloud` command.  ```
gcloud container clusters update –no-enable-service-externalips

```
**Updated: 2021-12-15** For GKE, the following mitigation is now available: 
  1. Starting in GKE version 1.21, services with ExternalIPs are blocked by a `DenyServiceExternalIPs` admission controller that is enabled by default for new clusters. 
  2. Customers who upgrade to GKE version 1.21 can block services with ExternalIPs using the following command: ```
gcloud container clusters update –no-enable-service-externalips

```


For more information, see  Hardening your cluster's security.  The Kubernetes project recently discovered a new security vulnerability, CVE-2020-8554, that might allow an attacker who has obtained permissions to create a Kubernetes Service of type LoadBalancer or ClusterIP to intercept network traffic originating from other Pods in the cluster. This vulnerability by itself does not give an attacker permissions to create a Kubernetes Service.  All Google Kubernetes Engine (GKE), GKE on VMware, and GKE on AWS clusters are affected by this vulnerability. 
#### What should I do?
For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin

| Medium  
## GCP-2020-014
**Published:** 2020-10-20 **Updated:** 2020-10-20 
### Description
Description | Severity | Notes  
---|---|---  
The Kubernetes project recently discovered several issues that allow for the exposure of secret data when verbose logging options are enabled. The issues are:
  * CVE-2020-8563: Secret leaks in logs for vSphere Provider kube-controller-manager
  * CVE-2020-8564: Docker config secrets leaked when file is malformed and loglevel >= 4
  * CVE-2020-8565: Incomplete fix for CVE-2019-11250 in Kubernetes allows for token leak in logs when logLevel >= 9. Discovered by GKE Security.
  * CVE-2020-8566: Ceph RBD adminSecrets exposed in logs when loglevel >= 4 


#### What should I do?
No further action is required due to the default verbosity logging levels of GKE. | None | 

  
### Google Cloud impact
Per-product details are listed below.
Product | Impact  
---|---  
**Google Kubernetes Engine (GKE)** | Google Kubernetes Engine (GKE) is not affected.   
| GKE On-Prem is not affected.   
| GKE on AWS is not affected.   
## GCP-2020-013
**Published:** 2020-09-29 
### Description
Microsoft has disclosed the following vulnerability:
Vulnerability | Severity | CVE  
---|---|---  
— A vulnerability in Windows Server allows attackers to use Netlogon Remote Protocol to run a specially-crafted application on a device on the network. |  NVD Base Score: 10 (Critical) |  CVE-2020-1472  
For more information, see the Microsoft disclosure.
### Google Cloud impact
The infrastructure hosting the Google Cloud and Google products is not impacted by this vulnerability. Additional per-product details are listed below.
Product | Impact  
---|---  
**Compute Engine** | CVE-2020-1472 **For most customers, no further action is required.** Customers using Compute Engine virtual machines running Windows Server should ensure their instances have been updated with the latest Windows patch or use Windows Server images published after 08-17-2020 (v20200813 or higher).  
**Google Kubernetes Engine** | CVE-2020-1472 **For most customers, no further action is required.** Any customers hosting domain controllers in their GKE Windows Server nodes should ensure both the nodes and the containerized workloads that run on those nodes have the latest Windows node image when it is available. A new node image version will be announced in the GKE release notes in October.  
**Managed Service for Microsoft Active Directory** | CVE-2020-1472 **For most customers, no further action is required.** The August patch released by Microsoft that includes fixes to the NetLogon protocol has been applied to all Managed Microsoft AD domain controllers. This patch delivers functionality to protect against potential exploitation. The timely application of patches is one of the key advantages of using the Managed Service for Microsoft Active Directory. Any customers manually running Microsoft Active Directory (and not utilizing Google Cloud’s managed service) should ensure their instances have the latest Windows patch or use Windows Server images.   
**Google Workspace** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine standard environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine flexible environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run functions** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Composer** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataflow** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataproc** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud SQL** |  **No customer action is required.** This service is not impacted by this vulnerability.  
## GCP-2020-012
**Published:** 2020-09-14 **Updated:** 2020-09-17 
### Description
Description | Severity | Notes  
---|---|---  
A vulnerability was recently discovered in the Linux kernel, described in CVE-2020-14386, that may allow container escape to obtain root privileges on the host node.  All GKE nodes are affected. Pods running in GKE Sandbox are not able to leverage this vulnerability.  For instructions and more details, see the: 
  * GKE security bulletin.
  * GKE on VMware security bulletin.
  * GKE on AWS security bulletin.

**What vulnerability is addressed by this patch?** The patch mitigates the following vulnerability: The vulnerability CVE-2020-14386, which allows containers with CAP_NET_RAW to write 1 to 10 bytes of kernel memory, and possibly escape the container and obtain root privileges on the host node. This is rated as a High severity vulnerability.  | High |  CVE-2020-14386  
## GCP-2020-011
**Published:** 2020-07-24 
### Description
Description | Severity | Notes  
---|---|---  
A networking vulnerability, CVE-2020-8558, was recently discovered in Kubernetes. Services sometimes communicate with other applications running inside the same Pod using the local loopback interface (127.0.0.1). This vulnerability allows an attacker with access to the cluster's network to send traffic to the loopback interface of adjacent Pods and nodes. Services that rely on the loopback interface not being accessible outside their Pod could be exploited. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin

| Low (GKE and GKE on AWS),Medium (GKE on VMware)  |  CVE-2020-8558  
## GCP-2020-010
**Published:** 2020-07-27 
### Description
Microsoft has disclosed the following vulnerability: 
Vulnerability | Severity | CVE  
---|---|---  
— Windows Servers that serve in a DNS server capacity can be exploited to run untrusted code by the Local System Account. |  NVD Base Score: 10.0 (Critical) |  CVE-2020-1350  
For more information, see the Microsoft disclosure.
### Google Cloud impact
The infrastructure hosting the Google Cloud and Google products is not impacted by this vulnerability. Additional per-product details are listed below.
Product | Impact  
---|---  
**Compute Engine** | CVE-2020-1350 **For most customers, no further action is required.** Customers using Compute Engine virtual machines running Windows Server in a DNS server capacity should ensure their instances have the latest Windows patch or use Windows Server images provided since 07/14/2020.  
**Google Kubernetes Engine** |  CVE-2020-1350 **For most customers, no further action is required.** Customers using GKE with Windows Server node in a DNS server capacity must manually update the nodes and the containerized workloads that run on those nodes to a Windows server version containing the fix.   
**Managed Service for Microsoft Active Directory** |  CVE-2020-1350 **For most customers, no further action is required.** All Managed Microsoft AD domains have been automatically updated with the patched image. Any customers manually running Microsoft Active Directory (and not utilizing Managed Microsoft AD) should ensure their instances have the latest Windows patch or use Windows Server images provided since 07/14/2020.  
**Google Workspace** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine standard environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine flexible environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run functions** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Composer** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataflow** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataproc** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud SQL** |  **No customer action is required.** This service is not impacted by this vulnerability.  
## GCP-2020-009
**Published:** 2020-07-15 
### Description
Description | Severity | Notes  
---|---|---  
A privilege escalation vulnerability, CVE-2020-8559, was recently discovered in Kubernetes. This vulnerability allows an attacker that has already compromised a node to execute a command in any Pod in the cluster. The attacker can thereby use the already compromised node to compromise other nodes and potentially read information, or cause destructive actions. Note that for an attacker to exploit this vulnerability, a node in your cluster must have already been compromised. This vulnerability, by itself, will not compromise any nodes in your cluster. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin

| Medium |  CVE-2020-8559  
## GCP-2020-008
**Published:** 2020-06-19 
### Description
Description | Severity | Notes  
---|---|---  
#### Description
VMs that have OS Login enabled might be susceptible to privilege escalation vulnerabilities. These vulnerabilities gives users that are granted OS Login permissions (but not given admin access) the ability to escalate to root access in the VM.  For instructions and more details, see the Compute Engine security bulletin. |  High  | 

  
## GCP-2020-007
**Published:** 2020-06-01 
### Description
Description | Severity | Notes  
---|---|---  
Server Side Request Forgery (SSRF) vulnerability, CVE-2020-8555, was recently discovered in Kubernetes, allowing certain authorized users to leak up to 500 bytes of sensitive information from the control plane host network. The Google Kubernetes Engine (GKE) control plane uses controllers from Kubernetes and is thus affected by this vulnerability. We recommend that you upgrade the control plane to the latest patch version. A node upgrade is not required. For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin

| Medium |  CVE-2020-8555  
## GCP-2020-006
**Published:** 2020-06-01 
### Description
Description | Severity | Notes  
---|---|---  
Kubernetes has disclosed a vulnerability that allows a privileged container to redirect node traffic to another container. Mutual TLS/SSH traffic, such as between the kubelet and API server or traffic from applications using mTLS cannot be read or modified by this attack. All Google Kubernetes Engine (GKE) nodes are affected by this vulnerability, and we recommend that you upgrade to the latest patch version.  For instructions and more details, see the: 
  * GKE security bulletin
  * GKE on VMware security bulletin
  * GKE on AWS security bulletin

| Medium |  Kubernetes issue 91507  
## GCP-2020-005
**Published:** 2020-05-07 
### Description
Vulnerability | Severity | CVE  
---|---|---  
A vulnerability was recently discovered in the Linux kernel, described in CVE-2020-8835, allowing container escape to obtain root privileges on the host node.  Google Kubernetes Engine (GKE) Ubuntu nodes running GKE 1.16 or 1.17 are affected by this vulnerability, and we recommend that you upgrade to the latest patch version as soon as possible.  Please see the GKE security bulletin for instructions and more details.  |  High |  CVE-2020-8835  
## GCP-2020-004
**Published:** 2020-03-31 **Updated:** 2020-03-31 
### Description
Kubernetes has disclosed the following vulnerabulities:
Vulnerability | Severity | CVE  
---|---|---  
— This is a Denial of Service (DoS) vulnerability that impacts the API server.  |  Medium |  CVE-2019-11254  
See the GKE on VMware security bulletin for instructions and more details.
## GCP-2020-003
**Published:** 2020-03-31 **Updated:** 2020-03-31 
### Description
Kubernetes has disclosed the following vulnerabulities:
Vulnerability | Severity | CVE  
---|---|---  
— This is a Denial of Service (DoS) vulnerability that impacts the API server.  |  Medium |  CVE-2019-11254  
See the GKE security bulletin for instructions and more details.
## GCP-2020-002
**Published:** 2020-03-23 **Updated:** 2020-03-23 
### Description
Kubernetes has disclosed the following vulnerabulities:
Vulnerability | Severity | CVE  
---|---|---  
— This is a Denial of Service (DoS) vulnerability that impacts the kubelet.  |  Medium |  CVE-2020-8551  
— This is a Denial of Service (DoS) vulnerability that impacts the API server.  |  Medium |  CVE-2020-8552  
See the GKE security bulletin for instructions and more details.
## GCP-2020-001
**Published:** 2020-01-21 **Updated:** 2020-01-21 
### Description
Microsoft has disclosed the following vulnerability:
Vulnerability | Severity | CVE  
---|---|---  
**CVE-2020-0601 — This vulnerability is also known as the Windows Crypto API Spoofing Vulnerability**. It could be exploited to make malicious executables appear trusted or allow the attacker to conduct man-in-the-middle attacks and decrypt confidential information on user connections to the affected software.  |  NVD Base Score: 8.1 (High) |  CVE-2020-0601  
For more information, see the Microsoft disclosure.
### Google Cloud impact
The infrastructure hosting the Google Cloud and Google products is not impacted by this vulnerability. Additional per-product details are listed below.
Product | Impact  
---|---  
**Compute Engine** |  CVE-2020-0601 **For most customers, no further action is required.** Customers using Compute Engine virtual machines running Windows Server should ensure their instances have the latest Windows patch or use Windows Server images provided since 1/15/2020. Please see the Compute Engine security bulletin for more details.  
**Google Kubernetes Engine** |  CVE-2020-0601 **For most customers, no further action is required.** Customers using GKE with Windows Server nodes, both the nodes and the containerized workloads that run on those nodes must be updated to patched versions to mitigate this vulnerability. Please see the GKE security bulletin for instructions and more details.   
**Managed Service for Microsoft Active Directory** |  CVE-2020-0601 **For most customers, no further action is required.** All Managed Microsoft AD domains have been automatically updated with the patched image. Any customers manually running Microsoft Active Directory (and not utilizing Managed Microsoft AD) should ensure their instances have the latest Windows patch or use Windows Server images provided since 1/15/2020.  
**Google Workspace** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine standard environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**App Engine flexible environment** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Run functions** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud Composer** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataflow** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Dataproc** |  **No customer action is required.** This service is not impacted by this vulnerability.  
**Cloud SQL** |  **No customer action is required.** This service is not impacted by this vulnerability.  
## GCP-2019-001
**Published:** 2019-11-12 **Updated:** 2019-11-12 
### Description
Intel has disclosed the following vulnerabilities:
Vulnerability | Severity | CVE  
---|---|---  
**CVE-2019-11135 — This vulnerability referred to as TSX Async Abort (TAA) can be used to exploit speculative execution within a TSX transaction.** This vulnerability potentially allows data to be exposed via the same microarchitectural data structures exposed by Microarchitectural Data Sampling (MDS).  |  Medium |  CVE-2019-11135  
**CVE-2018-12207 — This is a Denial of Service (DoS) vulnerability affecting virtual machine hosts (not guests).** This issue is known as "Machine Check Error on Page Size Change."  |  Medium |  CVE-2018-12207  
For more information, see the Intel disclosures:
  * Intel’s Developer Guidance Site: 
    * Machine Check Error on Page Size Change


### Google Cloud impact
The infrastructure hosting the Google Cloud and Google products is protected from these vulnerabilities. Additional per-product details are listed below.
Product | Impact  
---|---  
**Compute Engine** |  CVE-2019-11135 **For most customers, no additional action is required.** N2, C2 or M2 customers running untrusted code in their own multi-tenant services within Compute Engine virtual machines should stop and start their VMs to ensure that they have the latest security mitigations.  CVE-2018-12207 **For all customers, no additional action is required.**  
**Google Kubernetes Engine** |  CVE-2019-11135 **For most customers, no additional action is required.** If you use node pools with N2, M2, or C2 nodes, and those nodes run untrusted code inside your own multi-tenant GKE clusters, then you should restart your nodes. If you want to restart all nodes in your node pool, upgrade the affected node pool. CVE-2018-12207 **For all customers, no additional action is required.**  
**App Engine standard environment** | **No additional action is required.**  
**App Engine flexible environment** |  CVE-2019-11135 **No additional action is required.** Customers should review Intel best practices with respect to application-level sharing which may occur between hyperthreads within a Flex VM. CVE-2018-12207 **No additional action is required.**  
**Cloud Run** | **No additional action is required.**  
**Cloud Run functions** | **No additional action is required.**  
**Cloud Composer** | **No additional action is required.**  
**Dataflow** |  CVE-2019-11135 **For most customers, no additional action is required.** Dataflow customers who run multiple untrusted workloads on N2, C2, or M2 Compute Engine VMs managed by Dataflow and are concerned about intra-guest attacks should consider restarting any streaming pipelines that are currently running. Optionally, batch pipelines can be cancelled and re-run. No action is required for pipelines launched after today. CVE-2018-12207 **For all customers, no additional action is required.**  
**Dataproc** |  CVE-2019-11135 **For most customers, no additional action is required.** Cloud Dataproc customers who run multiple, untrusted workloads on the same Cloud Dataproc cluster running on Compute Engine N2, C2 or M2 VMs and are concerned about intra-guest attacks, should redeploy their clusters. CVE-2018-12207 **For all customers, no additional action is required.**  
**Cloud SQL** | **No additional action is required.**  
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-26 UTC.


