# Monitoring Looker  |  Google Cloud

**Source:** https://cloud.google.com/looker/docs/monitoring-looker

Skip to main content 
  * Español – América Latina

Console 


  * On this page
  * Application monitoring
  * Host monitoring
    * Alerting thresholds




Was this helpful?
Send feedback 
#  Monitoring Looker
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * Application monitoring
  * Host monitoring
    * Alerting thresholds


Although Looker application monitoring may not seem like it is strictly required, it is very important to set up on customer-hosted instances. In the rare instance that something goes wrong with your server, it is often much more difficult or impossible for Looker to help you fix the issue unless you can provide appropriate monitoring information from the time of the incident.
## Application monitoring
### URL
There are two simple ways to validate that your Looker instance is running.
  1. Append `/alive` to your Looker instance's URL like this:
`https://instance_name.looker.com/alive`
If your instance is able to respond to a web request you'll receive a 200 OK HTTP status code.
  2. Append `/availability` to your Looker instance's URL like this:
`https://instance_name.looker.com/availability`
This URL performs a more complete check of several underlying subsystems and will also respond with a 200 OK HTTP status code if all is well.


### JMX
The Java virtual machine that runs Looker may be monitored via JMX.
Many monitoring applications such as Zabbix and Nagios support JMX. See your monitoring application's documentation for more information.
#### Edit the Looker startup script
To enable JMX monitoring, you will need to edit your Looker startup script. By default it is named:
```
/home/looker/looker/looker

```

Look for the Java startup parameters:
```
java \
  -XX:+UseG1GC -XX:MaxGCPauseMillis=2000 \
  -Xms$JAVAMEM -Xmx$JAVAMEM \
  -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps \
  -Xloggc:/tmp/gc.log  ${JAVAARGS} \
  -jar looker.jar start ${LOOKERARGS}

```

> Starting in Looker 6.18, the Looker JAR file has been split into two separate JAR files: the Looker core JAR file and a Looker dependencies JAR file. Upon starting, the core JAR file will automatically start the dependencies JAR file. Both JAR files must be in the same directory so that the core JAR file can successfully find and start the dependencies JAR file.
By default, the `--no-daemonise` startup option is not set. If you have not set the `--no-daemonise` option, add a section following the line starting with `-Xms$JAVAMEM`:
```
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.port=9910 \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.ssl=false \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.local.only=false \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.authenticate=true \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.access.file=${HOME}/.lookerjmx/jmxremote.access \
  -Dcom.sun.akuma.jvmarg.com.sun.management.jmxremote.password.file=${HOME}/.lookerjmx/jmxremote.password \

```

If you have set the `--no-daemonise` startup option, add a section following the line starting with `-Xms$JAVAMEM`:
```
  -Dcom.sun.management.jmxremote \
  -Dcom.sun.management.jmxremote.port=9910 \
  -Dcom.sun.management.jmxremote.ssl=false \
  -Dcom.sun.management.jmxremote.local.only=false \
  -Dcom.sun.management.jmxremote.authenticate=true \
  -Dcom.sun.management.jmxremote.access.file=${HOME}/.lookerjmx/jmxremote.access \
  -Dcom.sun.management.jmxremote.password.file=${HOME}/.lookerjmx/jmxremote.password \

```

#### Create the `.lookerjmx` directory
Next, create the `.lookerjmx` directory under your Looker user's home directory, and set permissions:
```
sudo su - looker
mkdir ~/.lookerjmx
chmod 700 ~/.lookerjmx
cd ~/.lookerjmx

```

#### Create the JMX files
Using your favorite text editor create a file in the new directory named `jmxremote.access` with the following contents (you may customize for your environment):
```
monitorRole   readonly
controlRole   readwrite \
              create javax.management.monitor.*,javax.management.timer.* \
              unregister

```

Next create a file named `jmxremote.password` in the same directory with the following contents, using your own secure passwords:
```
monitorRole   some_password_here
controlRole   some_password_here

```

#### Setting permissions
Make it such that Java (and therefore Looker) will not start if the file permissions allow anyone _except the Looker user_ to read the password file.
```
chmod 400 jmxremote.*

```

#### Restart Looker
Looker needs to be restarted to enable JMX. Make sure you run this *as the Looker user and **not** root*:
```
cd ~/looker
./looker restart

```

Your Looker instance is now configured for remote JMX monitoring on port 9910, using the password you supplied. You may need to modify your firewall settings or network ACLs to allow your monitoring server to get network access on this port.
## Host monitoring
For every host running the Looker application, we recommend that you collect, graph and alert on at least the following performance metrics:
  * **CPU Utilization:** load and percent CPU utilized
  * **Memory Utilization:** total used and swap used
  * **Disk Usage**


### Alerting thresholds
To establish good alerting thresholds, first establish a baseline. Collect performance data with your Looker instance running under a normal load. Take a look at the performance graphs and observe the peaks. The length of time you will need to establish the baselines depends on your business and your Looker usage patterns. Some companies may use Looker in a stable, repeatable pattern every week during business hours. Others may use Looker more heavily at specific times (such as the end of each month).
In general, alerts should only be sent for events that are actionable. Sending alerts when there is nothing which needs to be done masks the importance of critical alerts.
The following thresholds may be used as a starting point for alerting. When the following values are exceeded for 15 minutes or more, manual intervention may be required.
Metric | Warning | Critical | Comments  
---|---|---|---  
CPU Load | 2 | 4 | Load should generally be 1 or less for a single-core system. Sustained high load leads to poor performance.  
CPU % Used | 80 | 90 | High CPU usage leads to poor performance.  
Memory % Used | 60 | 70 | High memory usage can indicate too much memory is allocated to Java.  
Disk % Used | 80 | 90 | Ensure the disk isn't full.  
Additional notes:
  * Systems with more than one core can handle high CPU loads without reduced performance. The rule of thumb is that sustained load should not be greater than the number of processor cores.
  * The percent of total CPU time in use before a system experiences performance degradation scales with the number of CPU cores in the system. In other words, a single-core system may have poor performance when the CPU is 80% utilized, whereas a sixteen-core host may still be usable at 95% utilization.
  * High sustained CPU utilization can be rectified by updating the host hardware, or upgrading to a larger instance. Sometimes large numbers of scheduled Looks or long-query derived tables can be reduced or made more efficient to improve performance.


## Next steps
After you have set up monitoring, you're ready to set up Looker backups.
Was this helpful?
Send feedback 
Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2025-07-22 UTC.


