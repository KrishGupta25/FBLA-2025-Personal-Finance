# -*- mode: python ; coding: utf-8 -*-

datas = [("Quicksand-Bold.ttf", "src")]

a = Analysis(
    pathex=[src/main.py],
    binaries=[],
    datas=[],
    hiddenimports=['src/addTransaction', 'src/dataPage', 'src/detailedProjectPage', 'src/editTransaction', 'src/errorPage', 'src/HomePage', 'src/infoPage', 'src/projectsPage', 'src/removeItem', 'src/report', 'src/signUp', 'src/success'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
