#!/usr/bin/python3
# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Name:        AIS 3USON logger setup
# Purpose:
#
# Author:      Savin Alexander Viktorovich aka alexqwesa
# Created:     2019
# Copyright:   Savin Alexander Viktorovich aka alexqwesa
# Licence:     LGPL 3
# This software is licensed under the "LGPLv3" License as described in the "LICENSE" file,
# which should be included with this package. The terms are also available at
# http://www.gnu.org/licenses/lgpl-3.0.html
# -------------------------------------------------------------------------------

import inspect
import logging
import sys
from functools import wraps
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Tuple, Callable

# from concurrent_log_handler import ConcurrentRotatingFileHandler
from global_constants import *

#############################
# setup app dir
# ---------------------------
home_dir = os.path.join(
    str(Path.home()), ".config")
home_dir = os.path.join(home_dir, "3USON")
if not os.path.isdir(home_dir):
    os.makedirs(home_dir)
# #############################
# # set project dir
# # ---------------------------
# if 'PROJECT_DIR' not in globals():
#     PROJECT_DIR = os.path.join(os.path.dirname(__file__).replace("/", os.path.sep), os.path.pardir)
#############################
# check frozen
# ---------------------------
if getattr(sys, 'frozen', False):
    # we are running in a bundle
    bundle_dir = sys._MEIPASS
else:
    # we are running in a normal Python environment
    bundle_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
#############################
# set project dir
# ---------------------------
PROJECT_DIR = os.path.join(bundle_dir, "../")


# print(PROJECT_DIR)
# print(__file__)


def caller_name(skip=2):
    """Get a name of a caller in the format module.class.method

       `skip` specifies how many levels of stack to skip while getting caller
       name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.

       An empty string is returned if skipped levels exceed stack height
    """
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
        return ''
    parent_frame = stack[start][0]

    name = []
    module = inspect.getmodule(parent_frame)
    pf = stack[start]
    if 'self' in pf.frame.f_locals:
        # name.append(parent_frame.frame.f_locals['self'].__class__.__name__)
        # # s = parent_frame.frame.f_locals['self']
        if hasattr(pf.frame.f_locals['self'], "objectName"):
            name.append(pf.frame.f_locals['self'].objectName())
    # `modname` can be None when frame is executed directly in console
    if module:
        name.append(module.__name__)
    # detect classname
    if 'self' in parent_frame.f_locals:
        # I don't know any way to detect call from the object method
        # XXX: there seems to be no way to detect static method call - it will
        #      be just a function call
        name.append(parent_frame.f_locals['self'].__class__.__name__)
    codename = parent_frame.f_code.co_name
    if codename != '<module>':  # top level usually
        name.append(codename)  # function or a method

    # Avoid circular refs and frame leaks
    #  https://docs.python.org/2.7/library/inspect.html#the-interpreter-stack
    del parent_frame, stack

    return ".".join(name)


def log_wrapper(fn):
    @wraps(fn)
    def ret_func(*args, **kwargs):
        try:
            #############################
            # make caller_name shorter
            # ---------------------------
            cn = caller_name()
            s = "{:60}".format(cn)
            if len(cn) <= 60:
                pass
            else:
                s = "{:30}|{:29}".format(cn[:30], cn[-29:])
            #############################
            # return object name
            # ---------------------------
            if len(args) and args[0] != []:
                nargs = [x for x in args]
                nargs[0] = "%s :" + str(args[0])
                nargs.insert(1, s)
            else:
                nargs = ["%s :"]
                nargs += [s]
                # nargs += args[1:]
            return fn(*nargs, **kwargs)
        except IndexError:
            return fn(*args, **kwargs)

    return ret_func


#############################
# setup logger
# ---------------------------
def LoggerSet() -> Tuple[Callable, Callable, Callable, Callable, Callable]:
    """Return: debug, info, warning, error, critical - functions of new logger"""
    #############################
    # setup
    # ---------------------------
    logger = logging.getLogger("3uson")
    if len(logger.handlers):
        #############################
        # skip setup if exist
        # ---------------------------
        return debug, info, warning, error, critical
    logger.setLevel(logging.DEBUG)
    #############################
    # create file handler
    # ---------------------------
    log_file = os.path.join(
        home_dir, '3uson.log')
    #############################
    # rotate logs handlers.RotatingFileHandler - works only in linux?
    # ---------------------------
    fh = RotatingFileHandler(log_file, maxBytes=2000000, backupCount=10)
    # logrotate = ConcurrentRotatingFileHandler(
    #     log_file, maxBytes=9000, backupCount=5)
    # logger.addHandler(logrotate)
    #############################
    # manual file handler
    # ---------------------------
    # with suppress(FileNotFoundError):
    #     if os.stat(log_file).st_size > 900000:
    #         try:
    #             os.rename(log_file, log_file + "-" + dt.now().strftime("%Y-%m-%d_%H%M%S"))
    #         except PermissionError:
    #             log_file = log_file + "-" + dt.now().strftime("%Y-%m-%d_%H%M%S")
    # fh = logging.FileHandler(log_file)
    # fh.setLevel(logging.DEBUG)
    #############################
    # create console handler
    # ---------------------------
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    #############################
    # create formatter and add it to the handlers
    # ---------------------------
    # formatter = logging.Formatter('%(levelname).1s - %(asctime)s - %(name)s - %(lineno)-4s: %(message)s')
    if FAST_LOG:
        log_fmt_str = '%(levelname).1s-%(relativeCreated)-6d-%(module)s.py:%(lineno)-4s-%(funcName)15s()- %(message)s'
    else:
        log_fmt_str = '%(levelname).1s-%(relativeCreated)-6d-%(module)s.py:%(lineno)-4s %(message)s'
    formatter1 = logging.Formatter(log_fmt_str)
    ch.setFormatter(formatter1)
    # for file
    log_fmt_str2 = log_fmt_str.replace("%(relativeCreated)-6d", "%(asctime)s")
    formatter2 = logging.Formatter(log_fmt_str2)
    fh.setFormatter(formatter2)
    #############################
    # add the handlers to logger
    # ---------------------------
    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info("logger set to file - %s", log_file)
    #############################
    # make logger static var
    # ---------------------------
    LoggerSet.lgr = logger
    lgr = logger
    arr = []
    if FAST_LOG:
        for f in lgr.debug, lgr.info, lgr.warning, lgr.error, lgr.critical:
            arr.append(f)
    else:
        for f in lgr.debug, lgr.info, lgr.warning, lgr.error, lgr.critical:
            arr.append(log_wrapper(f))
    return arr


#############################
# init logging system
# ---------------------------
debug, info, warning, error, critical = LoggerSet()
