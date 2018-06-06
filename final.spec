# -*- mode: python -*-

block_cipher = None


a = Analysis(['final.py'],
             pathex=['C:\\Users\\Stephie\\Documents\\Stanford\\Coterm\\cs377i\\pa3\\cs377_farm_simulation'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='final',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
