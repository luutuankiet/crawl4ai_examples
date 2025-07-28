# Configuring your SSL certificate for proper HTTPS  |  Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/ssl-certificate-for-proper-https

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Install the certificate
  * Validate the certificate
  * Validating a site's certificate against the CA bundle
  * Disabling insecure SSL protocols




Was this helpful?
Send feedback 
#  Configuring your SSL certificate for proper HTTPS
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Install the certificate
  * Validate the certificate
  * Validating a site's certificate against the CA bundle
  * Disabling insecure SSL protocols


A default installation of the Looker application uses self-signed SSL certificates for HTTPS. For production environments of customer-hosted instances, we recommend installing an SSL certificate from a trusted vendor.
To use an SSL certificate with Looker, you will need to create a Java keystore with your certificate and key.
You should have the following files:
  * A certificate file named `looker.pem` that contains your primary certificate
  * An associated key file named `looker.key`
  * Optionally, an intermediate Certificate Authority (CA) chain file named `ca.pem`


> Your `.pem` file does not need to contain a root certificate.
## Install the certificate
These files should all exist in the same directory. The default is `/home/looker/looker/.ssl`.
  1. Create the new directory and make it the current directory:
```
mkdir /home/looker/looker/.ssl
cd /home/looker/looker/.ssl

```

  2. Choose a password for the keystore and put it in a file called `.keystorepass`:
```
echo "some_password_here" > .keystorepass

```

  3. If you have a CA file, append it to the end of your certificate file:
```
echo >> looker.pem
cat ca.pem >> looker.pem

```

  4. Convert the certificate and key to a `pkcs12` keystore:
```
openssl pkcs12 -export \
    -in looker.pem       \
    -inkey looker.key    \
    -out importme.p12

```

  5. You will be prompted for an export password. Use the one that you put in the `.keystorepass` file.
  6. Convert the pkcs12 keystore to a Java keystore:
```
keytool -importkeystore     \
    -srckeystore importme.p12 \
    -destkeystore looker.jks  \
    -srcstoretype pkcs12      \
    -alias 1

```

  7. You will be prompted for the new keystore password and the pkcs12 keystore password. Keep using the one in the `.keystorepass` file.
  8. Create a file named `lookerstart.cfg` in the same directory as your `looker.jar`. This file will configure the requisite Looker options every time Looker starts. The file should contain:

```
LOOKERARGS="--ssl-keystore=/home/looker/looker/.ssl/looker.jks --ssl-keystore-pass-file=/home/looker/looker/.ssl/.keystorepass"

```

## Validate the certificate
Once Looker is running, you can verify that your cert is correctly installed with OpenSSL `s_client`.
```
openssl s_client -connect localhost:9999

```

If your hostname is `looker.yourdomain.com`, you should see a line in the output like this:
```
subject=/OU=Domain Control Validated/CN=looker.yourdomain.com

```

Another way to check is with `wget`. This test can be performed from any host which has network access to your Looker instance via HTTPS.
On a Looker using the default self-signed certificate, the output shows the certificate common name `self-signed.looker.com`:
```
$ wget https://looker.yourdomain.com:9999
--2014-12-31 12:06:03--  https://looker.yourdomain.com:9999/
Resolving looker.yourdomain.com (looker.yourdomain.com)... 192.168.23.66
Connecting to looker.yourdomain.com (looker.yourdomain.com)|192.168.23.66|:9999... connected.
ERROR: cannot verify looker.yourdomain.com's certificate, issued by '/CN=self-signed.looker.com':
  Self-signed certificate encountered.
    ERROR: certificate common name 'self-signed.looker.com' doesn't match requested host name 'looker.yourdomain.com'.
To connect to looker.yourdomain.com insecurely, use `--no-check-certificate'.

```

On a Looker using a certificate from a certificate authority, the certificate common name must match the DNS name that clients use to access Looker (or an equivalent wildcard certificate).
Here is an example of a server using a "real" (non-self signed) certificate:
```
$ wget https://looker.yourdomain.com:9999
--2014-12-31 12:06:47--  https://looker.yourdomain.com:9999/
Resolving looker.yourdomain.com (looker.yourdomain.com)... 10.10.10.10
Connecting to looker.yourdomain.com (looker.yourdomain.com)|10.10.10.10|:9999... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://looker.yourdomain.com:9999/login [following]
--2014-12-31 12:06:48--  https://looker.yourdomain.com:9999/login
Connecting to looker.yourdomain.com (looker.yourdomain.com)|10.10.10.10|:9999... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3491 (3.4K) [text/html]
Saving to: 'index.html'

100%[====================================================>] 3,491       --.-K/s   in 0.07s

2014-12-31 12:06:48 (50.5 KB/s) - 'index.html' saved [3491/3491]

```

## Validating a site's certificate against the CA bundle
As of Looker 5.18, Looker uses the Java Certificate Authority (CA) root certificate bundle. Looker uses the CA bundle to verify the authenticity of the hosts with which it communicates when making outbound requests from the Looker server. This includes actions like making requests to outbound webhooks, performing S3 backups, requesting various forms of authentication, and communicating with the license-verification server.
Java provides and manages the CA bundle, which resides on disk. This lets the admins of customer-hosted Looker instances add or remove certificates from the CA bundle.
If you choose to modify the CA bundle, you can use Looker's `test_ssl_cert_validation` utility to test whether or not Looker can validate a server certificate when making an outbound HTTP connection. The utility accepts the name of a file that contains a list of URLs you want to test, with one URL per line, like this:
```
https://www.google.com
https://looker.com
https://wrong.host.badssl.com/

```

If the name of this file was `hosts`, you would use `test_ssl_cert_validation` like this:
```
$ ./looker test_ssl_cert_validation hosts

```

The output of `test_ssl_cert_validation` would look like this:
```
Using CA file from .../jre/lib/security/cacerts

Attempting connection to https://www.google.com
Certificate verified successfully, connection returned with:
HTTP/1.1 200 OK

Attempting connection to https://looker.com
Certificate verified successfully, connection returned with:
HTTP/1.1 200 OK

Attempting connection to https://wrong.host.badssl.com/
Error connecting to https://wrong.host.badssl.com/: OpenSSL::SSL::SSLError: hostname
"wrong.host.badssl.com" does not match the server certificate

Summary:
Successes: 3, Redirects: 0, Failures: 1

```

## Disabling insecure SSL protocols
To disable inbound TSL1.0 connections to Looker, follow one of these two methods:
  * Modify the `ssl_protocols` line in your Nginx configuration file and remove the option for TLSv1, as shown in this code snippet:
```
   ssl-protocols: "TLSv1.2 TLSv1.3"

```

  * Set up a proxy or load balancer in front of Looker that terminates the TLS or SSL protocol. Then, disable SSL at the Looker level.


## Next steps
After you have set up your SSL certificate, you will be ready to add port forwarding for a cleaner URL.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


