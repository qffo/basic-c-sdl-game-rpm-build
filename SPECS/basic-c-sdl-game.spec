Name: basic-c-sdl-game
Version: 1.0
Release: alt1
Summary: A basic C SDL2-based grid game using CMake
License: MIT
Group: Games/Arcade
URL: https://gitlab.com/aminosbh/basic-c-sdl-game
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkg-config

%description
This is a basic SDL2-based game written in C, utilizing CMake as the build system. The game serves as a template for creating grid-based games. It can be easily customized for any other grid-based games by modifying the source code.

%description -l ru_RU.UTF-8
Простая игра на базе SDL2, написанная на языке C, использующая CMake как систему сборки. Игра служит шаблоном для создания игр с сеткой и может быть легко настроена для других игр, используя эту же основу.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_datadir/%name
install -d %buildroot%_libdir
install -d %buildroot%_docdir/%name

install -m 755 x86_64-alt-linux/%name %buildroot%_bindir/

install -d %buildroot%_desktopdir

echo "[Desktop Entry]
Name=Basic C SDL Game
Comment=A basic C SDL2-based grid game
Exec=%_bindir/basic-c-sdl-game
Terminal=false
Type=Application
Categories=Game;" > %buildroot%_desktopdir/basic-c-sdl-game.desktop

%files
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop

%changelog
* Thu Jan 05 2025 Viktor Viktor <viktor@example.com> 1.0-alt1
- Initial package creation for basic SDL2-based game
