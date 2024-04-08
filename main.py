# Part 1
from io import FileIO


def read_csv(filename):
  """
  read data from a csv file and edit it

  Parameters
  ----------
  filename:csv
      the file to be read

  Returns
  -------
  list
  """
  # Type your code below
  filename = open(filename, 'r')
  header = filename.readline().strip('\n').split(',')

  data_r = filename.readlines()[0:]
  data = []
  rows = []
  for line in data_r:
    rows.append(line.strip('\n').split(','))

  data = []    
  for row in rows:
    row = [int(row[0]), str(row[1]), str(row[2]), int(row[3])]
    data.append(row)
  # print(data)
  filename.close()
  #print(header, data)
  return (header, data)


# Part 2
def filter_gender(enrolment_by_age:list, sex:str) -> list:
  """
  filter the data

  Parameters
  ----------
  enrolment_by_age:list
      list of records
  sex:str
      the str to be matched with

  Returns
  -------
  list
  """
  new_data = []
  for record in enrolment_by_age:
      if record[2] == sex:
          new_row = [record[0], record[1], record[3]]
          new_data.append(new_row)
  return new_data


# Part 3
def sum_by_year(enrolment:list)->list:
  # Type your code below
  """
  sum up emrolment by year

  Parameters
  ----------
  enrolment:list
      list of data

  Returns
  -------
  list
  """
  enrolment_by_year = []
  new_row = [None, None]
  for record in enrolment:
      if new_row[0] is None:
          new_row = [record[0], record[2]]
      elif record[0] != new_row[0]:
          enrolment_by_year.append(new_row)
          new_row = [record[0], record[2]]
      else:
          new_row[1] = new_row[1] + record[2]
  return enrolment_by_year


# Part 4
def write_csv(filename, header:str, data:list):
  # Type your code below
  """
  write data into a csv file

  Parameters
  ----------
  filename:
    file to be written into
  header:list
    str to be header
  data:list
    ist of data to be written

  Returns
  -------
  file
  """
  file = open(filename, 'w')
  header = str(header)
  file.write(header + '/n')

  for row in data:
      row = str(row)
      file.write(row + '/n')

  num_lines_written = len(data) + 1  
  return num_lines_written



# TESTING
# You can write code below to call the above functions
