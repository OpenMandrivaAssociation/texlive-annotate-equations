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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands that make it easy to highlight terms in
equations and add annotation labels using TikZ. It should work with
pdfLaTeX as well as LuaLaTeX.

