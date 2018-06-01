from mininet.node import Agent
from mininet.util import quietRun

class OurAgent(Agent):
    def __init__(self, name, *ryuArgs, **kwargs):
        ourApp = 'learning_switch.py'

        currDir = quietRun('pwd').strip('\r\n')
        ryuCoreDir = '%s/' % currDir

        if not ryuArgs:
            ryuArgs = [ryuCoreDir + ourApp]
        elif type(ryuArgs) not in (list, tuple):
            ryuArgs = [ryuArgs]

        Agent.__init__(self, name,  command='ryu-manager --verbose',
                                    cargs='--ofp-tcp-listen-port %s ' + ' '.join(ryuArgs),
                                    cdir=ryuCoreDir, **kwargs)

