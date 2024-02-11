let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11";
  pkgs = import nixpkgs { config = {}; overlays = []; };

  git = pkgs.git.overrideAttrs (oldAttrs: rec {
    version = "2.42.0";
  });
in

pkgs.mkShell {
  packages = with pkgs; [
    git
    python311
    pkgs.pdm
  ];

  shellHook = ''
    export NIX_SHELL_DIR=$PWD/.nix-shell
    export LC_ALL=C
    export LANG=C.utf8
  '';
}