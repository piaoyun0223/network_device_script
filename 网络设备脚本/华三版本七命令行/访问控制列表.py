import cflw代码库py.cflw网络地址 as 地址
import cflw代码库py.cflw字符串 as 字符串
from ..基础接口 import 操作
from ..基础接口 import 协议
from ..基础接口 import 访问控制列表 as 北向列表
from ..命令行接口 import 命令
from ..命令行接口 import 模式
from ..命令行接口 import 访问控制列表 as 南向列表
from ..华三命令行.常量 import *
from ..华三命令行 import 访问控制列表 as 旧列表
#===============================================================================
# 声明
#===============================================================================
C助手 = 旧列表.C助手
#===============================================================================
# 生成
#===============================================================================
def f生成名称_v7(a名称):	#序号不带"number"
	v类型 = type(a名称)
	if v类型 == int:
		return "%s" % (a名称,)
	v名称 = str(a名称)
	if v名称.isdigit():
		return "%s" % (v名称,)
	return "name %s" % (v名称,)
#===============================================================================
# 显示
#===============================================================================
class I列表显示_v7(旧列表.I列表显示):
	def fg显示命令(self, a序号 = None):
		v命令 = 命令.C命令("display acl")
		v命令 += self.c协议
		v命令 += f生成名称_v7(self.m名称)
		if a序号 != None:
			v命令 += "| include rule.%d.[dp]" % (a序号,)
		return v命令
class C基本4显示_v7(I列表显示_v7, 旧列表.C基本4显示):
	c类型 = 旧列表.c基本
	c协议 = 旧列表.c网络协议4
class C高级4显示_v7(I列表显示_v7, 旧列表.C高级4显示):
	c类型 = 旧列表.c高级
	c协议 = 旧列表.c网络协议4
class C基本6显示_v7(I列表显示_v7, 旧列表.C基本6显示):
	c类型 = 旧列表.c基本
	c协议 = 旧列表.c网络协议6
class C高级6显示_v7(I列表显示_v7, 旧列表.C高级6显示):
	c类型 = 旧列表.c高级
	c协议 = 旧列表.c网络协议6
#===============================================================================
# 配置
#===============================================================================
class I列表配置_v7(旧列表.I列表配置):
	"""acl 类型 访问列表号
	适用于: v7.1"""
	def fg进入命令(self):
		v命令 = 命令.C命令("acl")
		v命令 += self.c协议
		v命令 += self.c类型
		v命令 += f生成名称_v7(self.m名称)
		return v命令
class C基本4配置_v7(I列表配置_v7, I列表显示_v7, 旧列表.C基本4配置, 旧列表.C基本4显示):
	c类型 = 旧列表.c基本
	c协议 = 旧列表.c网络协议4
class C高级4配置_v7(I列表配置_v7, I列表显示_v7, 旧列表.C高级4配置, 旧列表.C高级4显示):
	c类型 = 旧列表.c高级
	c协议 = 旧列表.c网络协议4
class C基本6配置_v7(I列表配置_v7, I列表显示_v7, 旧列表.C基本6配置, 旧列表.C基本6显示):
	c类型 = 旧列表.c基本
	c协议 = 旧列表.c网络协议6
class C高级6配置_v7(I列表配置_v7, I列表显示_v7, 旧列表.C高级6配置, 旧列表.C高级6显示):
	c类型 = 旧列表.c高级
	c协议 = 旧列表.c网络协议6