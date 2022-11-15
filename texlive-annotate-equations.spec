Name:		texlive-annotate-equations
Version:	62932
Release:	1
Summary:	Easily annotate math equations using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/annotate-equations
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate-equations.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate-equations.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands that make it easy to highlight
terms in equations and add annotation labels using TikZ. It
should work with pdfLaTeX as well as LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/annotate-equations
%doc %{_texmfdistdir}/doc/latex/annotate-equations

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
