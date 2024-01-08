# -*- mode: python -*-

block_cipher = None


a = Analysis(['./src/main.py'],
             pathex=['C:\\Users\\firep\\vsc_folders\\FBLA-23-24'], # just the directory not the file
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('Quicksand-Bold.ttf','C:\\Users\\firep\\vsc_folders\\FBLA-23-24\\Quicksand-Bold.ttf', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)

exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='CTE Partner Pro',
      debug=False,
      strip=False,
      upx=True,
      console=False # set True if command prompt window needed
)