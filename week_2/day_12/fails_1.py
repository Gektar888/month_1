
dir = '''
bin    etc    lib64       mnt   run   swapfile  var
boot   home   libx32      opt   sbin  sys
cdrom  lib    lost+found  proc  snap  tmp
dev    lib32  media       root  srv   usr
'''

with open("directories.txt", "w") as f:
    f.write(dir)
with open("directories.txt", "r") as ff:
    print(ff.read())

