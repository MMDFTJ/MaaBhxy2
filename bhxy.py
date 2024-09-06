import os
import time
from typing import Tuple

# python -m pip install maafw
from maa.define import RectType
from maa.resource import Resource
from maa.controller import AdbController
from maa.instance import Instance
from maa.toolkit import Toolkit

from maa.custom_recognizer import CustomRecognizer
from maa.custom_action import CustomAction

import asyncio

from allOperate import AllOperate


def x(msg, js, callback_arg):
    print(f'执行信息:{msg}')
    print(f'返回的js数据:{js}')
    print(f'callback_arg:{callback_arg}')
    print('-' * 20)


async def main():
    user_path = "./"
    Toolkit.init_option(user_path)
    # os.path.dirname(os.path.abspath(os.getcwd()))
    resource = Resource()
    await resource.load(os.path.join(os.getcwd(), 'resource'))

    device_list = await Toolkit.adb_devices()
    if not device_list:
        print("No ADB device found.")
        exit()

    # for demo, we just use the first device
    device = device_list[0]
    controller = AdbController(
        adb_path=device.adb_path,
        address=device.address,
    )
    await controller.connect()

    maa_inst = Instance(x)
    maa_inst.bind(resource, controller)
    if not maa_inst.inited:
        print("Failed to init MAA.")
        exit()

    """
        callback并不会返回json中next，感觉需要分开写，然后通过allOperate.py中集成操作达到每个操作都返回，先拆开写好流程在封装每一个操作方便维护
    """
    allOperate = AllOperate(maa_inst)
    maa_inst.register_recognizer("MyRec", my_rec)
    maa_inst.register_action("MyAct", my_act)
    maa_inst.register_action("AEZAKMIAction", AEZAKMIAction)
    maa_inst.register_action("GameTesterAction", gameTesterAction)
    #
    # await maa_inst.run_task('进入游戏')
    #
    # await allOperate.enter_game()

    await allOperate.expedition()
    # ------------------------------
    await allOperate.buy_gift_pack()

    await allOperate.dy_crack()

    await allOperate.bkxh()

    if inputNum == "0":
        await allOperate.judge_if_activity()
        await allOperate.enter_activity()
        await allOperate.cycle_battle(max_battle=3, double_bool=True)

    await allOperate.community()

    await allOperate.get_daily_rewards()


class MyRecognizer(CustomRecognizer):
    def analyze(self, context, image, task_name, custom_param) -> Tuple[bool, RectType, str]:
        return True, (0, 0, 100, 100), "Hello World!"


class MyAction(CustomAction):
    def run(self, context, task_name, custom_param, box, rec_detail) -> bool:
        print(
            f"MyAction.run: task_name: {task_name}, custom_param: {custom_param}, box: {box}, rec_detail: {rec_detail}")
        print(f'myAction Box:{box}')

        x, y = (box[0] + box[2]), (box[1] + box[3])
        success = context.click(x, y)
        return success

    def stop(self) -> None:
        pass


class AEZAKMIAction(CustomAction):
    def run(self, context, task_name, custom_param, box, rec_detail) -> bool:
        print(
            f"MyAction.run: task_name: {task_name}, custom_param: {custom_param}, box: {box}, rec_detail: {rec_detail}")
        print(f'myAction Box:{box}')
        x, y = (box[0] + box[2]), (box[1] + box[3])
        success = context.click(x, y)
        context.run_task("选择助战好友")
        if context.run_task("提示"):
            context.run_task("开战2")
        context.run_task("崩坏娘")
        context.run_task("开战")
        # while True:
        #     if context.run_task("点击愿望杯"):
        #         context.run_task("点击金簪")
        #         break
        # while True:
        #     start_time = time.time()
        #     while True:
        #         elapsed_time = time.time() - start_time
        #         if elapsed_time >= 3:
        #             break
        #         context.touch_down(0, 168, 400, 50)
        #         time.sleep(5)
        #     start_time = time.time()
        #     while True:
        #         elapsed_time = time.time() - start_time
        #         if elapsed_time >= 3:
        #             break
        #         context.touch_down(0, 168, 670, 50)
        #         time.sleep(5)
        while True:
            if context.run_task("确定文字版"):
                return success

    def stop(self) -> None:
        pass


class GameTesterAction(CustomAction):
    def run(self, context, task_name, custom_param, box, rec_detail) -> bool:
        print(
            f"MyAction.run: task_name: {task_name}, custom_param: {custom_param}, box: {box}, rec_detail: {rec_detail}")
        print(f'myAction Box:{box}')
        x, y = (box[0] + box[2]), (box[1] + box[3])
        success = context.click(x, y)
        context.run_task("选择助战好友")
        if context.run_task("提示"):
            context.run_task("开战2")
        context.run_task("崩坏娘")
        context.run_task("开战")

        while True:
            context.click(1008, 624)
            time.sleep(1)
            context.click(1181, 624)
            if context.run_task("确定文字版"):
                return success

    def stop(self) -> None:
        pass


AEZAKMIAction = AEZAKMIAction()
gameTesterAction = GameTesterAction()
my_rec = MyRecognizer()
my_act = MyAction()

if __name__ == "__main__":
    inputNum = input('0-清体力（输入0清体力，留空回车不清体力打崩科校活）:')
    if inputNum == '0' or inputNum == '':
        pass
    else:
        raise TypeError("参数错误")
    asyncio.run(main())

