from django.shortcuts import render
from django.views.generic.base import View
from .models import ImageInfo, ImageId
from userlogin.models import UserInfo
from mysite.settings import MEDIA_ROOT
from django.db.models import Q
import random
import json
import redis
import ast
import ast
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
origin_image_list = ['橡胶软管', '打火机', '企鹅', '拖拉机', '羊', '滑板', '山', '鼠标', '吊灯', '吉他', '过山车', '猫头鹰', '厕所', '地图', '蜗牛', '瑜伽', '勺子', '照相机', '电话', '长凳', '猪', '狮子', '颅骨', '手', '浣熊', '胡须', '教堂', '动物迁徙', '鲸鱼', '太阳', '洗衣机', '飞机', '扩音器', '睡袋', '监狱', '消火栓', '汽车', '谷仓', '摆幅', '耙', '画笔', '厢式货车', '龙', '帆船', '罗盘', '鸭子', '帽子', '袋鼠', '甜甜圈', '鳄鱼', '咖啡杯', '冷却器', '水滑道', '羽毛', '消防车', '立体音响', '腿', '树', '枕头', '钱包', '沙漏', '耳朵', '西兰花', '山羊胡子', '月亮', '桥', '豌豆', '扭动', '脚', '伪装', '菜豆', '裤子', '唇膏', '夹克', '曲棍球', '卡车', '桌子', '铁锤', '中国的长城', '油漆罐', '壁炉', '叶', '苹果', '海滩', '风车', '梨', '雨伞', '蝴蝶', '花', '灯塔', '降落伞', '奶牛', '猫', '瓶盖', '大象', '听诊器', '河', '刀', '快艇', '毛衣', '斧子', '龙卷风', '推土机', '麦克风', '篮球', '王冠', '彩虹', '曲奇饼干', '浴缸', '西瓜', '跳水板', '远程控制', '篝火', '海龟', '鸟', '闹钟', '眼镜', '笔记本电脑', '皮卡车', '洋葱', '轮', '萨克斯', '摩天大楼', '手镯', '注射器', '砧座', '溜冰鞋', '牙齿', '扫帚', '烤箱', '带', '芦笋', '项链', '池塘', '鞋', '信封', '蚂蚁', '标记', '梯子', '老虎', '高尔夫俱乐部', '汉堡包', '生日蛋糕', '缝线', '胡子', '火炉', '梳妆台', '三角形', '钢琴', '棒棒糖', '肘部', '医院', '牙刷', '领结', '手提箱', '哑铃', '杯子', '棒球棒', '时钟', '猴子', '青蛙', '停车标志', '黑莓', '落地灯', '狗', '长号', '橡皮擦', '鹦鹉', '沙发', '手电筒', '竖琴', '杯子', '马', '小提琴', '蜜蜂', '网球拍', '蝙蝠', '摩托车', '内衣', '煎锅', '犀牛', '脑', '护照', '牛排', '跷跷板', '曲棍球杆', '雨', '通气管', '草莓', '膝', '棒球运动', '回旋镖', '明信片', '鱼', '口', '耳机', '雪花', '水桶', '葡萄', '蝎子', '训练', '头盔', '短袜', '龙虾', '收音机', '自行车', '手臂', '直升机', '室内植物', '眼睛', '美人鱼', '灌木', '天使', '花瓶', '天鹅', '酒杯', '电视', '交通灯', '足球', '电源插座', '比赛', '蚊子', '热气球', '人字拖', '圆圈', '线', '画框', '蟹', '熊猫', '披萨', '吊扇', '鲨鱼', '钳子', '之字形的', '步枪', '警车', '城堡', '六角形', '大提琴', '书', '门', '长颈鹿', '兔子', '钥匙', '海洋', '手指', '埃菲尔铁塔', '单簧管', '火烈鸟', '香蕉', '电子表格', '下沉', '脸', '帐篷', '游轮', '广场', '栅栏', '航空母舰', '独木舟', '茶壶', '骆驼', '蘑菇', '路灯', '潜艇', '海豚', '微波', '八角形', '热水浴池', '仙人掌', '飓风', 'T恤衫', '雪人', '三明治', '铲子', '闪电', '面包', '斑马', '玩具熊', '笑脸', '脚趾', '火车', '背包', '蓝莓', '楼梯', '章鱼', '手机', '计算器', '椅子', '房子', '花生', '松鼠', '菠萝', '指甲', '公共汽车', '灯泡', '小号', '铅笔', '锯', '鼻子', '键盘', '蜡笔', '花园', '蛋糕', '风扇', '螺丝起子', '洗碗机', '胡萝卜', '云', '蒙娜丽莎', '蜡烛', '牙膏', '计算机', '鼓', '校车', '绷带', '水塘', '烤面包机', '马铃薯', '回形针', '手表', '叉', '草', '床', '熊', '救护车', '篮子', '热狗', '剪刀', '蛇', '大炮', '蜘蛛', '刺猬', '酒瓶', '日历', '信箱', '棕榈树', '双筒望远镜', '钻石', '明星', '冰棒', '飞碟', '剑', '冰淇淋', '灯笼', '短裤']

