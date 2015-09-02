Name:           ros-indigo-wireless-watcher
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS wireless_watcher package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rospy
Requires:       ros-indigo-wireless-msgs
BuildRequires:  ros-indigo-catkin

%description
The wireless_watcher package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Sep 02 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.0.6-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.0.5-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.0.4-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Mike Purvis <mpurvis@clearpathrobotics.com> - 0.0.3-0
- Autogenerated by Bloom

