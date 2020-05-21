# chat/consumers.py
# async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
import random
import redis
from userlogin.models import UserInfo
origin_image_dict = [{'image_id': 1, 'image_name': '橡胶软管'}, {'image_id': 2, 'image_name': '打火机'}, {'image_id': 3, 'image_name': '企鹅'}, {'image_id': 4, 'image_name': '拖拉机'}, {'image_id': 5, 'image_name': '羊'}, {'image_id': 6, 'image_name': '滑板'}, {'image_id': 7, 'image_name': '山'}, {'image_id': 8, 'image_name': '鼠标'}, {'image_id': 9, 'image_name': '吊灯'}, {'image_id': 10, 'image_name': '吉他'}, {'image_id': 11, 'image_name': '过山车'}, {'image_id': 12, 'image_name': '猫头鹰'}, {'image_id': 13, 'image_name': '厕所'}, {'image_id': 14, 'image_name': '地图'}, {'image_id': 15, 'image_name': '蜗牛'}, {'image_id': 16, 'image_name': '瑜伽'}, {'image_id': 17, 'image_name': '勺子'}, {'image_id': 18, 'image_name': '照相机'}, {'image_id': 19, 'image_name': '电话'}, {'image_id': 20, 'image_name': '长凳'}, {'image_id': 21, 'image_name': '猪'}, {'image_id': 22, 'image_name': '狮子'}, {'image_id': 23, 'image_name': '颅骨'}, {'image_id': 24, 'image_name': '手'}, {'image_id': 25, 'image_name': '浣熊'}, {'image_id': 26, 'image_name': '胡须'}, {'image_id': 27, 'image_name': '教堂'}, {'image_id': 28, 'image_name': '动物迁徙'}, {'image_id': 29, 'image_name': '鲸鱼'}, {'image_id': 30, 'image_name': '太阳'}, {'image_id': 31, 'image_name': '洗衣机'}, {'image_id': 32, 'image_name': '飞机'}, {'image_id': 33, 'image_name': '扩音器'}, {'image_id': 34, 'image_name': '睡袋'}, {'image_id': 35, 'image_name': '监狱'}, {'image_id': 36, 'image_name': '消火栓'}, {'image_id': 37, 'image_name': '汽车'}, {'image_id': 38, 'image_name': '谷仓'}, {'image_id': 39, 'image_name': '摆幅'}, {'image_id': 40, 'image_name': '耙'}, {'image_id': 41, 'image_name': '画笔'}, {'image_id': 42, 'image_name': '厢式货车'}, {'image_id': 43, 'image_name': '龙'}, {'image_id': 44, 'image_name': '帆船'}, {'image_id': 45, 'image_name': '罗盘'}, {'image_id': 46, 'image_name': '鸭子'}, {'image_id': 47, 'image_name': '帽子'}, {'image_id': 48, 'image_name': '袋鼠'}, {'image_id': 49, 'image_name': '甜甜圈'}, {'image_id': 50, 'image_name': '鳄鱼'}, {'image_id': 51, 'image_name': '咖啡杯'}, {'image_id': 52, 'image_name': '冷却器'}, {'image_id': 53, 'image_name': '水滑道'}, {'image_id': 54, 'image_name': '羽毛'}, {'image_id': 55, 'image_name': '消防车'}, {'image_id': 56, 'image_name': '立体音响'}, {'image_id': 57, 'image_name': '腿'}, {'image_id': 58, 'image_name': '树'}, {'image_id': 59, 'image_name': '枕头'}, {'image_id': 60, 'image_name': '钱包'}, {'image_id': 61, 'image_name': '沙漏'}, {'image_id': 62, 'image_name': '耳朵'}, {'image_id': 63, 'image_name': '西兰花'}, {'image_id': 64, 'image_name': '山羊胡子'}, {'image_id': 65, 'image_name': '月亮'}, {'image_id': 66, 'image_name': '桥'}, {'image_id': 67, 'image_name': '豌豆'}, {'image_id': 68, 'image_name': '扭动'}, {'image_id': 69, 'image_name': '脚'}, {'image_id': 70, 'image_name': '伪装'}, {'image_id': 71, 'image_name': '菜豆'}, {'image_id': 72, 'image_name': '裤子'}, {'image_id': 73, 'image_name': '唇膏'}, {'image_id': 74, 'image_name': '夹克'}, {'image_id': 75, 'image_name': '曲棍球'}, {'image_id': 76, 'image_name': '卡车'}, {'image_id': 77, 'image_name': '桌子'}, {'image_id': 78, 'image_name': '铁锤'}, {'image_id': 79, 'image_name': '中国的长城'}, {'image_id': 80, 'image_name': '油漆罐'}, {'image_id': 81, 'image_name': '壁炉'}, {'image_id': 82, 'image_name': '叶'}, {'image_id': 83, 'image_name': '苹果'}, {'image_id': 84, 'image_name': '海滩'}, {'image_id': 85, 'image_name': '风车'}, {'image_id': 86, 'image_name': '梨'}, {'image_id': 87, 'image_name': '雨伞'}, {'image_id': 88, 'image_name': '蝴蝶'}, {'image_id': 89, 'image_name': '花'}, {'image_id': 90, 'image_name': '灯塔'}, {'image_id': 91, 'image_name': '降落伞'}, {'image_id': 92, 'image_name': '奶牛'}, {'image_id': 93, 'image_name': '猫'}, {'image_id': 94, 'image_name': '瓶盖'}, {'image_id': 95, 'image_name': '大象'}, {'image_id': 96, 'image_name': '听诊器'}, {'image_id': 97, 'image_name': '河'}, {'image_id': 98, 'image_name': '刀'}, {'image_id': 99, 'image_name': '快艇'}, {'image_id': 100, 'image_name': '毛衣'}, {'image_id': 101, 'image_name': '斧子'}, {'image_id': 102, 'image_name': '龙卷风'}, {'image_id': 103, 'image_name': '推土机'}, {'image_id': 104, 'image_name': '麦克风'}, {'image_id': 105, 'image_name': '篮球'}, {'image_id': 106, 'image_name': '王冠'}, {'image_id': 107, 'image_name': '彩虹'}, {'image_id': 108, 'image_name': '曲奇饼干'}, {'image_id': 109, 'image_name': '浴缸'}, {'image_id': 110, 'image_name': '西瓜'}, {'image_id': 111, 'image_name': '跳水板'}, {'image_id': 112, 'image_name': '远程控制'}, {'image_id': 113, 'image_name': '篝火'}, {'image_id': 114, 'image_name': '海龟'}, {'image_id': 115, 'image_name': '鸟'}, {'image_id': 116, 'image_name': '闹钟'}, {'image_id': 117, 'image_name': '眼镜'}, {'image_id': 118, 'image_name': '笔记本电脑'}, {'image_id': 119, 'image_name': '皮卡车'}, {'image_id': 120, 'image_name': '洋葱'}, {'image_id': 121, 'image_name': '轮'}, {'image_id': 122, 'image_name': '萨克斯'}, {'image_id': 123, 'image_name': '摩天大楼'}, {'image_id': 124, 'image_name': '手镯'}, {'image_id': 125, 'image_name': '注射器'}, {'image_id': 126, 'image_name': '砧座'}, {'image_id': 127, 'image_name': '溜冰鞋'}, {'image_id': 128, 'image_name': '牙齿'}, {'image_id': 129, 'image_name': '扫帚'}, {'image_id': 130, 'image_name': '烤箱'}, {'image_id': 131, 'image_name': '带'}, {'image_id': 132, 'image_name': '芦笋'}, {'image_id': 133, 'image_name': '项链'}, {'image_id': 134, 'image_name': '池塘'}, {'image_id': 135, 'image_name': '鞋'}, {'image_id': 136, 'image_name': '信封'}, {'image_id': 137, 'image_name': '蚂蚁'}, {'image_id': 138, 'image_name': '标记'}, {'image_id': 139, 'image_name': '梯子'}, {'image_id': 140, 'image_name': '老虎'}, {'image_id': 141, 'image_name': '高尔夫俱乐部'}, {'image_id': 142, 'image_name': '汉堡包'}, {'image_id': 143, 'image_name': '生日蛋糕'}, {'image_id': 144, 'image_name': '缝线'}, {'image_id': 145, 'image_name': '胡子'}, {'image_id': 146, 'image_name': '火炉'}, {'image_id': 147, 'image_name': '梳妆台'}, {'image_id': 148, 'image_name': '三角形'}, {'image_id': 149, 'image_name': '钢琴'}, {'image_id': 150, 'image_name': '棒棒糖'}, {'image_id': 151, 'image_name': '肘部'}, {'image_id': 152, 'image_name': '医院'}, {'image_id': 153, 'image_name': '牙刷'}, {'image_id': 154, 'image_name': '领结'}, {'image_id': 155, 'image_name': '手提箱'}, {'image_id': 156, 'image_name': '哑铃'}, {'image_id': 157, 'image_name': '杯子'}, {'image_id': 158, 'image_name': '棒球棒'}, {'image_id': 159, 'image_name': '时钟'}, {'image_id': 160, 'image_name': '猴子'}, {'image_id': 161, 'image_name': '青蛙'}, {'image_id': 162, 'image_name': '停车标志'}, {'image_id': 163, 'image_name': '黑莓'}, {'image_id': 164, 'image_name': '落地灯'}, {'image_id': 165, 'image_name': '狗'}, {'image_id': 166, 'image_name': '长号'}, {'image_id': 167, 'image_name': '橡皮擦'}, {'image_id': 168, 'image_name': '鹦鹉'}, {'image_id': 169, 'image_name': '沙发'}, {'image_id': 170, 'image_name': '手电筒'}, {'image_id': 171, 'image_name': '竖琴'}, {'image_id': 172, 'image_name': '杯子'}, {'image_id': 173, 'image_name': '马'}, {'image_id': 174, 'image_name': '小提琴'}, {'image_id': 175, 'image_name': '蜜蜂'}, {'image_id': 176, 'image_name': '网球拍'}, {'image_id': 177, 'image_name': '蝙蝠'}, {'image_id': 178, 'image_name': '摩托车'}, {'image_id': 179, 'image_name': '内衣'}, {'image_id': 180, 'image_name': '煎锅'}, {'image_id': 181, 'image_name': '犀牛'}, {'image_id': 182, 'image_name': '脑'}, {'image_id': 183, 'image_name': '护照'}, {'image_id': 184, 'image_name': '牛排'}, {'image_id': 185, 'image_name': '跷跷板'}, {'image_id': 186, 'image_name': '曲棍球杆'}, {'image_id': 187, 'image_name': '雨'}, {'image_id': 188, 'image_name': '通气管'}, {'image_id': 189, 'image_name': '草莓'}, {'image_id': 190, 'image_name': '膝'}, {'image_id': 191, 'image_name': '棒球运动'}, {'image_id': 192, 'image_name': '回旋镖'}, {'image_id': 193, 'image_name': '明信片'}, {'image_id': 194, 'image_name': '鱼'}, {'image_id': 195, 'image_name': '口'}, {'image_id': 196, 'image_name': '耳机'}, {'image_id': 197, 'image_name': '雪花'}, {'image_id': 198, 'image_name': '水桶'}, {'image_id': 199, 'image_name': '葡萄'}, {'image_id': 200, 'image_name': '蝎子'}, {'image_id': 201, 'image_name': '训练'}, {'image_id': 202, 'image_name': '头盔'}, {'image_id': 203, 'image_name': '短袜'}, {'image_id': 204, 'image_name': '龙虾'}, {'image_id': 205, 'image_name': '收音机'}, {'image_id': 206, 'image_name': '自行车'}, {'image_id': 207, 'image_name': '手臂'}, {'image_id': 208, 'image_name': '直升机'}, {'image_id': 209, 'image_name': '室内植物'}, {'image_id': 210, 'image_name': '眼睛'}, {'image_id': 211, 'image_name': '美人鱼'}, {'image_id': 212, 'image_name': '灌木'}, {'image_id': 213, 'image_name': '天使'}, {'image_id': 214, 'image_name': '花瓶'}, {'image_id': 215, 'image_name': '天鹅'}, {'image_id': 216, 'image_name': '酒杯'}, {'image_id': 217, 'image_name': '电视'}, {'image_id': 218, 'image_name': '交通灯'}, {'image_id': 219, 'image_name': '足球'}, {'image_id': 220, 'image_name': '电源插座'}, {'image_id': 221, 'image_name': '比赛'}, {'image_id': 222, 'image_name': '蚊子'}, {'image_id': 223, 'image_name': '热气球'}, {'image_id': 224, 'image_name': '人字拖'}, {'image_id': 225, 'image_name': '圆圈'}, {'image_id': 226, 'image_name': '线'}, {'image_id': 227, 'image_name': '画框'}, {'image_id': 228, 'image_name': '蟹'}, {'image_id': 229, 'image_name': '熊猫'}, {'image_id': 230, 'image_name': '披萨'}, {'image_id': 231, 'image_name': '吊扇'}, {'image_id': 232, 'image_name': '鲨鱼'}, {'image_id': 233, 'image_name': '钳子'}, {'image_id': 234, 'image_name': '之字形的'}, {'image_id': 235, 'image_name': '步枪'}, {'image_id': 236, 'image_name': '警车'}, {'image_id': 237, 'image_name': '城堡'}, {'image_id': 238, 'image_name': '六角形'}, {'image_id': 239, 'image_name': '大提琴'}, {'image_id': 240, 'image_name': '书'}, {'image_id': 241, 'image_name': '门'}, {'image_id': 242, 'image_name': '长颈鹿'}, {'image_id': 243, 'image_name': '兔子'}, {'image_id': 244, 'image_name': '钥匙'}, {'image_id': 245, 'image_name': '海洋'}, {'image_id': 246, 'image_name': '手指'}, {'image_id': 247, 'image_name': '埃菲尔铁塔'}, {'image_id': 248, 'image_name': '单簧管'}, {'image_id': 249, 'image_name': '火烈鸟'}, {'image_id': 250, 'image_name': '香蕉'}, {'image_id': 251, 'image_name': '电子表格'}, {'image_id': 252, 'image_name': '下沉'}, {'image_id': 253, 'image_name': '脸'}, {'image_id': 254, 'image_name': '帐篷'}, {'image_id': 255, 'image_name': '游轮'}, {'image_id': 256, 'image_name': '广场'}, {'image_id': 257, 'image_name': '栅栏'}, {'image_id': 258, 'image_name': '航空母舰'}, {'image_id': 259, 'image_name': '独木舟'}, {'image_id': 260, 'image_name': '茶壶'}, {'image_id': 261, 'image_name': '骆驼'}, {'image_id': 262, 'image_name': '蘑菇'}, {'image_id': 263, 'image_name': '路灯'}, {'image_id': 264, 'image_name': '潜艇'}, {'image_id': 265, 'image_name': '海豚'}, {'image_id': 266, 'image_name': '微波'}, {'image_id': 267, 'image_name': '八角形'}, {'image_id': 268, 'image_name': '热水浴池'}, {'image_id': 269, 'image_name': '仙人掌'}, {'image_id': 270, 'image_name': '飓风'}, {'image_id': 271, 'image_name': 'T恤衫'}, {'image_id': 272, 'image_name': '雪人'}, {'image_id': 273, 'image_name': '三明治'}, {'image_id': 274, 'image_name': '铲子'}, {'image_id': 275, 'image_name': '闪电'}, {'image_id': 276, 'image_name': '面包'}, {'image_id': 277, 'image_name': '斑马'}, {'image_id': 278, 'image_name': '玩具熊'}, {'image_id': 279, 'image_name': '笑脸'}, {'image_id': 280, 'image_name': '脚趾'}, {'image_id': 281, 'image_name': '火车'}, {'image_id': 282, 'image_name': '背包'}, {'image_id': 283, 'image_name': '蓝莓'}, {'image_id': 284, 'image_name': '楼梯'}, {'image_id': 285, 'image_name': '章鱼'}, {'image_id': 286, 'image_name': '手机'}, {'image_id': 287, 'image_name': '计算器'}, {'image_id': 288, 'image_name': '椅子'}, {'image_id': 289, 'image_name': '房子'}, {'image_id': 290, 'image_name': '花生'}, {'image_id': 291, 'image_name': '松鼠'}, {'image_id': 292, 'image_name': '菠萝'}, {'image_id': 293, 'image_name': '指甲'}, {'image_id': 294, 'image_name': '公共汽车'}, {'image_id': 295, 'image_name': '灯泡'}, {'image_id': 296, 'image_name': '小号'}, {'image_id': 297, 'image_name': '铅笔'}, {'image_id': 298, 'image_name': '锯'}, {'image_id': 299, 'image_name': '鼻子'}, {'image_id': 300, 'image_name': '键盘'}, {'image_id': 301, 'image_name': '蜡笔'}, {'image_id': 302, 'image_name': '花园'}, {'image_id': 303, 'image_name': '蛋糕'}, {'image_id': 304, 'image_name': '风扇'}, {'image_id': 305, 'image_name': '螺丝起子'}, {'image_id': 306, 'image_name': '洗碗机'}, {'image_id': 307, 'image_name': '胡萝卜'}, {'image_id': 308, 'image_name': '云'}, {'image_id': 309, 'image_name': '蒙娜丽莎'}, {'image_id': 310, 'image_name': '蜡烛'}, {'image_id': 311, 'image_name': '牙膏'}, {'image_id': 312, 'image_name': '计算机'}, {'image_id': 313, 'image_name': '鼓'}, {'image_id': 314, 'image_name': '校车'}, {'image_id': 315, 'image_name': '绷带'}, {'image_id': 316, 'image_name': '水塘'}, {'image_id': 317, 'image_name': '烤面包机'}, {'image_id': 318, 'image_name': '马铃薯'}, {'image_id': 319, 'image_name': '回形针'}, {'image_id': 320, 'image_name': '手表'}, {'image_id': 321, 'image_name': '叉'}, {'image_id': 322, 'image_name': '草'}, {'image_id': 323, 'image_name': '床'}, {'image_id': 324, 'image_name': '熊'}, {'image_id': 325, 'image_name': '救护车'}, {'image_id': 326, 'image_name': '篮子'}, {'image_id': 327, 'image_name': '热狗'}, {'image_id': 328, 'image_name': '剪刀'}, {'image_id': 329, 'image_name': '蛇'}, {'image_id': 330, 'image_name': '大炮'}, {'image_id': 331, 'image_name': '蜘蛛'}, {'image_id': 332, 'image_name': '刺猬'}, {'image_id': 333, 'image_name': '酒瓶'}, {'image_id': 334, 'image_name': '日历'}, {'image_id': 335, 'image_name': '信箱'}, {'image_id': 336, 'image_name': '棕榈树'}, {'image_id': 337, 'image_name': '双筒望远镜'}, {'image_id': 338, 'image_name': '钻石'}, {'image_id': 339, 'image_name': '明星'}, {'image_id': 340, 'image_name': '冰棒'}, {'image_id': 341, 'image_name': '飞碟'}, {'image_id': 342, 'image_name': '剑'}, {'image_id': 343, 'image_name': '冰淇淋'}, {'image_id': 344, 'image_name': '灯笼'}, {'image_id': 345, 'image_name': '短裤'}]


