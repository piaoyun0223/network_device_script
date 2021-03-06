from ..基础接口 import 接口 as 北向接口
from ..华三命令行 import 接口 as 旧接口
#===============================================================================
# 常量&函数
#===============================================================================
#接口名称v7
ca接口名称v7 = 旧接口.ca接口名称 | {
	北向接口.E类型.e万兆以太网: "Ten-GigabitEthernet",
	北向接口.E类型.e管理: "M-GigabitEthernet",
	北向接口.E类型.e聚合: "Bridge-Aggregation",
}
f生成接口v7, f创建接口v7 = 北向接口.F接口工厂(ca接口名称v7)
#接口缩写v7
ca接口缩写v7 = 旧接口.ca接口缩写 | {
	北向接口.E类型.e管理: "MGE",
	北向接口.E类型.e聚合: "BAGG",	#Bridge-Aggregation
}
f生成接口缩写v7, f创建接口缩写v7 = 北向接口.F接口工厂(ca接口缩写v7)
#===============================================================================
# 接口配置模式
#===============================================================================
class C接口v7(旧接口.C接口):
	pass