origin_image_dict = [{'image_id': 1, 'image_name': '橡胶软管'}, {'image_id': 2, 'image_name': '打火机'}, {'image_id': 3, 'image_name': '企鹅'}, {'image_id': 4, 'image_name': '拖拉机'}, {'image_id': 5, 'image_name': '羊'}, {'image_id': 6, 'image_name': '滑板'}, {'image_id': 7, 'image_name': '山'}, {'image_id': 8, 'image_name': '鼠标'}, {'image_id': 9, 'image_name': '吊灯'}, {'image_id': 10, 'image_name': '吉他'}, {'image_id': 11, 'image_name': '过山车'}, {'image_id': 12, 'image_name': '猫头鹰'}, {'image_id': 13, 'image_name': '厕所'}, {'image_id': 14, 'image_name': '地图'}, {'image_id': 15, 'image_name': '蜗牛'}, {'image_id': 16, 'image_name': '瑜伽'}, {'image_id': 17, 'image_name': '勺子'}, {'image_id': 18, 'image_name': '照相机'}, {'image_id': 19, 'image_name': '电话'}, {'image_id': 20, 'image_name': '长凳'}, {'image_id': 21, 'image_name': '猪'}, {'image_id': 22, 'image_name': '狮子'}, {'image_id': 23, 'image_name': '颅骨'}, {'image_id': 24, 'image_name': '手'}, {'image_id': 25, 'image_name': '浣熊'}, {'image_id': 26, 'image_name': '胡须'}, {'image_id': 27, 'image_name': '教堂'}, {'image_id': 28, 'image_name': '动物迁徙'}, {'image_id': 29, 'image_name': '鲸鱼'}, {'image_id': 30, 'image_name': '太阳'}, {'image_id': 31, 'image_name': '洗衣机'}, {'image_id': 32, 'image_name': '飞机'}, {'image_id': 33, 'image_name': '扩音器'}, {'image_id': 34, 'image_name': '睡袋'}, {'image_id': 35, 'image_name': '监狱'}, {'image_id': 36, 'image_name': '消火栓'}, {'image_id': 37, 'image_name': '汽车'}, {'image_id': 38, 'image_name': '谷仓'}, {'image_id': 39, 'image_name': '摆幅'}, {'image_id': 40, 'image_name': '耙'}, {'image_id': 41, 'image_name': '画笔'}, {'image_id': 42, 'image_name': '厢式货车'}, {'image_id': 43, 'image_name': '龙'}, {'image_id': 44, 'image_name': '帆船'}, {'image_id': 45, 'image_name': '罗盘'}, {'image_id': 46, 'image_name': '鸭子'}, {'image_id': 47, 'image_name': '帽子'}, {'image_id': 48, 'image_name': '袋鼠'}, {'image_id': 49, 'image_name': '甜甜圈'}, {'image_id': 50, 'image_name': '鳄鱼'}, {'image_id': 51, 'image_name': '咖啡杯'}, {'image_id': 52, 'image_name': '冷却器'}, {'image_id': 53, 'image_name': '水滑道'}, {'image_id': 54, 'image_name': '羽毛'}, {'image_id': 55, 'image_name': '消防车'}, {'image_id': 56, 'image_name': '立体音响'}, {'image_id': 57, 'image_name': '腿'}, {'image_id': 58, 'image_name': '树'}, {'image_id': 59, 'image_name': '枕头'}, {'image_id': 60, 'image_name': '钱包'}, {'image_id': 61, 'image_name': '沙漏'}, {'image_id': 62, 'image_name': '耳朵'}, {'image_id': 63, 'image_name': '西兰花'}, {'image_id': 64, 'image_name': '山羊胡子'}, {'image_id': 65, 'image_name': '月亮'}, {'image_id': 66, 'image_name': '桥'}, {'image_id': 67, 'image_name': '豌豆'}, {'image_id': 68, 'image_name': '扭动'}, {'image_id': 69, 'image_name': '脚'}, {'image_id': 70, 'image_name': '伪装'}, {'image_id': 71, 'image_name': '菜豆'}, {'image_id': 72, 'image_name': '裤子'}, {'image_id': 73, 'image_name': '唇膏'}, {'image_id': 74, 'image_name': '夹克'}, {'image_id': 75, 'image_name': '曲棍球'}, {'image_id': 76, 'image_name': '卡车'}, {'image_id': 77, 'image_name': '桌子'}, {'image_id': 78, 'image_name': '铁锤'}, {'image_id': 79, 'image_name': '中国的长城'}, {'image_id': 80, 'image_name': '油漆罐'}, {'image_id': 81, 'image_name': '壁炉'}, {'image_id': 82, 'image_name': '叶'}, {'image_id': 83, 'image_name': '苹果'}, {'image_id': 84, 'image_name': '海滩'}, {'image_id': 85, 'image_name': '风车'}, {'image_id': 86, 'image_name': '梨'}, {'image_id': 87, 'image_name': '雨伞'}, {'image_id': 88, 'image_name': '蝴蝶'}, {'image_id': 89, 'image_name': '花'}, {'image_id': 90, 'image_name': '灯塔'}, {'image_id': 91, 'image_name': '降落伞'}, {'image_id': 92, 'image_name': '奶牛'}, {'image_id': 93, 'image_name': '猫'}, {'image_id': 94, 'image_name': '瓶盖'}, {'image_id': 95, 'image_name': '大象'}, {'image_id': 96, 'image_name': '听诊器'}, {'image_id': 97, 'image_name': '河'}, {'image_id': 98, 'image_name': '刀'}, {'image_id': 99, 'image_name': '快艇'}, {'image_id': 100, 'image_name': '毛衣'}, {'image_id': 101, 'image_name': '斧子'}, {'image_id': 102, 'image_name': '龙卷风'}, {'image_id': 103, 'image_name': '推土机'}, {'image_id': 104, 'image_name': '麦克风'}, {'image_id': 105, 'image_name': '篮球'}, {'image_id': 106, 'image_name': '王冠'}, {'image_id': 107, 'image_name': '彩虹'}, {'image_id': 108, 'image_name': '曲奇饼干'}, {'image_id': 109, 'image_name': '浴缸'}, {'image_id': 110, 'image_name': '西瓜'}, {'image_id': 111, 'image_name': '跳水板'}, {'image_id': 112, 'image_name': '远程控制'}, {'image_id': 113, 'image_name': '篝火'}, {'image_id': 114, 'image_name': '海龟'}, {'image_id': 115, 'image_name': '鸟'}, {'image_id': 116, 'image_name': '闹钟'}, {'image_id': 117, 'image_name': '眼镜'}, {'image_id': 118, 'image_name': '笔记本电脑'}, {'image_id': 119, 'image_name': '皮卡车'}, {'image_id': 120, 'image_name': '洋葱'}, {'image_id': 121, 'image_name': '轮'}, {'image_id': 122, 'image_name': '萨克斯'}, {'image_id': 123, 'image_name': '摩天大楼'}, {'image_id': 124, 'image_name': '手镯'}, {'image_id': 125, 'image_name': '注射器'}, {'image_id': 126, 'image_name': '砧座'}, {'image_id': 127, 'image_name': '溜冰鞋'}, {'image_id': 128, 'image_name': '牙齿'}, {'image_id': 129, 'image_name': '扫帚'}, {'image_id': 130, 'image_name': '烤箱'}, {'image_id': 131, 'image_name': '带'}, {'image_id': 132, 'image_name': '芦笋'}, {'image_id': 133, 'image_name': '项链'}, {'image_id': 134, 'image_name': '池塘'}, {'image_id': 135, 'image_name': '鞋'}, {'image_id': 136, 'image_name': '信封'}, {'image_id': 137, 'image_name': '蚂蚁'}, {'image_id': 138, 'image_name': '标记'}, {'image_id': 139, 'image_name': '梯子'}, {'image_id': 140, 'image_name': '老虎'}, {'image_id': 141, 'image_name': '高尔夫俱乐部'}, {'image_id': 142, 'image_name': '汉堡包'}, {'image_id': 143, 'image_name': '生日蛋糕'}, {'image_id': 144, 'image_name': '缝线'}, {'image_id': 145, 'image_name': '胡子'}, {'image_id': 146, 'image_name': '火炉'}, {'image_id': 147, 'image_name': '梳妆台'}, {'image_id': 148, 'image_name': '三角形'}, {'image_id': 149, 'image_name': '钢琴'}, {'image_id': 150, 'image_name': '棒棒糖'}, {'image_id': 151, 'image_name': '肘部'}, {'image_id': 152, 'image_name': '医院'}, {'image_id': 153, 'image_name': '牙刷'}, {'image_id': 154, 'image_name': '领结'}, {'image_id': 155, 'image_name': '手提箱'}, {'image_id': 156, 'image_name': '哑铃'}, {'image_id': 157, 'image_name': '杯子'}, {'image_id': 158, 'image_name': '棒球棒'}, {'image_id': 159, 'image_name': '时钟'}, {'image_id': 160, 'image_name': '猴子'}, {'image_id': 161, 'image_name': '青蛙'}, {'image_id': 162, 'image_name': '停车标志'}, {'image_id': 163, 'image_name': '黑莓'}, {'image_id': 164, 'image_name': '落地灯'}, {'image_id': 165, 'image_name': '狗'}, {'image_id': 166, 'image_name': '长号'}, {'image_id': 167, 'image_name': '橡皮擦'}, {'image_id': 168, 'image_name': '鹦鹉'}, {'image_id': 169, 'image_name': '沙发'}, {'image_id': 170, 'image_name': '手电筒'}, {'image_id': 171, 'image_name': '竖琴'}, {'image_id': 172, 'image_name': '杯子'}, {'image_id': 173, 'image_name': '马'}, {'image_id': 174, 'image_name': '小提琴'}, {'image_id': 175, 'image_name': '蜜蜂'}, {'image_id': 176, 'image_name': '网球拍'}, {'image_id': 177, 'image_name': '蝙蝠'}, {'image_id': 178, 'image_name': '摩托车'}, {'image_id': 179, 'image_name': '内衣'}, {'image_id': 180, 'image_name': '煎锅'}, {'image_id': 181, 'image_name': '犀牛'}, {'image_id': 182, 'image_name': '脑'}, {'image_id': 183, 'image_name': '护照'}, {'image_id': 184, 'image_name': '牛排'}, {'image_id': 185, 'image_name': '跷跷板'}, {'image_id': 186, 'image_name': '曲棍球杆'}, {'image_id': 187, 'image_name': '雨'}, {'image_id': 188, 'image_name': '通气管'}, {'image_id': 189, 'image_name': '草莓'}, {'image_id': 190, 'image_name': '膝'}, {'image_id': 191, 'image_name': '棒球运动'}, {'image_id': 192, 'image_name': '回旋镖'}, {'image_id': 193, 'image_name': '明信片'}, {'image_id': 194, 'image_name': '鱼'}, {'image_id': 195, 'image_name': '口'}, {'image_id': 196, 'image_name': '耳机'}, {'image_id': 197, 'image_name': '雪花'}, {'image_id': 198, 'image_name': '水桶'}, {'image_id': 199, 'image_name': '葡萄'}, {'image_id': 200, 'image_name': '蝎子'}, {'image_id': 201, 'image_name': '训练'}, {'image_id': 202, 'image_name': '头盔'}, {'image_id': 203, 'image_name': '短袜'}, {'image_id': 204, 'image_name': '龙虾'}, {'image_id': 205, 'image_name': '收音机'}, {'image_id': 206, 'image_name': '自行车'}, {'image_id': 207, 'image_name': '手臂'}, {'image_id': 208, 'image_name': '直升机'}, {'image_id': 209, 'image_name': '室内植物'}, {'image_id': 210, 'image_name': '眼睛'}, {'image_id': 211, 'image_name': '美人鱼'}, {'image_id': 212, 'image_name': '灌木'}, {'image_id': 213, 'image_name': '天使'}, {'image_id': 214, 'image_name': '花瓶'}, {'image_id': 215, 'image_name': '天鹅'}, {'image_id': 216, 'image_name': '酒杯'}, {'image_id': 217, 'image_name': '电视'}, {'image_id': 218, 'image_name': '交通灯'}, {'image_id': 219, 'image_name': '足球'}, {'image_id': 220, 'image_name': '电源插座'}, {'image_id': 221, 'image_name': '比赛'}, {'image_id': 222, 'image_name': '蚊子'}, {'image_id': 223, 'image_name': '热气球'}, {'image_id': 224, 'image_name': '人字拖'}, {'image_id': 225, 'image_name': '圆圈'}, {'image_id': 226, 'image_name': '线'}, {'image_id': 227, 'image_name': '画框'}, {'image_id': 228, 'image_name': '蟹'}, {'image_id': 229, 'image_name': '熊猫'}, {'image_id': 230, 'image_name': '披萨'}, {'image_id': 231, 'image_name': '吊扇'}, {'image_id': 232, 'image_name': '鲨鱼'}, {'image_id': 233, 'image_name': '钳子'}, {'image_id': 234, 'image_name': '之字形的'}, {'image_id': 235, 'image_name': '步枪'}, {'image_id': 236, 'image_name': '警车'}, {'image_id': 237, 'image_name': '城堡'}, {'image_id': 238, 'image_name': '六角形'}, {'image_id': 239, 'image_name': '大提琴'}, {'image_id': 240, 'image_name': '书'}, {'image_id': 241, 'image_name': '门'}, {'image_id': 242, 'image_name': '长颈鹿'}, {'image_id': 243, 'image_name': '兔子'}, {'image_id': 244, 'image_name': '钥匙'}, {'image_id': 245, 'image_name': '海洋'}, {'image_id': 246, 'image_name': '手指'}, {'image_id': 247, 'image_name': '埃菲尔铁塔'}, {'image_id': 248, 'image_name': '单簧管'}, {'image_id': 249, 'image_name': '火烈鸟'}, {'image_id': 250, 'image_name': '香蕉'}, {'image_id': 251, 'image_name': '电子表格'}, {'image_id': 252, 'image_name': '下沉'}, {'image_id': 253, 'image_name': '脸'}, {'image_id': 254, 'image_name': '帐篷'}, {'image_id': 255, 'image_name': '游轮'}, {'image_id': 256, 'image_name': '广场'}, {'image_id': 257, 'image_name': '栅栏'}, {'image_id': 258, 'image_name': '航空母舰'}, {'image_id': 259, 'image_name': '独木舟'}, {'image_id': 260, 'image_name': '茶壶'}, {'image_id': 261, 'image_name': '骆驼'}, {'image_id': 262, 'image_name': '蘑菇'}, {'image_id': 263, 'image_name': '路灯'}, {'image_id': 264, 'image_name': '潜艇'}, {'image_id': 265, 'image_name': '海豚'}, {'image_id': 266, 'image_name': '微波'}, {'image_id': 267, 'image_name': '八角形'}, {'image_id': 268, 'image_name': '热水浴池'}, {'image_id': 269, 'image_name': '仙人掌'}, {'image_id': 270, 'image_name': '飓风'}, {'image_id': 271, 'image_name': 'T恤衫'}, {'image_id': 272, 'image_name': '雪人'}, {'image_id': 273, 'image_name': '三明治'}, {'image_id': 274, 'image_name': '铲子'}, {'image_id': 275, 'image_name': '闪电'}, {'image_id': 276, 'image_name': '面包'}, {'image_id': 277, 'image_name': '斑马'}, {'image_id': 278, 'image_name': '玩具熊'}, {'image_id': 279, 'image_name': '笑脸'}, {'image_id': 280, 'image_name': '脚趾'}, {'image_id': 281, 'image_name': '火车'}, {'image_id': 282, 'image_name': '背包'}, {'image_id': 283, 'image_name': '蓝莓'}, {'image_id': 284, 'image_name': '楼梯'}, {'image_id': 285, 'image_name': '章鱼'}, {'image_id': 286, 'image_name': '手机'}, {'image_id': 287, 'image_name': '计算器'}, {'image_id': 288, 'image_name': '椅子'}, {'image_id': 289, 'image_name': '房子'}, {'image_id': 290, 'image_name': '花生'}, {'image_id': 291, 'image_name': '松鼠'}, {'image_id': 292, 'image_name': '菠萝'}, {'image_id': 293, 'image_name': '指甲'}, {'image_id': 294, 'image_name': '公共汽车'}, {'image_id': 295, 'image_name': '灯泡'}, {'image_id': 296, 'image_name': '小号'}, {'image_id': 297, 'image_name': '铅笔'}, {'image_id': 298, 'image_name': '锯'}, {'image_id': 299, 'image_name': '鼻子'}, {'image_id': 300, 'image_name': '键盘'}, {'image_id': 301, 'image_name': '蜡笔'}, {'image_id': 302, 'image_name': '花园'}, {'image_id': 303, 'image_name': '蛋糕'}, {'image_id': 304, 'image_name': '风扇'}, {'image_id': 305, 'image_name': '螺丝起子'}, {'image_id': 306, 'image_name': '洗碗机'}, {'image_id': 307, 'image_name': '胡萝卜'}, {'image_id': 308, 'image_name': '云'}, {'image_id': 309, 'image_name': '蒙娜丽莎'}, {'image_id': 310, 'image_name': '蜡烛'}, {'image_id': 311, 'image_name': '牙膏'}, {'image_id': 312, 'image_name': '计算机'}, {'image_id': 313, 'image_name': '鼓'}, {'image_id': 314, 'image_name': '校车'}, {'image_id': 315, 'image_name': '绷带'}, {'image_id': 316, 'image_name': '水塘'}, {'image_id': 317, 'image_name': '烤面包机'}, {'image_id': 318, 'image_name': '马铃薯'}, {'image_id': 319, 'image_name': '回形针'}, {'image_id': 320, 'image_name': '手表'}, {'image_id': 321, 'image_name': '叉'}, {'image_id': 322, 'image_name': '草'}, {'image_id': 323, 'image_name': '床'}, {'image_id': 324, 'image_name': '熊'}, {'image_id': 325, 'image_name': '救护车'}, {'image_id': 326, 'image_name': '篮子'}, {'image_id': 327, 'image_name': '热狗'}, {'image_id': 328, 'image_name': '剪刀'}, {'image_id': 329, 'image_name': '蛇'}, {'image_id': 330, 'image_name': '大炮'}, {'image_id': 331, 'image_name': '蜘蛛'}, {'image_id': 332, 'image_name': '刺猬'}, {'image_id': 333, 'image_name': '酒瓶'}, {'image_id': 334, 'image_name': '日历'}, {'image_id': 335, 'image_name': '信箱'}, {'image_id': 336, 'image_name': '棕榈树'}, {'image_id': 337, 'image_name': '双筒望远镜'}, {'image_id': 338, 'image_name': '钻石'}, {'image_id': 339, 'image_name': '明星'}, {'image_id': 340, 'image_name': '冰棒'}, {'image_id': 341, 'image_name': '飞碟'}, {'image_id': 342, 'image_name': '剑'}, {'image_id': 343, 'image_name': '冰淇淋'}, {'image_id': 344, 'image_name': '灯笼'}, {'image_id': 345, 'image_name': '短裤'}]


