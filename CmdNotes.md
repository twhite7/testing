# Cmd Notes

## Basic Maneuvering

Make a **rem**ark or comment (that appears but doesn't do anything).
```cmd
rem TypeWhateverYouWantHereItWontDoAnything
```
```cmd
:: UsingColonsIsAnotherWayToMakeComments
```

Get help information on how to use a command.
```cmd
[Command] /?
```

List all directories (folders) in current folder.
```cmd
dir
:: Adding "/P" after dir will only display one page of results at a time.
```

**C**hange **D**irectory to a child (lower) directory.
```cmd
cd [ChildDirectory]
```

**C**hange **D**irectory to the parent (higher) directory.
```cmd
cd ..
```

**C**hange **D**irectory to any specific 
```cmd
cd [destination]
rem Example: cd C:\Users\Joe\Desktop 
```


## System Status

Query all current sessions
```cmd
qwinsta
```

Display all current user sessions
```cmd
quser
```

List Tasks
```cmd
tasklist (local)
:: /s remote computer 
:: /u username 
:: /P password
```

Kill Tasks
```cmd
taskkill /F /T
:: /IM process name
:: /PID process pid
:: /S remote system /U username /P password
```

Export Event Logs
```cmd
wevtutil export-log (System/Security/Application) events.evtx
```

Last N event logs with id
```cmd
wevtutil query-events (System/Security/Application) /count:20 /rd:true /format:text /q:"Event[System[(EventID=12)]]"
:: rd - most recent first
```

## File Commands

View file contents
```cmd
type filename
(or) more filename
```

Sort file contents
```cmd
sort < filename
```

Delete a single file
```cmd
del filename
```

Create empty file
```cmd
type nul > filename
```

Rename file
```cmd
ren file newname

:: Change all file extensions
ren  *  *.txt

:: Append extension to all files
ren  *  *?.bak

:: Rename all .log files to .txt files in current directory and subdirectories
For /R %%G in (*.LOG) do ren "%%G" "%~nG.TXT"
```

Copy files/folders
```cmd
robocopy source destination
robocopy source destination file_selectors
:: /E copy all subfolders
:: /MOVE delete from source after copy
:: /L don't copy but list operation
```

Replace files
```cmd
replace Source Destination

:: Update the files in C:\delivery\ with the .exe files in C:\source files\
replace "C:\source files\*.exe" C:\delivery

:: Use /S to include all subdirectories
```

Delete directory
```cmd
rd directory
:: /S delete all files and subfolders
:: /Q no confirmation
```

Find Files / Search for files
```cmd
where /r path name
:: path can be remote, \\Server\Path
:: name allows wildcards
```

## History, Macros, and Environment Variables

Clear current command line
```cmd
Esc
```

Clear Screen (not history though!)
```cmd
cls
```

Clear History in cmd.exe session
```cmd
Alt + F7
```

View Current History in cmd.exe session
```cmd
doskey /history
```

Disable command history
```cmd
doskey /listsize=0
(use large number, then relaunch command prompt to get history back)
```

Declare a new macro
```cmd
doskey name=command

EX:
doskey note=notepad.exe
```
Note: Macros only save for current session

Delete a macro
```cmd
doskey [MacroName]=

EX:
doskey note=
```

Export list of macros
```cmd
doskey /macros >macros.cmd
for /f "tokens=*" %a in (macros.cmd) do (echo doskey %a) >> macros2.cmd
```

Restore list of macros
```cmd
macros2.cmd
```

Get environment variables
```cmd
set
```

Set an environment variable
```cmd
set name=value
setx name=value (permanent)
```

Set CMD prompt prefix
```cmd
prompt $P$G
(or) set(x) prompt=$P$G (default)

   $A  &           (Ampersand) 
   $B  |           (pipe) 
   $C  (           (Left parenthesis) 
   $D Current date 
   $E Escape code  (ASCII code 27) 
   $F  )           (Right parenthesis) 
   $G  >           (greater-than sign) 
   $H  Backspace   (erases previous character) 
   $L  <           (less-than sign) 
   $M  Display the remote name for Network drives
   $N  Current drive 
   $P  Current drive and path 
   $Q  =           (equal sign) 
   $S              (space) 
   $T  Current time 
   $V  Windows version number 
   $_  Carriage return and linefeed 
   $$  $           (dollar sign)
   $+  Will display plus signs (+) one for each level of the PUSHD directory stack
```

## Miscellaneous

Elevate current prompt to Administrator
```cmd
powershell -Command "Start-Process cmd -Verb RunAs"
```

Runas
```cmd
runas /user:DOMAIN\user program
```

Get current user name
```cmd
whoami
```

Push directory to the stack
```cmd
pushd .
(or) pushd Directory
```

Pop back to directory
```cmd
popd
```
