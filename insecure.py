#!/usr/bin/env python3
"""
OWASP insecure!

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__VERSION__ = '0.1'

import sys
import argparse

# Import framework
from core import initial

def cui(args, format_help):
	core = initial.initialize
	if args:
		option = args[0]
		if option in ['-v', '--version']:
			print(f"OWASP INSECURE V.{__VERSION__}")
			exit(0)
		if not option or option not in ['-e', '--execute', '-s', '--start']:
			print(format_help)
			exit(0)
		core = core('execute')
		if option in ['-e', '--execute', '-s', '--start']:
			core.onecmd(' '.join(args[1:]))
			if option in ['-e', '--execute']:
				exit(0)
	else:
		core = core('run')

	while True:
		try:
			core.cmdloop()
			break
		except KeyboardInterrupt:
			print('\n[!] Use exit command to exit')
		except Exception as e:
			raise e

if __name__ == '__main__':
	desc = 'insecure -h'
	parse = argparse.ArgumentParser(description=desc)
	parse.add_argument('-e', help='execute a command and exit', metavar='execute', dest='execute', action='store')
	parse.add_argument('-s', help='run a command without exit', metavar='start', dest='start', action='store')
	parse.add_argument('-v', help='show version and exit', action='version', version=f"OWASP INSECURE V.{__VERSION__}")
	format_help = parse.format_help()
	argv = [f'"{arg}"' if ' ' in arg else arg for arg in sys.argv[1:]]
	cui(argv, format_help)
