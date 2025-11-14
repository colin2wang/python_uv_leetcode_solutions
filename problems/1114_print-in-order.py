"""
LeetCode 1114 – Print In Order

URL: https://leetcode.com/problems/print-in-order/
"""
import pytest
import threading
from typing import Callable

class Foo:
    def __init__(self):
        """
        Initialize two semaphores to control the execution order.
        sem1 controls the transition from first() to second().
        sem2 controls the transition from second() to third().
        """
        self.sem1 = threading.Semaphore(0)
        self.sem2 = threading.Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        """
        Execute first task and signal completion to second task.
        
        Args:
            printFirst (Callable[[], None]): Function to print "first"
        """
        # Execute the first task
        printFirst()
        # Signal that first task is completed
        self.sem1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        """
        Wait for first task completion, execute second task, and signal completion to third task.
        
        Args:
            printSecond (Callable[[], None]): Function to print "second"
        """
        # Wait for first task to complete
        self.sem1.acquire()
        # Execute the second task
        printSecond()
        # Signal that second task is completed
        self.sem2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        """
        Wait for second task completion and execute third task.
        
        Args:
            printThird (Callable[[], None]): Function to print "third"
        """
        # Wait for second task to complete
        self.sem2.acquire()
        # Execute the third task
        printThird()