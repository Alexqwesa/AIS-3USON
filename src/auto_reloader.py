import inspect
import os
import sys
import types

from logger_setup import *
from functools import wraps

from qtpy.QtWidgets import QWidget, QVBoxLayout


def try_wrapper(fn):
    """Wrap function into try block to cache all exceptions"""

    @wraps(fn)
    def ret_fn(*arg, **kwarg):
        try:
            # new_fn = fn
            return fn(*arg, **kwarg)
        except:
            debug("error in %s", fn.__name__)
            exc_type, exc_value, exc_traceback = sys.exc_info()
            import traceback
            traceback.print_exception(exc_type, exc_value, exc_traceback)
            # input("Press key to continue...")

    return ret_fn


try:
    if os.environ["DEBUG_MODE"].lower() != "on":
        raise KeyError

    try:
        from watchdog1.events import FileSystemEventHandler
        from watchdog1.observers import Observer
    except ImportError:
        #############################
        # use stub if no watchdog imported
        # ---------------------------
        debug("stubs used instead of watchdog")


        class FileSystemEventHandler:
            pass


        class Observer:
            def schedule(self, *args, **kwargs):
                pass

            def start(self):
                pass


    # from watchdog1.tricks import Trick

    def auto_reload_class_code(decorator):
        def decorate(cls):
            cls_src = inspect.getsource(cls)
            for attr, attr_obj in inspect.getmembers(cls, inspect.isroutine):  # cls.__dict__:  types.MethodType
                # attr=attr_obj.__name__
                # if callable(getattr(cls, attr)):
                # if attr_obj is not getattr(super(cls),attr):
                if "def " + attr + "(self" in cls_src:
                    setattr(cls, attr, decorator(attr_obj))
            return cls

        return decorate


    def reloader(fn):
        @wraps(fn)
        def ret_fn(*arg, **kwarg):
            # ret = fn(*arg, **kwarg)
            AR.check_method(arg[0], fn)
            # new_fn = getattr(arg[0], fn.__name__).__wrapped__
            return fn(*arg, **kwarg)

        return ret_fn


    def force_reloader(fn):
        @wraps(fn)
        def ret_fn(*arg, **kwarg):
            # ret = fn(*arg, **kwarg)
            # AR.schedule_update_module(fn.__module__.partition(".")[2] + ".py")
            AR.schedule_update_module(fn.__module__ + ".py")
            AR.check_method(arg[0], fn)
            new_fn = getattr(arg[0], fn.__name__).__wrapped__
            # new_fn = fn
            return new_fn(*arg, **kwarg)

        return ret_fn


    class simple_watcher(FileSystemEventHandler):
        def __init__(self, receive_func):
            self.send_to = receive_func

        def on_modified(self, event):
            if "~" not in event.src_path:
                if not event.is_directory:
                    debug("File changed %s ", event.src_path)
                    self.send_to(event.src_path)


    class CodeAutoReloader:
        """
        Watch for source files and get new code from them,
        """
        __instance = None

        def __new__(cls):
            if CodeAutoReloader.__instance is None:
                CodeAutoReloader.__instance = object.__new__(cls)
            return CodeAutoReloader.__instance

        def __init__(self):
            # self.watched_files = []
            self.reloaded_modules = {}
            self._need_reload = set()
            self.obs = Observer()
            self.watcher = simple_watcher(self.schedule_update_module)
            self.obs.schedule(self.watcher, os.path.realpath("src"), recursive=True)
            debug("path %s ", os.path)
            self.mod_name = ""  # "src."
            self.obs.start()

        def schedule_update_module(self, path: str):
            """
            Schedule module update
            """
            fmodule = os.path.basename(path)
            if fmodule[-3:] == ".py":
                fmodule = self.mod_name + fmodule[:-3]
                self._need_reload.add(fmodule)
                self.reloaded_modules[fmodule] = None

        def new_module(self, modname):
            """
            Return updated module
            """
            if modname not in self.reloaded_modules:
                return None
            if modname in self._need_reload:
                import importlib
                spec = importlib.util.find_spec(modname)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self.reloaded_modules[modname] = module
                self._need_reload.remove(modname)
            return self.reloaded_modules[modname]

        # def get_class_that_defined_method(self, meth): # Python 2
        #     for cls in inspect.getmro(meth.im_class):
        #         if meth.__name__ in cls.__dict__:
        #             return cls
        #     return None

        def get_class_that_defined_method(self, meth):
            if inspect.ismethod(meth):
                for cls in inspect.getmro(meth.__self__.__class__):
                    if cls.__dict__.get(meth.__name__) is meth:
                        return cls
                meth = meth.__func__  # fallback to __qualname__ parsing
            if inspect.isfunction(meth):
                cls = getattr(inspect.getmodule(meth),
                              meth.__qualname__.split(".<locals>", 1)[0].rsplit(".", 1)[0])
                if isinstance(cls, type):
                    return cls
            return getattr(meth, "__objclass__", None)

        def check_method(self, cls, func):
            """
            Replace method if new version found
            :param self:
            :param cls:
            :param func:
            :return:
            """
            module = inspect.getmodule(func)
            try:
                # new_f = False
                if inspect.ismethod(func):
                    new_f = self.new_method(module.__name__,
                                            self.get_class_that_defined_method(func).__name__,
                                            func.__name__)
                else:
                    # if str(type(func)) == "<class 'function'>":
                    new_f = self.new_func(module.__name__, func.__name__)
                if new_f:
                    src = inspect.getsource(func)
                    new_src = inspect.getsource(new_f)
                    if src != new_src:  # always False - fix it
                        setattr(cls, func.__name__, types.MethodType(new_f, cls))
                    setattr(cls, func.__name__, types.MethodType(new_f, cls))
            except TypeError:
                warning("TypeError for class %s function %s", cls.__class__.__name__, func.__name__)

        def new_method(self, module_name: str, fclass: str, fname: str):
            """
            Get new function if exist
            :param self:
            :param module_name:
            :param fclass:
            :param fname:
            :return: new_function
            """
            module = self.new_module(module_name)
            if module:
                try:
                    new_class = getattr(module, fclass)
                    new_func = getattr(new_class, fname)
                    return new_func
                    # for member in dir(module):  # TODO: rework it
                    #     new_class = getattr(module, member)
                    #     if hasattr(new_class, fname):
                    #         new_func = getattr(new_class, fname)
                    #         return new_func
                except AttributeError:
                    error("new_class or new_method not found %s", fclass)
                    return False
            else:
                return None

        def new_func(self, module_name: str, fname: str):
            """
            Get new function if exist
            :param self:
            :param module_name:
            :param fname:
            :return: new_function
            """
            module = self.new_module(module_name)
            if module:
                try:
                    new_func = getattr(module, fname)
                    return new_func
                    # for member in dir(module):  # TODO: rework it
                    #     new_class = getattr(module, member)
                    #     if hasattr(new_class, fname):
                    #         new_func = getattr(new_class, fname)
                    #         return new_func
                except AttributeError:
                    try:
                        for member in dir(module):  # TODO: rework it
                            new_class = getattr(module, member)
                            if hasattr(new_class, fname) and hasattr(new_class, __class__):
                                new_func = getattr(new_class, fname)
                                return new_func
                    except AttributeError:

                        error("new_class or new_method not found %s", module_name)
                        return False
            else:
                return None


    def function_replacer(fmodule, fclass, fname):
        debug("fmodule - %s, fclass - %s, fname - %s", fmodule, fclass, fname)
        #############################
        # import module
        # ---------------------------
        import importlib
        spec = importlib.util.find_spec(fmodule)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        #############################
        # get class
        # ---------------------------
        try:
            debug(dir(module))
            new_class = getattr(module, fclass)
        except AttributeError:
            debug("new_class not found %s", type(fclass).__name__)
            return False
        #############################
        # get function
        # ---------------------------
        try:
            debug(dir(new_class))
            new_func = getattr(new_class, fname)
        except AttributeError:
            debug("new_method not found %s", type(fname).__name__)
            return False
        #############################
        # get old function
        # ---------------------------
        # try:
        old_class = getattr(sys.modules[fmodule], fclass)
        setattr(old_class, fname, new_func)
        # old_func = eval("setattr({},{},{})".format(fclass, fname))
        # old_func = new_method
        # except:
        #     debug("old_func not replaced ")
        #     return False


    def widget_replacer(widget_name):
        from data_worker import UI
        widget: QWidget = UI.main_window.findChild(QWidget, widget_name)
        #############################
        # import module
        # ---------------------------
        import importlib
        spec = importlib.util.find_spec("widgets.custumQWidgets")
        module = importlib.util.module_from_spec(spec)
        # importlib.reload(module)
        spec.loader.exec_module(module)
        try:
            debug(dir(module))
            new_class = getattr(module, type(widget).__name__)
        except AttributeError:
            debug("class not found %s", type(widget).__name__)
            return False
        #############################
        # get info
        # ---------------------------
        debug(widget.dumpObjectInfo())
        #############################
        # add widget
        # ---------------------------
        debug(widget)
        debug(widget.layout())
        layout: QVBoxLayout = widget.layout()  # QVBoxLayout()
        for i in range(layout.count() - 1, -1, -1):
            layout.takeAt(i)

        new_widget: QWidget = new_class(widget)
        layout.addWidget(new_widget)
        # widget.setLayout(layout)
        debug(new_widget)
        # new_widget.setGeometry(widget.geometry())
        new_widget.show()
        return True


except KeyError:
    def auto_reload_class_code(decorator):
        def decorate(cls):
            return cls

        return decorate


    def reloader(fn):
        @wraps(fn)
        def ret_fn(*arg, **kwarg):
            return fn(*arg, **kwarg)

        return ret_fn


    def force_reloader(fn):
        @wraps(fn)
        def ret_fn(*arg, **kwarg):
            return fn(*arg, **kwarg)

        return ret_fn


    class CodeAutoReloader:
        """
        Watch for source files and get new code from them,
        """
        __instance = None

        def __new__(cls):
            if CodeAutoReloader.__instance is None:
                CodeAutoReloader.__instance = object.__new__(cls)
            return CodeAutoReloader.__instance

        def __init__(self):
            pass



    def function_replacer(fmodule, fclass, fname):
        pass


    def widget_replacer(widget_name):
        pass

#############################
# make only one instance
# ---------------------------
AR = CodeAutoReloader()
