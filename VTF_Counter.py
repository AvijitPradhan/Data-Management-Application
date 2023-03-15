import os
import json
import logging

class Singleton(type):
  _instance = {}
  
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instance:
      cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instance[cls]
  

class VTFCounter(metaclass=Singleton):
  
"""
This class handles counting of real number of tests and outputs these numbers into an ini file, that can be consumed by the VTF network
"""

 def __init__(self):
    self.passed_tests = 0
    self.failed_tests = 0
    self.skipped_tests = 0
    
 def update_count(self, result):
  if result =='passed':
    self.passed_tests += 1
  elif result =='failed':
    self.failed_tests += 1
  elif result =='skipped':
    self.skipped_tests +=1
  else:
    logging.error("Unknown resulttype, class:{}".format(result))
    
 @property
  def passed(self):
    return self.passed
 @property
  def failed(self):
    return self.failed
 @property
  def skipped(self):
    return self.skipped
 @property
  def all_executed(self):
    return self.passed_test + self.failed_tests
 @property
  def all_tests(self):
    return self.passed_tests + self.failed_tests + self.skipped_tests
 
def dump_to_file (self, vtf_file = None):
  if not vtf_file:
    vtf_file = os.path.join("target", "vtf_counter.json")
  stats = {'executed' : self.all_executed,
           'passed' : self.passed_tests,
           'failed' : self.failed_tests,
           'skipped': self.skipped_tests}
  with open(vtf_file, 'w') as fp:
    json.dump(stats,fp)
