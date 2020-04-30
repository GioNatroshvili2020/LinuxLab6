Name: pythoncode		
Version: 0.0.1	
Release:	1%{?dist}
Summary: Cool Python Script	

Group:		System
License:	GPL
URL:		htpps://github.com/GioNatroshvili2020
Packager:	Giorgi Natroshvili

Requires: bash	
Requires: mc
Requires: screen
Requires: dmidecode
BuildRoot: /root/rpmbuild/

%description
Hottest script that has ever been written on planes of linux. It prints cool messages!

%prep
echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/usr/bin/

cp ../SOURCES/pythoncode.py $RPM_BUILD_ROOT/usr/bin

exit

%files
%attr(0777, root, root) /usr/bin/*

%post
#This part does bunch of sexy moves, like installing vim and  tmux#
yum install vim htop tmux -y
cd /usr/bin
# Save old python code if it exists
if [ -e pythoncode.py ]
then
   cp pythoncode.py pythoncode.py.orig
fi
if [ ! -e /usr/bin/tst ]
then
   ln -s test.py tst
fi 

%changelog
* Tue Apr 21 2020 Giorgi Natroshvili natroshvilig1999@gmail.com 
  - This is a lab assignment for cs470, SDSU Gerogia.
    shows simple exmaple of building an RPM package.

