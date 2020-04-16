# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['KochDrawv2.py'],
             pathex=['D:\\Files\\学习的相关资料\\研究生阶段的文件\\1.科研文件（除试验内容）\\7.Python与有限元\\0. Python_Exercise\\0.1.二级练习'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='KochDrawv2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='curve.ico')
