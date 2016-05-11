def groupClasses(classColumn):
    category={}
    category["apache2."] = 2
    category["back."] = 2
    category["buffer_overflow."] = 3
    category["ftp_write."] = 4
    category["guess_passwd."] = 4
    category["httptunnel."] = 4
    category["httptunnel."] = 3
    category["imap."] = 4
    category["ipsweep."] = 1
    category["land."] = 2
    category["loadmodule."] = 3
    category["mailbomb."] = 2
    category["mscan."] = 1
    category["multihop."] = 4
    category["multihop."] = 3  # note that this is a duplicate
    category["named."] = 4
    category["neptune."] = 2
    category["nmap."] = 1
    category["perl."] = 3
    category["phf."] = 4
    category["pod."] = 2
    category["portsweep."] = 1
    category["processtable."] = 2
    category["ps."] = 3
    category["rootkit."] = 3
    category["saint."] = 1
    category["satan."] = 1
    category["sendmail."] = 4
    category["smurf."] = 2
    category["snmpgetattack."] = 4
    category["snmpguess."] = 4
    category["sqlattack."] = 3
    category["teardrop."] = 2
    category["udpstorm."] = 2
    category["warezmaster."] = 2
    category["worm."] = 4
    category["xlock."] = 4
    category["xsnoop."] = 4
    category["xterm."] = 3
    category["normal."] = 0
    # training attack types

    category["back."] = 2
    category["buffer_overflow."] = 3
    category["ftp_write."] = 4
    category["guess_passwd."] = 4
    category["imap."] = 4
    category["ipsweep."] = 1
    category["land."] = 2
    category["loadmodule."] = 3
    category["multihop."] = 4
    category["neptune."] = 2
    category["nmap."] = 1
    category["perl."] = 3
    category["phf."] = 4
    category["pod."] = 2
    category["portsweep."] = 1
    category["rootkit."] = 3
    category["satan."] = 1
    category["smurf."] = 2
    category["spy."] = 4
    category["teardrop."] = 2
    category["warezclient."] = 4
    category["warezmaster."] = 4
    return category