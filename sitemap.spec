Name: sitemap
Version: 2.7
# Don't forget tu up
Release: 1
Summary: makes a site map page for you from description metadata
URL: http://www.catb.org/~esr/sitemap/
Source0: %{name}-%{version}.tar.gz
License: MIT-like
Group: Utilities/System
BuildRoot: %{_tmppath}/%{name}-root

%description 
sitemap indexes all pages under the current directory and writes an
HTML map page to standard output.  The code looks for description
information for each page in a meta `description' header; if it doesn't
find one, the page is omitted from the index.

%prep
%setup -q

%build
make sitemap.1

%install
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT"%{_bindir}
mkdir -p "$RPM_BUILD_ROOT"%{_mandir}/man1/
cp sitemap "$RPM_BUILD_ROOT"%{_bindir}
cp sitemap.1 "$RPM_BUILD_ROOT"%{_mandir}/man1/

%clean
[ "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%files
%doc README sitemaprc
%defattr(-,root,root,-)
%{_mandir}/man1/sitemap.1*
%{_bindir}/sitemap

%changelog
* Fri Sep 24 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.6-1
- Added Portuguese support.  Make it ignore Subversion directories.

* Mon Aug  2 2004 Eric S. Raymond <esr@snark.thyrsus.com> - 2.5-1
- Change default configuration to reflect new site.

* Mon Dec 29 2003 Eric S. Raymond <esr@snark.thyrsus.com> 2.4-1
- RPMs can be built by a non-root user.

# 1.2  changes by Dave Pearson <davep@hagbard.demon.co.uk>.
# 1.3  changes by Jean-Philippe Argaud <jp.argaud@iname.com>.
# 1.4  changes by ESR.
# 1.5  fix suggested by Imre Simon.
# 1.6  Corrected month array.
# 1.7  Jean-Philippe Argaud's change to support separator icons.
#      Erik Rossen <rossen@freesurf.ch> fixed a bug with wrapped meta tags.
#      Swedish-language support added.
# 1.8  German-language support by Michael Wiedmann.  Recognize .htm files.
# 1.9  Norwegian-language support added, national month names added by
#      Erik I. Bolsø <eriki@himolde.no>
# 1.10 Changes by Cosimo Vagarini <vaga@dada.it>   
#      - Italian language support.
#      - Y2K Compliance.
#      - Small bug fixed.
# 1.11 Ported to CGI by Immo Huneke <hunekei@logica.com>.
#      Finnish-language support by Jussi Vestman.
# 1.12 Erik Rossen fixed bugs in French and English date strings
#      and recognition of meta tags with extra spaces in attributes
# 1.13 Erik Rossen noticed a Y2K bug.
# 1.14 Matej Cepl added Czech support.
# 1.99.0 Rewrite of sitemap-1.9 in Python by Tom Bryan <tbryan@python.net>
#        Updated by Tom Bryan to incorporate changes through sitemap-1.13
# 2.0 Czech support merged in by ESR.  First public Python version.
# 2.1 Spanish support from  Pablo Marin Ramon <pabmara@inf.upv.es>.
#     Documentation masters moved from POD to DocBook.
# 2.2 Minor corrections to Czech localization by Matej Cepl.
# 2.3 Make attribute recognition a little smarter.




