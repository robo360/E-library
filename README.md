# E-library

A web-server built on top of a raspberry pi or any other small computer, running unix-based operating system.

#Requirements

1. A raspberry pi with raspbian in it

Raspbian is a linux distribution for Raspberry Pi.

2. Apache

Apache HTTP Server is an http server that we use to launch web files that contains links to the files you want to share.

3. PHP

A server-side scripting language for the website

4. Hostapd and dnsmasq

hostapd (host access point daemon) is a user space daemon software enabling a network interface card to act as an access point and authentication server.

[More info on hostapd](https://en.wikipedia.org/wiki/Hostapd)

Dnsmasq provides network infrastructure for small networks: DNS, DHCP, router advertisement and network boot. It is designed to be lightweight and have a small footprint, suitable for resource constrained routers and firewalls. It has also been widely used for tethering on smartphones and portable hotspots, and to support virtual networking in virtualisation frameworks. Supported platforms include Linux (with glibc and uclibc), Android, *BSD, and Mac OS X. Dnsmasq is included in most Linux distributions and the ports systems of FreeBSD, OpenBSD and NetBSD. Dnsmasq provides full IPv6 support.
[a More info on dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html)

#Turning a raspberry pi into file-server

Step 1: Install Raspbian on a raspberry Pi
 
   For this step, Follow the official guide to install raspbian on a raspberry pi
   [Install Raspbian-official guide](https://www.raspberrypi.org/documentation/installation/installing-images/)

Step 2:Install Apache HTTP Server and PHP

After installing raspbian, install php and apache http server using the following commands.
  
   sudo apt-get install apache2 -y
   sudo apt-get install php libapache2-mod-php -y
  
Note: for these commands to run correctly WIFI should be on.

Step 3:Turn a raspberry pi into a stand-alone network access point

This following guide works you through installing hostapd and dnsmasq.

[Install guide](https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md)

Step 4: Finalize
	
Download the web and copy the files into var/www/html
