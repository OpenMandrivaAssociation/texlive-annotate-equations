%global tl_name annotate-equations
%global tl_revision 67044

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Easily annotate math equations using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/annotate-equations
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate-equations.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate-equations.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands that make it easy to highlight terms in
equations and add annotation labels using TikZ. It should work with
pdfLaTeX as well as LuaLaTeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/annotate-equations
%dir %{_datadir}/texmf-dist/tex/latex/annotate-equations
%doc %{_datadir}/texmf-dist/doc/latex/annotate-equations/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/annotate-equations/README.md
%doc %{_datadir}/texmf-dist/doc/latex/annotate-equations/annotate-equations.pdf
%doc %{_datadir}/texmf-dist/doc/latex/annotate-equations/annotate-equations.tex
%{_datadir}/texmf-dist/tex/latex/annotate-equations/annotate-equations.sty
