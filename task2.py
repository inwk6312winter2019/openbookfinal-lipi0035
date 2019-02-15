#Task2---1---

def seperate_log_files(fin):
  fin_get = open("get.log","w")
  fin_put = open("put.log","w")
  fin_post = open("push.log","w")
  fin_delete = open("delete.log","w")
  for line in fin:
    line = line.strip()
    if("GET" in line):
      fin_get.write(line)
      fin_get.write("\n")
    elif("PUT" in line):
      fin_put.write(line)
    elif("POST" in line):
      fin_post.write(line)
    elif("DELETE" in line):
      fin_delete.write(line)
  fin_get.close()
  fin_put.close()
  fin_post.close()
  fin_delete.close()

fin = open("access.log")
seperate_log_files(fin)
print("Done")
