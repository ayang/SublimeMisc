import sublime, sublime_plugin
import os, subprocess

class OpenInGvimCommand(sublime_plugin.WindowCommand):
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        else:
            sublime.status_message(__name__ + ': No file')
            return False

    def is_enabled(self):
        return True

    def run(self, *args):
        print("Opening in gvim")
        path = self.get_path()
        if not path:
            return
        view = self.window.active_view()
        if not view:
            print("view is empty")
            return

        (row, col) = view.rowcol(view.sel()[0].begin())

        subprocess.call(['gvim', '+%d' % (row+1), path])