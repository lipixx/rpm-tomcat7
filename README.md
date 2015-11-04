rpm-tomcat7
===========

An RPM spec file to build Tomcat 7.0 RPMs.

Steps to build them:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

wget -P ~/rpmbuild/SPECS https://raw.github.com/inab/rpm-tomcat7/7.0.65/tomcat7.spec
wget -P ~/rpmbuild/SOURCES https://raw.github.com/inab/rpm-tomcat7/7.0.65/tomcat7.init
wget -P ~/rpmbuild/SOURCES https://raw.github.com/inab/rpm-tomcat7/7.0.65/tomcat7.sysconfig
wget -P ~/rpmbuild/SOURCES https://raw.github.com/inab/rpm-tomcat7/7.0.65/tomcat7.logrotate
wget -P ~/rpmbuild/SOURCES https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.65/bin/apache-tomcat-7.0.65.tar.gz
rpmbuild -bb ~/rpmbuild/SPECS/tomcat7.spec
```

then you can install the RPMs available at ~/rpmbuild/RPMS/noarch using either `yum` or `rpm`
