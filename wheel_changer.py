import re
import sublime, sublime_plugin

class WheelChangerCommand(sublime_plugin.TextCommand):
	''' cool Wheeler. 
	Simple command to chage digits or lists by mouse wheel 
	On future: lists+options+diff file-types'''
	def run(self, edit, back=False, step=1):
		settings = sublime.load_settings('wheel_changer.sublime-settings')
		lists = settings.get('lists', [])
		self.anew = settings.get('anew', True)
		dec_ptrn = settings.get('decimal_pattern', "[+-]?\d+[.\d]*")
		dec_re = re.compile(dec_ptrn)
		sels = self.view.sel()
		all_lists = []
		self.dic_repl = {}
		self.not_in = []
		for v in lists:
			if not isinstance(v, list):
				continue
			for vv in v:
				if not back:
					if self.anew or not v.index(vv)-1 < 0:
						var = v[v.index(vv)-1]
					else:
						var = v[0]
				else:
					if v.index(vv)+1 >= len(v):
						if self.anew:
							var = v[v.index(vv)-len(v)-1]
						else:
							var = v[len(v)-1]
					else:
						var = v[v.index(vv)+1]
				self.dic_repl[ str(vv) ] = str(var)
		
		for sel in sels:
			l, r = sel.a, sel.b
			if(l == r):
				sel = self.view.word(sel)
				pre = self.view.substr(sublime.Region(sel.a-1,sel.a))
				if pre=='-' or pre=='+':
					sel = sublime.Region(sel.a-1,sel.b)
			sel_str = self.view.substr(sel)
			findes = dec_re.findall(sel_str)
			for f in findes:
				dig = self.isnumeric(f)
				print dig
				if not dig == None:
					if not back:
						dig += step
					else:
						dig -= step
					print dig
					self.dic_repl[ str(f) ] = str(dig)
			new_str = self.replace_all(sel_str)
			self.view.replace(edit,sel,new_str)

	def isnumeric(self, txt):
		try:
			if(txt.__contains__('.')):
				return float(txt)
			else:
				return int(txt)
		except ValueError:
			return None

	def replace_all(self, text):
		for i, j in self.dic_repl.iteritems():
			if not i in self.not_in:
				if text.__contains__(i):
					text = text.replace(i, j)
					self.not_in.append(j)
		return text