Name:		texlive-hulipsum
Version:	56848
Release:	1
Summary:	Hungarian dummy text (Lorum ipse)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hulipsum
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lorem ipsum is an improper Latin filler dummy text, cf. the
lipsum package. It is commonly used for demonstrating the
textual elements of a document template. Lorum ipse is a
Hungarian variation of Lorem ipsum. (Lorum is a Hungarian card
game, and ipse is a Hungarian slang word meaning bloke.) With
this package you can typeset 150 paragraphs of Lorum ipse. All
paragraphs are taken with permission from
http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy
and David Takacs) for their work.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hulipsum
%{_texmfdistdir}/tex/latex/hulipsum
%doc %{_texmfdistdir}/doc/latex/hulipsum

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
