from Pyro4 import expose
import math

class Solver: 
  def __init__(self, workers=None, input_file_name=None, output_file_name=None):
    self.input_file_name = input_file_name
    self.output_file_name = output_file_name
    self.workers = workers
    print("Inited")

  def solve(self):
    print("Job Started")
    print("Workers %d" % len(self.workers))

    key, hash1 = self.read_input()
    step = 1000000//len(self.workers)
    mapped = []
    for i in xrange(0, int(len(self.workers))):    
      mapped.append(self.workers[i].mymap([j for j in xrange(i*step, int(i*step+step))], key, hash1))

    self.write_output(Solver.myreduce(mapped))
    print("Job Finished")


  @staticmethod
  @expose 
  def mymap(prime, key, hash):
    for el in prime:
      if(Solver.get_hash(key, int(el)) == hash): 
        return int(el)
    return 0
  
  @staticmethod
  @expose 
  def myreduce(mapped):
    print("reduce")
    output = []
    for result in mapped:      
      if result.value != 0:
        output.append(result.value)
    return output

  def read_input(self):
    f = open(self.input_file_name, 'r')
    lines = [line.rstrip('\n') for line in f] 
    f.close()
    return (lines[0], int(lines[1]))
    # return ("lab_on_parcs_in_python", 3430241358440852784793199005805084337799821294526899580122749051196784003514368)

  def write_output(self, output):
    f = open(self.output_file_name, 'w')
    f.write(str(output))
    f.close()
  
  @staticmethod
  @expose
  def get_hash(key, prime):
    result = 0
    for i in xrange(0, len(key)):
      result += ord(key[i])*math.pow(prime, i)
    return int(result)
