# Makefile for the sitemap distribution

# Don't forget to update the spec file.
VERS=$(shell sed <sitemap.spec -n -e '/Version: \(.*\)/s//\1/p')

MANDIR=/usr/share/man/man1
BINDIR=/usr/bin

all: sitemap-$(VERS).tar.gz

install: sitemap.1
	cp sitemap $(BINDIR)
	cp sitemap.1 $(MANDIR)/sitemap.1

sitemap.1: sitemap.xml
	xmlto man sitemap.xml
 
SOURCES = README sitemap sitemap.xml sitemap.1 Makefile sitemaprc sitemap.spec ChangeLog NEWS

sitemap-$(VERS).tar.gz: $(SOURCES)
	mkdir sitemap-$(VERS)
	cp $(SOURCES) sitemap-$(VERS)
	tar -czf sitemap-$(VERS).tar.gz sitemap-$(VERS)
	rm -fr sitemap-$(VERS)
	ls -l sitemap-$(VERS).tar.gz

dist: sitemap-$(VERS).tar.gz

release: sitemap-$(VERS).tar.gz sitemap.html
	shipper -f; rm -f CHANGES ANNOUNCE* *.1 *.html *.rpm *.lsm MANIFEST
