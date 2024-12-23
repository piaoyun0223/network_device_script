from ..基础接口 import 异常
from ..命令行接口 import 设备 as 南向设备
from ..命令行接口 import 命令
from . import 用户模式
from ..华三命令行.常量 import *
ca错误文本与异常类 = [
	("% Unrecognized command found at '^' position.", 异常.X命令),	#命令无法解析，符号“^”指示位置出错
	("% Incomplete command found at '^' position.", 异常.X命令),	#符号“^”指示位置的参数输入不完整
	("% Ambiguous command found at '^' position.", 异常.X命令),	#符号“^”指示位置的关键字不明确，存在二义性
	("% Too many parameters found at '^' position.", 异常.X命令),	#符号“^”指示位置的参数输入太多
	("% Wrong parameter found at '^' position.", 异常.X命令),	#在符号“^”指示位置的参数错误
]
class C设备_v7(南向设备.I设备):
	def __init__(self, a连接, a型号, a版本):
		南向设备.I设备.__init__(self, a连接)
		self.fs自动换页("---- More ----")
		self.m连接.fs编码("utf-8")
		self.m型号 = a型号
		self.m版本 = a版本
	def f退出(self):
		self.f执行命令("quit")
	def f输入_结束符(self):
		self.f输入(c中断符 + c回车符)
		self.f输入(c结束符 + c回车符)
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_v7(self)
	def f模式_启动(self):
		from . import 启动
		return 启动.C启动v7(self)
	def f处理显示结果(self, a输出):
		v输出 = a输出.replace("\r", "")	#可能有多个\r,清掉
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
	def f显示_当前模式配置(self):
		v输出 = self.f执行显示命令("display this", a自动换页 = True)
		v输出 = 南向设备.f去头尾行(v输出)
		return v输出
class C设备_ev7(C设备_v7):
	"""适用于: (模拟器)华三msr3620(v7.1.*), (模拟器)华三s5820v2(v7.1.*)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_ev7(self)
class C设备_us5v7(C设备_v7):
	"""适用于: 紫光s5200(v7.1.*)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_us5v7(self)
class C设备_s7v7(C设备_v7):
	"""适用于: 紫光s8600x(v7.1.070), 紫光s7800xp(v7.1.*)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_s7v7(self)
class C设备_s9v7(C设备_v7):
	"""适用于: 华三S9810(v7.1.*)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_s9v7(self)
class C设备_s5v7(C设备_v7):
	"""适用于: 华三s5560x(v7.1.070 r6526)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_s5v7(self)
class C设备_sv7_2019(C设备_v7):
	"""适用于: 华三s5560x(v7.1.070 r1119p20), 紫光s5600(v7.1.070 r7734p05)"""
	def f模式_用户(self):
		from . import 用户模式
		return 用户模式.C用户视图_sv7_2019(self)