class ChatConsumer(AsyncWebsocketConsumer):
    rooms_data_dict = {}
    # start_game_flag_dict = {}

    async def connect(self):
        print(self.scope['url_route'])
        print(self.scope['url_route']['kwargs'])
        print(self.channel_name)
        print("connect rooms_data_dict = {}".format(self.rooms_data_dict))
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.return_list = []
        self.start_game_flag = 0
        self.uuid = ''
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("group_add-------------------------------")
        await self.accept()
        print("connect accept-=----------------------------")
        # self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name
        # )
        # print("group_add-------------------------------")
        # self.accept()
        # print("connect accept-=----------------------------")

    async def disconnect(self, close_code):
        # Leave room group
        print("==========================================================")
        print("========================disconnect========================")
        print("disconnect self uuid = {}".format(self.uuid))
        print("disconnect return list = {}".format(self.return_list))
        print("disconnect rooms_data_dict = {}".format(self.rooms_data_dict))
        for i in range(len(self.return_list)):
            if self.return_list[i]['uuid'] == self.uuid:
                del self.return_list[i]
                break
        self.rooms_data_dict[self.room_group_name] = self.return_list
        print("disconnect after del rooms_data_dict = {}".format(self.rooms_data_dict))
        # try:
        #     print("in disconnect start game flag = {}".format(self.start_game_flag_dict[self.room_group_name]))
        #     flag = self.start_game_flag_dict[self.room_group_name]
        #     print("flag ==============={}".format(flag))
        #     if flag:
        #         del self.start_game_flag_dict[self.room_group_name]
        #         print("after delete room_name:{}".format(self.start_game_flag_dict))
        #     print("room_name dict:{}".format(self.start_game_flag_dict))
        # except Exception as e:
        #     print(e)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'data': self.return_list
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def get_nickname_avatarurl(self, uuid):
        userinfo = UserInfo.objects.filter(session__uuid=uuid)[0]
        my_info = eval(userinfo.session.user_info)
        avatarUrl = my_info['avatarUrl']
        nickName = my_info['nickName']
        return avatarUrl, nickName

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("==========================================================")
        print("=========================receive==========================")
        text_data_json = json.loads(text_data)
        uuid = text_data_json['uuid']
        start_flag = text_data_json['start_flag']
        have_flag = 0

        print("receive uuid = {}--------------------------".format(uuid))
        print("receive start_flag = {}-----------------------".format(start_flag))
        if int(start_flag):
            # self.start_game_flag_dict[self.room_group_name] = 1
            # print("in receive start game flag = {}".format(self.start_game_flag_dict[self.room_group_name]))
            print("receive start_flag = 1")
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_start',
                    'data': '1'
                }
            )
        else:
            self.uuid = uuid
            # avatarUrl, nickName = await self.get_nickname_avatarurl(uuid)
            userinfo = UserInfo.objects.filter(session__uuid=uuid)

            if userinfo:
                my_info = eval(userinfo[0].session.user_info)
                avatarUrl = my_info['avatarUrl']
                nickName = my_info['nickName']
                dict = {}
                try:
                    print("rec rooms_data_dict = {}--------".format(self.rooms_data_dict[self.room_group_name]))
                    self.return_list = self.rooms_data_dict[self.room_group_name]
                    if len(self.return_list) > 0:
                        for i in range(len(self.return_list)):
                            if self.return_list[i] == uuid:
                                have_flag = 1
                        if not have_flag:
                            dict['uuid'] = uuid
                            dict['avatarUrl'] = avatarUrl
                            dict['nickName'] = nickName
                            self.return_list.append(dict)
                    else:
                        dict['uuid'] = uuid
                        dict['avatarUrl'] = avatarUrl
                        dict['nickName'] = nickName
                        self.return_list.append(dict)
                except Exception as e:
                    print(e)
                    dict['uuid'] = uuid
                    dict['avatarUrl'] = avatarUrl
                    dict['nickName'] = nickName
                    self.return_list.append(dict)
                self.rooms_data_dict[self.room_group_name] = self.return_list
                print("receive return_list = {}-----------------------".format(self.return_list))
                print("add return list rooms_data_dict = {}--------".format(self.rooms_data_dict[self.room_group_name]))
                # Send message to room group
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'data': self.return_list
                    }
                )

    # Receive message from room group
    async def chat_message(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': data
        }))

    # Receive message from room group
    async def chat_start(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'start_flag': data
        }))


