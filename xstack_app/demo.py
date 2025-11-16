import os
import qtility
import xstack

from .config import AppConfig
from .application import AppWindow


# --------------------------------------------------------------------------------------
class DemoAppConfig(AppConfig):

    label = "Stack Demo"

    component_paths = [
        os.path.join(
            os.path.dirname(xstack.__file__),
            "test",
        )
    ]

    stack_class = xstack.Stack

# --------------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences,PyUnusedLocal
def launch_demo(blocking: bool = True, load_file: str = None, run_on_launch: bool = False):
    """
    This function should be called to invoke the app ui in demonstration
    mode, which exposes all the components used by xstacks unit tests.
    """
    q_app = qtility.app.get()

    w = AppWindow(app_config=DemoAppConfig)
    w.show()

    if load_file:
        w.core.import_stack(filepath=load_file, silent=True)

    if run_on_launch and w.core.stack:
        w.core.build()

    if blocking:
        q_app.exec_()
