class Node:
  '''
  Represents a node in a linked list
  contains two values - data and the pointer to the next node
  '''
  data = None
  nextNode = None

  def __init__(self, data) -> None:
    self.data = data
  
  def __repr__(self) -> str:
    return f'<Node data: {self.data}>'
  



class LinkedList:
  '''
  Represents a singly linked list
  '''

  def __init__(self) -> None:
    self.head = None

  def __repr__(self) -> str:
    '''
    Represents the string representation of the List
    O(n) time
    '''
    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append(f'[head: {current.data}]')

      elif current.nextNode == None:
        nodes.append(f'[tail: {current.data}]')
      
      else:
        nodes.append(f'[{current.data}]')

      current = current.nextNode
    return ' -> '.join(nodes)
  
  def isEmpty(self) -> bool:
    '''
    O(1) time
    '''
    return self.head == None
  
  def size(self) -> int:
    '''
    loops through the list to calculate its size
    O(n) time
    '''
    count = 0
    current = self.head

    while current:
      count += 1
      current = current.nextNode
    
    return count
  
  def prepend(self, data) -> None:
    '''
    Adds a new node to the head of the list
    O(1) time
    '''
    newNode = Node(data)
    newNode.nextNode = self.head
    self.head = newNode
    