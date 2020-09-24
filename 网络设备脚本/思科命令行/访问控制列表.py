import functools
import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 异常
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 访问控制列表 as 南向列表
from .常量 import *
#===============================================================================
# 生成&解析
#===============================================================================
c标准 = "standard"
c扩展 = "extended"
#访问控制列表序号范围
ca标准范围 = (range(1, 100), range(1300, 2000))
ca扩展范围 = (range(100, 200), range(2000, 2700))
class F序号范围检查:
	def __init__(self, aa范围, a异常文本):
		self.ma范围 = aa范围
		self.m异常文本 = a异常文本
	def __call__(self, a序号, a异常 = True):
		if type(a序号) == int:
			for v in self.ma范围:
				if a序号 in v:
					return True
			if a异常:
				raise ValueError(a错误文本)
			return False
		return False
fi标准范围 = F序号范围检查(ca标准范围, "标准访问控制列表号码范围应为1~99,1300~1999")
fi扩展范围 = F序号范围检查(ca扩展范围, "扩展访问控制列表号码范围应为100~199,2000~2699")
#端口号
class C端口号到字符串(北向列表.I端口号到字符串):
	def f大于(self, a值):
		return "gt " + str(a值)
	def f小于(self, a值):
		return "lt " + str(a值)
	def f等于(self, a序列):
		return "eq " + " ".join(字符串.ft字符串序列(a序列))
	def f不等于(self, a序列):
		return "neq " + " ".join(字符串.ft字符串序列(a序列))
	def f范围(self, a值: range):
		return "range %d %d" % (a值.start, a值.stop - 1)