class PlayingConsumer(AsyncWebsocketConsumer):
    playing_data_dict = {}

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'play_%s' % self.room_name
        self.success_list = []
        self.uuid = ''
        all_questions = origin_image_dict
        random.shuffle(all_questions)
        questions = all_questions[:20]
        pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
        r = redis.Redis(connection_pool=pool)
        if r.exists(self.room_name):
            print("room_name exist-----delete")
            r.delete(self.room_name)
            print("delete {}".format(r.exists(self.room_name)))
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'quest_list',
                'data': questions
            }
        )

    async def disconnect(self, close_code):
        # Leave room group
        print("playing disconnect {}".format(self.uuid))
        # assert self.valid_group_name(self.room_group_name)
        # print(self.groups[self.room_group_name])
        # if not self.groups[self.room_group_name]:
        #     print("self.group is none")
        #     self.playing_data_dict[self.room_group_name] = []
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        uuid = text_data_json['uuid']
        success_count = text_data_json['success_count']
        userinfo = UserInfo.objects.filter(session__uuid=uuid)
        if userinfo:
            my_info = eval(userinfo[0].session.user_info)
            avatarUrl = my_info['avatarUrl']
            have_flag = 0
            dict = {}
            try:
                self.success_list = self.playing_data_dict[self.room_group_name]
                print(uuid, success_count)
                print(self.playing_data_dict)
                for i in range(len(self.success_list)):
                    if self.success_list[i]['uuid'] == uuid:
                        self.success_list[i]['success_count'] = success_count
                        have_flag = 1
                if not have_flag:
                    dict['uuid'] = uuid
                    dict['success_count'] = success_count
                    dict['avatarUrl'] = avatarUrl
                    self.success_list.append(dict)
            except Exception as e:
                print(e)
                dict['uuid'] = uuid
                dict['success_count'] = success_count
                dict['avatarUrl'] = avatarUrl
                self.success_list.append(dict)
            self.playing_data_dict[self.room_group_name] = self.success_list
            print("========================after add return list ===================================")
            print(self.playing_data_dict)
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'play_message',
                    'data': self.success_list
                }
            )

    # Receive message from room group
    async def play_message(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'data': data
        }))

    async def quest_list(self, event):
        data = event['data']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'question_list': data
        }))
# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# import json
#
# sync
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
