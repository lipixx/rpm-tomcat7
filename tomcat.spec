%define __jar_repack %{nil}
%define tomcat_home /usr/share/tomcat
%define tomcat_group tomcat
%define tomcat_user tomcat

Summary:    Apache Servlet/JSP Engine, RI for Servlet 2.4/JSP 2.0 API
Name:       tomcat
Version:    7.0.68
BuildArch:  noarch
Release:    1
License:    Apache Software License
Group:      Networking/Daemons
URL:        http://tomcat.apache.org/
Source0:    apache-tomcat-%{version}.tar.gz
Source1:    %{name}.service
Source2:    %{name}.sysconfig
Source3:    %{name}.logrotate
Source4:    %{name}.conf
Source5:    libexec_tomcat/functions
Source6:    libexec_tomcat/preamble
Source7:    libexec_tomcat/server
Requires:   java, %{name}-lib = %{version}-%{release}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

Tomcat is developed in an open and participatory environment and
released under the Apache Software License. Tomcat is intended to be
a collaboration of the best-of-breed developers from around the world.
We invite you to participate in this open development project. To
learn more about getting involved, click here.

This package contains the base tomcat installation that depends on Sun's JDK and not
on JPP packages.

%package lib
Group: Development/Compilers
Summary: Libraries needed to run the Tomcat Web container
Requires: %{name} = %{version}-%{release}

%description lib
Libraries needed to run the Tomcat Web container

%package admin-webapps
Group: System Environment/Applications
Summary: The host-manager and manager web applications for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description admin-webapps
The host-manager and manager web applications for Apache Tomcat.

%package docs-webapp
Group: System Environment/Applications
Summary: The docs web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description docs-webapp
The docs web application for Apache Tomcat.

%package examples-webapp
Group: System Environment/Applications
Summary: The examples web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description examples-webapp
The examples web application for Apache Tomcat.

%package root-webapp
Group: System Environment/Applications
Summary: The ROOT web application for Apache Tomcat
Requires: %{name} = %{version}-%{release}

%description root-webapp
The ROOT web application for Apache Tomcat.

%prep
%setup -q -n apache-tomcat-%{version}

%build

%install
install -d -m 755 %{buildroot}/%{tomcat_home}/
cp -R * %{buildroot}/%{tomcat_home}/

# Put logging in /var/log and link back.
rm -rf %{buildroot}/%{tomcat_home}/logs
install -d -m 755 %{buildroot}/var/log/%{name}/
cd %{buildroot}/%{tomcat_home}/
ln -s /var/log/%{name}/ logs
cd -

# Put temp in /var/cache and link back.
rm -rf %{buildroot}/%{tomcat_home}/temp
install -d -m 755 %{buildroot}/var/cache/%{name}/temp
cd %{buildroot}/%{tomcat_home}/
ln -s /var/cache/%{name}/temp temp
cd -

# Put work in /var/cache and link back.
rm -rf %{buildroot}/%{tomcat_home}/work
install -d -m 755 %{buildroot}/var/cache/%{name}/work
cd %{buildroot}/%{tomcat_home}/
ln -s /var/cache/%{name}/work work
cd -

