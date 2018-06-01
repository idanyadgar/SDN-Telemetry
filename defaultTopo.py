from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import (OVSSwitch, Agent, RemoteController)
from switches.agent import OurAgent

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

        a0 = self.addAgent('a0')
        a1 = self.addAgent('a1')
        a2 = self.addAgent('a2')
        a3 = self.addAgent('a3')

        self.attach(a0, s0)
        self.attach(a1, s1)
        self.attach(a2, s2)
        self.attach(a3, s3)

def main():
    topo = MyTopo()
    net = Mininet(topo = topo, switch = OVSSwitch, controller = RemoteController, agent = OurAgent, autoSetMacs = True)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()

