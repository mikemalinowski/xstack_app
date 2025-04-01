

# xstack_app

This is a Qt based application/widget which is designed to visualise an xstack stack.

The app is not a requirement for using xstack, but can be used as a front end to build
and execute stacks. 

![xstack Image](xstack_app/_res/xstack_demo.png)

## Installing

You can install the xstack_app using `pip install xstack_app`

Note: This requires either PySide2 or PySide6 to also be available.

## Running

```python
import xstack_app

xstack_app.launch(blocking=True)
```

If you want to run it with some example components, you can run:

```python
import xstack_app

xstack_app.launch_demo(blocking=True)
```