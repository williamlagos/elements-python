#!/usr/bin/env python
#
# This file is part of elements project.
# 
# Copyright (C) 2009-2011 William Oliveira de Lagos <william.lagos@icloud.com>
#
# Elements is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Elements is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with elements.  If not, see <http://www.gnu.org/licenses/>.
#

# from elements.engine.ranking import Nodes
from elements.server.http import Runtime,Coronae
import sys,json

class NodeSample(Coronae):
	def get(self):
		# nodes = Nodes()
		# nodes.prepare_elements('objects.json')
		# self.write('<pre>'+self.to_json(nodes.elements)+' %i</pre>'%nodes.tree.depth)
		self.write('<pre>%s</pre>'%json.load(open('elements.json')))

def main(argv):
	runtime = Runtime([('/',NodeSample)])
	runtime.run()

if __name__ == "__main__": main(sys.argv)
