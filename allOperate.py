class AllOperate:
    def __init__(self, maa_inst):
        self.maa_inst = maa_inst

    async def enter_game(self):
        """
        从进游戏到关闭公告
        Returns:

        """
        await self.maa_inst.run_task('进入游戏')
        while True:
            if await self.maa_inst.run_task('进入'):
                break

        await self.maa_inst.run_task('抚摸屏幕继续')
        await self.maa_inst.run_task("领取月卡")  # 不知道成不成功
        await self.maa_inst.run_task("每日签到")
        while True:
            if await self.maa_inst.run_task("前往"):
                continue
            else:
                break
        await self.maa_inst.run_task("关闭公告")

        await self.maa_inst.run_task("确定文字版")

    async def expedition(self):
        """
        使魔探险
        Returns:

        """
        while True:
            if await self.maa_inst.run_task("进入任务"):
                continue
            else:
                break
        await self.maa_inst.run_task("点击使魔探险")
        while True:
            if await self.maa_inst.run_task("点击领取使魔探险奖励"):
                await self.maa_inst.run_task("点击使魔探险")  # 防止点完最后一个然后还显示着领取东西的界面，从而避免无法识别到派遣使魔探险
                if await self.maa_inst.run_task("信息提示"):
                    await self.maa_inst.run_task("确定")
                continue
            elif await self.maa_inst.run_task("派遣使魔探险"):
                continue
            else:
                break

    async def enter_presence(self, task_name):

        await self.maa_inst.run_task("进入首页")
        while True:
            if await self.maa_inst.run_task("进入任务"):
                continue
            else:
                break
        await self.maa_inst.run_task("点击存在感")
        while True:
            if not await self.maa_inst.run_task(task_name):
                # 这里需要向下滑动一点点让前往出来
                await self.maa_inst.run_task("下边往上拉")
            else:
                while True:
                    if await self.maa_inst.run_task(task_name):
                        await self.maa_inst.run_task("下边往上拉")
                    else:
                        return

    async def buy_gift_pack(self):
        """
        购买礼包
        Returns:

        """
        await self.enter_presence("战力补强")
        for i in range(5):
            await self.maa_inst.run_task("滚动到下面")
            if await self.maa_inst.run_task("点击零时馈礼"):
                if await self.maa_inst.run_task("点击是否购买零时馈礼"):
                    await self.maa_inst.run_task("购买")
                    await self.maa_inst.run_task("确定")
                    break
        await self.maa_inst.run_task("商店")
        await self.maa_inst.run_task("确认")
        await self.maa_inst.run_task("进入崩坏屋")
        await self.maa_inst.run_task("共鸣屋")
        await self.maa_inst.run_task("刷新共鸣屋和购买零时之种")
        await self.maa_inst.run_task("确定")


    async def judge_if_activity(self):
        """
        判断是否在活动的界面上
        Returns:

        """
        if await self.maa_inst.run_task("活动") is None:
            await self.maa_inst.run_task("返回到活动界面")
            if await self.maa_inst.run_task("活动") is None:
                await self.maa_inst.run_task("返回到活动界面")
            await self.maa_inst.run_task("活动")

    async def dy_crack(self):
        """
        多元裂缝里面的操作
        Returns:

        """
        await self.enter_presence("火线救援")
        await self.maa_inst.run_task("使魔的爱")
        if await self.maa_inst.run_task("快捷战斗"):
            await self.maa_inst.run_task("确定文字版")
            await self.maa_inst.run_task("确定文字版")

        await self.maa_inst.run_task("进入战斗")
        await self.maa_inst.run_task("虚轴之庭")
        await self.maa_inst.run_task("出击")  # 会抛错 用FeatureMatch可以识别到出击 用TemplateMatch识别到的只有0.5左右
        for i in range(3):
            if await self.maa_inst.run_task("快捷战斗"):
                await self.maa_inst.run_task("确定文字版")
                await self.maa_inst.run_task("确定文字版")
            else:
                break
        await self.maa_inst.run_task("进入战斗")

    async def enter_activity(self):
        """
        进入活动的BONUS关
        Returns:

        """
        # await self.maa_inst.run_task("进入战斗")
        while True:
            if await self.maa_inst.run_task("进入活动"):
                break
            await self.maa_inst.run_task("右边往下拉")
            # await self.maa_inst.run_task("左边往上拉")

        while True:
            if await self.maa_inst.run_task("进入BONUS关"):
                break
            else:
                await self.maa_inst.run_task("点击小箭头")

    async def cycle_battle(self, max_battle=6, double_bool=False):
        """
        循环战斗
        Args:
            double_bool: 是否使用双倍卷
            max_battle:最大战斗次数

        Returns:

        """
        total_battle_number = 0
        if double_bool:
            await self.maa_inst.run_task("双倍券1")
        while True:
            double_bool = double_bool
            if await self.maa_inst.run_task("补充体力"):
                if await self.maa_inst.run_task("兑换双倍体力"):
                    await self.maa_inst.run_task("兑换")
                    await self.maa_inst.run_task("补充体力")

                if await self.maa_inst.run_task("补充体力roi中间的"):
                    await self.maa_inst.run_task("购买体力按钮")

            await self.maa_inst.run_task("选择助战好友")
            if await self.maa_inst.run_task("提示"):
                await self.maa_inst.run_task("开战2")
            await self.maa_inst.run_task("崩坏娘")
            await self.maa_inst.run_task("开战")
            total_battle_number += 1
            while True:
                if await self.maa_inst.run_task("点击愿望杯"):
                    await self.maa_inst.run_task("点击金簪")
                    break

            while True:
                if double_bool:
                    if await self.maa_inst.run_task("单纯检测再次挑战"):
                        await self.maa_inst.run_task("双倍券2")
                        break
                else:
                    break

            if total_battle_number == max_battle:
                while True:
                    if await self.maa_inst.run_task("确定文字版"):
                        print('打完啦')
                        return

            while True:
                if await self.maa_inst.run_task("再次挑战"):
                    """
                    判断是否刷完这么多把副本不能放这里，会因为买体力continue后多+=1一次，这样就不准了
                    """

                    if await self.maa_inst.run_task("补充体力roi中间的"):
                        await self.maa_inst.run_task("购买体力按钮")
                        continue

                    elif await self.maa_inst.run_task("兑换双倍体力"):
                        await self.maa_inst.run_task("兑换")
                        continue

                    else:
                        break

    async def get_daily_rewards(self):
        """
        领取每日奖励
        Returns:

        """
        # await self.maa_inst.run_task("进入战斗")
        await self.maa_inst.run_task("进入首页")
        await self.maa_inst.run_task("进入任务")
        await self.maa_inst.run_task('点击存在感')
        await self.maa_inst.run_task("点击一键领取")

    async def bkxh(self):
        """
        崩科校活
        Returns:

        """
        await self.enter_presence("崩科校活")
        await self.maa_inst.run_task("实验楼")
        await self.maa_inst.run_task("领取收益")
        await self.maa_inst.run_task("获得")  # 这里匹配不到获得 但是能实现想要的功能（） 点的是将使魔放置在实验仓内，可随时间获得使魔碎片
        await self.maa_inst.run_task("x")
        for i in range(2):
            await self.maa_inst.run_task("崩科校活右边往左拉")
            if await self.maa_inst.run_task("崩科校活战斗图标"):
                if await self.maa_inst.run_task("AEZAKMI"):
                    continue
                if await self.maa_inst.run_task("游戏测试员"):
                    continue
                await self.maa_inst.run_task("选择助战好友")
                if await self.maa_inst.run_task("提示"):
                    await self.maa_inst.run_task("开战2")
                await self.maa_inst.run_task("备用装备")
                await self.maa_inst.run_task("开战")
                while True:
                    if await self.maa_inst.run_task("点击愿望杯"):
                        await self.maa_inst.run_task("点击金簪")
                        break
                while True:
                    if await self.maa_inst.run_task("确定文字版"):
                        break
            else:
                break
        await self.maa_inst.run_task("崩科校活左边往右拉")
        await self.maa_inst.run_task("崩科校活占卜图标")
        await self.maa_inst.run_task("开始占卜")
        await self.maa_inst.run_task("点击空白位置关闭")
        await self.maa_inst.run_task("崩科校活返回图标")

    async def community(self):
        """
        领取社团体力
        Returns:

        """
        await self.maa_inst.run_task("社交")
        await self.maa_inst.run_task("我的社团")
        if await self.maa_inst.run_task("不可领"):
            return
        await self.maa_inst.run_task("可领")
        await self.maa_inst.run_task("领取")
        await self.maa_inst.run_task("确定")
        if await self.maa_inst.run_task("信息提示"):
            await self.maa_inst.run_task("确定")
