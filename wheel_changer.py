import re
import sublime, sublime_plugin

if sublime.version() < '3000':
	# we are on ST2 and Python 2.X
	_ST3 = False
else:
	_ST3 = True

class WheelChangerCommand(sublime_plugin.TextCommand):
	''' cool Wheeler. 
	Simple command to chage digits or lists by mouse wheel
	On future: file-types'''
	def run(self, edit, back=False, step=1):
		digits_list = range(10)
		addi_ls = ['-','+', '.']
		if _ST3:
			digits_list = list(digits_list)+addi_ls
		else:
			digits_list = digits_list+addi_ls
		settings = sublime.load_settings('WheelChanger.sublime-settings')
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
							var = v[0]
						else:
							var = v[len(v)-1]
					else:
						var = v[v.index(vv)+1]
				self.dic_repl[ str(vv) ] = str(var)
		for sel in sels:
			l, r = sel.a, sel.b
			if l == r:
				pre = self.view.substr(sublime.Region(l-1,l))
				while pre in digits_list or self.isnumeric(pre) in digits_list:
					l -= 1
					pre = self.view.substr(sublime.Region(l-1,l))
				post = self.view.substr(sublime.Region(r,r+1))
				while post in digits_list or self.isnumeric(post) in digits_list:
					r += 1
					post = self.view.substr(sublime.Region(r,r+1))
				fregion = sublime.Region(l,r)
				sstr = self.view.substr(fregion)
				ss = dec_re.findall(sstr)
				if(len(ss)):
					sel = fregion
				else:
					wsl = self.view.word(sel)
					if self.view.substr(wsl) in self.dic_repl:
						sel = wsl
					else:
						continue
			sel_str = self.view.substr(sel)
			findes = dec_re.findall(sel_str)
			if len(findes)>0:
				for f in findes:
					dig = self.isnumeric(f)
					if not dig == None:
						if not back:
							dig += step
						else:
							dig -= step
						self.dic_repl[ str(f) ] = str(dig)
			new_str = self.replace_all(sel_str)
			self.view.replace(edit,sel,new_str)

	def isnumeric(self, txt):
		'''Test if txt is numeric'''
		try:
			if(txt.__contains__('.')):
				return float(txt)
			else:
				return int(txt)
		except ValueError:
			return None

	def replace_all(self, text):
		'''Replace all keys to items from self.dic_repl in text'''
		if _ST3:
			items = self.dic_repl.items()
		else:
			items = self.dic_repl.iteritems()
		for i, j in items:
			if not i in self.not_in:
				if text.__contains__(i):
					text = text.replace(i, j)
					self.not_in.append(j)
		return text