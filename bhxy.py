import time
import os

# python -m pip install maafw
# from maa.define import RectType
from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker
from maa.toolkit import Toolkit
from maa.notification_handler import NotificationHandler, NotificationType

from maa.custom_action import CustomAction
from allOperate import AllOperate
from maa.context import Context
import adbutils
device = adbutils.device()
device.shell('ps -ef | grep -v grep | grep com.miHoYo.HSoDv22144.uc')

class MyNotificationHandler(NotificationHandler):
    def __init__(self, text_edit_signal):
        super().__init__()
        # self.tasker = None
        self.text_edit_signal = text_edit_signal

    def on_raw_notification(self, msg: str, details: dict):
        print(f'执行信息:{msg}')
        print(f'返回的js数据:{details}')
        print('-' * 20)
        self.text_edit_signal.emit(f'任务名:{details.get("entry")} 执行状态:{msg.split(".")[-1]}')

        if msg.split('.')[-1] == 'Starting':
            shell_return = device.shell('ps -ef | grep -v grep | grep com.miHoYo.HSoDv22144.uc')
            if len(shell_return) < 1:
                self.text_edit_signal.emit('发现游戏闪退...正在重启')
            self.tasker.post_pipeline('进入游戏')

        super().on_raw_notification(msg, details)

    def set_task(self, tasker):
        self.tasker = tasker


class Bhxy:
    def __init__(self, text_edit_signal):
        self.resource = None
        self.tasker = None
        self.text_edit_signal = text_edit_signal

    def get_adb_device(self):
        user_path = "./"
        Toolkit.init_option(user_path)

        self.resource = Resource()  # 写到这里
        res_job = self.resource.post_path(os.path.join(os.getcwd(), 'resource'))
        res_job.wait()

        adb_devices = Toolkit.find_adb_devices()
        if not adb_devices:
            print("No ADB device found.")
            exit()
        return adb_devices
        # for demo, we just use the first device

    def connect_adb(self, adb_devices):
        self.text_edit_signal.emit('连接ing...')
        device = adb_devices
        controller = AdbController(
            adb_path=device.adb_path,
            address=device.address,
            screencap_methods=device.screencap_methods,
            input_methods=device.input_methods,
            config=device.config,
        )
        controller.post_connection().wait()
        my_notificationHandler = MyNotificationHandler(self.text_edit_signal)
        self.tasker = Tasker(my_notificationHandler)
        my_notificationHandler.set_task(self.tasker)
        self.tasker.bind(self.resource, controller)
        # self.tasker.set_save_draw(True)
        if not self.tasker.inited:
            print("Failed to init MAA.")
            exit()
        else:
            try:
                self.text_edit_signal.emit('连接成功')
            except AttributeError as e:
                print(e)
        self.resource.register_custom_action("AEZAKMIAction", AEZAKMIAction())
        self.resource.register_custom_action("GameTesterAction", GameTesterAction())

    def start_expedition(self, task_bool=False, max_battle=3, double_bool=True):
        allOperate = AllOperate(self.tasker, self.text_edit_signal)

        allOperate.expedition()

        allOperate.buy_gift_pack()

        allOperate.dy_crack()

        # allOperate.bkxh()

        if task_bool:
            allOperate.judge_if_activity()
            allOperate.enter_activity()
            allOperate.cycle_battle(max_battle, double_bool)

        allOperate.community()

        allOperate.get_daily_rewards()

    def start_cycle_battle(self, max_battle=3, double_bool=True):
        allOperate = AllOperate(self.tasker, self.text_edit_signal)
        allOperate.cycle_battle(max_battle, double_bool)

    def start(self):
        adb_device = self.get_adb_device()
        for i in range(len(adb_device)):
            print(f'序号{i}:模拟器{adb_device[i].name} {adb_device[i].address}')
        self.connect_adb(adb_device[0])
        self.start_expedition()


class AEZAKMIAction(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> CustomAction.RunResult:
        print(
            f"on MyAction.run, context: {context}, task_detail: {argv.task_detail}, action_name: {argv.custom_action_name}, action_param: {argv.custom_action_param}, box: {argv.box}, reco_detail: {argv.reco_detail}"
        )
        controller = context.tasker.controller
        x, y = (argv.box[0] + argv.box[2]), (argv.box[1] + argv.box[3])
        controller.post_click(x, y)
        context.run_pipeline("选择助战好友")
        if context.run_pipeline("提示"):
            context.run_pipeline("开战2")
        context.run_pipeline("崩坏娘")
        context.run_pipeline("开战")

        while True:
            if context.run_pipeline("确定文字版").nodes:
                return CustomAction.RunResult(success=True)


class GameTesterAction(CustomAction):
    def run(
        self,
        context: Context,
        argv: CustomAction.RunArg,
    ) -> CustomAction.RunResult:
        print(
            f"on MyAction.run, context: {context}, task_detail: {argv.task_detail}, action_name: {argv.custom_action_name}, action_param: {argv.custom_action_param}, box: {argv.box}, reco_detail: {argv.reco_detail}"
        )
        controller = context.tasker.controller
        x, y = (argv.box[0] + argv.box[2]), (argv.box[1] + argv.box[3])
        controller.post_click(x, y)
        context.run_pipeline("选择助战好友")
        if context.run_pipeline("提示"):
            context.run_pipeline("开战2")
        context.run_pipeline("崩坏娘")
        context.run_pipeline("开战")

        while True:
            controller.post_click(1008, 624)
            time.sleep(1)
            controller.post_click(1181, 624)
            if context.run_pipeline("确定文字版").nodes:
                return CustomAction.RunResult(success=True)


if __name__ == '__main__':
    b = Bhxy(text_edit_signal=None)
    b.start()