class UserImgaeList(View):
    #返回用户待画的题目列表
    @csrf_exempt
    def post(self, request):
        #返回用户待画取的画作信息
        origin_images = origin_image_dict
        mydata = str(request.body,encoding="utf-8")
        print(mydata)
        data = json.loads(mydata)
        print(type(data))
        uuid = data.get('uuid', None)
        skey = data.get('skey', None)
        back_list = []
        if uuid and skey:
            image_list = ImageInfo.objects.filter(uuid=uuid)
            if not image_list:
                random.shuffle(origin_images)
                return JsonResponse({'ok': 'success', 'msg': 'first_image_list', 'data': origin_images})
            else:
                for name in image_list:
                    #构造一个字典判断是否在原生列表中，除去用户已经画过的题目
                    compare_dict = {}
                    compare_dict['image_id'] = name.imageKey.image_id
                    compare_dict['image_name'] = name.imageKey.image_name
                    if compare_dict in origin_images:
                        origin_images.remove(compare_dict)
                if origin_images is None:
                    back_list = origin_image_dict
                else:
                    back_list = origin_images
            random.shuffle(back_list)
            return JsonResponse({'ok': 'success', 'msg': 'image_list', 'data': back_list})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})


class SaveImage(View):
    #保存用户提供的画作
    def post(self, request):
        file = request.FILES.get("img", None)
        # 题目id
        title_id = request.POST.get("image_id", None)
        print(title_id)
        # 用户的唯一标识
        uuid = request.POST.get("uuid", None)
        print(uuid)
        skey = request.POST.get('skey', None)
        print(skey)
        if uuid and skey and title_id and file:
            # 获得题目对象进而可以获得是哪个题目
            image = ImageId.objects.filter(image_id=title_id)
            if image:
                object_info = ImageInfo.objects.filter(uuid=uuid, imageKey__image_id=title_id)
                if not object_info:
                    ImageInfo.objects.create(uuid=uuid, skey=skey, image_path=file.name, imageKey=image[0])
                    # 更新用户等级信息
                    my_info = UserInfo.objects.filter(session__uuid=uuid)[0]
                    success_count = my_info.success_count + 1
                    grade = int(success_count / 5)
                    remainder = int(success_count % 5)
                    UserInfo.objects.filter(session__uuid=uuid).update(grade=grade, success_count=success_count, remainder=remainder)

                    # 软连接路径到static目录，ln -s /media2/aguessimage/ ./    ---返回给前端的src  /static/+mage_path
                    with open(MEDIA_ROOT + file.name, "wb+") as f:
                        for chunk in file.chunks():
                            f.write(chunk)
                    return JsonResponse({'ok': 'success', "msg": 'create new image'})
                else:
                    ImageInfo.objects.filter(uuid=uuid, imageKey__image_id=title_id).update(image_path=file.name, skey=skey)
                    with open(MEDIA_ROOT + file.name, "wb+") as f:
                        for chunk in file.chunks():
                            f.write(chunk)
                    return JsonResponse({'ok': 'success', "msg": 'update the image'})
            else:
                return JsonResponse({'ok': 'fail', 'msg': 'have not this image_id'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})


