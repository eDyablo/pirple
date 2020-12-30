'''
Homework assignment for the 'Python is easy' course by Pirple.

Written by Ed Yablonsky

The example demonstrates how to use threading library to organize interaction
between simultaneously running procedures sharing one resource.
'''

from threading import Thread, Lock, Event
import logging as log
from time import sleep

queue = list()

queue_lock = Lock()

production_completed = Event()

products = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
  'ten',
]

def produce(id):
  for product in products:
    log.info("%s produce %s", id, product)
    with queue_lock:
      queue.append(product)
    sleep(0.5)

def consume(id):
  while True:
    product = None
    with queue_lock:
      if len(queue):
        product = queue.pop()
      elif production_completed.is_set():
        break
    if product:
      log.info("%s consumed %s", id, product)

production = list() # holds all the production threads

def start_production():
  production.append(Thread(target=produce, args=('p1',)))
  production.append(Thread(target=produce, args=('p2',)))
  production.append(Thread(target=produce, args=('p3',)))
  for thread in production:
    thread.start()

def wait_for_production_completed():
  for thread in production:
    thread.join()
  production_completed.set()

consumption = list() # holds all the consumption threads

def start_consumption():
  consumption.append(Thread(target=consume, args=('c1',)))
  consumption.append(Thread(target=consume, args=('c2',)))
  for thread in consumption:
    thread.start()

def wait_for_consumption_completed():
  for thread in consumption:
    thread.join()

log.basicConfig(level=log.INFO)

start_consumption()
start_production()
wait_for_production_completed()
wait_for_consumption_completed()