# Put conf in /etc/ and link back.
install -d -m 755 %{buildroot}/%{_sysconfdir}/%{name}/Catalina/localhost
mv %{buildroot}/%{tomcat_home}/conf/* %{buildroot}/%{_sysconfdir}/%{name}/
rmdir %{buildroot}/%{tomcat_home}/conf
cd %{buildroot}/%{tomcat_home}/
ln -s %{_sysconfdir}/%{name} conf
cd -

# Put webapps in /var/lib and link back.
install -d -m 755 %{buildroot}/var/lib/%{name}
mv %{buildroot}/%{tomcat_home}/webapps %{buildroot}/var/lib/%{name}
cd %{buildroot}/%{tomcat_home}/
ln -s /var/lib/%{name}/webapps webapps
cd -

# Put lib in /usr/share/java and link back.
install -d -m 755 %{buildroot}/usr/share/java
mv %{buildroot}/%{tomcat_home}/lib %{buildroot}/usr/share/java/%{name}
cd %{buildroot}/%{tomcat_home}/
ln -s /usr/share/java/%{name} lib
cd -

# Put docs in /usr/share/doc
install -d -m 755 %{buildroot}/usr/share/doc/%{name}-%{version}
mv %{buildroot}/%{tomcat_home}/{RUNNING.txt,LICENSE,NOTICE,RELEASE*} %{buildroot}/usr/share/doc/%{name}-%{version}

# Put executables in /usr/bin
rm  %{buildroot}/%{tomcat_home}/bin/*bat
install -d -m 755 %{buildroot}/usr/{bin,sbin}
mv %{buildroot}/%{tomcat_home}/bin/digest.sh %{buildroot}/usr/bin/%{name}-digest
mv %{buildroot}/%{tomcat_home}/bin/tool-wrapper.sh %{buildroot}/usr/bin/%{name}-tool-wrapper

# Drop init script
install -d -m 755 %{buildroot}/%{_unitdir}
install    -m 0644 %_sourcedir/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service

# Drop sysconfig script
install -d -m 755 %{buildroot}/%{_sysconfdir}/sysconfig/
install -d -m 755 %{buildroot}/%{_sysconfdir}/%{name}/
install    -m 644 %_sourcedir/%{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install    -m 644 %_sourcedir/%{name}.sysconfig %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf

# Drop logrotate script
install -d -m 755 %{buildroot}/%{_sysconfdir}/logrotate.d
install    -m 644 %_sourcedir/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}

# Drop libexec
install -d -m 755 %{buildroot}/%{_libexecdir}/%{name}
install    -m 644 %_sourcedir/libexec_tomcat/functions %{buildroot}/%{_libexecdir}/%{name}/functions
install    -m 755 %_sourcedir/libexec_tomcat/preamble %{buildroot}/%{_libexecdir}/%{name}/preamble
install    -m 755 %_sourcedir/libexec_tomcat/server %{buildroot}/%{_libexecdir}/%{name}/server

%clean
rm -rf %{buildroot}

%pre
getent group %{tomcat_group} >/dev/null || groupadd -r %{tomcat_group}
getent passwd %{tomcat_user} >/dev/null || /usr/sbin/useradd --comment "Tomcat Daemon User" --shell /bin/bash -M -r -g %{tomcat_group} --home %{tomcat_home} %{tomcat_user}

%files
%defattr(-,%{tomcat_user},%{tomcat_group})
/var/log/%{name}/
/var/cache/%{name}
%dir /var/lib/%{name}/webapps
%defattr(-,root,root)
%{tomcat_home}/*
%attr(0755,root,root) /usr/bin/*
%dir /var/lib/%{name}
%{_unitdir}/%{name}.service
%{_sysconfdir}/logrotate.d/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%doc /usr/share/doc/%{name}-%{version}

%files lib
%defattr(0644,root,root,0755)
/usr/share/java/%{name}

%files admin-webapps
%defattr(0644,root,root,0755)
/var/lib/%{name}/webapps/host-manager
/var/lib/%{name}/webapps/manager

%files docs-webapp
%defattr(0644,root,root,0755)
/var/lib/%{name}/webapps/docs

%files examples-webapp
%defattr(0644,root,root,0755)
/var/lib/%{name}/webapps/examples

%files root-webapp
%defattr(0644,root,root,0755)
/var/lib/%{name}/webapps/ROOT

%post
  /bin/systemctl enable %{name}  >/dev/null 2>&1

%preun
if [ $1 = 0 ]; then
  /bin/systemctl stop %{name} >/dev/null 2>&1
  /bin/systemctl disable %{name} >/dev/null 2>&1
  /bin/systemctl daemon-reload  >/dev/null 2>&1 
fi

%postun
if [ $1 -ge 1 ]; then
  /bin/systemctl condrestart tomcat >/dev/null 2>&1  
fi

%changelog
* Thu Apr 14 2016 Felip Moll Marquès <lipixx@gmail.com>
- Match RHEL 7 and systemd
* Thu Apr 7 2016 Jose Maria Fernandez <jmfernandez@cnio.es>
- 7.0.68
* Wed Nov 4 2015 Jose Maria Fernandez <jmfernandez@cnio.es>
- 7.0.65
* Wed Jul 22 2015 Jeremy McMillan <jeremy.mcmillan@gmail.com>
- 7.0.63
* Mon May 11 2015 Forest Handford <foresthandford+VS@gmail.com>
- 7.0.61
* Thu Sep 4 2014 Edward Bartholomew <edward@bartholomew>
- 7.0.55
* Fri Apr 4 2014 Elliot Kendall <elliot.kendall@ucsf.edu>
- Update to 7.0.53
- Changes to more closely match stock EL tomcat package
* Mon Jul 1 2013 Nathan Milford <nathan@milford.io>
- 7.0.41

