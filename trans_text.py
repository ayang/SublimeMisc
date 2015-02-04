import sublime, sublime_plugin

class TransTextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		for sel in sels:
			text = self.view.substr(sel)
			text = "{{ _('%s') }}" % text
			self.view.replace(edit, sel, text)
