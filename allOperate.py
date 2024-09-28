class AllOperate:
    def __init__(self, tasker, text_edit_signal):
        self.tasker = tasker
        self.text_edit_signal = text_edit_signal

    def enter_game(self):
        """
        从进游戏到关闭公告
        Returns:

        """
        self.tasker.post_pipeline('进入游戏').wait()
        while True:
            if self.tasker.post_pipeline('进入').wait().get().nodes:
                break

        self.tasker.post_pipeline('抚摸屏幕继续').wait()
        self.tasker.post_pipeline("领取月卡").wait()  # 不知道成不成功
        self.tasker.post_pipeline("每日签到").wait()
        while True:
            if self.tasker.post_pipeline("前往").wait().get().nodes:
                continue
            else:
                break
        self.tasker.post_pipeline("关闭公告").wait()

        self.tasker.post_pipeline("确定文字版").wait()

    def expedition(self):
        """
        使魔探险
        Returns:

        """
        while True:
            if self.tasker.post_pipeline("进入任务").wait().get().nodes:
                continue
            else:
                break
        self.tasker.post_pipeline("点击使魔探险").wait()
        while True:
            if self.tasker.post_pipeline("点击领取使魔探险奖励").wait().get().nodes:
                self.tasker.post_pipeline("点击使魔探险").wait()  # 防止点完最后一个然后还显示着领取东西的界面，从而避免无法识别到派遣使魔探险
                if self.tasker.post_pipeline("信息提示").wait().get().nodes:
                    self.tasker.post_pipeline("确定").wait()
                continue
            elif self.tasker.post_pipeline("派遣使魔探险").wait().get().nodes:
                continue
            else:
                break

    def enter_presence(self, task_name):

        self.tasker.post_pipeline("进入首页").wait()
        while True:
            if self.tasker.post_pipeline("进入任务").wait().get().nodes:
                continue
            else:
                break
        self.tasker.post_pipeline("点击存在感").wait()
        while True:
            if not self.tasker.post_pipeline(task_name).wait().get().nodes:
                # 这里需要向下滑动一点点让前往出来
                self.tasker.post_pipeline("下边往上拉").wait()
            else:
                while True:
                    if self.tasker.post_pipeline(task_name).wait().get().nodes:
                        self.tasker.post_pipeline("下边往上拉").wait()
                    else:
                        return

    def buy_gift_pack(self):
        """
        购买礼包
        Returns:

        """
        self.enter_presence("战力补强")
        for i in range(3):
            self.tasker.post_pipeline("滚动到下面").wait()
            if self.tasker.post_pipeline("点击零时馈礼").wait().get().nodes:
                if self.tasker.post_pipeline("点击是否购买零时馈礼").wait().get().nodes:
                    self.tasker.post_pipeline("购买").wait()
                    self.tasker.post_pipeline("确定").wait()
                    break
        self.tasker.post_pipeline("商店").wait()
        self.tasker.post_pipeline("确认").wait()
        self.tasker.post_pipeline("进入崩坏屋").wait()
        self.tasker.post_pipeline("共鸣屋").wait()
        self.tasker.post_pipeline("刷新共鸣屋和购买零时之种").wait()
        self.tasker.post_pipeline("确定").wait()

    def judge_if_activity(self):
        """
        判断是否在活动的界面上
        Returns:

        """
        self.tasker.post_pipeline("进入战斗").wait()
        if not self.tasker.post_pipeline("活动").wait().get().nodes:
            self.tasker.post_pipeline("返回到活动界面").wait()
            if not self.tasker.post_pipeline("活动").wait().get().nodes:
                self.tasker.post_pipeline("返回到活动界面")
            self.tasker.post_pipeline("活动").wait()

    def dy_crack(self):
        """
        多元裂缝里面的操作
        Returns:

        """
        self.enter_presence("火线救援")
        self.tasker.post_pipeline("使魔的爱").wait()
        if self.tasker.post_pipeline("快捷战斗").wait().get().nodes:
            self.tasker.post_pipeline("确定文字版").wait()
            self.tasker.post_pipeline("确定文字版").wait()

        self.tasker.post_pipeline("进入战斗").wait()
        self.tasker.post_pipeline("虚轴之庭").wait()
        self.tasker.post_pipeline("出击")  # 会抛错 用FeatureMatch可以识别到出击 用TemplateMatch识别到的只有0.5左右
        for i in range(3):
            if self.tasker.post_pipeline("快捷战斗").wait().get().nodes:
                self.tasker.post_pipeline("确定文字版").wait()
                self.tasker.post_pipeline("确定文字版").wait()
            else:
                break
        self.tasker.post_pipeline("进入战斗").wait()

    def enter_activity(self):
        """
        进入活动的BONUS关
        Returns:

        """
        # self.tasker.post_pipeline("进入战斗")
        while True:
            if self.tasker.post_pipeline("进入活动").wait().get().nodes:
                break
            self.tasker.post_pipeline("右边往下拉").wait()
            # self.tasker.post_pipeline("左边往上拉")

        while True:
            if self.tasker.post_pipeline("进入BONUS关").wait().get().nodes:
                break
            else:
                self.tasker.post_pipeline("点击小箭头").wait()

    def cycle_battle(self, max_battle=6, double_bool=False):
        """
        循环战斗
        Args:
            double_bool: 是否使用双倍卷
            max_battle:最大战斗次数

        Returns:

        """
        total_battle_number = 0
        if double_bool:
            self.tasker.post_pipeline("双倍券1").wait()
        while True:
            double_bool = double_bool
            if self.tasker.post_pipeline("补充体力").wait().get().nodes:
                if self.tasker.post_pipeline("兑换双倍体力").wait().get().nodes:
                    self.tasker.post_pipeline("兑换").wait()
                    self.tasker.post_pipeline("补充体力").wait()

                if self.tasker.post_pipeline("补充体力roi中间的").wait().get().nodes:
                    self.tasker.post_pipeline("购买体力按钮").wait()

            self.tasker.post_pipeline("选择助战好友").wait()
            if self.tasker.post_pipeline("提示").wait().get().nodes:
                self.tasker.post_pipeline("开战2").wait()
            self.tasker.post_pipeline("崩坏娘").wait()
            self.tasker.post_pipeline("开战").wait()
            total_battle_number += 1
            while True:
                if self.tasker.post_pipeline("点击愿望杯").wait().get().nodes:
                    self.tasker.post_pipeline("点击金簪").wait()
                    break

            while True:
                if double_bool:
                    print(self.tasker.post_pipeline("单纯检测再次挑战").wait().get().nodes)
                    if self.tasker.post_pipeline("单纯检测再次挑战").wait().get().nodes:
                        self.tasker.post_pipeline("双倍券2").wait()
                        break
                else:
                    break

            if total_battle_number == max_battle:
                while True:
                    if self.tasker.post_pipeline("确定文字版").wait().get().nodes:
                        self.text_edit_signal.emit(f'当前刷取次数:{total_battle_number}')
                        self.text_edit_signal.emit('打完辣')
                        print('打完啦')
                        return

            while True:
                if self.tasker.post_pipeline("再次挑战").wait().get().nodes:
                    """
                    判断是否刷完这么多把副本不能放这里，会因为买体力continue后多+=1一次，这样就不准了
                    """

                    if self.tasker.post_pipeline("补充体力roi中间的").wait().get().nodes:
                        self.tasker.post_pipeline("购买体力按钮").wait()
                        continue

                    elif self.tasker.post_pipeline("兑换双倍体力").wait().get().nodes:
                        self.tasker.post_pipeline("兑换").wait()
                        continue

                    else:
                        break
            self.text_edit_signal.emit(f'当前刷取次数:{total_battle_number}')

    def get_daily_rewards(self):
        """
        领取每日奖励
        Returns:

        """
        self.tasker.post_pipeline("进入战斗").wait()
        self.tasker.post_pipeline("进入首页").wait()
        self.tasker.post_pipeline("进入任务").wait()
        self.tasker.post_pipeline('点击存在感').wait()
        self.tasker.post_pipeline("点击一键领取").wait()

    def bkxh(self):
        """
        崩科校活
        Returns:

        """
        # self.enter_presence("崩科校活")
        self.tasker.post_pipeline("进入装备").wait()
        self.tasker.post_pipeline("进入崩科校活").wait()
        self.tasker.post_pipeline("实验楼").wait()
        self.tasker.post_pipeline("领取收益").wait()
        self.tasker.post_pipeline("获得").wait()  # 这里匹配不到获得 但是能实现想要的功能（） 点的是将使魔放置在实验仓内，可随时间获得使魔碎片
        self.tasker.post_pipeline("x").wait()
        for i in range(2):
            self.tasker.post_pipeline("崩科校活右边往左拉").wait()
            if self.tasker.post_pipeline("崩科校活战斗图标").wait().get().nodes:
                if self.tasker.post_pipeline("AEZAKMI").wait().get().nodes:
                    continue
                if self.tasker.post_pipeline("游戏测试员").wait().get().nodes:
                    continue
                self.tasker.post_pipeline("选择助战好友").wait()
                if self.tasker.post_pipeline("提示").wait().get().nodes:
                    self.tasker.post_pipeline("开战2").wait()
                self.tasker.post_pipeline("备用装备").wait()
                self.tasker.post_pipeline("开战").wait()
                while True:
                    if self.tasker.post_pipeline("点击愿望杯").wait().get().nodes:
                        self.tasker.post_pipeline("点击金簪").wait()
                        break
                while True:
                    if self.tasker.post_pipeline("确定文字版").wait().get().nodes:
                        break
            else:
                break
        self.tasker.post_pipeline("崩科校活左边往右拉").wait()
        self.tasker.post_pipeline("崩科校活占卜图标").wait()
        self.tasker.post_pipeline("开始占卜").wait()
        self.tasker.post_pipeline("点击空白位置关闭").wait()
        self.tasker.post_pipeline("崩科校活返回图标").wait()

    def community(self):
        """
        领取社团体力
        Returns:

        """
        try:
            self.tasker.post_pipeline("社交").wait()
            self.tasker.post_pipeline("我的社团").wait()
            if self.tasker.post_pipeline("不可领").wait().get().nodes:
                return
            self.tasker.post_pipeline("可领").wait()
            self.tasker.post_pipeline("领取").wait()
            self.tasker.post_pipeline("确定").wait()
            if self.tasker.post_pipeline("信息提示").wait().get().nodes:
                self.tasker.post_pipeline("确定").wait()
        except TypeError as e:
            print('强制中断')
