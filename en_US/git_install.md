### Install from source code


<strong>Note: This is run from source code and requires some programming skills. For quick start, see
[GIA Launcher Usage](doc/install.md)</strong>

Require:

- python version [3.7.6](https://www.python.org/downloads/release/python-376/).
- [git](https://git-scm.com/download/win).
- **Open the command prompt and your IDE with administrator privileges!!! **

## Installation


1. Enter the following command to complete the download of the source code and dependencies.

   ```shell
   git clone https://github.com/infstellar/genshin_impact_assistant.git&cd genshin_impact_assistant&python setup.py install&git submodule init&git submodule update
   ```
   Windows Powershell
   ```shell
   git clone https://github.com/infstellar/genshin_impact_assistant.git;cd genshin_impact_assistant;python setup.py install;git submodule init;git submodule update
   ```

   **Notice if the submodule clones successfully at the same time! **

2. Enter the following command to run the program.

   ```shell
   python genshin_assistant.py
   ```

~~ (recommended to use VsCode, so your run and debug will have several shortcuts to run, fat good! And variable coloring Oh (doge))~~

## Update


- 使用setup.py更新:
   ```shell
   python setup.py update&git submodule update
   ```
   Windows Powershell
    ```shell
   python setup.py update;git submodule init;git submodule update
   ```