class GetUserCurImage(View):
    #获取当前用户一次游戏完成的所有成功画作
    @csrf_exempt
    def post(self, request):
        mydata = str(request.body,encoding="utf-8")
        data = json.loads(mydata)
        uuid = data.get("uuid", None)
        skey = data.get('skey', None)
        success_count = data.get('success_count', None)
        if uuid and skey and success_count:
            image_list = ImageInfo.objects.filter(uuid=uuid).order_by('-id')[:int(success_count)]
            if image_list and len(image_list) >= int(success_count):
                back_list = []
                dict_info = {}
                for image in image_list:
                    #拼接图片路径
                    src = "https://www.qien.xyz/static/guessimage/{}".format(image.image_path)
                    dict_info['src'] = src
                    dict_info['image_name'] = image.imageKey.image_name
                    dict_info['image_id'] = image.imageKey.image_id
                    back_list.append(dict_info)
                    dict_info = {}
                return JsonResponse({'ok': 'success', 'msg': 'success', 'data': back_list})
            else:
                return JsonResponse({'ok': 'fail', 'msg': 'too many success count or wrong input'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})


class GetOthersImage(View):
    def post(self, request):
        #根据提供的画作id获取最多9张图片src返回前端
        mydata = str(request.body,encoding="utf-8")
        data = json.loads(mydata)
        uuid = data.get("uuid", None)
        skey = data.get('skey', None)
        image_id = data.get("image_id", None)
        backe_list = []
        if image_id and uuid and skey:
            #判断用户是否已经画成功过对应的画作
            image_list = ImageInfo.objects.filter(uuid=uuid, imageKey__image_id=image_id)
            if image_list:
                #剔除当前用户画作筛选出其他用户对应画作id的画作
                all_other_images = ImageInfo.objects.filter(~Q(uuid=uuid), imageKey__image_id=image_id)
                if all_other_images:
                    if len(all_other_images) >= 9:
                        for image in all_other_images[:9]:
                            #拼接所有的图片地址
                            src = "https://www.qien.xyz/static/guessimage/{}".format(image.image_path)
                            backe_list.append(src)
                    else:
                        for image in all_other_images:
                            #拼接所有的图片地址
                            src = "https://www.qien.xyz/static/guessimage/{}".format(image.image_path)
                            backe_list.append(src)
                    return JsonResponse({'ok': 'success', 'msg': '成功', 'data': backe_list})
                else:
                    return JsonResponse({'ok': 'success', 'msg': '还没有用户画对过该类型画作', 'data': backe_list})
            else:
                return JsonResponse({'ok': 'fail', 'msg': '用户未画对过该类型画作', 'data': backe_list})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误', 'data': backe_list})


