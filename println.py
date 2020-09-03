import sublime
import sublime_plugin
import re
from collections import OrderedDict


class SurroundWithPrintCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				line = self.view.line(region)
				lineContents = self.view.substr(line)
				indent = re.findall(r'^\s*', lineContents)[0]
				resultText = indent+ 'print(' + lineContents.strip() + ')'
				self.view.replace(edit, line, resultText)
				(row,col) = self.view.rowcol(region.begin())
				self.view.run_command("goto_line", {"line": row+2})


class UniqueRowsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		lines = contents.split('\n')
		lines = [line.strip() for line in lines]
		distinct_lines = list(OrderedDict.fromkeys(lines))
		text = '\n'.join(distinct_lines)
		self.view.replace(edit, sublime.Region(0, self.view.size()), text)


