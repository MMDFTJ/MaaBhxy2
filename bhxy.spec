# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['bhxy.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\L\\miniconda3\\envs\\maaTest\\Lib\\site-packages\\maa\\bin', 'maa/bin'), ('C:\\Users\\L\\miniconda3\\envs\\maaTest\\Lib\\site-packages\\MaaAgentBinary', 'MaaAgentBinary')],
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
    name='BHXY',
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
