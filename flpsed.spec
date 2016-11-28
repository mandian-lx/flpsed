Summary:	A Postscript and PDF annotator
Name:		flpsed
Version:	0.7.3
Release:	0
License:	GPLv3+
Group:		Office
URL:		http://flpsed.org/%{name}.html
Source0:	http://flpsed.org/%{name}-%{version}.tar.gz

BuildRequires:	fltk-devel
BuildRequires: 	imagemagick
BuildRequires:	librsvg2
BuildRequires: 	pkgconfig(x11)

Requires:	ghostscript-module-X
Suggests:	poppler

%description
flpsed is a WYSIWYG PostScript annotator.

You can't remove or modify existing elements of a document. But flpsed lets
you add arbitrary text lines to existing PostScript documents (PostScript
is a registered trademark of Adobe Systems Incorporated). Added lines can
later be reedited with flpsed. Using pdftops, which is part of xpdf one can
convert PDF documents to PostScript and also add text to them. flpsed is
useful for filling in forms, adding notes etc.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%doc README
%doc NEWS
%doc AUTHORS
%doc ChangeLog
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	rsvg-convert -f png -h ${d} -w ${d} %{name}.svg \
		-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
#    scacable
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps
%__install -pm 644 %{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
#    pixmap
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps/
install -dm 0755 %{buildroot}/%{_miconsdir}/
convert %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# .desktop
install -d -m 755 %{buildroot}%{_datadir}/applications/
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{name}.desktop