class InsertImageId(View):
    @csrf_exempt
    def get(self, request):
        for i in range(len(origin_image_list)):
            print(len(origin_image_list))
            ImageId.objects.create(image_id=i + 1, image_name=origin_image_list[i])
            # image_id = ImageId()
            # image_id.image_id = i
            # image_id.image_name = origin_image_list[i]
            # image_id.save()

        # image_list = ImageInfo.objects.all()
        # back_list = []
        # image_info = []
        # for image in image_list:
        #     src = "http://127.0.0.1:8005/static/images/{}".format(image.image_path)
        #     print(image.imageKey.image_name)
        #     image_info.append(src)
        #     image_info.append(image.imageKey.image_name)
        #     back_list.append(image_info)
        #     image_info = []

        return HttpResponse("插入成功")


class SavePlayImage(View):
    #保存用户提供的画作
    def post(self, request):
        file = request.FILES.get("img", None)
        room_name = request.POST.get("room_name", None)
        image_id = request.POST.get("image_id", None)
        print(image_id)
        uuid = request.POST.get("uuid", None)
        image_name = request.POST.get('image_name', None)
        img_flag = request.POST.get('img_flag', None)
        img_dict = {}
        image_info_list = []
        have_image_flag = 0
        user_dict = {}
        all_user_data_list = []
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        userinfo = UserInfo.objects.filter(session__uuid=uuid)
        if userinfo:
            my_info = ast.literal_eval(userinfo[0].session.user_info)
            avatarUrl = my_info['avatarUrl']
            nickName = my_info['nickName']
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})
        if uuid and image_name and image_id and img_flag:
            img_dict["image_id"] = image_id
            img_dict["image_name"] = image_name
            img_dict["img_flag"] = img_flag
            if file:
                # 组装个人数据
                image_src = "http://124.156.178.97:8183/static/guessimage/{}".format(file.name)
                img_dict["image_src"] = image_src
            else:
                image_src = ''
                img_dict["image_src"] = image_src

            # 存入redis
            # 判断房间信息是否存在
            if not r.exists(room_name):
                print("create room==============================")
                image_info_list.append(img_dict)
                user_dict["uuid"] = uuid
                user_dict["nickName"] = nickName
                user_dict["avatarUrl"] = avatarUrl
                user_dict["image_info"] = image_info_list
                all_user_data_list.append(user_dict)
                r.set(room_name, str(all_user_data_list))
            else:
                all_user_data_list = r.get(room_name)
                all_user_data_list = ast.literal_eval(all_user_data_list)
                # print("======================{}".format(all_user_data_list))
                # 查看房间信息中该用户是否已经存入画作数据
                for i in range(len(all_user_data_list)):
                    if all_user_data_list[i]['uuid'] == uuid:
                        print("===========uuid exist=============")
                        # 已有画作数据，在基础上添加新的画作数据
                        image_info_list = all_user_data_list[i]['image_info']
                        # print("before add image list = {}".format(all_user_data_list[i]))
                        image_info_list.append(img_dict)
                        all_user_data_list[i]['image_info'] = image_info_list
                        print("after add image list = {}".format(all_user_data_list[i]))
                        have_image_flag = 1
                if not have_image_flag:
                    # 该用户未提交过画作数据，存入该用户信息
                    print("===========first add=====================")
                    new_image_info_list = []
                    new_image_info_list.append(img_dict)
                    user_dict["uuid"] = uuid
                    user_dict["nickName"] = nickName
                    user_dict["avatarUrl"] = avatarUrl
                    user_dict["image_info"] = new_image_info_list
                    all_user_data_list.append(user_dict)
                    print("======================{}".format(all_user_data_list))
                r.set(room_name, str(all_user_data_list))

            # 写入本地，用户返回前端图片url可用
            with open(MEDIA_ROOT + file.name, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)
            return JsonResponse({'ok': 'success', "msg": 'save play image'})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})


class GetPlayImage(View):
    #保存用户提供的画作
    def post(self, request):
        mydata = str(request.body,encoding="utf-8")
        data = json.loads(mydata)
        room_name = data.get("room_name", None)
        # room_name = request.POST.get("room_name", None)
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        print(room_name)
        if room_name:
            print(r.exists(room_name))
            if not r.exists(room_name):
                return JsonResponse({'ok': 'fail', 'msg': '参数错误'})
            else:
                all_user_data_list = r.get(room_name)
                all_user_data_list = ast.literal_eval(all_user_data_list)
                return JsonResponse({'ok': 'success', 'msg': '成功', 'data': all_user_data_list})
        else:
            return JsonResponse({'ok': 'fail', 'msg': '参数错误'})