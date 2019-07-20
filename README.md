Online judge aware Rust IDE
==============================
<a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

[![Travis](https://img.shields.io/travis/fukatani/rujaion.svg)](https://travis-ci.org/fukatani/rujaion)

![screen_shot](https://github.com/fukatani/rust-gui-debugger/blob/master/doc/debug.png)

Introduction
==============================
Lightweight rust GUI Debugger based on PyQt and rust-gdb.

Current version is alpha, some function is not implemented. 

Support one file project only.

Feature
==============================
* GUI debug
* Online judge testcases downloading and testing. (based on online-judge-tools)
* Debug with online judge testcases
* Do online judge submission
* Completer and jumper (based on racer) 
* Auto Formatting (based on rustfmt)
* Rust REPL (based on evcxr_repl)
* Live Templates (IntelliJ style)
* Contest Task Browsing

Software Requirements
==============================
* Python (3.5 or later)
* PyQt5
* PyQtWebEngine
* pexpect
* online-judge-tools (6.1 or later)
* evcxr_repl
* rustfmt
* racer


Usage
==============================

```bash
$ git clone https://github.com/fukatani/rujaion.git
$ cd rujaion
$ python3 setup.py install
$ rujaion_main.py
```

KeyBinds
==============================
- Open File (Ctrl + o)
- Save File (Ctrl + s)
- Set or unset brake point (F5)
- Start Debug or continue (F9)
- Start Debug with downloaded testcase (F4)
- Download sample testcases (F6)
- Run (Ctrl + F9)
- Next (F8)
- Step in (F7)
- Step out (Shift + F8)
- Jump to definition (F2)
- Terminate debug process (Esc)
- display value (editting display widget "Name" columns)
- Comment out (Ctrl + /)
- Toggle Show/Hide Browser Widget (F11)
- Toggle Show/Hide Console Widget (F12)

Contest Task Browsing
==============================
![browse](https://github.com/fukatani/rust-gui-debugger/blob/master/doc/browse.png)

You can browse contest task by Dock Browser Widget.
You can hide (or show) browser, press F11 key.
If page URL is contest task page, contest task is downloaded automatically by online-judge-tools.
