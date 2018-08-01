import salt.client
caller = salt.client.Caller('/etc/salt/minion')
caller.sminion.functions['event.send'](
    'salt/beacon/minion1/inotify//home/vagrant/importantfile',
    {
    "_stamp": "2018-05-16T10:58:25.264779",
    "change": "IN_MODIFY",
    "id": "minion1",
    "path": "/home/vagrant/importantfile",
    "ASN": "AS25361"
    }
)
