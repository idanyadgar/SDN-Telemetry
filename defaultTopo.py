from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import (OVSSwitch, Agent, RemoteController)

class MyTopo(Topo):
    def build(self):
        s0 = self.addSwitch('s0')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s1, s2)

        h1 = self.addHost('laptop')
        h3 = self.addHost('printer')
        h2 = self.addHost('pc')

        self.addLink(h1, s0)
        self.addLink(h2, s3)
        self.addLink(h3, s1)

def main():
    topo = MyTopo()
    net = Mininet(topo = topo, switch = OVSSwitch, controller = RemoteController, autoSetMacs = True)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()

