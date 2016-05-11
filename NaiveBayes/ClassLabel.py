
def groupClasses(classColumn):
        if classColumn == 'apache2.' : return 2
        if classColumn == 'back.' :return 2
        if classColumn == 'buffer_overflow.' : return 3
        if classColumn == 'ftp_write.' : return 4
        if classColumn == 'guess_passwd.' : return 4
        if classColumn == 'httptunnel.' : return 4
        if classColumn == 'httptunnel.' : return 3
        if classColumn == 'imap.' : return 4
        if classColumn == 'ipsweep.' : return 1
        if classColumn == 'land.' : return 2
        if classColumn == 'loadmodule.' : return 3
        if classColumn == 'mailbomb.' : return 2
        if classColumn == 'mscan.' : return 1
        if classColumn == 'multihop.' : return 4
        if classColumn == 'multihop.' : return 3  # note that this is a duplicate
        if classColumn == 'named.' : return 4
        if classColumn == 'neptune.' : return 2
        if classColumn == 'nmap.' : return 1
        if classColumn == 'perl.' : return 3
        if classColumn == 'phf.' : return 4
        if classColumn == 'pod.' : return 2
        if classColumn == 'portsweep.' : return 1
        if classColumn == 'processtable.' : return 2
        if classColumn == 'ps.' : return 3
        if classColumn == 'rootkit.' : return 3
        if classColumn == 'saint.' : return 1
        if classColumn == 'satan.' : return 1
        if classColumn == 'sendmail.' : return 4
        if classColumn == 'smurf.' : return 2
        if classColumn == 'snmpgetattack.' : return 4
        if classColumn == 'snmpguess.' : return 4
        if classColumn == 'sqlattack.' : return 3
        if classColumn == 'teardrop.' : return 2
        if classColumn == 'udpstorm.' : return 2
        if classColumn == 'warezmaster.' : return 2
        if classColumn == 'worm.' : return 4
        if classColumn == 'xlock.' : return 4
        if classColumn == 'xsnoop.' : return 4
        if classColumn == 'xterm.' : return 3
        if classColumn == 'normal.' : return 0
        # training attack types

        if classColumn == 'back.' : return 2
        if classColumn == 'buffer_overflow.' : return 3
        if classColumn == 'ftp_write.' : return 4
        if classColumn == 'guess_passwd.' : return 4
        if classColumn == 'imap.' : return 4
        if classColumn == 'ipsweep.' : return 1
        if classColumn == 'land.' : return 2
        if classColumn == 'loadmodule.' : return 3
        if classColumn == 'multihop.' : return 4
        if classColumn == 'neptune.' : return 2
        if classColumn == 'nmap.' : return 1
        if classColumn == 'perl.' : return 3
        if classColumn == 'phf.' : return 4
        if classColumn == 'pod.' : return 2
        if classColumn == 'portsweep.' : return 1
        if classColumn == 'rootkit.' : return 3
        if classColumn == 'satan.' : return 1
        if classColumn == 'smurf.' : return 2
        if classColumn == 'spy.' : return 4
        if classColumn == 'teardrop.' : return 2
        if classColumn == 'warezclient.' : return 4
        if classColumn == 'warezmaster.' : return 4