g端口号到字符串 = C端口号到字符串()
f生成端口 = functools.partial(南向列表.f生成端口, g端口号到字符串)
#规则序号
def f生成规则序号4(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return a序号
def f生成规则序号6(a序号):
	if a序号 == None or a序号 < 0:
		return ""
	else:
		return "sequence " + str(a序号)
#协议
#允许
f生成允许 = functools.partial(南向列表.f生成允许, 南向列表.c允许元组)
#地址
def f生成地址标准4(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return v地址.fg地址s()
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
def f生成地址扩展4(a地址):
	"转成字符串"
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址4.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return "%s %s" % (v地址.fg网络号s(), v地址.fg反掩码s())
def f生成地址6(a地址):
	if not a地址:
		return "any"
	v地址 = 地址.S网络地址6.fc自动(a地址)
	if v地址.fi主机():
		return "host %s" % (v地址.fg地址s())
	elif v地址.fi空():
		return "any"
	else:
		return str(v地址)
#===============================================================================
# 类
#===============================================================================
class I访问控制列表(南向列表.I列表配置):
	def __init__(self, a, a名称, a类型: str = "", a协议: str = "ip"):
		南向列表.I列表配置.__init__(self, a)
		self.m名称 = a名称
		self.m类型 = a类型
		self.m协议 = a协议
	def fg模式参数(self):
		return (self.m类型, self.m名称)
	def fg进入命令(self):
		return 命令.C命令(self.m协议, "access-list", self.m类型, self.m名称)
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("show", self.m协议, "access-list", self.m名称)
		if a序号 != None:
			v命令 += f"| include ^____{a序号}_"
		return v命令
	def f添加规则(self, a序号, a规则):
		raise NotImplementedError()
	def f删除规则(self, a序号: int):
		self.f执行当前模式命令(c不 + str(a序号))
	def fs规则(self, a序号 = 北向列表.c空序号, a规则 = 北向列表.c空规则, a操作 = 操作.E操作.e设置):
		v操作 = 操作.f解析操作(a操作)
		if v操作 in (操作.E操作.e设置, 操作.E操作.e新建, 操作.E操作.e添加):
			self.f添加规则(a序号, a规则)
		elif v操作 == 操作.E操作.e修改:
			v序号 = a序号 if a序号 >= 0 else a规则.m序号
			v规则 = self.fg规则(v序号)
			v规则.f更新_规则(a规则)
			self.f删除规则(v序号)
			self.f添加规则(v序号, v规则)
		elif v操作 == 操作.E操作.e删除:
			self.f删除规则(a序号)
		else:
			raise 异常.X操作()
	def fe规则0(self, af解析):
		v命令 = self.fg显示命令()
		v输出 = self.m设备.f执行显示命令(v命令)
		v位置 = 字符串.f连续找最后(v输出, "access list", "\n")
		for v行 in v输出[v位置+1:].split("\n"):
			if v行[0:4] != "    ":
				continue
			yield af解析(v行)
	def fe规则(self):
		return self.fe规则0(self.f解析规则)
	def fg规则(self, a序号):
		v命令 = self.fg显示命令(a序号)
		v输出 = self.m设备.f执行显示命令(v命令)
		v规则 = self.f解析规则(v输出)
		return v规则
	@staticmethod
	def f解析规则(self):
		raise NotImplementedError()
#===============================================================================
class C标准4(I访问控制列表):
	def __init__(self, a, a名称):
		I访问控制列表.__init__(self, a, a名称, a类型 = "standard")
	def f添加规则(self, a序号, a规则):
		v序号 = f生成规则序号4(a序号)
		v允许 = f生成允许(a规则.m允许)
		v源地址 = f生成地址标准4(a规则.m源地址)
		v命令 = f"{v序号} {v允许} {v源地址}"
		self.f执行当前模式命令(v命令)
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号4()
		v规则.m允许 = v解析器.f允许()
		v规则.m源地址 = v解析器.f地址标准4()
		return v规则
class C扩展4(I访问控制列表):
	def __init__(self, a, a名称):
		I访问控制列表.__init__(self, a, a名称, a类型 = "extended")
	def f添加规则(self, a序号, a规则):
		v命令 = 命令.C命令()
		v命令 += f生成规则序号4(a序号)
		v命令 += f生成允许(a规则.m允许)
		#确定
		v命令 += 南向列表.ca协议到字符串4[a规则.m协议]
		v层 = 协议.f取协议层(a规则.m协议)
		#按层
		if v层 == 3:
			v命令 += f生成地址扩展4(a规则.m源地址)
			v命令 += f生成地址扩展4(a规则.m目的地址)
		elif v层 == 4:
			v命令 += f生成地址扩展4(a规则.m源地址)
			v命令 += f生成端口(a规则.m源端口)
			v命令 += f生成地址扩展4(a规则.m目的地址)
			v命令 += f生成端口(a规则.m目的端口)
		else:
			raise NotImplementedError("迷之逻辑")
		#执行命令
		self.f执行当前模式命令(v命令)
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m序号 = v解析器.f序号4()
		v规则.m允许 = v解析器.f允许()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址扩展4()
		v规则.m源端口 = v解析器.f端口号()
		v规则.m目的地址 = v解析器.f地址扩展4()
		v规则.m目的端口 = v解析器.f端口号()
		return v规则
#===============================================================================
class C六(I访问控制列表):
	"互联网协议第6版命名访问控制列表"
	def __init__(self, a, a名称):
		I访问控制列表.__init__(self, a, a名称, a协议 = "ipv6")
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("show", self.m协议, "access-list", self.m名称)
		if a序号 != None:
			v命令 += f"| include sequence_{a序号}$"
		return v命令
	def f添加规则(self, a序号, a规则):
		v命令 = 命令.C命令()
		v命令 += f生成规则序号6(a序号)
		v命令 += f生成允许(a规则.m允许)
		#确定
		v命令 += 南向列表.ca协议到字符串6[a规则.m协议]
		v层 = 协议.f取协议层(a规则.m协议)
		#按层
		if v层 == 3:
			v命令 += f生成地址6(a规则.m源地址)
			v命令 += f生成地址6(a规则.m目的地址)
		elif v层 == 4:
			v命令 += f生成地址6(a规则.m源地址)
			v命令 += f生成端口(a规则.m源端口)
			v命令 += f生成地址6(a规则.m目的地址)
			v命令 += f生成端口(a规则.m目的端口)
		else:
			raise NotImplementedError("迷之逻辑")
		#执行命令
		self.f执行当前模式命令(v命令)
	@staticmethod
	def f解析规则(a规则: str):
		v解析器 = C规则解析器(a规则)
		v规则 = 北向列表.S规则()
		v规则.m允许 = v解析器.f允许()
		v规则.m协议 = v解析器.f协议()
		v规则.m源地址 = v解析器.f地址6()
		v规则.m源端口 = v解析器.f端口号()
		v规则.m目的地址 = v解析器.f地址6()
		v规则.m目的端口 = v解析器.f端口号()
		v规则.m序号 = v解析器.f序号6()
		return v规则
#===============================================================================
class C助手(北向列表.I助手):
	#元组结构含意:(序号开始, 序号结束（不包含）, 到目标序号的增加值)
	c计算标准4 = [(0, 99, 1), (99, 799, 1200)]
	c计算扩展4 = [(0, 99, 100), (99, 799, 1900)]
	c反算标准4 = [(1, 100, -1), (1300, 2000, -1200)]
	c反算扩展4 = [(100, 200, -100), (2000, 2700, -1900)]
	def F计算(a0, a1):
		@staticmethod
		def f(n):
			v类型 = type(n)
			if v类型 == int:
				if n in range(a0[0], a0[1]):
					return n + a0[2]
				elif n in range(a1[0], a1[1]):
					return n + a1[2]
				else:
					raise ValueError("n超出范围")
			else:
				return n
		return f
	f计算标准4 = F计算(*c计算标准4)
	f计算扩展4 = F计算(*c计算扩展4)
	f反算标准4 = F计算(*c反算标准4)
	f反算扩展4 = F计算(*c反算扩展4)
	def F判断类型(a0, a1, a类型):
		@staticmethod
		def f(n):
			try:
				v = int(n)
				if v in range(a0[0], a0[1]):
					return a类型
				elif v in range(a1[0], a1[1]):
					return a类型
				else:
					return None
			except:
				return None
		return f
	f判断标准4 = F判断类型(*c反算标准4, 北向列表.E类型.e标准4)
	f判断扩展4 = F判断类型(*c反算扩展4, 北向列表.E类型.e扩展4)
	#实现
	@staticmethod
	def ft特定序号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f计算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f计算扩展4(n)
		else:
			raise ValueError("类型错")
	@staticmethod
	def ft统一序号(n, a类型):
		if a类型 == 北向列表.E类型.e标准4:
			return C助手.f反算标准4(n)
		elif a类型 == 北向列表.E类型.e扩展4:
			return C助手.f反算扩展4(n)
		else:
			raise ValueError("类型错")
	@staticmethod
	def f判断类型(n):
		v = C助手.f判断标准4(n)
		if v:
			return v
		v = C助手.f判断扩展4(n)
		return v
#===============================================================================
# 解析器
#===============================================================================
class C规则解析器:
	def __init__(self, a文本):
		self.m取词 = 字符串.C推进取词(a文本)
	def f允许(self):
		return self.m取词.f取词推进() == "permit"
	def f协议(self):
		return 南向列表.ca字符串到协议[self.m取词.f取词推进()]
	def f序号4(self):
		return int(self.m取词.f取词推进())
	def f序号6(self):
		self.m取词.f推进()	#"sequence"
		return int(self.m取词.f取词推进())
	def f地址标准4(self):	#标准4
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		if v词0[-1] == ",":	#有通配符
			v词0 = v词0[:-1]
			self.m取词.f推进()
			self.m取词.f推进()
			v词1 = self.m取词.f取词推进()
			v掩码 = 地址.S网络地址4.c全f - 地址.S网络地址4.f地址字符串转整数(v词1)
			return 地址.S网络地址4.fc地址掩码(v词0, v掩码)
		else:	#主机地址
			return 地址.S网络地址4.fc主机地址字符串(v词0)
	def f地址扩展4(self):	#扩展4
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址4.fc主机地址字符串(v词)
		v词1 = self.m取词.f取词()	#通配符
		if not v词1:
			return 地址.S网络地址4.fc主机地址字符串(v词0)
		self.m取词.f推进()
		v掩码 = 地址.S网络地址4.c全f - 地址.S网络地址4.f地址字符串转整数(v词1)
		return 地址.S网络地址4.fc地址掩码(v词0, v掩码)
	def f地址6(self):	#六
		v词0 = self.m取词.f取词推进()
		if v词0 == "any":
			return None
		elif v词0 == "host":
			v词1 = self.m取词.f取词推进()
			return 地址.S网络地址6.fc自动(v词1)
		return 地址.S网络地址6.fc自动(v词0)
	def f端口号(self):
		v词 = self.m取词.f取词()
		if not v词 in C规则解析器.ca端口号运算函数:
			return None	#不是端口号
		self.m取词.f推进()
		vf端口号 = C规则解析器.ca端口号运算函数[v词]
		return vf端口号(self)
	def f端口号_大于(self):
		return 北向列表.S端口号.fc大于(int(self.m取词.f取词推进()))
	def f端口号_小于(self):
		return 北向列表.S端口号.fc小于(int(self.m取词.f取词推进()))
	def f端口号_等于(self):
		va端口号 = []
		while True:
			v词 = self.m取词.f取词()
			if v词 and v词.isdigit():
				self.m取词.f推进()
				va端口号.append(int(v词))
			else:
				break
		return 北向列表.S端口号.fc等于(*va端口号)
	def f端口号_不等于(self):
		va端口号 = []
		while True:
			v词 = self.m取词.f取词()
			if v词.isdigit():
				self.m取词.f推进()
				va端口号.append(int(v词))
		return 北向列表.S端口号.fc不等于(*va端口号)
	def f端口号_范围(self):
		v词1 = self.m取词.f取词推进()
		v词2 = self.m取词.f取词推进()
		return 北向列表.S端口号.fc范围(range(int(v词1), int(v词2) + 1))
	ca端口号运算函数 = {
		"eq": f端口号_等于,
		"neq": f端口号_不等于,
		"gt": f端口号_大于,
		"lt": f端口号_小于,
		"range": f端口号_范围,
	}