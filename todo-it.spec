# -*- mode: python -*-

block_cipher = None


a = Analysis(['todoit_website/manage.py'],
             pathex=["/media/kevinn09/KEVIN'S USB/RPI/Semester_8_2018/SD&D/todo-it"],
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
          name='todo-it',
          debug=True,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
