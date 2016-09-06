# CLI-TYPESETTER

## README

The "cli-typesetter" is a project that helps typesetting a TeX file/project less pain.
Initially, user just needs to create a typesetting config file containning all desired preferences.
From later tasks such as typesetting or viewing resulted pdf file, user just runs only a simple
command.

## AUTHOR

* Doan Duy Hai
* Email: dduyhai@gmail.com
* Github: https://github.com/dduyhai/cli_typesetter.git

## CHANGELOG
  
### Version 0.1

This is testing version that offers a few number of preferences.

## INSTALL

1. Clone from github
  ```
  git clone https://github.com/dduyhai/cli_typesetter.git cli_typesetter
  ```

2. Setup 
  a. In macOS
    ```
    cd cli_typesetter
    python3 setup.py install
    ```
    Then add the installing directory to `PATH`:
    ```
    PATH=PATH:/Library/Frameworks/Python.framework/Versions/3.5/bin
    ```

  b. In Linux
    ```
    cd cli_typesetter
    python3 setup.py install --user
    ```
    Then add the install directory to `PATH`:
    ```
    PATH=PATH=${HOME}/.local/bin
    ```

## TODO

Add exception for better experience.

## DESIRED FEATURES

1. Add more tex engine such as __xelatex__.
2. Add bibliography engine such as __bibtex__ and __biber__
3. Add index engine

