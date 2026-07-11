%global tl_name hulipsum
%global tl_revision 77317

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Hungarian dummy text (Lorum ipse)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hulipsum
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hulipsum.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Lorem ipsum is an improper Latin filler dummy text, cf. the lipsum
package. It is commonly used for demonstrating the textual elements of a
document template. Lorum ipse is a Hungarian variation of Lorem ipsum.
(Lorum is a Hungarian card game, and ipse is a Hungarian slang word
meaning bloke.) With this package you can typeset 150 paragraphs of
Lorum ipse. All paragraphs are taken with permission from
http://www.lorumipse.hu. Thanks to Lorum Ipse Lab (Viktor Nagy and David
Takacs) for their work.

