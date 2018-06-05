import socket
import cmd


class ControllerCLI(cmd.Cmd):
	intro = 'Welcome to the controller CLI.\nType help or ? to list commands.\n'
	prompt = 'controller> '

	def __init__(self, sock):
		cmd.Cmd.__init__(self)
		self.sock = sock

	def do_packet_count(self, args):
		'Usage: packet_count [interval in seconds]\n'

		self.sock.send("(PacketCount ,[%s])" % args)

	def do_byte_count(self, args):
		'Usage: byte_count [interval in seconds]\n'

		self.sock.send("(ByteCount ,[%s])" % args)

	def do_EOF(self, args):
		'Usage: Ctrl+D exists the CLI\n'

		self.sock.close()

		print ''
		return True


s = socket.socket()
s.connect((socket.gethostname(), 9999))

s.send("(LearningSwitches, [])")

ControllerCLI(s).cmdloop()
