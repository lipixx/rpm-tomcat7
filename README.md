rpm-tomcat7
===========

An RPM spec file to build Tomcat 7.0 RPMs.

Steps to build them:

```bash
sudo yum -y install rpmdevtools && rpmdev-setuptree

wget -P ~/rpmbuild/SPECS https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/tomcat7.spec
wget -P ~/rpmbuild/SOURCES https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/tomcat7.service
wget -P ~/rpmbuild/SOURCES https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/tomcat7.sysconfig
wget -P ~/rpmbuild/SOURCES https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/tomcat7.logrotate

wget -P ~/rpmbuild/SOURCES/libexec_tomcat https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/libexec_tomcat/functions
wget -P ~/rpmbuild/SOURCES/libexec_tomcat https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/libexec_tomcat/preamble
wget -P ~/rpmbuild/SOURCES/libexec_tomcat https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/libexec_tomcat/server

wget -P ~/rpmbuild/SOURCES/libexec_tomcat https://raw.github.com/lipixx/rpm-tomcat7/7.0.68/apache-tomcat-7.0.68.tar.gz

or

wget -P ~/rpmbuild/SOURCES https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.68/bin/apache-tomcat-7.0.68.tar.gz

rpmbuild -bb ~/rpmbuild/SPECS/tomcat.spec
```

then you can install the RPMs available at ~/rpmbuild/RPMS/noarch using either `yum` or `rpm`
