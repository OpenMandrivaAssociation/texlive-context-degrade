# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-degrade
# catalog-date 2008-08-18 23:54:09 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-degrade
Version:	20170414
Release:	2
Summary:	Degrading JPEG images in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-degrade
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-degrade.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-degrade.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
TeXLive context-degrade package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/degrade/t-degrade.tex
%doc %{_texmfdistdir}/doc/context/third/degrade/degrade-demo.pdf
%doc %{_texmfdistdir}/doc/context/third/degrade/degrade-doc.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080818-2
+ Revision: 750492
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080818-1
+ Revision: 718127
- texlive-context-degrade
- texlive-context-degrade
- texlive-context-degrade
- texlive-context-degrade

