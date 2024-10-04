# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['03_프로그램_설치.py'],
    pathex=[],
    binaries=[],
    datas=[('erp1.png', '.'), ('erp2.png', '.'), ('erp3.png', '.'), ('erp4.png', '.'), ('ms1.png', '.'), ('ms2.png', '.'), ('ms3.png', '.'), ('ms4.png', '.'), ('ms5.png', '.'), ('ms6.png', '.'), ('ms7.png', '.'), ('ms8.png', '.'), ('talk1.png', '.'), ('talk2.png', '.'), ('vpn1.png', '.'), ('vpn2.png', '.'), ('vpn3.png', '.')],
    hiddenimports=[],
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
    name='03_프로그램_설치',
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
